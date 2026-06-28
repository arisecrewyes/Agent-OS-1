#!/usr/bin/env bash
# Lead Connector Bridge — BuildwithOS Connection Script
# Tests connectivity to BuildwithOS JSON-RPC API and verifies agent key.

set -euo pipefail

echo "=== BuildwithOS Connection Test ==="
echo ""

if [[ -z "${BUILDOS_AGENT_TOKEN:-}" ]]; then
  echo "ERROR: BUILDOS_AGENT_TOKEN not set."
  echo ""
  echo "To get your Agent Key:"
  echo "  1. Log into BuildwithOS"
  echo "  2. Go to Profile → Agent Keys"
  echo "  3. Click Generate"
  echo "  4. Choose your client profile (OpenClaw, Custom HTTP, etc.)"
  echo "  5. Copy the env block"
  echo "  6. Set: export BUILDOS_AGENT_TOKEN=\"boca_your_one_time_secret\""
  echo ""
  echo "Optional:"
  echo "  export BUILDOS_BASE_URL=\"https://build-os.com\""
  echo "  export BUILDOS_CALLEE_HANDLE=\"buildos:user:YOUR_USER_ID\""
  echo "  export BUILDOS_CALLER_KEY=\"openclaw:local:your-handle\""
  exit 1
fi

echo "Agent Token: ${BUILDOS_AGENT_TOKEN:0:12}... (truncated)"
echo ""

BASE_URL="${BUILDOS_BASE_URL:-https://build-os.com}"

# Test 1: Dial (verify connection)
echo "--- Test 1: Connection Dial ---"
DIAL=$(curl -s -w "\n%{http_code}" \
  -X POST "${BASE_URL}/api/agent-call/buildos" \
  -H "Authorization: Bearer ${BUILDOS_AGENT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "call.dial",
    "params": {},
    "id": 1
  }')

HTTP_CODE=$(echo "$DIAL" | tail -1)
BODY=$(echo "$DIAL" | sed '$d')

if [[ "$HTTP_CODE" == "200" ]]; then
  echo "✅ Connection successful! Agent key verified."
  echo "   Response: ${BODY:0:300}"
elif [[ "$HTTP_CODE" == "401" ]]; then
  echo "❌ Authentication failed. Check your agent token."
  echo "   Note: Agent keys are one-time use. Generate a new one if needed."
  exit 1
else
  echo "⚠️  Unexpected response: HTTP ${HTTP_CODE}"
  echo "   Body: ${BODY:0:300}"
fi

echo ""

# Test 2: List Projects
echo "--- Test 2: List Projects ---"
PROJECTS=$(curl -s -w "\n%{http_code}" \
  -X POST "${BASE_URL}/api/agent-call/buildos" \
  -H "Authorization: Bearer ${BUILDOS_AGENT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "call_id": "list-projects-1",
      "name": "list_onto_projects",
      "arguments": {}
    },
    "id": 2
  }')

PROJ_HTTP=$(echo "$PROJECTS" | tail -1)
PROJ_BODY=$(echo "$PROJECTS" | sed '$d')

if [[ "$PROJ_HTTP" == "200" ]]; then
  echo "✅ Projects accessible!"
  echo "   Response: ${PROJ_BODY:0,300}"
else
  echo "⚠️  Could not list projects: HTTP ${PROJ_HTTP}"
  echo "   This may be a scope issue. Ensure your key has read_write access."
fi

echo ""
echo "=== Connection Complete ==="
echo "BuildwithOS is ready for operations."
