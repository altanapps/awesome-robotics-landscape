import json, os, glob, html

base = "/Users/altan/Desktop/new-chapter/ideas/research/robotics-landscape"

# Bake in the Anthropic key from env so the user doesn't have to paste it.
# WARNING: This makes the resulting index.html contain the key. Do not share/commit it.
EMBEDDED_KEY = os.environ.get('ANTHROPIC_API_KEY', '')

# Load all markdown files
docs = {}
docs["gap-analysis.md"] = open(f"{base}/gap-analysis.md").read()
docs["data-collection-deep-dive.md"] = open(f"{base}/data-collection-deep-dive.md").read()
docs["index.md"] = open(f"{base}/index.md").read()
if os.path.exists(f"{base}/external-second-opinion.md"):
    docs["external-second-opinion.md"] = open(f"{base}/external-second-opinion.md").read()

for f in sorted(glob.glob(f"{base}/companies/*.md")):
    name = os.path.basename(f)
    docs[f"companies/{name}"] = open(f).read()

# Optional: ecosystem files if present
for eco in ["ecosystem-substacks.md", "ecosystem-youtube.md"]:
    p = f"{base}/{eco}"
    if os.path.exists(p):
        docs[eco] = open(p).read()

# Validation research files
research_files = [
    "research-vc-portfolio-scan.md",
    "research-job-posting-signals.md",
    "research-insurance-prior-art.md",
    "research-failure-postmortems.md",
    "research-eu-regulatory.md",
]
for rf in research_files:
    p = f"{base}/{rf}"
    if os.path.exists(p):
        docs[rf] = open(p).read()

verticals = [
    ("1. General-purpose humanoids", ["figure-ai","tesla-optimus","1x-technologies","apptronik","agility-robotics","unitree","boston-dynamics","lute"]),
    ("2. Foundation models", ["physical-intelligence","skild-ai","world-labs","nvidia-isaac-groot","covariant","google-deepmind-robotics","flexion"]),
    ("3. Industrial arms / cobots", ["fanuc","abb-robotics","kuka","universal-robots","doosan-robotics","jaka-robotics","techman-robot"]),
    ("4. Warehouse / fulfillment", ["symbotic","locus-robotics","autostore","geek-plus","greyorange","berkshire-grey","amazon-robotics"]),
    ("5. Last-mile / delivery", ["serve-robotics","starship-technologies","nuro","coco-robotics","avride","zipline"]),
    ("6. Surgical / medical", ["intuitive-surgical","medtronic-hugo","cmr-surgical","distalmotion","moon-surgical","vicarious-surgical"]),
    ("7. Agriculture", ["john-deere","carbon-robotics","monarch-tractor","verdant-robotics","aigen","agco"]),
    ("8. Construction", ["built-robotics","dusty-robotics","canvas","boston-dynamics-spot-construction","nlink-hilti","toggle-industries","spacer-robotics"]),
    ("9. Defense / dual-use", ["anduril","shield-ai","saronic","helsing","skydio","brinc-drones","saildrone"]),
    ("10. Domestic / consumer", ["irobot","roborock","ecovacs","dreame","eufy","matic-robots"]),
    ("11. Hospitality / service", ["pudu-robotics","bear-robotics","keenon-robotics","miso-robotics","chef-robotics","avidbots"]),
    ("12. Picks-and-shovels", ["scale-ai","foxglove","nvidia-isaac-sim","intrinsic","realman","maxon","tangram-vision","pollen-robotics","nomadicml"]),
]

# Display names from index.md ordering
display = {
  "figure-ai":"Figure AI","tesla-optimus":"Tesla Optimus","1x-technologies":"1X Technologies",
  "apptronik":"Apptronik","agility-robotics":"Agility Robotics","unitree":"Unitree",
  "boston-dynamics":"Boston Dynamics","lute":"Lute",
  "physical-intelligence":"Physical Intelligence (π)","skild-ai":"Skild AI","world-labs":"World Labs",
  "nvidia-isaac-groot":"NVIDIA Isaac GR00T","covariant":"Covariant","google-deepmind-robotics":"Google DeepMind Robotics","flexion":"Flexion",
  "fanuc":"FANUC","abb-robotics":"ABB Robotics","kuka":"KUKA","universal-robots":"Universal Robots",
  "doosan-robotics":"Doosan Robotics","jaka-robotics":"JAKA Robotics","techman-robot":"Techman Robot",
  "symbotic":"Symbotic","locus-robotics":"Locus Robotics","autostore":"AutoStore","geek-plus":"Geek+",
  "greyorange":"GreyOrange","berkshire-grey":"Berkshire Grey","amazon-robotics":"Amazon Robotics",
  "serve-robotics":"Serve Robotics","starship-technologies":"Starship Technologies","nuro":"Nuro",
  "coco-robotics":"Coco Robotics","avride":"Avride","zipline":"Zipline",
  "intuitive-surgical":"Intuitive Surgical","medtronic-hugo":"Medtronic Hugo","cmr-surgical":"CMR Surgical",
  "distalmotion":"Distalmotion","moon-surgical":"Moon Surgical","vicarious-surgical":"Vicarious Surgical",
  "john-deere":"John Deere","carbon-robotics":"Carbon Robotics","monarch-tractor":"Monarch Tractor",
  "verdant-robotics":"Verdant Robotics","aigen":"Aigen","agco":"AGCO / PTx Trimble",
  "built-robotics":"Built Robotics","dusty-robotics":"Dusty Robotics","canvas":"Canvas",
  "boston-dynamics-spot-construction":"Boston Dynamics Spot (construction)","nlink-hilti":"nLink (Hilti)",
  "toggle-industries":"Toggle Industries","spacer-robotics":"Spacer Robotics",
  "anduril":"Anduril","shield-ai":"Shield AI","saronic":"Saronic","helsing":"Helsing",
  "skydio":"Skydio","brinc-drones":"BRINC Drones","saildrone":"Saildrone",
  "irobot":"iRobot","roborock":"Roborock","ecovacs":"Ecovacs","dreame":"Dreame",
  "eufy":"Eufy (Anker)","matic-robots":"Matic Robots",
  "pudu-robotics":"Pudu Robotics","bear-robotics":"Bear Robotics","keenon-robotics":"Keenon Robotics",
  "miso-robotics":"Miso Robotics","chef-robotics":"Chef Robotics","avidbots":"Avidbots",
  "scale-ai":"Scale AI (Robotics)","foxglove":"Foxglove","nvidia-isaac-sim":"NVIDIA Isaac Sim / Cosmos",
  "intrinsic":"Intrinsic","realman":"RealMan Robotics","maxon":"maxon group",
  "tangram-vision":"Tangram Vision","pollen-robotics":"Pollen Robotics","nomadicml":"NomadicML",
}

eco_links = ""
if "ecosystem-substacks.md" in docs:
    eco_links += '    <li><a class="top-link" href="#doc=ecosystem-substacks.md">Ecosystem — Substacks &amp; newsletters</a></li>\n'
if "ecosystem-youtube.md" in docs:
    eco_links += '    <li><a class="top-link" href="#doc=ecosystem-youtube.md">Ecosystem — YouTube &amp; podcasts</a></li>\n'

research_labels = {
    "research-vc-portfolio-scan.md": "VC + YC portfolio scan",
    "research-job-posting-signals.md": "Job-posting signals",
    "research-insurance-prior-art.md": "Insurance prior art (Wedge 1)",
    "research-failure-postmortems.md": "Robotics failure post-mortems",
    "research-eu-regulatory.md": "EU regulatory deep-dive (Wedge 2)",
}
research_links = ""
for rf, label in research_labels.items():
    if rf in docs:
        research_links += f'    <li><a href="#doc={rf}">{html.escape(label)}</a></li>\n'

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Robotics Landscape</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fbbf24'%3E%3Cpath d='M13 2L3 14h7l-1 8 10-12h-7l1-8z'/%3E%3C/svg%3E">
<style>
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; padding: 0; height: 100%; }}
  body {{ font: 15px/1.55 -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
         color: #1a1a1a; background: #fff; display: flex; }}
  aside {{ width: 320px; min-width: 320px; height: 100vh; overflow-y: auto;
           background: #f6f8fa; border-right: 1px solid #e3e8ef; padding: 20px 18px; }}
  main {{ flex: 1; height: 100vh; overflow-y: auto; padding: 36px 56px; max-width: 920px; }}
  aside h1 {{ font-size: 16px; margin: 0 0 4px; }}
  aside .subtitle {{ font-size: 12px; color: #666; margin-bottom: 18px; }}
  aside h3 {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;
              color: #555; margin: 18px 0 6px; padding-bottom: 4px;
              border-bottom: 1px solid #d8dee5; }}
  aside ul {{ list-style: none; padding: 0; margin: 0 0 10px; }}
  aside li {{ margin: 0; }}
  aside a {{ display: block; padding: 4px 8px; color: #0a58ca; text-decoration: none;
             border-radius: 4px; font-size: 13.5px; }}
  aside a:hover {{ background: #e7eef8; }}
  aside a.active {{ background: #0a58ca; color: white; }}
  aside .top-link {{ font-weight: 600; padding: 6px 8px; }}
  main h1 {{ font-size: 26px; margin-top: 0; padding-bottom: 8px; border-bottom: 1px solid #eee; }}
  main h2 {{ font-size: 20px; margin-top: 28px; }}
  main h3 {{ font-size: 17px; margin-top: 22px; }}
  main p, main li {{ font-size: 15px; }}
  main code {{ background: #f1f3f5; padding: 1px 5px; border-radius: 3px; font-size: 13px; }}
  main pre {{ background: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }}
  main blockquote {{ border-left: 3px solid #ddd; margin: 0; padding: 0 16px; color: #555; }}
  main table {{ border-collapse: collapse; margin: 12px 0; font-size: 14px; }}
  main th, main td {{ border: 1px solid #e3e8ef; padding: 6px 10px; text-align: left; }}
  main th {{ background: #f6f8fa; }}
  main a {{ color: #0a58ca; }}
  .placeholder {{ color: #888; font-style: italic; padding: 80px 0; text-align: center; }}

  /* Chat panel */
  #chat-fab {{ position: fixed; bottom: 20px; right: 20px; width: 52px; height: 52px;
              border-radius: 26px; background: #0a58ca; color: white; border: none;
              cursor: pointer; font-size: 22px; box-shadow: 0 4px 12px rgba(0,0,0,0.18);
              z-index: 1000; display: flex; align-items: center; justify-content: center; }}
  #chat-fab:hover {{ background: #0848a8; }}
  #chat-panel {{ position: fixed; top: 0; right: 0; width: 420px; height: 100vh;
                background: #fff; border-left: 1px solid #e3e8ef;
                box-shadow: -4px 0 16px rgba(0,0,0,0.06);
                display: flex; flex-direction: column;
                transform: translateX(100%); transition: transform 0.2s ease; z-index: 999; }}
  #chat-panel.open {{ transform: translateX(0); }}
  #chat-header {{ padding: 14px 18px; border-bottom: 1px solid #e3e8ef;
                 display: flex; align-items: center; justify-content: space-between; }}
  #chat-header h3 {{ margin: 0; font-size: 14px; border: none; padding: 0;
                    text-transform: none; letter-spacing: 0; color: #1a1a1a; }}
  #chat-header-buttons button {{ background: none; border: none; cursor: pointer;
                                color: #666; font-size: 13px; padding: 4px 8px; margin-left: 4px; }}
  #chat-header-buttons button:hover {{ color: #1a1a1a; }}
  #chat-settings {{ padding: 10px 16px; border-bottom: 1px solid #eee; display: flex; gap: 6px; }}
  #chat-settings select, #chat-settings input {{ padding: 5px 8px; border: 1px solid #d8dee5;
                                                border-radius: 4px; font: inherit; font-size: 12px; }}
  #chat-settings input {{ flex: 1; min-width: 100px; }}
  #chat-history {{ flex: 1; overflow-y: auto; padding: 12px 16px; }}
  #chat-history-empty {{ color: #999; font-size: 12px; padding: 20px; text-align: center; }}
  .chat-msg {{ margin-bottom: 12px; padding: 10px 12px; border-radius: 6px;
               font-size: 13.5px; line-height: 1.5; }}
  .chat-msg.q {{ background: #eef2f8; cursor: pointer; }}
  .chat-msg.q:hover {{ background: #e3eaf5; }}
  .chat-msg.a {{ background: #f6f8fa; white-space: pre-wrap; word-wrap: break-word; }}
  .chat-msg.a a {{ color: #0a58ca; }}
  .chat-msg.error {{ background: #fef2f2; color: #991b1b; font-size: 12px; }}
  .chat-msg-meta {{ font-size: 10.5px; color: #888; margin-bottom: 4px; text-transform: uppercase;
                   letter-spacing: 0.3px; }}
  .chat-msg.loading {{ background: #fff8e1; color: #92400e; font-style: italic; }}
  #chat-input-area {{ padding: 12px 16px; border-top: 1px solid #e3e8ef; }}
  #chat-context {{ font-size: 11px; color: #666; margin-bottom: 6px; }}
  #chat-context strong {{ color: #1a1a1a; }}
  #chat-input {{ width: 100%; min-height: 64px; padding: 8px; border: 1px solid #d8dee5;
                border-radius: 4px; resize: vertical; font: inherit; font-size: 13.5px; }}
  .chat-buttons {{ display: flex; gap: 6px; margin-top: 8px; }}
  .chat-buttons button {{ padding: 6px 12px; border: 1px solid #d8dee5;
                          background: white; border-radius: 4px; cursor: pointer; font-size: 12px; }}
  .chat-buttons button.primary {{ background: #0a58ca; color: white; border-color: #0a58ca; }}
  .chat-buttons button.primary:hover {{ background: #0848a8; }}
  .chat-buttons button:hover {{ background: #f6f8fa; }}
  .chat-buttons .hint {{ flex: 1; font-size: 11px; color: #888; align-self: center; text-align: right; }}
</style>
</head>
<body>

<aside>
  <h1><svg width="16" height="16" viewBox="0 0 24 24" fill="#fbbf24" style="vertical-align: -2px; margin-right: 4px;"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg>Robotics Landscape</h1>
  <div class="subtitle">82 dossiers · 12 verticals · April 2026</div>

  <h3>Synthesis</h3>
  <ul>
    <li><a class="top-link" href="#doc=gap-analysis.md">Gap analysis (top 5 wedges)</a></li>
    <li><a class="top-link" href="#doc=data-collection-deep-dive.md">Data-collection deep-dive</a></li>
    <li><a class="top-link" href="#doc=external-second-opinion.md">External second opinion</a></li>
{eco_links}    <li><a class="top-link" href="#doc=index.md">Raw scout index</a></li>
  </ul>

  <h3>Validation research</h3>
  <ul>
{research_links}  </ul>
"""

# Build verticals nav
for vname, slugs in verticals:
    html_doc += f'  <h3>{html.escape(vname)}</h3>\n  <ul>\n'
    for slug in slugs:
        path = f"companies/{slug}.md"
        if path in docs:
            label = html.escape(display.get(slug, slug))
            html_doc += f'    <li><a href="#doc={path}">{label}</a></li>\n'
    html_doc += '  </ul>\n'

html_doc += """</aside>

<main id="content">
  <div class="placeholder">Pick something on the left to start. Recommended first read: <strong>Gap analysis</strong>.</div>
</main>

<button id="chat-fab" title="Ask a question">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="white"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg>
</button>

<aside id="chat-panel">
  <div id="chat-header">
    <h3>Ask</h3>
    <div id="chat-header-buttons">
      <button id="chat-clear" title="Clear all history">Clear</button>
      <button id="chat-close" title="Close">Close</button>
    </div>
  </div>
  <div id="chat-settings">
    <select id="chat-provider">
      <option value="anthropic">Anthropic</option>
      <option value="openai">OpenAI</option>
    </select>
    <input id="chat-apikey" type="password" placeholder="API key (saved locally)" autocomplete="off">
  </div>
  <div id="chat-key-status"></div>
  <div id="chat-history">
    <div id="chat-history-empty">No questions yet. Pick a doc on the left, then ask. History is saved locally.</div>
  </div>
  <div id="chat-input-area">
    <div id="chat-context">Context: <strong id="chat-doc-name">none selected</strong></div>
    <textarea id="chat-input" placeholder="Ask about the active document. Cmd/Ctrl+Enter to send."></textarea>
    <div class="chat-buttons">
      <button class="primary" id="chat-send">Send</button>
      <button id="chat-copy">Copy as prompt</button>
      <span class="hint">⌘+Enter</span>
    </div>
  </div>
</aside>

<script src="https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js"></script>
<script>
const docs = """ + json.dumps(docs) + """;

function render(key) {
  const main = document.getElementById('content');
  const text = docs[key];
  if (!text) {
    main.innerHTML = '<div class="placeholder">Document not found: ' + key + '</div>';
    return;
  }
  main.innerHTML = marked.parse(text);
  main.scrollTop = 0;
  document.querySelectorAll('aside a').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === '#doc=' + key);
  });
}

let currentDocKey = null;
const _origRender = render;
render = function(key) {
  currentDocKey = key;
  const el = document.getElementById('chat-doc-name');
  if (el) el.textContent = key || 'none selected';
  return _origRender(key);
};

function handleHash() {
  const m = location.hash.match(/^#doc=(.+)$/);
  if (m) render(decodeURIComponent(m[1]));
}

window.addEventListener('hashchange', handleHash);
handleHash();

// ===== Chat panel =====
const HISTORY_KEY = 'robotics-landscape-history';
const SETTINGS_KEY = 'robotics-landscape-settings';
const EMBEDDED_KEY = """ + json.dumps(EMBEDDED_KEY) + """;

function loadHistory() {
  try { return JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]'); }
  catch(e) { return []; }
}
function saveHistory(h) { localStorage.setItem(HISTORY_KEY, JSON.stringify(h)); }
function loadSettings() {
  try { return JSON.parse(localStorage.getItem(SETTINGS_KEY) || '{}'); }
  catch(e) { return {}; }
}
function saveSettings(s) { localStorage.setItem(SETTINGS_KEY, JSON.stringify(s)); }

function escapeHtml(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function renderHistory() {
  const history = loadHistory();
  const container = document.getElementById('chat-history');
  if (history.length === 0) {
    container.innerHTML = '<div id="chat-history-empty">No questions yet. Pick a doc on the left, then ask. History is saved locally.</div>';
    return;
  }
  container.innerHTML = history.map((item, i) => {
    const time = new Date(item.ts).toLocaleString();
    const docLabel = item.doc ? item.doc.replace('companies/','') : 'no doc';
    let block = '<div class="chat-msg q" data-idx="' + i + '" title="Click to revisit context">' +
                '<div class="chat-msg-meta">' + escapeHtml(time) + ' · ' + escapeHtml(docLabel) + '</div>' +
                escapeHtml(item.q) + '</div>';
    if (item.loading) {
      block += '<div class="chat-msg loading">Thinking…</div>';
    } else if (item.a) {
      block += '<div class="chat-msg a">' + marked.parseInline(item.a) + '</div>';
    }
    if (item.error) {
      block += '<div class="chat-msg error">' + escapeHtml(item.error) + '</div>';
    }
    return block;
  }).join('');
  container.scrollTop = container.scrollHeight;
  container.querySelectorAll('.chat-msg.q').forEach(el => {
    el.onclick = () => {
      const idx = parseInt(el.dataset.idx);
      const h = loadHistory();
      const item = h[idx];
      if (item && item.doc && item.doc !== currentDocKey) {
        location.hash = '#doc=' + item.doc;
      }
    };
  });
}

function buildPrompt(question) {
  const docContent = currentDocKey ? docs[currentDocKey] : '';
  const system = 'You are a research assistant for a startup founder evaluating robotics opportunities. The founder compiled a research bundle covering 82 robotics companies plus a gap analysis identifying software-only wedges. Be direct and concise. Cite specific companies or sections when relevant.';
  const user = currentDocKey
    ? '# Active document: ' + currentDocKey + '\\n\\n' + docContent + '\\n\\n---\\n\\nQuestion: ' + question
    : 'Question (no specific document selected): ' + question;
  return { system: system, user: user };
}

async function callOpenAI(apiKey, system, user) {
  const res = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + apiKey },
    body: JSON.stringify({
      model: 'gpt-4o',
      messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
      temperature: 0.3
    })
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error('OpenAI ' + res.status + ': ' + txt.slice(0, 300));
  }
  const data = await res.json();
  return data.choices[0].message.content;
}

async function callAnthropic(apiKey, system, user) {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'anthropic-dangerous-direct-browser-access': 'true'
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5',
      max_tokens: 2048,
      system: system,
      messages: [{ role: 'user', content: user }]
    })
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error('Anthropic ' + res.status + ': ' + txt.slice(0, 300));
  }
  const data = await res.json();
  return data.content[0].text;
}

async function sendQuestion() {
  const input = document.getElementById('chat-input');
  const q = input.value.trim();
  if (!q) return;

  const provider = document.getElementById('chat-provider').value;
  const apiKey = document.getElementById('chat-apikey').value.trim();
  saveSettings({ provider: provider, apiKey: apiKey });

  const history = loadHistory();
  const item = { ts: Date.now(), q: q, doc: currentDocKey, provider: provider, loading: !!apiKey };
  history.push(item);
  saveHistory(history);
  renderHistory();
  input.value = '';

  if (!apiKey) {
    item.error = 'No API key. Use "Copy as prompt" to paste into ChatGPT/Claude, or paste an API key above and resend.';
    item.loading = false;
    saveHistory(history);
    renderHistory();
    return;
  }

  try {
    const p = buildPrompt(q);
    const fn = provider === 'anthropic' ? callAnthropic : callOpenAI;
    const answer = await fn(apiKey, p.system, p.user);
    item.a = answer;
    item.loading = false;
    saveHistory(history);
    renderHistory();
  } catch (e) {
    item.error = e.message + '\\n\\nTip: API calls from file:// often hit CORS. Try "Copy as prompt" instead, or run a local server.';
    item.loading = false;
    saveHistory(history);
    renderHistory();
  }
}

function copyAsPrompt() {
  const q = document.getElementById('chat-input').value.trim();
  if (!q) { alert('Type a question first.'); return; }
  const p = buildPrompt(q);
  const text = '[System]\\n' + p.system + '\\n\\n[User]\\n' + p.user;
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.getElementById('chat-copy');
    const orig = btn.textContent;
    btn.textContent = 'Copied!';
    setTimeout(() => { btn.textContent = orig; }, 1500);
  }).catch(e => alert('Copy failed: ' + e.message));
}

// Wire up
document.getElementById('chat-fab').onclick = () => {
  document.getElementById('chat-panel').classList.toggle('open');
};
document.getElementById('chat-close').onclick = () => {
  document.getElementById('chat-panel').classList.remove('open');
};
document.getElementById('chat-clear').onclick = () => {
  if (confirm('Clear all question history?')) { saveHistory([]); renderHistory(); }
};
document.getElementById('chat-send').onclick = sendQuestion;
document.getElementById('chat-copy').onclick = copyAsPrompt;
document.getElementById('chat-input').addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); sendQuestion(); }
});

// Restore settings — prefer localStorage, fall back to embedded key
const _settings = loadSettings();
const _provider = _settings.provider || 'anthropic';
const _apiKey = _settings.apiKey || EMBEDDED_KEY;
document.getElementById('chat-provider').value = _provider;
document.getElementById('chat-apikey').value = _apiKey;
if (EMBEDDED_KEY && !_settings.apiKey) {
  document.getElementById('chat-key-status').innerHTML =
    '<div style="font-size:10.5px;color:#92400e;background:#fff8e1;padding:6px 16px;border-bottom:1px solid #fde68a;">Anthropic key embedded from env. Do not share this file.</div>';
}
renderHistory();
</script>

</body>
</html>"""

with open(f"{base}/index.html", "w") as f:
    f.write(html_doc)

import os
size = os.path.getsize(f"{base}/index.html")
print(f"Written: {f.name if hasattr(f,'name') else 'index.html'}")
print(f"Size: {size:,} bytes")
print(f"Docs embedded: {len(docs)}")
