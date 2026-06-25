const express = require('express');
const app = express();
app.use(express.json());

const TOOL_REGISTRY = {
  openclaw: { name: "OpenClaw", containers: [{ url: "http://openclaw-oi15-openclaw-1", port: 51461 }] },
  "openclaw-2": { name: "OpenClaw #2", containers: [{ url: "http://openclaw-x9sc-openclaw-1", port: 51461 }] },
  hermes: { name: "Hermes Agent", containers: [{ url: "http://hermes-agent-7llb-hermes-agent-1", port: 4860 }] },
  "memory-engine": { name: "Memory Engine", containers: [{ url: "http://memory-engine", port: 8090 }] },
  "memory-brain": { name: "Memory & Brain", containers: [{ url: "http://memory-engine", port: 8090 }] },
  "skill-master": { name: "Skill Master", containers: [{ url: "http://skill-master", port: 9100 }] },
  "content-creator": { name: "Content Creator", containers: [{ url: "http://content-creator", port: 8080 }] },
  "osint-specialist": { name: "OSINT Specialist", containers: [{ url: "http://osint-sherlock", port: 9090 }] },
  "hermes-automation": { name: "Hermes Automation", containers: [{ url: "http://hermes-agent-7llb-hermes-agent-1", port: 4860 }] },
  "conductor-stack": { name: "Conductor", containers: [{ url: "http://conductor", port: 3002 }] },
  "hermes-voice": { name: "Hermes Voice", containers: [{ url: "http://hermes-voice", port: 8643 }] },
  "bolt-diy": { name: "Bolt DIY", containers: [{ url: "http://bolt-diy", port: 5173 }] },
  "goldie-stack": { name: "Goldie Stack", containers: [{ url: "http://goldie-codex", port: 8651 }] },
  "minimax-hermes": { name: "MiniMax M3", containers: [{ url: "http://minimax-hermes", port: 8660 }] },
  "odysseus-agent": { name: "Odysseus", containers: [{ url: "http://odysseus", port: 7000 }] },
  "second-brain": { name: "Second Brain", containers: [{ url: "http://second-brain", port: 8095 }] },
  "universal-gateway": { name: "Universal API Gateway", containers: [{ url: "http://universal-api-gateway", port: 8889 }] },
  "getting-started-agent": { name: "Getting Started", containers: [] }
};

app.get('/health', (req, res) => res.json({ status: 'ok', uptime: process.uptime() }));
app.get('/agents', (req, res) => res.json({ agents: Object.keys(TOOL_REGISTRY), count: Object.keys(TOOL_REGISTRY).length }));

app.post('/route', async (req, res) => {
  const { agentId, message } = req.body;
  if (!agentId || !message) return res.status(400).json({ error: 'agentId and message required' });
  const agent = TOOL_REGISTRY[agentId];
  if (!agent) return res.status(404).json({ error: `Agent '${agentId}' not found`, available: Object.keys(TOOL_REGISTRY) });
  const t = agent.containers[0];
  if (!t || !t.url) return res.status(503).json({ error: `'${agent.name}' has no active container` });
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 30000);
    const r = await fetch(`${t.url}:${t.port}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
      signal: controller.signal
    });
    clearTimeout(timeout);
    const d = await r.json();
    res.json({ agent: agent.name, agentId, response: d });
  } catch(e) {
    res.status(502).json({ error: e.message, agent: agent.name, target: `${t.url}:${t.port}` });
  }
});

app.listen(8888, '0.0.0.0', () => {
  console.log('Agent OS Connector listening on :8888');
  console.log(`Registered ${Object.keys(TOOL_REGISTRY).length} agents`);
});
