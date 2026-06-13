#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';
import { basename, resolve } from 'node:path';

const BASE = '/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2';
const PORT = 9237;
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const QA_DIR = `${BASE}/qa/question_bank_mobile_20260613`;
const samples = new Set(['unit02_genai_mechanism', 'unit23_ai_project_poc', 'unit45_case_simulation']);
mkdirSync(QA_DIR, { recursive: true });

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
function fileUrl(path) { return `file://${resolve(path)}`; }
async function getJson(url) { const r = await fetch(url); if (!r.ok) throw new Error(`${url} ${r.status}`); return r.json(); }

const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
  `--remote-debugging-port=${PORT}`, '--remote-allow-origins=*', 'about:blank'
], { stdio: 'ignore' });

let ws;
let seq = 0;
const pending = new Map();
function call(method, params = {}) {
  const id = ++seq;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject, method }));
}

try {
  let page;
  for (let i = 0; i < 80; i++) {
    try {
      const list = await getJson(`http://127.0.0.1:${PORT}/json`);
      page = list.find(x => x.type === 'page' && x.webSocketDebuggerUrl) || list[0];
      if (page?.webSocketDebuggerUrl) break;
    } catch {}
    await sleep(100);
  }
  if (!page?.webSocketDebuggerUrl) throw new Error('CDP page not ready');
  ws = new WebSocket(page.webSocketDebuggerUrl);
  ws.addEventListener('message', ev => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id); pending.delete(msg.id);
      if (msg.error) p.reject(new Error(`${p.method}: ${JSON.stringify(msg.error)}`));
      else p.resolve(msg.result || {});
    }
  });
  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve, { once: true });
    ws.addEventListener('error', reject, { once: true });
  });
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Emulation.setDeviceMetricsOverride', {
    width: 390, height: 844, deviceScaleFactor: 2, mobile: true, screenWidth: 390, screenHeight: 844
  });
  await call('Emulation.setTouchEmulationEnabled', { enabled: true });

  const glob = await import('node:fs/promises');
  const { readdirSync } = await import('node:fs');
  const unitDirs = readdirSync(`${BASE}/question_bank`, { withFileTypes: true })
    .filter(d => d.isDirectory() && /^unit\d{2}_/.test(d.name))
    .map(d => d.name).sort();
  const results = [];
  for (const unit of unitDirs) {
    const url = fileUrl(`${BASE}/question_bank/${unit}/index.html`);
    await call('Page.navigate', { url });
    for (let i = 0; i < 100; i++) {
      const r = await call('Runtime.evaluate', { expression: "document.readyState === 'complete' && !!document.querySelector('.choice')", returnByValue: true });
      if (r.result?.value === true) break;
      await sleep(100);
    }
    const evalResult = await call('Runtime.evaluate', { expression: `(() => {
      const q = typeof QUESTIONS !== 'undefined' ? QUESTIONS : [];
      const h1 = document.querySelector('h1')?.getBoundingClientRect();
      const hero = document.querySelector('.hero')?.getBoundingClientRect();
      const focus = document.querySelector('.focus-card')?.getBoundingClientRect();
      const firstChoice = document.querySelector('.choice')?.getBoundingClientRect();
      const statsStyle = getComputedStyle(document.querySelector('.stats')).gridTemplateColumns;
      return {
        unit: ${JSON.stringify(unit)},
        clientWidth: document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
        bodyScrollWidth: document.body.scrollWidth,
        titleRight: Math.round(h1?.right || 0),
        heroRight: Math.round(hero?.right || 0),
        focusRight: Math.round(focus?.right || 0),
        firstChoiceHeight: Math.round(firstChoice?.height || 0),
        statsColumns: statsStyle,
        miniCount: document.querySelectorAll('.mini').length,
        questionCount: q.length,
        feedbackVisible: false,
        hasHorizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth || document.body.scrollWidth > document.documentElement.clientWidth
      };
    })()`, returnByValue: true });
    const metrics = evalResult.result.value;
    if (samples.has(unit)) {
      const shot = await call('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
      writeFileSync(`${QA_DIR}/${unit}_cdp_390x844.png`, Buffer.from(shot.data, 'base64'));
    }
    const interactionResult = await call('Runtime.evaluate', { expression: `(() => {
      document.querySelector('.choice')?.click();
      return document.querySelector('.feedback')?.classList.contains('show') || false;
    })()`, returnByValue: true });
    metrics.feedbackVisible = interactionResult.result.value === true;
    results.push(metrics);
  }
  const errors = results.filter(r => r.questionCount !== 20 || r.miniCount !== 20 || r.hasHorizontalOverflow || !r.feedbackVisible || r.firstChoiceHeight < 48);
  writeFileSync(`${QA_DIR}/mobile_cdp_metrics.json`, JSON.stringify({ generatedAt: new Date().toISOString(), results, errors }, null, 2));
  console.log(`MOBILE_CDP_UNITS ${results.length}`);
  console.log(`MOBILE_CDP_ERRORS ${errors.length}`);
  for (const e of errors.slice(0, 20)) console.log(`ERROR ${e.unit} ${JSON.stringify(e)}`);
  if (errors.length) process.exitCode = 1;
} finally {
  try { ws?.close(); } catch {}
  chrome.kill('SIGTERM');
}
