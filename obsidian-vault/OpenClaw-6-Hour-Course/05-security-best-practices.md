# OpenClaw — Security Best Practices

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## ⚠️ CRITICAL: 5 Security Rules

### Rule 1: Don't Use VPS Without Proper Security

- People are **actively scanning** for exposed OpenClaw instances
- If you must use VPS, use proper authentication and firewall rules
- **Better option:** Use Cloudflare Workers (Molt Worker) for sandboxed setup
- Never expose the gateway port publicly without authentication

### Rule 2: Don't Connect Personal Email

- **Risk:** Prompt injection — someone emails you malicious instructions that OpenClaw may execute
- **If you need email:** Create a separate email account for OpenClaw only
- Set strict filters on what it can access
- Consider using a dedicated email with limited permissions

### Rule 3: Protect Your API Keys

- **Never** share screenshots with API keys visible
- Store keys in **environment variables**, not plain text files
- Use API keys with **minimal required permissions**
- Rotate keys if you suspect they've been exposed
- Monitor your API usage for unexpected spikes

### Rule 4: Start Small

- Begin with **test accounts** — don't give full system access immediately
- Test in **sandbox environments** first
- Gradually increase permissions as you verify everything works
- Don't connect sensitive systems (banking, production databases) on day one

### Rule 5: Set Spending Limits

- All AI APIs have spending limits — **set them!**
- Monitor token usage regularly
- Some models (Claude Opus) burn through tokens quickly
- Set up alerts for unusual usage patterns
- Consider using cheaper models for high-volume tasks

## Security Checklist

- [ ] Running locally or on properly secured VPS (not exposed)
- [ ] API keys stored in environment variables
- [ ] Spending limits set on all API accounts
- [ ] Test accounts used for initial setup
- [ ] No personal email connected (or separate account created)
- [ ] Separate WordPress account created for OpenClaw (not your admin account)
- [ ] Browser extension properly sandboxed
- [ ] Regular monitoring of logs and usage

## Additional Security Tips

- Keep OpenClaw updated to the latest version
- Review installed skills — remove any you don't recognize
- Use a dedicated Docker network for OpenClaw containers
- Enable Traefik authentication for web-facing services
- Regularly audit connected messaging app sessions

---

## Metadata

- Tags: `openclaw`, `security`, `best-practices`, `api-keys`
- Related: [[01 - Installation & Setup]] | [[04 - Skills & Plugins]]
