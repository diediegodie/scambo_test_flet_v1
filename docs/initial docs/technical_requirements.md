1. **Authentication & Authorization**
    
    - OAuth2 / JWT with refresh tokens (signed, short expirations).
        
    - 2FA via SMS or app (TOTP) for sensitive actions.
        
    - Roles: user, verified_user, moderator, admin, audit.
        
2. **Identity Verification**
    
    - Phased onboarding: email + phone -> social login -> lightweight KYC (document + selfie with liveness) -> full KYC (for high limits).
        
    - Integrations with providers: Onfido / Veriff / Jumio (OCR + liveness + matching).
        
    - Store only hashes and provider verification IDs; do not retain images longer than necessary.
        
3. **Item/Service Proofs**
    
    - Mandatory uploads: photos with watermark (userID + date), short video (<=30s) and preserve EXIF metadata.
        
    - Generate pHash/perceptual-hash of images to detect duplicates/theft.
        
4. **Escrow / Internal Credit**
    
    - Internal wallet with immutable ledger; symbolic deposits (internal tokens) to ensure commitment.
        
    - Payment provider (optional) for purchases/settlements (Stripe / Mercado Pago).
        
5. **Fraud Detection**
    
    - Static rules + ML score (features: account age, IP geolocation, EXIF mismatch, language, number of reports, rapid behavior).
        
    - Reverse image search / pHash + comparison with public image databases.
        
6. **Secure Communication**
    
    - Internal messaging (end-to-end not required, but TLS + at-rest encryption).
        
    - Block external links for new users; URL analysis.
        
7. **Rate limiting, anti-bot and device fingerprinting**
    
    - Rate limits per IP / user / device.
        
    - Adaptive CAPTCHAs and headless-browser detection.
        
    - Lightweight fingerprint (user-agent, accept headers, optional canvas hash).
        
8. **Logs, auditing and monitoring**
    
    - Immutable audit logs (append-only), configurable retention.
        
    - Fraud metrics and alerts: disputes, new verified profiles, spikes.
        
9. **Dispute process**
    
    - Endpoint to open dispute with evidence (photo, video, chat).
        
    - Queues for automatic/human review; SLA and verdict documented.
        
10. **Privacy & compliance**
    
    - TLS 1.2+; at-rest AES-256.
        
    - Data retention policies; support for deletion requests (LGPD/GDPR).
        
    - Clear consent for KYC and data use.
        
11. **Infra & sec ops**
    
    - WAF, IDS/IPS, backups, secrets in vault, secure CI/CD deployments.
        
    - Periodic pentests and bug-bounty.
        

# Recommended third parties (for security and convenience)

- **KYC / Liveness / OCR:** Onfido, Veriff, Jumio.
    
- **Payments & wallets:** Stripe (Connect), Mercado Pago (Brazil).
    
- **SMS / 2FA:** Twilio, Vonage, Telesign (or local providers).
    
- **Image search / detection:** Google Vision API (safe-search), reverse image services; pHash libraries for local deduplication.
    
- **Anti-fraud / ML:** Sift, Riskified (or build internal scoring with simple models).
    
- **Secure storage:** AWS S3 with SSE + presigned URLs; Cloudflare R2 as alternative.  
    (Integrate by IDs and hashes; minimize storage of sensitive data.)
    

# Database design (essentials)

- Users (id, email_hash, phone_hash, role, kyc_status, reputation_score, created_at)
    
- Profiles (user_id, display_name, location, verified_badges)
    
- Listings (id, owner_id, title, description, value_estimate, images_meta, video_meta, verification_level, created_at, status)
    
- Images (id, listing_id, phash, exif_hash, s3_key, uploaded_at)
    
- Wallets (user_id, balance, ledger_entries)
    
- Trades/Offers (id, listing_id, proposer_id, counter_listing_id / counter_description, status, escrow_id, offered_value, timestamps)
    
- Escrow (id, trade_id, amount_credits, state, hold_until, release_timestamp)
    
- Disputes (id, trade_id, complainant_id, evidence_links, status, verdict, moderator_id)
    
- AuditLogs (entity, action, actor_id, timestamp, metadata)
    
- Devices (device_id, user_id, fingerprint_hash, last_seen, geo)
    

# Endpoints (REST) — grouped by area

Notes: all endpoints must use HTTPS; sensitive endpoints require JWT + 2FA/role checks. Limit upload body sizes and use presigned URLs for files.

## Auth & user

- `POST /auth/register`
    
    - Body: { email, password, display_name, phone }
        
    - Returns: { user_id, email_verification_token }
        
    - Actions: create user, send email + SMS.
        
- `POST /auth/login`
    
    - Body: { email, password }
        
    - Returns: { access_token, refresh_token, mfa_required }
        
- `POST /auth/refresh`
    
    - Body: { refresh_token } -> new access token.
        
- `POST /auth/verify-email`
    
    - Body: { token }.
        
- `POST /auth/enable-2fa`
    
    - Requires: JWT; response: provisioning URI or SMS setup.
        
- `POST /auth/verify-2fa`
    
    - Body: { code }.
        
- `POST /auth/social-callback`
    
    - OAuth callback for Google/Facebook/LinkedIn.
        

## KYC / Verification

- `POST /kyc/request`
    
    - Body: { user_id, level_requested } -> creates flow; returns provider_session_id (Onfido/Veriff).
        
- `GET /kyc/status`
    
    - Params: user_id -> status (pending/approved/rejected), provider_report_id.
        
- `POST /kyc/upload-doc` (using presigned URL)
    
    - Body: { doc_type, presigned_url_meta }.
        
- `POST /kyc/selfie`
    
    - Body: presigned_url for video/selfie.
        

## Listings / item or service proofs

- `POST /listings`
    
    - Auth: JWT. Body: { title, description, est_value, location, required_proofs_level }
        
    - Result: listing_id; force upload of images/video before publishing.
        
- `PUT /listings/:id/upload-url`
    
    - Generate presigned URL for images/videos; save metadata (phash, exif).
        
- `GET /listings/:id`
    
    - Public, returns verification status and badges.
        
- `POST /listings/:id/verify-evidence`
    
    - (Internal/automatic) receives hashes and performs pHash check, reverse-search flag.
        

## Proposals & trades

- `POST /trades`
    
    - Body: { listing_id, proposer_id, counter_listing_id | counter_description, offered_value_estimate }
        
    - Auth required. Create trade, status = pending, lock stake/escrow if applicable.
        
- `POST /trades/:id/accept`
    
    - Auth; check verifications/limits; move trade to `in_progress`; create escrow.
        
- `POST /trades/:id/confirm-delivery`
    
    - Auth; each party confirms delivery/service with evidence (photo/video + timestamp). When both confirm -> release escrow.
        
- `POST /trades/:id/cancel`
    
    - Rules and penalties applied (depends on role/age/reputation).
        

## Escrow & wallet

- `GET /wallet`
    
    - Returns balance, holds, ledger (paginated).
        
- `POST /wallet/deposit`
    
    - Initiates deposit flow (provider idempotent).
        
- `POST /escrow/:id/hold`
    
    - Internal: secure credits/tokens; record hold.
        
- `POST /escrow/:id/release`
    
    - Requires approvals: both confirmed or moderator verdict.
        
- `POST /escrow/:id/claim`
    
    - Open claim -> creates dispute automatically.
        

## Disputes & moderation

- `POST /disputes`
    
    - Body: { trade_id, complainant_id, reason_code, evidence: [links] }
        
    - Generates ticket; auto-triage (score); if high score -> auto-temporary suspension of the other user.
        
- `GET /moderation/disputes`
    
    - For moderators: prioritized listing.
        
- `POST /moderation/disputes/:id/verdict`
    
    - Moderator decides: refund credits, release escrow, suspend user, ban.
        
- `POST /reports/profile`
    
    - User can report profile/listing; creates a case.
        

## Images / anti-fraud

- `POST /images/phash-check` (internal)
    
    - Body: { phash } -> returns similar_count, matches (ids).
        
- `GET /images/:id/metadata`
    
    - Returns EXIF, upload_ip, uploader_id, phash.
        

## Admin / audit

- `GET /admin/audit-logs`
    
    - Filter by actor, action, timeframe.
        
- `POST /admin/ban-user`
    
    - Bans, reason, duration.
        
- `GET /metrics/fraud`
    
    - KPIs for dashboards.
        

## Notifications / messaging

- `POST /messages`
    
    - Internal messages between users linked to trade/listing; attachments via presigned URLs.
        
- `GET /notifications`
    
    - Push/email/in-app history.
        

# Important rules per endpoint

- All uploads via presigned URL; server only receives metadata, hashes, and secure link.
    
- Validate MIME type + sizes + limits.
    
- Content scanner: check EXIF against declared location; if high mismatch -> flag.
    
- Rate limit per endpoint and by user role (e.g.: new users: 5 listings/day).
    

# Security flows (practical summary)

1. New user: register -> email+SMS -> limited publishing (low value) -> require proofs (photo+video) -> allow small trade.
    
2. Medium/high-value trade: require lightweight KYC and stake/escrow; enforce mandatory 2FA.
    
3. Dispute: collect all evidence, apply automatic rules (score) and escalate to human; block reputation and hold credits until verdict.
    

# Logs, storage and retention

- Archive evidences for X days (configurable), keep hashes indefinitely.
    
- Record chain-of-actions for each trade (who did what, when, ip, device).
    
- Provide API to export logs for audit (admins/authorities only).
    

# Additional operational security

- Secrets in Vault (HashiCorp), using short-lived creds for services.
    
- CI pipeline with SAST/DAST scans; deploy with Canary + rollback.
    
- WAF and rules for OWASP Top 10.
