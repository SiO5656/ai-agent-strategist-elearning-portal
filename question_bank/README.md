# [[AIエージェント・ストラテジスト]] HTML問題集

## 目的

各Unitの学習内容を、四択でスマホ復習できるHTML問題集として展開する。

## 成果物

- [[Unit01]]: `unit01_course_orientation/index.html`
- [[Unit02]]〜[[Unit45]]: `unitXX_slug/index.html`
- 全体QA: `qa_report.md`
- 仕様: `DESIGN.md`
- 生成スクリプト: `scripts/build_all_question_banks.py`
- モバイルQAスクリプト: `scripts/mobile_cdp_qa_question_banks.mjs`

## 概要

- 問題数: 45Unit × 20問 = 900問
- 形式: 四択 / 即時正誤判定 / 解説表示 / 正解・復習カウント / 検索 / タグ絞り込み / シャッフル
- モバイルQA: CDP 390x844で全45HTMLを検証し、横スクロールなし

## 生成・検証

- 生成: `python3 question_bank/scripts/build_all_question_banks.py`
- モバイルQA: `node question_bank/scripts/mobile_cdp_qa_question_banks.mjs`

関連: [[AIエージェント・ストラテジスト]] / [[HTML問題集]] / [[四択問題]] / [[スマホQA]]
