# [[Unit06]] 四択HTML問題集 QA Report

## 成果物
- HTML: `question_bank/unit06_agent_trigger_types/index.html`
- QA: `question_bank/unit06_agent_trigger_types/qa_report.md`
- 生成スクリプト: `question_bank/scripts/build_all_question_banks.py`

## 内容
- Unit: [[Unit06]]
- タイトル: AIエージェントの起動タイプを判別する
- 問題数: 20問
- 形式: 四択 / 即時正誤判定 / 解説表示 / 正解・復習カウント / 検索 / タグ絞り込み / シャッフル
- 素材: `units/unit06_agent_trigger_types/lesson.md` / `quiz.md` / `exam_cards.md`
- 素材抽出: quiz 5件 / exam_cards 0件 / lesson 43件
- タグ: 1. 起動タイプは「きっかけ」の設計, 2. 指示型, 3. 定時型, 学習ゴール, 対象範囲, 理解度チェック

## 検証結果
- 静的検証: PASS
- 20問固定: OK
- 各問4択: OK
- `correct` 0〜3: OK
- `explanation` / `point` / `tag` / `level`: OK
- 削除済みフッター文言: 未検出
- 秘密情報パターン: 未検出

## エラー
- なし

## 生成時刻
- 2026-06-21T07:57:13+09:00

関連: [[Unit06]] / [[HTML問題集]] / [[四択問題]] / [[AIエージェント・ストラテジスト]]
