# [[question_bank]] Unit02-45 展開 Findings

## 2026-06-13 初期確認
- `units/` 配下に [[Unit01]]〜[[Unit45]] の45ディレクトリが存在する。
- 全45ユニットに `lesson.md` / `quiz.md` / `exam_cards.md` が存在する。
- [[Unit01]]の四択HTMLテンプレートは `question_bank/unit01_course_orientation/index.html`、生成元は `question_bank/scripts/build_unit01_question_bank.py`。
- 削除対象だったフッター文言は [[Unit01]] HTMLと生成スクリプトから削除済み。

## 2026-06-13 生成結果
- 汎用生成スクリプト `question_bank/scripts/build_all_question_banks.py` は、`course_manifest.json` からUnitタイトル、各Unitの `quiz.md` / `exam_cards.md` / `lesson.md` から問題素材を抽出する。
- [[Unit02]]〜[[Unit45]]の44ユニットすべてで、20問・4択・`correct` 0〜3・`explanation` / `point` / `tag` / `level` を持つHTMLを生成できた。
- 既存[[Unit01]]を含めると `question_bank/unitXX_*/index.html` は45件、`qa_report.md` はUnit別45件 + 全体サマリー1件。
- 削除済みフッター文言は `question_bank/` 配下で完全一致ヒット0件。

関連: [[AIエージェント・ストラテジスト]] / [[question_bank]]
