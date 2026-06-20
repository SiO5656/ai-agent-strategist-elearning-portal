# [[question_bank]] Unit02-45 四択HTML問題集 展開計画

## 目的
- [[Unit01]]で作成したスマホ向け四択問題集パターンを、[[Unit02]]〜[[Unit45]]の残り44ユニットへ展開する。
- 各Unitの `lesson.md` / `quiz.md` / `exam_cards.md` を素材に、各20問の四択HTMLを生成する。

## 実行体制
- 統合・検証: [[default]] profile
- 実装ワーカー: [[coder]] profile

## フェーズ
1. 素材と既存構成を確認する。
2. 汎用生成スクリプトを作成する。
3. [[Unit02]]〜[[Unit45]]のHTMLとQAレポートを生成する。
4. 全Unitの静的検証、JS/HTML構造検証、モバイル幅サンプルQAを行う。
5. 成果物・ログ・日次メモを更新して報告する。

## 受け入れ条件
- `question_bank/unitXX_*/index.html` が44件追加される。
- 各HTMLに20問の `QUESTIONS` が埋め込まれている。
- 各問題が4択、`correct` が0〜3、解説とポイントを持つ。
- Unit01で削除したフッター文言を含めない。
- 代表的なスマホ幅〜PC幅で横スクロールを出さないCSSを維持する。

関連: [[AIエージェント・ストラテジスト]] / [[question_bank]]
