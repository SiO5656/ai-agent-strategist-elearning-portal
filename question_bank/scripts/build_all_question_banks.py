#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import random
import re
from pathlib import Path
from typing import Any

BASE = Path('/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2')
UNITS_DIR = BASE / 'units'
QB_DIR = BASE / 'question_bank'
SUMMARY_QA = QB_DIR / 'qa_report.md'
FORBIDDEN_FOOTER = ''.join([
    '保存先: question_bank/unit01_course_orientation/index.html',
    ' / ',
    '四択版テンプレートとしてUnit02以降に展開可能。',
])
SECRET_PATTERNS = ['@gmail.com', 'sk-', 'BEGIN PRIVATE KEY', 'refresh_token', 'client_secret']
LETTERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
LEVELS = ['基本', '標準', '応用']
GENERIC_DISTRACTORS = [
    '最新ツール名だけを暗記すればよい',
    '全社一斉導入を先に決めればよい',
    'AIの精度だけを見れば導入判断は十分である',
    '現場確認や効果測定は省略してよい',
    '人間の確認をすべてなくすことを最優先する',
    '業務やデータの整理は導入後に後回しでよい',
    'リスクや責任分界は運用後に考えればよい',
    'PoCなしで本番へ一気に展開することが望ましい',
]
SKIP_HEADINGS = {'unit概要', '概要', 'シーン構成', '関連', '対象ページ', '品質条件', '必須成果物'}

HTML_TEMPLATE = r'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>__UNIT_LABEL__ 四択問題集 | AIエージェント・ストラテジスト</title>
  <style>
    :root {
      --bg:#f6f8fb; --panel:#fff; --text:#172033; --muted:#63708a; --line:#dfe6f1;
      --blue:#2563eb; --blue2:#dbeafe; --green:#10b981; --green2:#dcfce7; --red:#ef4444; --red2:#fee2e2; --orange:#f59e0b;
      --shadow:0 18px 50px rgba(16,24,40,.10); --radius:24px;
      font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Yu Gothic","YuGothic","Noto Sans JP",sans-serif;
    }
    *{box-sizing:border-box} html,body{margin:0;min-height:100%;background:var(--bg);color:var(--text)} body{overflow-x:hidden} button,input,select{font:inherit}
    .app{width:min(1120px,100%);margin:0 auto;padding:20px clamp(14px,3vw,32px) 64px}
    .hero{background:linear-gradient(135deg,#fff 0%,#eef5ff 56%,#f7fbff 100%);border:1px solid #e5edf8;border-radius:30px;padding:clamp(18px,4vw,34px);box-shadow:var(--shadow);overflow:hidden;position:relative}
    .hero:after{content:"";position:absolute;right:-70px;top:-80px;width:220px;height:220px;background:rgba(37,99,235,.10);border-radius:50%}
    .eyebrow{display:inline-flex;gap:8px;align-items:center;color:#1d4ed8;background:#eff6ff;border:1px solid #bfdbfe;padding:7px 12px;border-radius:999px;font-weight:800;font-size:13px}
    h1{margin:16px 0 10px;font-size:clamp(26px,5.8vw,44px);line-height:1.12;letter-spacing:-.04em;overflow-wrap:anywhere;word-break:break-word;max-width:100%}
    .lead{margin:0;color:var(--muted);font-size:clamp(15px,2vw,18px);line-height:1.75;max-width:780px;overflow-wrap:anywhere;word-break:break-word}
    .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:20px}
    .stat{background:rgba(255,255,255,.78);border:1px solid #e5edf8;border-radius:18px;padding:12px;min-width:0}.stat b{display:block;font-size:22px;line-height:1}.stat span{display:block;margin-top:6px;color:var(--muted);font-size:12px}
    .progress-shell{height:10px;background:#e8eef8;border-radius:999px;overflow:hidden;margin-top:12px}.progress-bar{height:100%;width:0%;background:linear-gradient(90deg,var(--blue),#06b6d4);border-radius:999px;transition:width .2s}
    .toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0}.control{flex:1 1 180px;min-width:0;border:1px solid var(--line);background:#fff;border-radius:16px;padding:12px 14px;color:var(--text)}
    .btn{border:0;border-radius:16px;padding:13px 16px;background:#e8eef8;color:#1f2a44;font-weight:900;cursor:pointer;min-height:48px}.btn.primary{background:var(--blue);color:#fff}.btn.ghost{background:#fff;border:1px solid var(--line)}.btn:active{transform:translateY(1px)}
    .main-grid{display:grid;grid-template-columns:minmax(0,1.12fr) minmax(300px,.88fr);gap:18px;align-items:start}
    .focus-card,.list-panel{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);min-width:0}.focus-card{padding:clamp(18px,4vw,30px)}.list-panel{padding:18px}
    .meta-row{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:18px}.pill{display:inline-flex;border-radius:999px;padding:7px 11px;background:#f1f5f9;color:#475569;font-size:12px;font-weight:900}.pill.blue{background:var(--blue2);color:#1d4ed8}
    .qtext{font-size:clamp(21px,5.2vw,32px);line-height:1.45;letter-spacing:-.02em;margin:10px 0 18px;font-weight:900;overflow-wrap:anywhere}
    .choices{display:grid;gap:10px;margin-top:14px}.choice{width:100%;text-align:left;border:2px solid var(--line);background:#fff;border-radius:18px;padding:14px 14px;min-height:58px;display:flex;gap:10px;align-items:flex-start;line-height:1.55;cursor:pointer}
    .choice .label{flex:0 0 auto;width:28px;height:28px;border-radius:50%;display:inline-grid;place-items:center;background:#eef2ff;color:#1d4ed8;font-weight:900}.choice .txt{min-width:0;overflow-wrap:anywhere}
    .choice.correct{border-color:#22c55e;background:var(--green2)}.choice.wrong{border-color:#f87171;background:var(--red2)}.choice.dim{opacity:.55}
    .feedback{display:none;margin-top:16px;padding:16px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:20px;line-height:1.75}.feedback.show{display:block}.feedback b.ok{color:#15803d}.feedback b.ng{color:#b91c1c}
    .point{border-left:4px solid var(--green);padding-left:12px;color:#334155;margin-top:10px}
    .actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:18px}
    .list-panel h2{margin:0 0 12px;font-size:20px}.cards{display:grid;gap:10px;max-height:620px;overflow:auto;padding-right:4px}
    .mini{text-align:left;border:1px solid var(--line);background:#fff;border-radius:16px;padding:12px;cursor:pointer;min-width:0}.mini.done{border-color:#86efac;background:#f0fdf4}.mini.wrong{border-color:#fca5a5;background:#fff1f2}
    .mini strong{display:block;font-size:14px;line-height:1.45;white-space:normal;overflow-wrap:anywhere}.mini small{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;color:var(--muted)}
    @media(max-width:760px){.app{padding:12px 12px 48px}.hero{border-radius:24px}.stats{grid-template-columns:repeat(2,1fr)}.main-grid{grid-template-columns:1fr}.control{flex-basis:100%}.btn{width:100%}.actions{grid-template-columns:1fr}.cards{max-height:none;overflow:visible}}
    @media(max-width:430px){h1{font-size:clamp(24px,7.1vw,30px);line-height:1.18;letter-spacing:-.035em}.lead{font-size:14px}.hero{padding:18px 20px}}
    @media(max-width:390px){.app{padding-left:10px;padding-right:10px}.hero,.focus-card,.list-panel{border-radius:20px}.stat b{font-size:20px}.choice{padding:13px 12px}}
  </style>
</head>
<body>
  <main class="app">
    <section class="hero">
      <div class="eyebrow">__UNIT_LABEL__ · 四択問題集</div>
      <h1>__TITLE_HTML__</h1>
      <p class="lead">スマホで解きやすい四択形式。選択するとすぐ正誤と解説が出ます。__UNIT_LABEL__の講義ノート・理解度チェック・試験直前カードから20問に再構成。</p>
      <div class="stats" aria-label="学習状況">
        <div class="stat"><b id="statTotal">20</b><span>全問題</span></div><div class="stat"><b id="statCorrect">0</b><span>正解</span></div><div class="stat"><b id="statWrong">0</b><span>復習</span></div><div class="stat"><b id="statRate">0%</b><span>正答率</span></div>
      </div>
      <div class="progress-shell"><div class="progress-bar" id="progressBar"></div></div>
    </section>
    <section class="toolbar" aria-label="操作">
      <input class="control" id="searchBox" type="search" placeholder="検索：例 リスク / データ / KPI" />
      <select class="control" id="tagFilter" aria-label="タグ絞り込み"><option value="all">すべてのタグ</option></select>
      <button class="btn ghost" id="shuffleBtn" type="button">シャッフル</button>
      <button class="btn ghost" id="resetBtn" type="button">記録リセット</button>
    </section>
    <section class="main-grid">
      <article class="focus-card" aria-live="polite">
        <div class="meta-row"><span class="pill blue" id="cardIndex">Q 1 / 20</span><span class="pill" id="cardTag">基本</span><span class="pill" id="cardLevel">基本</span></div>
        <div class="qtext" id="questionText"></div>
        <div class="choices" id="choices"></div>
        <div class="feedback" id="feedback"></div>
        <div class="actions"><button class="btn ghost" id="prevBtn" type="button">前へ</button><button class="btn primary" id="nextBtn" type="button">次へ</button></div>
      </article>
      <aside class="list-panel"><h2>全問リスト</h2><div class="cards" id="cardList"></div></aside>
    </section>
  </main>
  <script>
  const QUESTIONS = __DATA__;
  const stateKey = '__STATE_KEY__';
  let order = QUESTIONS.map((_, i) => i); let current = 0; let selected = null; let progress = loadProgress();
  const $ = id => document.getElementById(id);
  const els = {total:$('statTotal'),correct:$('statCorrect'),wrong:$('statWrong'),rate:$('statRate'),bar:$('progressBar'),q:$('questionText'),choices:$('choices'),feedback:$('feedback'),cardIndex:$('cardIndex'),cardTag:$('cardTag'),cardLevel:$('cardLevel'),list:$('cardList'),tagFilter:$('tagFilter'),search:$('searchBox')};
  function loadProgress(){try{return JSON.parse(localStorage.getItem(stateKey))||{}}catch{return {}}} function saveProgress(){localStorage.setItem(stateKey,JSON.stringify(progress))}
  function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
  function tags(){return [...new Set(QUESTIONS.map(q=>q.tag))]}
  function filteredOrder(){const term=els.search.value.trim().toLowerCase();const tag=els.tagFilter.value;return order.filter(i=>{const q=QUESTIONS[i];const hay=`${q.question} ${q.options.join(' ')} ${q.explanation} ${q.point} ${q.tag}`.toLowerCase();return (tag==='all'||q.tag===tag)&&(!term||hay.includes(term));})}
  function safeList(){const list=filteredOrder(); if(!list.length)return []; if(current>=list.length)current=list.length-1; if(current<0)current=0; return list;}
  function renderStats(){const vals=Object.values(progress); const correct=vals.filter(v=>v==='correct').length; const wrong=vals.filter(v=>v==='wrong').length; const answered=correct+wrong; const rate=answered?Math.round(correct/answered*100):0; els.total.textContent=QUESTIONS.length; els.correct.textContent=correct; els.wrong.textContent=wrong; els.rate.textContent=`${rate}%`; els.bar.style.width=`${Math.round(answered/QUESTIONS.length*100)}%`;}
  function renderFocus(){const list=safeList(); selected=null; els.feedback.classList.remove('show'); if(!list.length){els.cardIndex.textContent='該当なし';els.cardTag.textContent='-';els.cardLevel.textContent='-';els.q.textContent='条件に合う問題がありません。';els.choices.innerHTML='';return;} const q=QUESTIONS[list[current]]; els.cardIndex.textContent=`Q ${current+1} / ${list.length}`; els.cardTag.textContent=q.tag; els.cardLevel.textContent=q.level; els.q.textContent=q.question; els.choices.innerHTML=q.options.map((opt,i)=>`<button class="choice" data-choice="${i}" type="button"><span class="label">${String.fromCharCode(65+i)}</span><span class="txt">${escapeHtml(opt)}</span></button>`).join(''); els.choices.querySelectorAll('.choice').forEach(btn=>btn.addEventListener('click',()=>choose(Number(btn.dataset.choice))));}
  function choose(i){const list=safeList(); if(!list.length)return; const q=QUESTIONS[list[current]]; selected=i; const ok=i===q.correct; progress[q.id]=ok?'correct':'wrong'; saveProgress(); els.choices.querySelectorAll('.choice').forEach((btn,idx)=>{btn.disabled=true; if(idx===q.correct)btn.classList.add('correct'); else if(idx===i)btn.classList.add('wrong'); else btn.classList.add('dim');}); els.feedback.innerHTML=`<b class="${ok?'ok':'ng'}">${ok?'正解':'不正解'}</b><br>${escapeHtml(q.explanation)}<div class="point"><b>ポイント：</b>${escapeHtml(q.point)}</div>`; els.feedback.classList.add('show'); renderStats(); renderList();}
  function renderList(){const list=filteredOrder(); els.list.innerHTML=list.map((i,pos)=>{const q=QUESTIONS[i];const st=progress[q.id]||'';const label=st==='correct'?'正解':st==='wrong'?'復習':'未回答';return `<button class="mini ${st==='correct'?'done':st==='wrong'?'wrong':''}" data-pos="${pos}" type="button"><strong>${pos+1}. ${escapeHtml(q.question)}</strong><small><span>${escapeHtml(q.tag)}</span><span>${escapeHtml(q.level)}</span><span>${label}</span></small></button>`;}).join(''); els.list.querySelectorAll('.mini').forEach(btn=>btn.addEventListener('click',()=>{current=Number(btn.dataset.pos);renderFocus();window.scrollTo({top:document.querySelector('.focus-card').offsetTop-10,behavior:'smooth'})}));}
  function renderAll(){renderStats();renderFocus();renderList();}
  function setup(){for(const tag of tags()){const opt=document.createElement('option');opt.value=tag;opt.textContent=tag;els.tagFilter.appendChild(opt)} $('nextBtn').addEventListener('click',()=>{const list=safeList(); if(current<list.length-1)current++; renderFocus();}); $('prevBtn').addEventListener('click',()=>{if(current>0)current--; renderFocus();}); $('shuffleBtn').addEventListener('click',()=>{order=order.map(v=>[Math.random(),v]).sort((a,b)=>a[0]-b[0]).map(v=>v[1]);current=0;renderAll();}); $('resetBtn').addEventListener('click',()=>{if(confirm('学習記録をリセットしますか？')){progress={};saveProgress();renderAll();}}); els.search.addEventListener('input',()=>{current=0;renderAll();}); els.tagFilter.addEventListener('change',()=>{current=0;renderAll();}); renderAll();}
  window.addEventListener('DOMContentLoaded', setup);
  </script>
</body>
</html>'''


def now_iso() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).isoformat(timespec='seconds')


def clean(s: str) -> str:
    s = re.sub(r'\[\[([^\]|]+\|)?([^\]]+)\]\]', lambda m: m.group(2), s)
    s = re.sub(r'[`*_#>]', '', s)
    s = re.sub(r'^\s*[-*]\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip(' 　:：-')


def short(s: str, limit: int = 94) -> str:
    s = clean(s)
    if len(s) <= limit:
        return s
    cut = s[:limit].rstrip('、。・, ')
    return cut + '…'


def title_chunks(text: str, max_chars: int = 13) -> list[str]:
    text = clean(text)
    chunks: list[str] = []
    text = text.replace('導入プロジェクト', '導入|プロジェクト')
    text = text.replace('・LLM', '・|LLM')
    for part in re.split(r'([・/／|])', text):
        if not part:
            continue
        if part in {'・', '/', '／'} and chunks:
            chunks[-1] += part
            continue
        if part == '|':
            continue
        while len(part) > max_chars:
            chunks.append(part[:max_chars])
            part = part[max_chars:]
        if part:
            chunks.append(part)
    merged: list[str] = []
    for part in chunks:
        if merged and len(merged[-1] + part) <= max_chars:
            merged[-1] += part
        else:
            merged.append(part)
    return merged or [text]


def title_html(title: str) -> str:
    title = clean(title)
    if '：' in title:
        left, right = title.split('：', 1)
        parts = title_chunks(left, 13) + title_chunks(right, 13)
        return '<br>'.join(html.escape(p) for p in parts)
    if ':' in title:
        left, right = title.split(':', 1)
        parts = title_chunks(left, 13) + title_chunks(right, 13)
        return '<br>'.join(html.escape(p) for p in parts)
    return '<br>'.join(html.escape(p) for p in title_chunks(title, 14))


def manifest_titles() -> dict[str, str]:
    path = BASE / 'course_manifest.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    out: dict[str, str] = {}
    for item in data.get('units', []):
        unit_dir = Path(item.get('unit_dir', '')).name
        if unit_dir:
            out[unit_dir] = clean(item.get('title', unit_dir))
    return out


def unit_number(unit_dir: Path) -> int:
    m = re.match(r'unit(\d{2})_', unit_dir.name)
    if not m:
        raise ValueError(f'unit番号を読めない: {unit_dir.name}')
    return int(m.group(1))


def unit_label(num: int) -> str:
    return f'Unit{num:02d}'


def extract_lesson_title(unit_dir: Path, titles: dict[str, str]) -> str:
    if unit_dir.name in titles:
        return titles[unit_dir.name]
    text = (unit_dir / 'lesson.md').read_text(encoding='utf-8')
    for line in text.splitlines():
        if line.startswith('#'):
            return clean(re.sub(r'^#+\s*', '', line))
    return unit_dir.name


def parse_quiz(text: str, label: str, unit_num: int) -> list[dict[str, Any]]:
    blocks = re.split(r'(?=^##\s*(?:Q|問)\s*\d+)', text, flags=re.M)
    questions: list[dict[str, Any]] = []
    for block in blocks:
        if not re.match(r'^##\s*(?:Q|問)\s*\d+', block.strip()):
            continue
        lines = block.splitlines()
        q_lines: list[str] = []
        options: list[str] = []
        correct_letter = ''
        explanation_lines: list[str] = []
        in_explanation = False
        for raw in lines[1:]:
            line = raw.strip()
            if not line:
                continue
            opt = re.match(r'^(?:[-*]\s*)?([A-D])(?:[\.．]|\s)\s*(.+)$', line)
            if opt:
                options.append(short(opt.group(2), 110))
                in_explanation = False
                continue
            ans = re.search(r'正解\s*[:：]\s*([A-D])', line)
            if ans:
                correct_letter = ans.group(1)
                in_explanation = False
                continue
            exp = re.match(r'解説\s*[:：]\s*(.*)$', line)
            if exp:
                in_explanation = True
                if exp.group(1).strip():
                    explanation_lines.append(clean(exp.group(1)))
                continue
            if line.startswith('関連:'):
                in_explanation = False
                continue
            if in_explanation:
                explanation_lines.append(clean(line))
            elif len(options) == 0 and not line.startswith('#'):
                q_lines.append(clean(line))
        if len(options) == 4 and correct_letter in LETTERS and q_lines:
            correct = LETTERS[correct_letter]
            correct_text = options[correct]
            explanation = ' '.join(explanation_lines) if explanation_lines else f'正解は「{correct_text}」。{label}の理解度チェックで確認する基本論点。'
            questions.append({
                'tag': '理解度チェック',
                'level': '基本',
                'question': short(' '.join(q_lines), 120),
                'options': options,
                'correct': correct,
                'explanation': short(explanation, 180),
                'point': short(correct_text, 70),
                'source': 'quiz.md',
            })
    return questions


def parse_exam_entries(text: str) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    card_blocks = re.split(r'(?=^##\s+)', text, flags=re.M)
    for block in card_blocks:
        if not block.strip().startswith('##'):
            continue
        heading = clean(re.sub(r'^##\s+', '', block.splitlines()[0]))
        qa = re.search(r'Q[\.．]\s*(.+?)\s*(?:\n|  \n)A[\.．]\s*(.+?)(?=\n\s*\n|\Z)', block, flags=re.S)
        if qa:
            entries.append((clean(qa.group(1)), clean(qa.group(2))))
            continue
        mem = re.search(r'覚え方\s*[:：]\s*(.+)', block)
        if mem:
            entries.append((f'「{heading}」の覚え方として最も適切なものは？', clean(mem.group(1))))
    return entries


def parse_lesson_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    current = ''
    for raw in text.splitlines():
        line = raw.rstrip()
        h = re.match(r'^(#{2,3})\s+(.+)$', line)
        if h:
            current = clean(re.sub(r'^Scene\s*\d+\s*[:：]\s*', '', h.group(2), flags=re.I))
            continue
        item = clean(line)
        if not item or item.startswith('関連:') or item.startswith('Unit:') or item.startswith('タイトル:') or item.startswith('対象ページ:'):
            continue
        if current and current.lower() not in SKIP_HEADINGS and len(item) >= 5:
            if len(item) > 130:
                sentence = re.split(r'(?<=[。.!?？])', item)[0]
                item = sentence if len(sentence) >= 5 else item
            entries.append((current, short(item, 120), current))
    seen: set[tuple[str, str]] = set()
    unique: list[tuple[str, str, str]] = []
    for heading, answer, tag in entries:
        key = (heading, answer)
        if key not in seen:
            unique.append((heading, answer, tag))
            seen.add(key)
    return unique


def unique_texts(values: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        v = short(value, 110)
        if len(v) < 4 or v in seen:
            continue
        out.append(v)
        seen.add(v)
    return out


def make_options(correct_text: str, pool: list[str], desired_correct: int) -> tuple[list[str], int]:
    correct_text = short(correct_text, 110)
    distractors = [p for p in unique_texts(pool + GENERIC_DISTRACTORS) if p != correct_text]
    selected = distractors[:3]
    while len(selected) < 3:
        selected.append(GENERIC_DISTRACTORS[len(selected) % len(GENERIC_DISTRACTORS)])
    desired_correct = desired_correct % 4
    options: list[str] = []
    it = iter(selected)
    for i in range(4):
        if i == desired_correct:
            options.append(correct_text)
        else:
            options.append(next(it))
    return options, desired_correct


def generated_question(question: str, answer: str, pool: list[str], tag: str, level: str, idx: int, source: str, label: str) -> dict[str, Any]:
    options, correct = make_options(answer, pool, idx % 4)
    return {
        'tag': short(tag, 18),
        'level': level,
        'question': short(question, 120),
        'options': options,
        'correct': correct,
        'explanation': short(f'正解は「{answer}」。{label}では、この観点を業務導入の判断材料として押さえる。', 190),
        'point': short(answer, 72),
        'source': source,
    }


def build_questions(unit_dir: Path, titles: dict[str, str]) -> tuple[str, list[dict[str, Any]], dict[str, int]]:
    num = unit_number(unit_dir)
    label = unit_label(num)
    lesson_text = (unit_dir / 'lesson.md').read_text(encoding='utf-8')
    quiz_text = (unit_dir / 'quiz.md').read_text(encoding='utf-8')
    exam_text = (unit_dir / 'exam_cards.md').read_text(encoding='utf-8')
    title = extract_lesson_title(unit_dir, titles)

    quiz_qs = parse_quiz(quiz_text, label, num)
    exam_entries = parse_exam_entries(exam_text)
    lesson_entries = parse_lesson_entries(lesson_text)
    pool = [a for _, a in exam_entries] + [a for _, a, _ in lesson_entries]

    qs: list[dict[str, Any]] = []
    qs.extend(quiz_qs)

    for q_text, answer in exam_entries:
        if len(qs) >= 20:
            break
        question = q_text if q_text.endswith('？') or q_text.endswith('?') else f'{q_text}として最も適切なものは？'
        qs.append(generated_question(question, answer, pool, '試験カード', '基本', len(qs), 'exam_cards.md', label))

    for heading, answer, tag in lesson_entries:
        if len(qs) >= 20:
            break
        question = f'{label}の「{heading}」で押さえるべき内容は？'
        level = LEVELS[min(len(qs) // 8, 2)]
        qs.append(generated_question(question, answer, pool, tag or '講義ノート', level, len(qs), 'lesson.md', label))

    while len(qs) < 20:
        answer = pool[len(qs) % len(pool)] if pool else '業務課題、リスク、効果測定をセットで確認する'
        qs.append(generated_question(f'{label}の要点として最も適切なものは？', answer, pool, '追加確認', '標準', len(qs), 'lesson.md', label))

    final: list[dict[str, Any]] = []
    seen_questions: set[str] = set()
    for i, q in enumerate(qs):
        q = dict(q)
        question = clean(q['question'])
        if question in seen_questions:
            question = f'{question}（確認{i+1}）'
        seen_questions.add(question)
        q['id'] = f'u{num:02d}-{len(final)+1:03d}'
        q['question'] = question
        q['level'] = q.get('level') or LEVELS[min(i // 8, 2)]
        q['tag'] = q.get('tag') or '確認'
        q['explanation'] = q.get('explanation') or f'正解は「{q["options"][q["correct"]]}」。'
        q['point'] = q.get('point') or q['options'][q['correct']]
        q.pop('source', None)
        final.append(q)
        if len(final) == 20:
            break
    counts = {'quiz': len(quiz_qs), 'exam_entries': len(exam_entries), 'lesson_entries': len(lesson_entries)}
    return title, final, counts


def validate_questions(questions: list[dict[str, Any]], unit_name: str) -> list[str]:
    errors: list[str] = []
    if len(questions) != 20:
        errors.append(f'{unit_name}: question count {len(questions)} != 20')
    ids = [q.get('id') for q in questions]
    if len(ids) != len(set(ids)):
        errors.append(f'{unit_name}: duplicated ids')
    required = ['id', 'question', 'options', 'correct', 'explanation', 'point', 'tag', 'level']
    for idx, q in enumerate(questions, 1):
        for key in required:
            if key not in q or q[key] in ('', None, []):
                errors.append(f'{unit_name} Q{idx}: missing {key}')
        if not isinstance(q.get('options'), list) or len(q.get('options', [])) != 4:
            errors.append(f'{unit_name} Q{idx}: options count != 4')
        if not isinstance(q.get('correct'), int) or not 0 <= q.get('correct', -1) <= 3:
            errors.append(f'{unit_name} Q{idx}: correct out of range')
        if isinstance(q.get('options'), list) and len(set(q['options'])) != len(q['options']):
            errors.append(f'{unit_name} Q{idx}: duplicated options')
    text = json.dumps(questions, ensure_ascii=False)
    if FORBIDDEN_FOOTER in text:
        errors.append(f'{unit_name}: forbidden footer text found in questions')
    for pat in SECRET_PATTERNS:
        if pat in text:
            errors.append(f'{unit_name}: secret pattern found: {pat}')
    return errors


def build_html(unit_dir: Path, title: str, questions: list[dict[str, Any]]) -> str:
    num = unit_number(unit_dir)
    label = unit_label(num)
    data = json.dumps(questions, ensure_ascii=False, indent=2)
    out = HTML_TEMPLATE
    out = out.replace('__DATA__', data)
    out = out.replace('__UNIT_LABEL__', label)
    out = out.replace('__TITLE_HTML__', title_html(title))
    out = out.replace('__STATE_KEY__', f'sio-{unit_dir.name}-four-choice-v1')
    return out


def write_qa(unit_dir: Path, out_dir: Path, title: str, questions: list[dict[str, Any]], counts: dict[str, int], errors: list[str]) -> None:
    num = unit_number(unit_dir)
    label = unit_label(num)
    rel_html = out_dir.relative_to(BASE) / 'index.html'
    rel_qa = out_dir.relative_to(BASE) / 'qa_report.md'
    status = 'PASS' if not errors else 'FAIL'
    tags = sorted({q['tag'] for q in questions})
    correct_range_ok = all(isinstance(c := q.get('correct'), int) and 0 <= c <= 3 for q in questions)
    content = f'''# [[{label}]] 四択HTML問題集 QA Report

## 成果物
- HTML: `{rel_html}`
- QA: `{rel_qa}`
- 生成スクリプト: `question_bank/scripts/build_all_question_banks.py`

## 内容
- Unit: [[{label}]]
- タイトル: {title}
- 問題数: {len(questions)}問
- 形式: 四択 / 即時正誤判定 / 解説表示 / 正解・復習カウント / 検索 / タグ絞り込み / シャッフル
- 素材: `units/{unit_dir.name}/lesson.md` / `quiz.md` / `exam_cards.md`
- 素材抽出: quiz {counts['quiz']}件 / exam_cards {counts['exam_entries']}件 / lesson {counts['lesson_entries']}件
- タグ: {', '.join(tags)}

## 検証結果
- 静的検証: {status}
- 20問固定: {'OK' if len(questions) == 20 else 'NG'}
- 各問4択: {'OK' if all(len(q.get('options', [])) == 4 for q in questions) else 'NG'}
- `correct` 0〜3: {'OK' if correct_range_ok else 'NG'}
- `explanation` / `point` / `tag` / `level`: {'OK' if all(q.get('explanation') and q.get('point') and q.get('tag') and q.get('level') for q in questions) else 'NG'}
- 削除済みフッター文言: {'未検出' if FORBIDDEN_FOOTER not in json.dumps(questions, ensure_ascii=False) else '検出'}
- 秘密情報パターン: {'未検出' if not any(p in json.dumps(questions, ensure_ascii=False) for p in SECRET_PATTERNS) else '検出'}

## エラー
{chr(10).join('- ' + e for e in errors) if errors else '- なし'}

## 生成時刻
- {now_iso()}

関連: [[{label}]] / [[HTML問題集]] / [[四択問題]] / [[AIエージェント・ストラテジスト]]
'''
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'qa_report.md').write_text(content, encoding='utf-8')


def target_units() -> list[Path]:
    units = sorted(p for p in UNITS_DIR.iterdir() if p.is_dir() and re.match(r'unit\d{2}_', p.name))
    return [p for p in units if unit_number(p) >= 2]


def build_all(validate_only: bool = False) -> tuple[list[dict[str, Any]], list[str]]:
    titles = manifest_titles()
    summaries: list[dict[str, Any]] = []
    all_errors: list[str] = []
    for unit_dir in target_units():
        title, questions, counts = build_questions(unit_dir, titles)
        errors = validate_questions(questions, unit_dir.name)
        out_dir = QB_DIR / unit_dir.name
        html_text = build_html(unit_dir, title, questions)
        if FORBIDDEN_FOOTER in html_text:
            errors.append(f'{unit_dir.name}: forbidden footer text found in html')
        for pat in SECRET_PATTERNS:
            if pat in html_text:
                errors.append(f'{unit_dir.name}: secret pattern found in html: {pat}')
        if not validate_only:
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / 'index.html').write_text(html_text, encoding='utf-8')
            write_qa(unit_dir, out_dir, title, questions, counts, errors)
        summaries.append({
            'unit': unit_number(unit_dir),
            'unit_dir': unit_dir.name,
            'title': title,
            'questions': len(questions),
            'output': str((out_dir / 'index.html').relative_to(BASE)),
            'qa_report': str((out_dir / 'qa_report.md').relative_to(BASE)),
            'status': 'PASS' if not errors else 'FAIL',
            'errors': errors,
        })
        all_errors.extend(errors)
    return summaries, all_errors


def write_summary_report(summaries: list[dict[str, Any]], errors: list[str]) -> None:
    pass_count = sum(1 for s in summaries if s['status'] == 'PASS')
    lines = [
        '# [[question_bank]] Unit02-45 四択HTML問題集 QA Summary',
        '',
        '## 概要',
        f'- 生成対象: {len(summaries)}ユニット（[[Unit02]]〜[[Unit45]]）',
        f'- PASS: {pass_count}',
        f'- FAIL: {len(summaries) - pass_count}',
        f'- 生成時刻: {now_iso()}',
        '',
        '## 検証観点',
        '- 各Unit 20問',
        '- 各問4択',
        '- `correct` は0〜3',
        '- `explanation` / `point` / `tag` / `level` を保持',
        '- 削除済みフッター文言を含めない',
        '- 秘密情報パターンを含めない',
        '',
        '## Unit別結果',
    ]
    for s in summaries:
        lines.append(f"- [[Unit{s['unit']:02d}]] `{s['output']}` / `{s['qa_report']}` / {s['questions']}問 / {s['status']}")
    lines.extend(['', '## エラー', *(('- ' + e for e in errors) if errors else ['- なし']), '', '関連: [[AIエージェント・ストラテジスト]] / [[question_bank]] / [[HTML問題集]]'])
    SUMMARY_QA.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def validate_written_files() -> tuple[int, int, list[str]]:
    html_count = 0
    qa_count = 0
    errors: list[str] = []
    for unit_dir in target_units():
        out_dir = QB_DIR / unit_dir.name
        index = out_dir / 'index.html'
        qa = out_dir / 'qa_report.md'
        if index.exists():
            html_count += 1
            text = index.read_text(encoding='utf-8')
            if FORBIDDEN_FOOTER in text:
                errors.append(f'{index}: forbidden footer')
            if '<script>' not in text or 'const QUESTIONS =' not in text:
                errors.append(f'{index}: QUESTIONS script missing')
        else:
            errors.append(f'{index}: missing')
        if qa.exists():
            qa_count += 1
            if FORBIDDEN_FOOTER in qa.read_text(encoding='utf-8'):
                errors.append(f'{qa}: forbidden footer')
        else:
            errors.append(f'{qa}: missing')
    return html_count, qa_count, errors


def main() -> None:
    parser = argparse.ArgumentParser(description='Build four-choice HTML question banks for Unit02-45.')
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    summaries, errors = build_all(validate_only=args.validate_only)
    if not args.validate_only:
        write_summary_report(summaries, errors)
    html_count, qa_count, file_errors = validate_written_files() if not args.validate_only else (0, 0, [])
    total_errors = errors + file_errors
    print(f'TARGET_UNITS {len(summaries)}')
    print(f'GENERATED_HTML {html_count}')
    print(f'GENERATED_QA {qa_count}')
    print(f'QUESTION_COUNT_OK {sum(1 for s in summaries if s["questions"] == 20)}/{len(summaries)}')
    print(f'PASS_UNITS {sum(1 for s in summaries if s["status"] == "PASS")}/{len(summaries)}')
    print(f'FORBIDDEN_FOOTER_FOUND {"YES" if any("forbidden" in e for e in total_errors) else "NO"}')
    print(f'ERROR_COUNT {len(total_errors)}')
    if total_errors:
        for error in total_errors[:50]:
            print(f'ERROR {error}')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
