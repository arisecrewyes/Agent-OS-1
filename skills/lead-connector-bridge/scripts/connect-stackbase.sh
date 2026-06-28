#!/usr/bin/env bash
# Lead Connector Bridge — GoStackBase Connection Script
# Tests connectivity to GoStackBase API and verifies credentials.

set -euo pipefail

echo "=== GoStackBase Connection Test ==="
echo ""

if [[ -z "${STACKBASE_API_KEY:-}" ]]; then
  echo "ERROR: STACKBASE_API_KEY not set."
  echo ""
  echo "To get your API key:"
  echo "  1. Log into GoStackBase (Premium or Elite plan required)"
  echo "  2. Go to Settings → API / Integrations"
  echo "  3. Generate API key"
  echo "  4. Set: export STACKBASE_API_KEY=\"your_key_here\""
  echo ""
  echo "Note: GoStackBase API is only available on Premium ($119/mo) and Elite ($239/mo) plans."
  echo "      GoStackBase does NOT have public funnel share links."
  echo "      Templates must be recreated via the dashboard UI or API."
  exit 1
fi

echo "API Key: ${STACKBASE_API_KEY:0:8}... (truncated)"
echo ""

# Test: List contacts
echo "--- Test: List Contacts ---"
RESPONSE=$(curl -s -w "\n%{http_code}" \
  "https://gostackbase.com/api/contacts?limit=1" \
  -H "Authorization: Bearer ${STACKBASE_API_KEY}" \
  -H "Content-Type: application/json")

HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | sed '$d')

if [[ "$HTTP_CODE" == "200" ]]; then
  echo "✅ Connection successful! Auth verified."
  echo "   Response: ${BODY:0:200}"
elif [[ "$HTTP_CODE" == "401" ]]; then
  echo "❌ Authentication failed. Check your API key."
  exit 1
elif [[ "$HTTP_CODE" == "403" ]]; then
  echo "❌ Access forbidden. Ensure you have a Premium or Elite plan."
  exit 1
else
  echo "⚠️  Unexpected response: HTTP ${HTTP_CODE}"
  echo "   Body: ${BODY:0:200}"
  echo ""
  echo "Note: GoStackBase API endpoints may not be publicly documented."
  echo "      You may need to use the dashboard UI for template creation."
fi

echo ""
echo "=== Connection Complete ==="
