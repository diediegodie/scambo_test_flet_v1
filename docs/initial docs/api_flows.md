```
```
from graphviz import Digraph

dot = Digraph("detailed_trade_flow", format="png")
dot.attr(rankdir="LR")

# Nodes (minimal)
dot.node("U1", "User A")
dot.node("U2", "User B")
dot.node("API", "API Gateway / App API")
dot.node("AUTH", "Auth Service\n(JWT, 2FA)")
dot.node("USER", "User Service / DB")
dot.node("KYCP", "KYC Provider\n(Onfido/Veriff)")
dot.node("STORAGE", "Object Storage\n(S3 / CDN)")
dot.node("IMGPROC", "Image Processor\n(pHash, EXIF, reverse search)")
dot.node("FRAUD", "Fraud Detection\n(ML + Rules)")
dot.node("LIST", "Listings Service")
dot.node("TRADE", "Trade Service")
dot.node("ESCROW", "Escrow / Wallet Service\nLedger")
dot.node("PAY", "Payment Provider\n(Stripe / MercadoPago)")
dot.node("MSG", "Messaging Service")
dot.node("NOTIF", "Notification Service\n(Email/SMS/Push)")
dot.node("MOD", "Moderation Service / Admin UI")
dot.node("AUDIT", "Audit Logs / SIEM")

# Registration & verification flow
dot.edge("U1", "API", "POST /auth/register\n-> triggers: Email provider, SMS provider")
dot.edge("API", "AUTH", "POST /auth/login\nPOST /auth/verify-email\nPOST /auth/verify-phone\nPOST /auth/enable-2fa")
dot.edge("AUTH", "USER", "create / update user record\nJWT issued, store 2FA status")
dot.edge("API", "FRAUD", "on register: scoreUser(user_id)")

# Listing creation flow (evidence upload)
dot.edge("U1", "API", "POST /listings\n(body: title, desc, est_value, proofs_level)")
dot.edge("API", "LIST", "create listing record -> status=draft")
dot.edge("API", "STORAGE", "POST /listings/:id/upload-url\n-> presigned URL returned")
dot.edge("U1", "STORAGE", "PUT upload image/video to S3 (presigned URL)")
dot.edge("STORAGE", "API", "callback/notify upload complete\n(POST /images/notify)")
dot.edge("API", "IMGPROC", "POST /images/phash-check\nPOST /images/exif-validate")
dot.edge("IMGPROC", "FRAUD", "if suspicious -> flag listing")
dot.edge("API", "LIST", "POST /listings/:id/publish\n-> triggers: FRAUD check, badge assignment")
dot.edge("API", "AUDIT", "log: listing_created/listing_published")

# Trade proposal flow
dot.edge("U2", "API", "POST /trades\n(body: listing_id, counter_listing_id|counter_desc)")
dot.edge("API", "TRADE", "create trade record (status=pending)")
dot.edge("TRADE", "USER", "check limits, reputation, kyc_status\n(GET /users/:id/kyc-status)")
dot.edge("TRADE", "FRAUD", "scoreTrade(trade_id)")
dot.edge("TRADE", "ESCROW", "POST /escrow/:trade_id/hold\n(hold credits/stake)")
dot.edge("ESCROW", "PAY", "if low balance -> initiate /wallet/deposit (payment provider)")
dot.edge("API", "NOTIF", "notify parties (in-app/email/sms)")

# Acceptance & scheduling
dot.edge("U1", "API", "POST /trades/:id/accept")
dot.edge("API", "TRADE", "update trade -> in_progress\nlog in AUDIT")
dot.edge("API", "NOTIF", "notify schedule and delivery steps")

# Delivery & confirmation
dot.edge("U1", "API", "POST /trades/:id/confirm-delivery\n(attach evidence: presigned URLs)")
dot.edge("U2", "API", "POST /trades/:id/confirm-delivery\n(attach evidence)")
dot.edge("API", "STORAGE", "POST /trades/:id/upload-evidence -> presigned upload")
dot.edge("API", "IMGPROC", "run evidence validation (EXIF, video timestamp, checksum)")
dot.edge("API", "FRAUD", "re-evaluate trade risk on confirmations")
dot.edge("API", "ESCROW", "POST /escrow/:id/release -> if both confirm or auto-release rules")
dot.edge("ESCROW", "TRADE", "notify trade of funds release\nupdate ledger")
dot.edge("API", "USER", "update reputation score")
dot.edge("API", "AUDIT", "log: trade_completed")

# Dispute flow
dot.edge("U1", "API", "POST /disputes\n(body: trade_id, reason, evidence_links)")
dot.edge("API", "MOD", "create moderation ticket\nPOST /moderation/disputes")
dot.edge("MOD", "API", "POST /moderation/disputes/:id/verdict\n(action: refund/release/suspend/ban)")
dot.edge("MOD", "ESCROW", "invoke /escrow/:id/claim or /escrow/:id/refund")
dot.edge("MOD", "USER", "update user status (suspend/ban)")
dot.edge("MOD", "AUDIT", "log moderator decision")

# Messaging & notifications during flow
dot.edge("U1", "API", "POST /messages (trade_id, text, attachments)")
dot.edge("API", "MSG", "store message, presigned URLs for attachments")
dot.edge("API", "NOTIF", "push notifications on new messages")

# Admin, monitoring, and blocking actions
dot.edge("FRAUD", "MOD", "auto-flag -> create moderation ticket\n(POST /moderation/disputes)")
dot.edge("FRAUD", "API", "block or throttle user via /admin/ban-user or rate-limit")
dot.edge("API", "AUDIT", "write: login_attempts, suspicious_activity")

# Minimal legend note as a node (no style)
dot.node("LEG", "Endpoints shown on edges (POST/GET) and services called\nS3=Storage, KYC=KYC Provider, PAY=Payment Provider")

output_path = "/mnt/data/trade_flow_endpoints.png"
dot.render(output_path, cleanup=True)
output_path

```

```
# Flow of a secure exchange (layman's version)

1. **User registration**
    
    - João opens the app, creates an account, and confirms their phone number and email.
        
    - The app may also ask for a quick identity check, like a photo of an ID and a selfie. This is an **anti-fraud system** to ensure the person is real.
        
2. **Posting an offer**
    
    - João wants to offer **guitar lessons** in exchange for some service.
        
    - To post, he must provide photos, videos, or a detailed description, which the **app checks** before showing it.
        
3. **Another user makes an offer**
    
    - Maria sees João's listing and proposes a swap: she offers **English lessons** in exchange for the guitar lessons.
        
    - Before confirming, the app may also ask Maria to complete the same identity verification.
        
4. **Trade guarantee (escrow)**
    
    - To prevent scams, the app creates a “security hold”: both put a **symbolic deposit** into the platform as a guarantee.
        
    - This deposit is only released when both confirm the exchange is complete.
        
5. **Scheduling and performing the exchange**
    
    - The app helps João and Maria arrange time/place.
        
    - They perform the exchange: João gives guitar lessons, Maria gives English lessons.
        
6. **Confirmation**
    
    - Afterwards, each person marks “Exchange successfully completed” in the app.
        
    - Once both confirm, the system returns the symbolic deposit and increases each user's reputation.
        
7. **If there's a problem (dispute)**
    
    - If Maria claims she completed the exchange but João disputes it, a **dispute is opened in the app**.
        
    - Both submit evidence (messages, photos, videos).
        
    - Moderation reviews and decides who is correct.
        
    - The symbolic deposit is used to compensate the party that was wronged.
        

---

This flow makes clear to the average user:

- **Secure registration** (no one is anonymous; everyone goes through a filter).
    
- **Proof of offering** (photos, videos, descriptions).
    
- **Trade guarantee** (symbolic deposit).
    
- **Reputation system** (good behavior builds trust).
    
- **Dispute channel** (to resolve problems).
```
