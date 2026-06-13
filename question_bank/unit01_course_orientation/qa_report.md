# [[Unit01]] 四択HTML問題集 QA Report

## 成果物

- HTML: `question_bank/unit01_course_orientation/index.html`
- 生成スクリプト: `question_bank/scripts/build_unit01_question_bank.py`
- モバイルQAスクリプト: `question_bank/scripts/mobile_cdp_qa_unit01.py`
- 390px QAスクリーンショット: `question_bank/unit01_course_orientation/mobile_cdp_390x844.png`

## 内容

- 問題数: 20問
- 形式: 四択 / 即時正誤判定 / 解説表示 / 正解・復習カウント / 検索 / タグ絞り込み / シャッフル
- 素材: `units/unit01_course_orientation/lesson.md` / `quiz.md` / `exam_cards.md`
- 変更: 初期の一問一答式から、しおの希望に合わせて四択問題へ変更。

## 検証結果

### ブラウザ動作

- `file:///.../question_bank/unit01_course_orientation/index.html` を[[ブラウザ]]で表示確認。
- JS console: エラーなし。
- 正解選択: 正解カウント `1`、解説表示を確認。
- 不正解選択: 復習カウント `1`、正答ハイライト・解説表示を確認。
- 検索 `3本柱`: 5件に絞り込み確認。

### モバイルQA

[[Chrome]] [[CDP]]で `390x844`, `deviceScaleFactor=2` として検証。

```json
{
  "clientWidth": 390,
  "scrollWidth": 390,
  "bodyScrollWidth": 390,
  "miniCount": 20,
  "firstQuestion": "生成AIの個人利用と組織導入の違いとして最も適切なものは？",
  "buttons": [
    {"text": "シャッフル", "h": 52, "w": 370},
    {"text": "記録リセット", "h": 52, "w": 370},
    {"text": "A...", "h": 80, "w": 332},
    {"text": "B...", "h": 104, "w": 332},
    {"text": "C...", "h": 80, "w": 332}
  ],
  "titleRect": {"x": 29, "width": 332, "right": 361}
}
```

- 横スクロールなし。
- 右端切れなし。
- 見出し改行崩れなし。
- 選択肢ボタンは80px以上でタップしやすい。
- 主要カードは画面幅内。ファーストビュー下端で問題カードが続くが、縦スクロール前提として自然。

### 秘密情報チェック

- `@gmail.com`, `sk-`, `BEGIN PRIVATE KEY`, `refresh_token`, `client_secret` の混入なし。

## 注意点

- テスト版のためDriveアップロードは未実施。
- Unit02以降は同じ四択構造で、各Unitの `lesson.md` / `quiz.md` / `exam_cards.md` から20問前後へ再構成する。

関連: [[Unit01]] / [[HTML問題集]] / [[四択問題]] / [[スマホQA]] / [[AIエージェント・ストラテジスト]]
