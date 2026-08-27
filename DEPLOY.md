# Deploying and switching on the enquiry form

The site is static. The one moving part is `api/enquiry.js`, a Vercel serverless
function that every form on the site posts to.

## What the form does today

Out of the box, with no environment variables set, the form **will not send**. It
validates, shows a clear error, and tells the visitor to email `info@maaliksoft.com`
directly. That is deliberate — better a working fallback than a form that silently
swallows enquiries.

Set one variable and it starts sending. Set three and it is fully hardened.

## The three keys

| Variable | Needed for | Where to get it |
|---|---|---|
| `RESEND_API_KEY` | **Sending at all.** Without it nothing is delivered. | [resend.com](https://resend.com) — free tier covers 3,000 emails a month |
| `TURNSTILE_SECRET_KEY` | Bot protection | [Cloudflare Turnstile](https://dash.cloudflare.com/?to=/:account/turnstile) — free, unlimited |
| `VIRUSTOTAL_API_KEY` | Scanning file uploads | [virustotal.com](https://www.virustotal.com/gui/my-apikey) — free tier, 4 requests a minute |

Add them in Vercel under **Project → Settings → Environment Variables**, then redeploy.

### Optional

| Variable | Default |
|---|---|
| `ENQUIRY_TO` | `info@maaliksoft.com` |
| `ENQUIRY_FROM` | `Maalik website <onboarding@resend.dev>` |

Resend's shared `onboarding@resend.dev` sender works immediately but marks mail as
third-party. Verify `maaliksoft.com` in Resend and set `ENQUIRY_FROM` to something
like `Website enquiries <website@maaliksoft.com>` so replies and deliverability
behave properly.

## Turning the captcha on

Turnstile needs a key in two places:

1. The **secret key** goes in Vercel as `TURNSTILE_SECRET_KEY`.
2. The **site key** is public and goes in the build:
   `_build/pages2.py` → `TURNSTILE_SITE_KEY = "0x4AAA..."`, then rebuild.

Leave the site key empty and the widget is not rendered at all — no broken challenge
box appears. The API then falls back to the honeypot field and the rate limit, which
still stop ordinary spam.

## What happens to an attachment

The RFI form accepts a file up to 25 MB. Before anything is emailed:

1. The extension must be in the allow list (PDF, Word, Excel, ZIP, 7z, text).
2. The **first bytes must match the extension** — a `.pdf` that is not really a PDF is
   refused. An extension is a claim; the file header is evidence.
3. The bytes are uploaded to VirusTotal and the verdict is polled for up to 30 seconds.
4. Anything flagged malicious or suspicious is refused and never reaches the inbox.

With no `VIRUSTOTAL_API_KEY` set, uploads are **refused rather than forwarded
unscanned**, and the visitor is told to send the enquiry without the file. That is the
safe failure direction for a defence contractor's inbox.

## Other protections

- **Honeypot field** — hidden from people, filled in by bots. A submission carrying it
  gets a success response and goes nowhere.
- **Rate limit** — five submissions per IP per ten minutes.
- **Length caps and HTML escaping** on every field, so nothing user-supplied is rendered
  as markup in the notification email.

## Rebuilding after a content change

```bash
python _build/run.py
```

That regenerates all 77 pages, prunes any page whose source entry has been deleted, and
rewrites `sitemap.xml` and `robots.txt`.

## Changing the domain

The sitemap host is set in `_build/run.py`:

```python
def sitemap(base="https://maaliksoft.vercel.app"):
```

Change it and rebuild when the real domain goes live.
