# 1) Cadastro e verificação básica (onboarding inicial)

**What happens (UI):** user creates an account with email, phone and password; confirms email/SMS; enables 2FA.

**Endpoints**

- `POST /auth/register` — creates user (email, phone_hash, password_hash)
- `POST /auth/send-email-verif` — generates token, sends link
- `POST /auth/verify-email` — validates token
- `POST /auth/send-sms-code` — generates and sends SMS OTP
- `POST /auth/verify-sms` — validates OTP
- `POST /auth/enable-2fa` / `POST /auth/verify-2fa` — TOTP provisioning & verification
- `POST /auth/login` / `POST /auth/refresh`

**Internal services / components**

- Auth Service (OAuth2 / JWT, refresh tokens) — can use Keycloak/Auth0 or implement JWT + refresh with DB blacklist.
- User Service / Users DB (users table, phone/email hashes).
- Rate limiter (Redis).
- Audit log writer (append-only).

**Recommended third parties**

- Email: SendGrid, SES.
- SMS / OTP: Twilio, Vonage, Zenvia (Brazil).
- 2FA: implement TOTP (lib: otplib) + SMS fallback.

**Validations and security**

- Password strength policy; store salted+peppered hash (Argon2).
- Throttle by IP & account creation.
- Store only hashes for email/phone; log IP, device fingerprint.
- Enforce HTTPS, HSTS, TLS 1.2+.

---

# 2) Identity verification (light KYC / liveness) — by levels

**When:** required only for exchanges above a threshold, or for a “verified” badge.

**Endpoints**

- `POST /kyc/request` — starts KYC session, returns provider_session_id
- `GET /kyc/status` — checks result
- `POST /kyc/callback` — provider webhook with result

**Services**

- KYC Orchestrator (service that starts flow with provider and records status).
- Short-term storage (encrypted) for files until processing.
- Job workers to reconcile callbacks.

**Third parties**

- Onfido / Veriff / Jumio (OCR + liveness + matching). Choose based on coverage and cost for your market.
- For CNPJ and companies in Brazil: integrate with Serpro / Receita WS (or commercial APIs) for business validation.

**Security / privacy**

- Do not store images/documents longer than necessary; use provider IDs (do not retain raw images).
- Encrypted-at-rest (SSE-KMS), access audit.
- Retention policy (e.g., delete images after X days, keep proof-hash long-term).

---

# 3) Publish listing and proofs of the item/service

**UI:** create title/description, upload photos and a short video.

**Endpoints**

- `POST /listings` — creates a draft listing (status: draft)
- `PUT /listings/:id/upload-url` — generates presigned URL for S3
- `POST /images/notify` — callback when upload is complete (or processing via consumer)
- `POST /listings/:id/publish` — requests publication (triggers checks)

**Services**

- Listings Service (DB: listings, images_meta)
- Object Storage (S3/R2) — files via presigned URLs
- Image Processor Worker — generates pHash, extracts EXIF, creates thumbnails, verifies size/format
- Reverse-image check module (local DB + third-party reverse search)
- Fraud Scoring Service — applies rules/score (duplicate image, template text, user age)

**Third parties / libs**

- Storage: AWS S3 + CloudFront or Cloudflare R2 + CDN
- Image analysis: ImageMagick, pHash lib, Google Vision (safe-search + label detection)
- Reverse image: Google Reverse Image / Bing Image Search API (if needed)

**Validations**

- Reject uploads with missing EXIF when expected; mark listing as “requires manual review” if pHash matches public images.
- Watermark generation: apply user id + timestamp (server-side) to at least one image version to prevent repost fraud.

---

# 4) Search, chat and create proposal (trade)

**UI:** user B proposes a trade for listing A, chats to negotiate.

**Endpoints**

- `POST /trades` — creates trade (listing_id, proposer_id, counter_listing_id|counter_desc, est_value)
- `GET /trades/:id` — retrieve trade
- `POST /messages` — send message in chat (associated to trade)

**Services**

- Trade Service (states: pending → in_progress → completed → disputed → cancelled)
- Messaging Service (persist chat, attachments via presigned URLs)
- Reputation Service (read user reputation/limits)
- Fraud Service (score trade at creation)
- API Gateway enforces auth & role checks

**Checks**

- At creation: check user KYC level, reputation_score, listing verification_level, local limits.
- If score > threshold → route to manual review / block / require additional stake.

---

# 5) Escrow / security deposit (safeguard mechanism)

**Goal:** hold internal credits/tokens as collateral; avoid real money flow but allow penalties.

**Design**

- Internal Wallet Service with ledger (immutable entries): each operation is a DB transaction that writes ledger entry and updates balance.
- Escrow Service: state machine (hold, partial_release, release, refund, claim). Tied to trade_id.

**Endpoints**

- `POST /escrow/:trade_id/hold` — creates hold (reserve credits)
- `POST /escrow/:trade_id/release` — releases (requires event: both confirmed OR moderator)
- `POST /escrow/:trade_id/claim` — opens dispute/claim against escrow

**Integrations**

- Payment Provider (only if user deposits fiat to convert to credits): Stripe / Mercado Pago connector
- Optional: stablecoin/crypto if you want on-chain (complex) — not recommended for MVP.

**Implementation notes**

- Ledger must be ACID (use RDBMS with strong transactions or append-only ledger + reconciliation).
- Idempotency keys on endpoints.
- Holds should expire after configurable TTL; automated escalation job on expiry.

**Security**

- 2FA required to release large escrows.
- Audit log entries for every ledger mutation.

---

# 6) Acceptance, scheduling and execution

**UI:** owner accepts proposal; schedule time; perform service/product exchange.

**Endpoints**

- `POST /trades/:id/accept`
- `POST /trades/:id/schedule` — saves date/time/location
- `POST /trades/:id/confirm-delivery` — attaches evidence (presigned URL)
- `POST /trades/:id/request-code` — (optional) generates confirmation code for meetup

**Services**

- Trade Service updates state; Scheduling Service (calendar reminders) — integrate with Google Calendar optional.
- Notification Service (email, push, SMS) — Twilio/SendGrid.
- Evidence ingestion pipeline (upload -> process -> store metadata/hashes).

**Checks**

- On `confirm-delivery`: validate evidence (image/video checksum, EXIF time, pHash comparison).
- If both parties confirm => call `POST /escrow/:id/release`.

---

# 7) Escrow release + reputation

**Endpoints**

- `POST /escrow/:id/release` — triggered when both confirmations received OR auto-release rules passed
- `POST /users/:id/reputation-update` — increment reputation, write audit

**Services**

- Escrow Service performs ledger credit/debit, posts events to Event Bus (Kafka/Rabbit).
- Reputation Service recalculates trust score and level.
- Notification Service informs parties.

**Safeguards**

- Delay window for auto-release (configurable, e.g.: 24–72h) to allow dispute opening.
- Manual override by moderator only.

---

# 8) Dispute and moderation

**UI:** open dispute, attach evidence.

**Endpoints**

- `POST /disputes` — creates ticket (trade_id, complainant, evidence_links)
- `GET /moderation/disputes` — for moderators
- `POST /moderation/disputes/:id/verdict` — applies decision (refund, release, suspend user)
- `POST /moderation/escalate` — send to legal/external

**Services**

- Moderation UI (dashboard)
- Evidence Viewer (secure URLs, watermarking, time-limited access)
- Fraud Service re-score using new evidence
- Escrow Service invoked per verdict
- Audit / Case DB for legal records

**Process**

- Auto-triage rules (if evidence matches pattern → automatic partial refund or auto-dismiss).
- Human-in-the-loop for medium/high risk cases.
- Keep all evidence + logs exportable for legal if needed.

**Policies**

- SLA times (e.g., initial triage 24h, verdict 3–7 days).
- Penalty engine: deduct stake, suspend, ban, notify authorities (if criminal).

---

# 9) Infrastructure, observability and operational security

**Infra components**

- API Gateway (rate limiting, WAF)
- Services: Auth, User, Listing, Trade, Escrow, Wallet, Messaging, KYC Orchestrator, ImageProcessor, Fraud, Moderation
- DB: Postgres (primary), Redis (cache+rate limiter), ElasticSearch (search), MinIO/S3 (object), Kafka/RabbitMQ (event bus)
- Workers: Celery / Sidekiq / Cloud Functions
- Secrets: Vault (HashiCorp) or AWS Secrets Manager
- CI/CD: pipeline with SAST/DAST, canary deploy
- Backups + point-in-time recovery

**Logging & monitoring**

- Centralized logs (ELK / Datadog), tracing (OpenTelemetry), SIEM for alerts.
- Audit logs immutable (append-only table, write-once policy), exportable.

**Security controls**

- WAF, IDS/IPS, DDoS protection (Cloudflare/AWS Shield)
- MFA enforced for admin/moderator access
- Pen-tests, bug bounty, monthly dependency scans
- Privacy: LGPD/GDPR compliance, data minimization, retention policies

---

# 10) Recommended stacks and practical libs

- **Auth & Identity:** Keycloak (self-hosted) or Auth0 (managed) + TOTP lib (otplib).
- **KYC:** Veriff / Onfido / Jumio.
- **SMS/Email:** Twilio / Zenvia, SendGrid / SES.
- **Storage:** AWS S3 + CloudFront / Cloudflare R2.
- **Image processing:** Python + Pillow + imagehash (pHash) + Google Vision API.
- **Worker / queue:** Celery + RabbitMQ / Redis or AWS SQS + Lambda.
- **DB:** PostgreSQL (ACID ledger), Redis (cache + rate limit).
- **Payments (optional):** Stripe Connect / Mercado Pago (Brazil) to accept fiat to credits.
- **ML / Anti-fraud:** Sift (SaaS) or build scoring with scikit-learn / LightGBM using features; start with rule-based thresholds.
- **Observability:** ELK / Datadog, OpenTelemetry.

---

# 11) Critical business rules / invariants to implement

1. **Escrow atomicity:** hold/release must be transactional — ledger entry + trade state change in same DB transaction or via idempotent distributed transaction pattern.
2. **Idempotency in financial endpoints:** clients use idempotency key for /escrow/hold and /escrow/release.
3. **Presigned uploads:** server only receives metadata; blobs do not pass through the API to reduce cost and risk.
4. **TTL for evidence:** evidence kept for X days; hashes retained indefinitely for audit.
5. **Progressive limits:** new_user_max_value < verified_user_max_value < pro_max_value.
6. **All actions logged:** who, when, ip, device, request_id.

---

# 12) Quick mapping (summary by step -> endpoint/service)

- Registration: `POST /auth/register` → Auth Service, Email/SMS provider, FraudService(score)
- Identity verification: `POST /kyc/request` → KYC Orchestrator → Onfido/Veriff → callback `POST /kyc/callback`
- Create listing: `POST /listings` → Listings Service; `PUT /listings/:id/upload-url` → S3 presigned → ImageProcessor → FraudService
- Proposal: `POST /trades` → Trade Service → FraudService + ReputationService → `POST /escrow/:trade_id/hold` (Escrow Service)
- Acceptance/scheduling: `POST /trades/:id/accept` + `POST /trades/:id/schedule` → Notification Service
- Confirmation: `POST /trades/:id/confirm-delivery` → Evidence ingestion → ImageProcessor/FraudService → if ok `POST /escrow/:id/release`
- Dispute: `POST /disputes` → Moderation Service → Escrow Service action → update Reputation & Audit

---
---
---
---

# Onboarding (registration and initial setup, plain language)

1. **Create account**
- **User does:** provides email, phone and creates password.
- **App checks:** sends codes to confirm email and SMS.
- **Result:** account created; basic access granted.

2. **Enable extra protection**
- **User does:** enables two-step verification (SMS code or authenticator app).
- **App checks:** confirms that protection is active for sensitive actions (accepting higher-value trades, changing data).
- **Result:** account is more secure.

3. **Complete profile**
- **User does:** profile photo, display name, city/operating radius, short description.
- **App checks:** appropriate content, no suspicious external links.
- **Result:** profile ready to list and propose trades.

4. **Identity verification (anti-fraud) by levels**
- **User does:** submits document photo and a quick selfie (only when wanting to trade medium/high values).
- **App checks:** compares document and selfie, confirms real person.
- **Result:**
    - **Basic Level:** browse, list and trade low-value items.
    - **Verified Level:** allows higher-value trades and gives trust badge.
    - **Advanced Level (optional):** for professionals/companies, increases limits and visibility.

5. **Quick security tour**
- **User sees:** best practices (how to prove service/product, how escrow works, and ratings).
- **Result:** user understands “how it works” before first trade.

---

# Publish a listing (offer of product/service)

1. **Create listing**
- **User does:** title, clear description, approximate value for trade reference, location/online or in-person.
- **App checks:** required fields and appropriate language.

2. **Proofs of what is offered**
- **User does:** uploads photos and, if possible, a short video showing the product/service.
- **App checks:** minimum quality, signs of stolen/duplicated images, approximate date/location when relevant.
- **Result:** “verified” listing gains prominence and more trust.

3. **Publication**
- **App checks:** automated anti-fraud filters; if something seems off, sends to quick review.
- **Result:** listing published (with “basic”, “verified” or “professional” badge based on profile level).

---

# Make a proposal and close the trade

1. **Find and chat**
- **User B does:** finds User A’s listing, sends a proposal describing what they offer in exchange and approximate value.
- **App checks:** User B limits (new, identity verified for higher values), and risk signals.
- **Result:** chat opens in the app.

2. **Formal proposal**
- **User B does:** records the proposal in the app (“I want X in exchange for Y”).
- **App checks:** both have profiles and listings/proofs sufficient for that trade value.
- **Result:** proposal created, User A notified.

3. **Security deposit (escrow)**
- **Both do:** place a symbolic deposit inside the app (internal credits), returned when trade completes well.
- **App checks:** balance/limits and applies rules: new users deposit less and only for low-value trades; verified profiles can trade larger amounts.
- **Result:** proposal becomes “protected”; financial consequences deter fraud.

4. **Acceptance and scheduling**
- **User A does:** accepts the proposal.
- **Both do:** agree date/time/location (or online link).
- **App checks:** sends reminders and records the arrangement.
- **Result:** trade scheduled.

5. **Execution with confirmation**
- **Both do:** perform the exchange.
- **App guides:** may use a confirmation code at the end of the session or request a quick photo/video as proof (e.g., photo of delivered item or final service screen).
- **Result:** each marks “completed” in the app.

6. **Release of deposit and reputation**
- **App checks:** if both confirmed, returns deposit and records the trade as successful.
- **Both do:** rate each other with score and comment (mandatory if problem).
- **Result:** reputation increases, future limits improve.

---

# If something goes wrong (cancellation, no-show or dispute)

1. **Cancellation before the day**
- **Simple rule:** free cancellation within an agreed window; after that, small penalty for the canceller.
- **Result:** reduces last-minute dropouts.

2. **No-show**
- **Rule:** no-show without notice loses part or all of the deposit, and reputation is affected.
- **Result:** discourages bad behavior.

3. **Dispute**
- **The aggrieved party does:** opens a dispute in the app explaining the issue and attaching evidence (messages, photos, videos).
- **App does:** automatic triage and, when necessary, moderation team reviews and decides.
- **Result:** deposit can compensate the harmed party; bad actors can be suspended/banned.

---

# Security rules that operate “behind the scenes”

- **Continuous anti-fraud system:** watches suspicious patterns (many accounts on same device, copied images, proposals with values far from market).
- **Limits by trust:** new users start with lower value/quantity limits; as they complete successful trades and verifications, limits increase.
- **Account protection:** sensitive actions (accepting high-value trades, changing data, withdrawing credits) require extra code.
- **Privacy and data:** only necessary data is stored; proofs are kept for a limited time to assist disputes.

---

# Ultra-brief version for presentation

1. Create account → confirm email and phone → enable extra protection.
2. Complete profile → if you want higher values, do quick identity verification.
3. Publish listing with proofs.
4. Receive proposal and both put a security deposit.
5. Perform the trade and confirm in the app (with code or proof).
6. Deposit returned and reputation increases.
7. If issues, dispute inside the app with review and decision.
