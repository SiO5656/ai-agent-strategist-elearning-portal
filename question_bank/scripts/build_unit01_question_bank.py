#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

BASE = Path('/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2')
OUT = BASE / 'question_bank' / 'unit01_course_orientation' / 'index.html'

QUESTIONS = [
    {
        'id': 'u01-001', 'tag': '基本姿勢', 'level': '基本',
        'question': '生成AIの個人利用と組織導入の違いとして最も適切なものは？',
        'options': ['個人利用はリスクがなく、組織導入だけにリスクがある', '個人利用は作業効率化が中心で、組織導入は業務選定・定着・効果測定まで含む', '組織導入ではプロンプトを書く必要がない', '組織導入ではAIの精度だけを確認すればよい'],
        'correct': 1,
        'explanation': '個人が使えることと、組織で成果が出ることは別。組織導入では業務選定、現場受容、リスク、費用対効果、運用定着まで設計する。',
        'point': '「使える」と「成果が出る」は別能力。'
    },
    {
        'id': 'u01-002', 'tag': '役割', 'level': '基本',
        'question': 'AIエージェント・ストラテジストの役割として最も近いものは？',
        'options': ['便利なAIツールだけを紹介する人', 'AI画像を作る専門担当者', 'AIを業務や組織へ実装し、成果につなげる導入設計者', 'AIモデルをゼロから開発する研究者'],
        'correct': 2,
        'explanation': 'AIエージェント・ストラテジストは、技術・業務・組織をつなぎ、関係者を巻き込みながら導入を設計する役割。',
        'point': '単なるツール紹介ではなく導入設計。'
    },
    {
        'id': 'u01-003', 'tag': '3本柱', 'level': '基本',
        'question': 'この講座の3本柱として正しい組み合わせは？',
        'options': ['画像生成・文章生成・音声生成', 'プロンプト・モデル・API', '営業・経理・人事', 'AIエージェント・業務設計・組織設計'],
        'correct': 3,
        'explanation': '講座全体の土台は、AIエージェント、業務設計、組織設計の3本柱。',
        'point': '技術・業務・組織を同時に見る。'
    },
    {
        'id': 'u01-004', 'tag': '3本柱', 'level': '基本',
        'question': '「AIエージェント」の柱で主に学ぶことは？',
        'options': ['仕組み、限界、起動タイプ、接続標準、価値とリスク', '現場の評価制度だけ', '財務諸表の読み方だけ', '動画編集とデザイン'],
        'correct': 0,
        'explanation': 'AIエージェントの柱では、技術の可能性だけでなく、限界やリスクも説明できるようにする。',
        'point': '可能性と制約の両方を説明する。'
    },
    {
        'id': 'u01-005', 'tag': '3本柱', 'level': '基本',
        'question': '「業務設計」の柱で重視することは？',
        'options': ['AIを入れる業務と入れ方を決めるため、業務を構造的に分析すること', '最新AIツールを毎日比較すること', '社内広報だけを担当すること', 'AIの精度だけを測ること'],
        'correct': 0,
        'explanation': '業務設計では、対象業務を見極め、必要ならAI前提で業務を作り直す。',
        'point': '対象業務の選定が先。'
    },
    {
        'id': 'u01-006', 'tag': '3本柱', 'level': '基本',
        'question': '「組織設計」の柱で重視することは？',
        'options': ['AIの出力をきれいに整えることだけ', '現場と技術を橋渡しし、AIが根づく仕組みを作ること', 'プログラミング言語を暗記すること', '全員に同じプロンプトを配ること'],
        'correct': 1,
        'explanation': '組織設計では、推進体制、KPI、役割設計、リスキリング、変化への不安への対応などを扱う。',
        'point': '使われ続ける仕組みが必要。'
    },
    {
        'id': 'u01-007', 'tag': '学習法', 'level': '基本',
        'question': '各Sectionの学習の流れとして正しいものは？',
        'options': ['理解度チェック → 業務シナリオ → 知識', '知識 → 業務シナリオ → 理解度チェック', '動画視聴 → 雑談 → 暗記', 'ツール選定 → 契約 → 導入'],
        'correct': 1,
        'explanation': 'まず知識を押さえ、業務シナリオで実務に当てはめ、理解度チェックで判断ポイントを確認する。',
        'point': '暗記だけでなくケース判断まで進める。'
    },
    {
        'id': 'u01-008', 'tag': '学習法', 'level': '基本',
        'question': '読む時に意識する3つの問いとして最も適切なものは？',
        'options': ['どの業務に適用するか、どこにリスクがあるか、誰に何を確認すべきか', 'どのAIが一番新しいか、価格はいくらか、SNSで話題か', '誰が反対したか、誰を説得するか、誰が悪いか', 'どの画像が綺麗か、音声が自然か、字幕が大きいか'],
        'correct': 0,
        'explanation': '試験対策でも実務でも、適用業務・リスク・確認相手を考えることが判断力につながる。',
        'point': '実務判断の型として覚える。'
    },
    {
        'id': 'u01-009', 'tag': '理解度チェック', 'level': '基本',
        'question': '「AIの精度だけを見れば導入は成功する」という説明は？',
        'options': ['正しい。精度が高ければ必ず定着する', '正しい。現場設計は導入後でよい', '誤り。業務の選び方と現場で使われる仕組みまで設計が必要', '誤り。ただしリスク整理は不要'],
        'correct': 2,
        'explanation': 'AIの精度だけでは、業務に合うか、現場が使うか、効果が測れるかは判断できない。',
        'point': '精度だけではなく業務・組織を見る。'
    },
    {
        'id': 'u01-010', 'tag': '理解度チェック', 'level': '基本',
        'question': '「画像生成・文章生成・音声生成」は、この講座の3本柱として正しい？',
        'options': ['正しい。生成AIの主要機能なので3本柱である', '誤り。正しくはAIエージェント・業務設計・組織設計', '正しい。ただし音声生成は任意である', '誤り。正しくは営業・経理・人事'],
        'correct': 1,
        'explanation': '画像・文章・音声生成は機能分類。導入設計の柱はAIエージェント、業務設計、組織設計。',
        'point': '機能分類と導入設計の柱を混同しない。'
    },
    {
        'id': 'u01-011', 'tag': '導入観点', 'level': '標準',
        'question': 'AIエージェント導入で、技術以外に考えるべき観点として不適切なものは？',
        'options': ['対象業務の選定', '現場受容と運用定着', '効果測定や費用対効果', '最新ツール名だけを覚えること'],
        'correct': 3,
        'explanation': '最新ツール名だけを覚えても導入判断には不十分。業務・現場・効果・リスクを整理する必要がある。',
        'point': '技術以外の観点を複数持つ。'
    },
    {
        'id': 'u01-012', 'tag': 'ひっかけ', 'level': '標準',
        'question': '「最新ツールを選ぶことが最重要なので、業務分析は導入後でよい」は正しい？',
        'options': ['正しい。ツールが決まらないと何も判断できない', '正しい。業務分析は現場に任せればよい', '誤り。先に対象業務、業務構造、関係者、リスク、効果測定を整理する', '誤り。ただし関係者調整は不要'],
        'correct': 2,
        'explanation': '導入前に、何の業務課題を解くのか、誰が関わるのか、効果をどう測るのかを整理する。',
        'point': 'ツール選定より業務設計が先。'
    },
    {
        'id': 'u01-013', 'tag': 'ケース判断', 'level': '標準',
        'question': '社内でChatGPT利用者は増えたが生産性改善につながっていない。最初に見るべきものは？',
        'options': ['利用者にもっと長いプロンプトを書かせること', 'どの業務課題に適用するのか、使う流れと効果測定指標があるか', '有料プランに全員で加入しているか', 'AIの回答をすべて人手で修正するか'],
        'correct': 1,
        'explanation': '利用者数ではなく、業務課題、現場の利用フロー、効果測定指標を確認する。',
        'point': '利用率だけで成果は判断しない。'
    },
    {
        'id': 'u01-014', 'tag': '導入観点', 'level': '標準',
        'question': '組織導入で出やすい壁として最も適切なものは？',
        'options': ['どの業務に導入すべきか分からない', '個人利用ではAIが一切使えない', 'AI導入では法務や情シスは関係ない', '現場が使い続けなくても成果は出る'],
        'correct': 0,
        'explanation': 'ほかにも、現場が使い続けない、効果測定できない、関係者調整が追いつかないなどの壁がある。',
        'point': '導入前・導入中・導入後の壁を意識。'
    },
    {
        'id': 'u01-015', 'tag': '判断軸', 'level': '標準',
        'question': '導入する人が答えるべき問いとして適切でないものは？',
        'options': ['どの業務にAIエージェントを適用するか', 'どの業務には適用しないか', '投資対効果をどう説明するか', 'とにかく全業務にAIを入れるにはどうするか'],
        'correct': 3,
        'explanation': '導入設計では、適用する業務だけでなく、適用しない業務も判断する。全業務に無条件で入れる発想は危険。',
        'point': '「適用しない」判断も重要。'
    },
    {
        'id': 'u01-016', 'tag': '学習マップ', 'level': '標準',
        'question': 'Chapter 1で学ぶ中心テーマは？',
        'options': ['AIエージェントを知る', '組織文化だけを学ぶ', '5Dモデルだけを学ぶ', '会計処理だけを学ぶ'],
        'correct': 0,
        'explanation': 'Chapter 1では、生成AI、AIエージェント、起動タイプ、RPAとの違い、MCP、価値とリスクを学ぶ。',
        'point': '基礎概念と違いの説明が中心。'
    },
    {
        'id': 'u01-017', 'tag': '学習マップ', 'level': '標準',
        'question': 'Chapter 2〜3で学ぶ中心テーマは？',
        'options': ['業務とデータを見る', '動画編集を覚える', '採用面接だけを設計する', 'SNS投稿を自動化する'],
        'correct': 0,
        'explanation': 'Chapter 2〜3では、As-Is/To-Be、BPR、業務可視化、ナレッジ、RAG、ガバナンス、データ設計などを扱う。',
        'point': 'AI導入前に業務とデータを構造化する。'
    },
    {
        'id': 'u01-018', 'tag': '学習マップ', 'level': '標準',
        'question': 'Chapter 4〜6の流れとして最も適切なものは？',
        'options': ['画像生成 → 音声生成 → 動画生成', 'ワークフロー作成 → 組織を動かす → 5Dモデルでプロジェクトを回す', '契約 → 請求 → 支払い', '採用 → 評価 → 退職'],
        'correct': 1,
        'explanation': 'Chapter 4はワークフロー、Chapter 5は組織、Chapter 6は5Dモデルによる導入プロジェクト運営を扱う。',
        'point': '設計 → 組織 → プロジェクト運営。'
    },
    {
        'id': 'u01-019', 'tag': '共通シナリオ', 'level': '標準',
        'question': 'Chapter 1〜2の共通シナリオは？',
        'options': ['採用スクリーニングAI', '請求書処理AI', '社内ITヘルプデスクAI', '営業提案書の自動生成AI'],
        'correct': 2,
        'explanation': '社内ITヘルプデスクAIを題材に、問い合わせ、FAQ対応、担当者工数、現場の問い合わせ内容を見ながら導入判断を学ぶ。',
        'point': '概念を実務ケースで判断する。'
    },
    {
        'id': 'u01-020', 'tag': '試験対策', 'level': '応用',
        'question': 'このUnitで最も避けたい勘違いは？',
        'options': ['用語だけでなく導入判断も説明する必要がある', 'AIの精度や最新ツールだけを見れば導入は成功する', '業務設計と組織設計も重要である', 'リスクや確認相手を考える必要がある'],
        'correct': 1,
        'explanation': '最新ツールや精度だけでは導入は成功しない。業務設計・組織設計・リスク整理・定着設計が必要。',
        'point': 'ひっかけは「技術だけで十分」に寄りやすい。'
    },
]


def build_html() -> str:
    data = json.dumps(QUESTIONS, ensure_ascii=False, indent=2)
    return f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>Unit01 四択問題集 | AIエージェント・ストラテジスト</title>
  <style>
    :root {{
      --bg:#f6f8fb; --panel:#fff; --text:#172033; --muted:#63708a; --line:#dfe6f1;
      --blue:#2563eb; --blue2:#dbeafe; --green:#10b981; --green2:#dcfce7; --red:#ef4444; --red2:#fee2e2; --orange:#f59e0b;
      --shadow:0 18px 50px rgba(16,24,40,.10); --radius:24px;
      font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Yu Gothic","YuGothic","Noto Sans JP",sans-serif;
    }}
    *{{box-sizing:border-box}} html,body{{margin:0;min-height:100%;background:var(--bg);color:var(--text)}} body{{overflow-x:hidden}} button,input,select{{font:inherit}}
    .app{{width:min(1120px,100%);margin:0 auto;padding:20px clamp(14px,3vw,32px) 64px}}
    .hero{{background:linear-gradient(135deg,#fff 0%,#eef5ff 56%,#f7fbff 100%);border:1px solid #e5edf8;border-radius:30px;padding:clamp(18px,4vw,34px);box-shadow:var(--shadow);overflow:hidden;position:relative}}
    .hero:after{{content:"";position:absolute;right:-70px;top:-80px;width:220px;height:220px;background:rgba(37,99,235,.10);border-radius:50%}}
    .eyebrow{{display:inline-flex;gap:8px;align-items:center;color:#1d4ed8;background:#eff6ff;border:1px solid #bfdbfe;padding:7px 12px;border-radius:999px;font-weight:800;font-size:13px}}
    h1{{margin:16px 0 10px;font-size:clamp(26px,5.8vw,44px);line-height:1.12;letter-spacing:-.04em}}
    .lead{{margin:0;color:var(--muted);font-size:clamp(15px,2vw,18px);line-height:1.75;max-width:780px}}
    .stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:20px}}
    .stat{{background:rgba(255,255,255,.78);border:1px solid #e5edf8;border-radius:18px;padding:12px;min-width:0}} .stat b{{display:block;font-size:22px;line-height:1}} .stat span{{display:block;margin-top:6px;color:var(--muted);font-size:12px}}
    .progress-shell{{height:10px;background:#e8eef8;border-radius:999px;overflow:hidden;margin-top:12px}} .progress-bar{{height:100%;width:0%;background:linear-gradient(90deg,var(--blue),#06b6d4);border-radius:999px;transition:width .2s}}
    .toolbar{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0}} .control{{flex:1 1 180px;min-width:0;border:1px solid var(--line);background:#fff;border-radius:16px;padding:12px 14px;color:var(--text)}}
    .btn{{border:0;border-radius:16px;padding:13px 16px;background:#e8eef8;color:#1f2a44;font-weight:900;cursor:pointer;min-height:48px}} .btn.primary{{background:var(--blue);color:#fff}} .btn.ghost{{background:#fff;border:1px solid var(--line)}} .btn:active{{transform:translateY(1px)}}
    .main-grid{{display:grid;grid-template-columns:minmax(0,1.12fr) minmax(300px,.88fr);gap:18px;align-items:start}}
    .focus-card,.list-panel{{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);min-width:0}} .focus-card{{padding:clamp(18px,4vw,30px)}} .list-panel{{padding:18px}}
    .meta-row{{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:18px}} .pill{{display:inline-flex;border-radius:999px;padding:7px 11px;background:#f1f5f9;color:#475569;font-size:12px;font-weight:900}} .pill.blue{{background:var(--blue2);color:#1d4ed8}}
    .qtext{{font-size:clamp(21px,5.2vw,32px);line-height:1.45;letter-spacing:-.02em;margin:10px 0 18px;font-weight:900;overflow-wrap:anywhere}}
    .choices{{display:grid;gap:10px;margin-top:14px}} .choice{{width:100%;text-align:left;border:2px solid var(--line);background:#fff;border-radius:18px;padding:14px 14px;min-height:58px;display:flex;gap:10px;align-items:flex-start;line-height:1.55;cursor:pointer}}
    .choice .label{{flex:0 0 auto;width:28px;height:28px;border-radius:50%;display:inline-grid;place-items:center;background:#eef2ff;color:#1d4ed8;font-weight:900}} .choice .txt{{min-width:0;overflow-wrap:anywhere}}
    .choice.correct{{border-color:#22c55e;background:var(--green2)}} .choice.wrong{{border-color:#f87171;background:var(--red2)}} .choice.dim{{opacity:.55}}
    .feedback{{display:none;margin-top:16px;padding:16px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:20px;line-height:1.75}} .feedback.show{{display:block}} .feedback b.ok{{color:#15803d}} .feedback b.ng{{color:#b91c1c}}
    .point{{border-left:4px solid var(--green);padding-left:12px;color:#334155;margin-top:10px}}
    .actions{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:18px}}
    .list-panel h2{{margin:0 0 12px;font-size:20px}} .cards{{display:grid;gap:10px;max-height:620px;overflow:auto;padding-right:4px}}
    .mini{{text-align:left;border:1px solid var(--line);background:#fff;border-radius:16px;padding:12px;cursor:pointer;min-width:0}} .mini.done{{border-color:#86efac;background:#f0fdf4}} .mini.wrong{{border-color:#fca5a5;background:#fff1f2}}
    .mini strong{{display:block;font-size:14px;line-height:1.45;white-space:normal;overflow-wrap:anywhere}} .mini small{{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;color:var(--muted)}}
    .footer-note{{color:var(--muted);margin:20px 0 0;font-size:13px;line-height:1.7}}
    @media(max-width:760px){{.app{{padding:12px 12px 48px}}.hero{{border-radius:24px}}.stats{{grid-template-columns:repeat(2,1fr)}}.main-grid{{grid-template-columns:1fr}}.control{{flex-basis:100%}}.btn{{width:100%}}.actions{{grid-template-columns:1fr}}.cards{{max-height:none;overflow:visible}}}}
    @media(max-width:390px){{.app{{padding-left:10px;padding-right:10px}}.hero,.focus-card,.list-panel{{border-radius:20px}}.stat b{{font-size:20px}}.choice{{padding:13px 12px}}}}
  </style>
</head>
<body>
  <main class="app">
    <section class="hero">
      <div class="eyebrow">Unit01 テスト版 · 四択問題集</div>
      <h1>講座オリエンテーション<br>AIを使う人から<br>導入する人へ</h1>
      <p class="lead">スマホで解きやすい四択形式。選択するとすぐ正誤と解説が出ます。Unit01の講義ノート・理解度チェック・試験直前カードから20問に再構成。</p>
      <div class="stats" aria-label="学習状況">
        <div class="stat"><b id="statTotal">20</b><span>全問題</span></div><div class="stat"><b id="statCorrect">0</b><span>正解</span></div><div class="stat"><b id="statWrong">0</b><span>復習</span></div><div class="stat"><b id="statRate">0%</b><span>正答率</span></div>
      </div>
      <div class="progress-shell"><div class="progress-bar" id="progressBar"></div></div>
    </section>
    <section class="toolbar" aria-label="操作">
      <input class="control" id="searchBox" type="search" placeholder="検索：例 3本柱 / リスク / Chapter" />
      <select class="control" id="tagFilter" aria-label="タグ絞り込み"><option value="all">すべてのタグ</option></select>
      <button class="btn ghost" id="shuffleBtn" type="button">シャッフル</button>
      <button class="btn ghost" id="resetBtn" type="button">記録リセット</button>
    </section>
    <section class="main-grid">
      <article class="focus-card" aria-live="polite">
        <div class="meta-row"><span class="pill blue" id="cardIndex">Q 1 / 20</span><span class="pill" id="cardTag">基本姿勢</span><span class="pill" id="cardLevel">基本</span></div>
        <div class="qtext" id="questionText"></div>
        <div class="choices" id="choices"></div>
        <div class="feedback" id="feedback"></div>
        <div class="actions"><button class="btn ghost" id="prevBtn" type="button">前へ</button><button class="btn primary" id="nextBtn" type="button">次へ</button></div>
      </article>
      <aside class="list-panel"><h2>全問リスト</h2><div class="cards" id="cardList"></div></aside>
    </section>
  </main>
  <script>
  const QUESTIONS = {data};
  const stateKey = 'sio-unit01-four-choice-v1';
  let order = QUESTIONS.map((_, i) => i); let current = 0; let selected = null; let progress = loadProgress();
  const $ = id => document.getElementById(id);
  const els = {{total:$('statTotal'),correct:$('statCorrect'),wrong:$('statWrong'),rate:$('statRate'),bar:$('progressBar'),q:$('questionText'),choices:$('choices'),feedback:$('feedback'),cardIndex:$('cardIndex'),cardTag:$('cardTag'),cardLevel:$('cardLevel'),list:$('cardList'),tagFilter:$('tagFilter'),search:$('searchBox')}};
  function loadProgress(){{try{{return JSON.parse(localStorage.getItem(stateKey))||{{}}}}catch{{return {{}}}}}} function saveProgress(){{localStorage.setItem(stateKey,JSON.stringify(progress))}}
  function escapeHtml(s){{return String(s).replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
  function tags(){{return [...new Set(QUESTIONS.map(q=>q.tag))]}}
  function filteredOrder(){{const term=els.search.value.trim().toLowerCase();const tag=els.tagFilter.value;return order.filter(i=>{{const q=QUESTIONS[i];const hay=`${{q.question}} ${{q.options.join(' ')}} ${{q.explanation}} ${{q.point}} ${{q.tag}}`.toLowerCase();return (tag==='all'||q.tag===tag)&&(!term||hay.includes(term));}})}}
  function safeList(){{const list=filteredOrder(); if(!list.length)return []; if(current>=list.length)current=list.length-1; if(current<0)current=0; return list;}}
  function renderStats(){{const vals=Object.values(progress); const correct=vals.filter(v=>v==='correct').length; const wrong=vals.filter(v=>v==='wrong').length; const answered=correct+wrong; const rate=answered?Math.round(correct/answered*100):0; els.total.textContent=QUESTIONS.length; els.correct.textContent=correct; els.wrong.textContent=wrong; els.rate.textContent=`${{rate}}%`; els.bar.style.width=`${{Math.round(answered/QUESTIONS.length*100)}}%`;}}
  function renderFocus(){{const list=safeList(); selected=null; els.feedback.classList.remove('show'); if(!list.length){{els.cardIndex.textContent='該当なし';els.cardTag.textContent='-';els.cardLevel.textContent='-';els.q.textContent='条件に合う問題がありません。';els.choices.innerHTML='';return;}} const q=QUESTIONS[list[current]]; els.cardIndex.textContent=`Q ${{current+1}} / ${{list.length}}`; els.cardTag.textContent=q.tag; els.cardLevel.textContent=q.level; els.q.textContent=q.question; els.choices.innerHTML=q.options.map((opt,i)=>`<button class="choice" data-choice="${{i}}" type="button"><span class="label">${{String.fromCharCode(65+i)}}</span><span class="txt">${{escapeHtml(opt)}}</span></button>`).join(''); els.choices.querySelectorAll('.choice').forEach(btn=>btn.addEventListener('click',()=>choose(Number(btn.dataset.choice))));}}
  function choose(i){{const list=safeList(); if(!list.length)return; const q=QUESTIONS[list[current]]; selected=i; const ok=i===q.correct; progress[q.id]=ok?'correct':'wrong'; saveProgress(); els.choices.querySelectorAll('.choice').forEach((btn,idx)=>{{btn.disabled=true; if(idx===q.correct)btn.classList.add('correct'); else if(idx===i)btn.classList.add('wrong'); else btn.classList.add('dim');}}); els.feedback.innerHTML=`<b class="${{ok?'ok':'ng'}}">${{ok?'正解':'不正解'}}</b><br>${{escapeHtml(q.explanation)}}<div class="point"><b>ポイント：</b>${{escapeHtml(q.point)}}</div>`; els.feedback.classList.add('show'); renderStats(); renderList();}}
  function renderList(){{const list=filteredOrder(); els.list.innerHTML=list.map((i,pos)=>{{const q=QUESTIONS[i];const st=progress[q.id]||'';const label=st==='correct'?'正解':st==='wrong'?'復習':'未回答';return `<button class="mini ${{st==='correct'?'done':st==='wrong'?'wrong':''}}" data-pos="${{pos}}" type="button"><strong>${{pos+1}}. ${{escapeHtml(q.question)}}</strong><small><span>${{escapeHtml(q.tag)}}</span><span>${{escapeHtml(q.level)}}</span><span>${{label}}</span></small></button>`;}}).join(''); els.list.querySelectorAll('.mini').forEach(btn=>btn.addEventListener('click',()=>{{current=Number(btn.dataset.pos);renderFocus();window.scrollTo({{top:document.querySelector('.focus-card').offsetTop-10,behavior:'smooth'}})}}));}}
  function renderAll(){{renderStats();renderFocus();renderList();}}
  function setup(){{for(const tag of tags()){{const opt=document.createElement('option');opt.value=tag;opt.textContent=tag;els.tagFilter.appendChild(opt)}} $('nextBtn').addEventListener('click',()=>{{const list=safeList(); if(current<list.length-1)current++; renderFocus();}}); $('prevBtn').addEventListener('click',()=>{{if(current>0)current--; renderFocus();}}); $('shuffleBtn').addEventListener('click',()=>{{order=order.map(v=>[Math.random(),v]).sort((a,b)=>a[0]-b[0]).map(v=>v[1]);current=0;renderAll();}}); $('resetBtn').addEventListener('click',()=>{{if(confirm('学習記録をリセットしますか？')){{progress={{}};saveProgress();renderAll();}}}}); els.search.addEventListener('input',()=>{{current=0;renderAll();}}); els.tagFilter.addEventListener('change',()=>{{current=0;renderAll();}}); renderAll();}}
  window.addEventListener('DOMContentLoaded', setup);
  </script>
</body>
</html>'''


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_html(), encoding='utf-8')
    print(f'WROTE {OUT}')
    print(f'QUESTION_COUNT {len(QUESTIONS)}')
    print('FORMAT four_choice')

if __name__ == '__main__':
    main()
