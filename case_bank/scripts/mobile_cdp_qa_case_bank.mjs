#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const BASE = '/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2';
const PORT = 9251;
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const QA_DIR = `${BASE}/qa/case_bank_mobile_20260613`;
mkdirSync(QA_DIR, { recursive: true });

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
async function getJson(url) { const r = await fetch(url); if (!r.ok) throw new Error(`${url} ${r.status}`); return r.json(); }
function fileUrl(path) { return `file://${resolve(path)}`; }

const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
  `--remote-debugging-port=${PORT}`, '--remote-allow-origins=*', 'about:blank'
], { stdio: 'ignore' });

let ws;
let seq = 0;
const pending = new Map();
const consoleMessages = [];
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
    if (msg.method === 'Runtime.consoleAPICalled') consoleMessages.push(msg.params.type);
    if (msg.method === 'Runtime.exceptionThrown') consoleMessages.push('exception');
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
  await call('Page.navigate', { url: fileUrl(`${BASE}/case_bank/index.html`) });
  for (let i = 0; i < 100; i++) {
    const r = await call('Runtime.evaluate', { expression: "document.readyState === 'complete' && document.querySelectorAll('.caseCard').length === 100", returnByValue: true });
    if (r.result?.value === true) break;
    await sleep(100);
  }
  const metricsResult = await call('Runtime.evaluate', { expression: `(() => {
    const cards = [...document.querySelectorAll('.caseCard')];
    const first = cards[0]?.getBoundingClientRect();
    const hero = document.querySelector('.heroCard')?.getBoundingClientRect();
    const choice = document.querySelector('.choice')?.getBoundingClientRect();
    return {
      clientWidth: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      bodyScrollWidth: document.body.scrollWidth,
      hasHorizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth || document.body.scrollWidth > document.documentElement.clientWidth,
      caseCount: cards.length,
      categoryOptions: document.querySelectorAll('#categoryFilter option').length,
      typeOptions: document.querySelectorAll('#typeFilter option').length,
      chipCount: document.querySelectorAll('.chip').length,
      firstCardRight: Math.round(first?.right || 0),
      heroRight: Math.round(hero?.right || 0),
      choiceHeight: Math.round(choice?.height || 0),
      h1Text: document.querySelector('h1')?.textContent || '',
      statSolved: document.querySelector('#solvedCount')?.textContent || ''
    };
  })()`, returnByValue: true });
  const metrics = metricsResult.result.value;
  const shot = await call('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  writeFileSync(`${QA_DIR}/case_bank_cdp_390x844.png`, Buffer.from(shot.data, 'base64'));

  await call('Runtime.evaluate', { expression: "document.querySelector('.choice')?.click()", returnByValue: true });
  await sleep(200);
  const interactionResult = await call('Runtime.evaluate', { expression: `(() => ({
    openAnswer: document.querySelector('.answerBox.open') !== null,
    solvedCount: document.querySelector('#solvedCount')?.textContent || '',
    hasCorrectChoice: document.querySelector('.choice.correct') !== null,
    firstAnswerText: document.querySelector('.answerBox.open')?.textContent || ''
  }))()`, returnByValue: true });
  metrics.interaction = interactionResult.result.value;
  const answerShot = await call('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  writeFileSync(`${QA_DIR}/case_bank_answer_cdp_390x844.png`, Buffer.from(answerShot.data, 'base64'));

  await call('Runtime.evaluate', { expression: "document.querySelector('#search').value = 'RAG'; document.querySelector('#search').dispatchEvent(new Event('input', { bubbles: true }));", returnByValue: true });
  const searchResult = await call('Runtime.evaluate', { expression: "document.querySelectorAll('.caseCard').length", returnByValue: true });
  metrics.searchRagCount = searchResult.result.value;

  const errors = [];
  if (metrics.caseCount !== 100) errors.push('caseCount');
  if (metrics.categoryOptions !== 11) errors.push('categoryOptions');
  if (metrics.typeOptions !== 6) errors.push('typeOptions');
  if (metrics.chipCount !== 11) errors.push('chipCount');
  if (metrics.hasHorizontalOverflow) errors.push('horizontalOverflow');
  if (metrics.choiceHeight < 44) errors.push('choiceHeight');
  if (!metrics.interaction?.openAnswer || metrics.interaction?.solvedCount !== '1') errors.push('interaction');
  if (metrics.searchRagCount < 1) errors.push('search');
  if (consoleMessages.includes('exception') || consoleMessages.includes('error')) errors.push('consoleError');
  const report = { generatedAt: new Date().toISOString(), metrics, consoleMessages, errors };
  writeFileSync(`${QA_DIR}/case_bank_mobile_metrics.json`, JSON.stringify(report, null, 2));
  console.log(`CASE_BANK_MOBILE_CASE_COUNT ${metrics.caseCount}`);
  console.log(`CASE_BANK_MOBILE_CATEGORY_OPTIONS ${metrics.categoryOptions}`);
  console.log(`CASE_BANK_MOBILE_TYPE_OPTIONS ${metrics.typeOptions}`);
  console.log(`CASE_BANK_MOBILE_OVERFLOW ${metrics.hasHorizontalOverflow ? 'YES' : 'NO'}`);
  console.log(`CASE_BANK_MOBILE_SEARCH_RAG ${metrics.searchRagCount}`);
  console.log(`CASE_BANK_MOBILE_ERRORS ${errors.length}`);
  if (errors.length) {
    console.log(`ERRORS ${errors.join(',')}`);
    process.exitCode = 1;
  }
} finally {
  try { ws?.close(); } catch {}
  chrome.kill('SIGTERM');
}
