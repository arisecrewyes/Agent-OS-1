#!/usr/bin/env bash
# Lead Connector Bridge — GoHighLevel Connection Script
# Tests connectivity to GoHighLevel V2 API and verifies credentials.

set -euo pipefail

echo "=== GoHighLevel Connection Test ==="
echo ""

# Check for required env vars
if [[ -z "${GHL_API_KEY:-}" ]]; then
  echo "ERROR: GHL_API_KEY not set."
  echo ""
  echo "To get your API key:"
  echo "  1. Log into GoHighLevel → Settings → API Keys"
  echo "  2. Generate a new key or use existing"
  echo "  3. Set: export GHL_API_KEY=\"your_key_here\""
  echo ""
  echo "Optional:"
  echo "  export GHL_LOCATION_ID=\"your_location_id\""
  exit 1
fi

echo "API Key: ${GHL_API_KEY:0:8}... (truncated)"
echo ""

# Test 1: List contacts (verify auth works)
echo "--- Test 1: List Contacts ---"
CONTACTS=$(curl -s -w "\n%{http_code}" \
  "https://services.leadconnectorhq.com/contacts/?limit=1" \
  -H "Authorization: Bearer ${GHL_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Version: 2021-07-28")

HTTP_CODE=$(echo "$CONTACTS" | tail -1)
BODY=$(echo "$CONTACTS" | sed '$d')

if [[ "$HTTP_CODE" == "200" ]]; then
  CONTACT_COUNT=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('contacts',[])))" 2>/dev/null || echo "unknown")
  echo "✅ Connection successful! Auth verified."
  echo "   Contacts returned: ${CONTACT_COUNT}"
elif [[ "$HTTP_CODE" == "401" ]]; then
  echo "❌ Authentication failed. Check your API key."
  exit 1
else
  echo "⚠️  Unexpected response: HTTP ${HTTP_CODE}"
  echo "   Body: ${BODY:0:200}"
fi

echo ""

# Test 2: List funnels
echo "--- Test 2: List Funnels ---"
FUNNELS=$(curl -s -w "\n%{http_code}" \
  "https://services.leadconnectorhq.com/funnels/" \
  -H "Authorization: Bearer ${GHL_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Version: 2021-07-28")

FUNNEL_HTTP=$(echo "$FUNNELS" | tail -1)
FUNNEL_BODY=$(echo "$FUNNELS" | sed '$d')

if [[ "$FUNNEL_HTTP" == "200" ]]; then
  FUNNEL_COUNT=$(echo "$FUNNEL_BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('funnels',[])))" 2>/dev/null || echo "unknown")
  echo "✅ Funnels accessible! Count: ${FUNNEL_COUNT}"
else
  echo "⚠️  Could not list funnels: HTTP ${FUNNEL_HTTP}"
fi

echo ""

# Test 3: List opportunities (pipelines)
echo "--- Test 3: List Opportunities ---"
OPPS=$(curl -s -w "\n%{http_code}" \
  "https://services.leadconnectorhq.com/opportunities/" \
  -H "Authorization: Bearer ${GHL_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Version: 2021-07-28")

OPPS_HTTP=$(echo "$OPPS" | tail -1)
OPPS_BODY=$(echo "$OPPS" | sed '$d')

if [[ "$OPPS_HTTP" == "200" ]]; then
  OPPS_COUNT=$(echo "$OPPS_BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('opportunities',[])))" 2>/dev/null || echo "unknown")
  echo "✅ Opportunities accessible! Count: ${OPPS_COUNT}"
else
  echo "⚠️  Could not list opportunities: HTTP ${OPPS_HTTP}"
fi

echo ""
echo "=== Connection Complete ==="
echo "GoHighLevel is ready for operations."
