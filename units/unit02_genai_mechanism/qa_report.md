# Unit02 QAレポート

## 対象
- Unit: [[Unit02]] 生成AIの基本構造：従来AI・機械学習・LLMの違い
- Unit dir: `units/unit02_genai_mechanism/`
- Manifest範囲: p.11〜p.17
- 実参照ファイル: `../extracted_text/pages/page_011.txt`〜`page_017.txt`

## 現在状態
- 状態: `materials_created`
- 教材: `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` 作成済み
- [[GPT Image 2]]完成スライド: 未生成
- 音声: 未生成
- 正式動画: 未生成
- [[Google Drive]]: 未アップロード

## ソース・サニタイズQA
- 原文丸写しなし: 講義ノートとして再構成済み
- 個人情報透かし・メールアドレス・購入者情報: 生成教材本文へ入れない方針

関連: [[AIエージェント・ストラテジスト]] / [[Unit02]] / [[GPT Image 2]] / [[Google Drive]]

## 2026-06-06 Unit02素材生成開始
- 教材: `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` / `prompts_gptimage2/scene01.txt`〜`scene08.txt` 作成済み。
- ソース範囲: p.11〜p.17を参照し、原文丸写しではなく講義用に再構成。
- サニタイズ検索: `t.shio` / `gmail.com` / `盭目` / `剛` は生成教材内0件。
- 音声: `audio/scene01.mp3`〜`scene08.mp3` 生成済み。

関連: [[AIエージェント・ストラテジスト]] / [[Unit02]] / [[TTS]] / [[GPT Image 2]]


## 2026-06-06 Unit02制作・レンダーQA

### 教材・音声
- `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` 作成済み。
- `audio/scene01.mp3`〜`audio/scene08.mp3` 生成済み。
- 音声合計: 約188.88秒。

### [[GPT Image 2]]スライドQA
- `assets_gptimage2/scene01.png`〜`scene08.png` 生成済み。
- scene01〜scene08: Vision QAで主要ラベル、見切れなし、番号バッジなし、透かしなし、個人情報なしを確認。
- scene08は「鵜呑み」漢字の字形が不安定だったため2枚不採用。最終スライドでは「うのみにしない」へ簡略化。
- 不採用画像:
  - `assets_gptimage2/rejected/scene08_unomi_glyph_20260606_1714.png`
  - `assets_gptimage2/rejected/scene08_unomi_glyph_second_20260606_1718.png`

### Remotion / MP4
- render dir: `/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2/units/unit02_genai_mechanism/remotion_video_study_20260606_172413`
- lint: `npm run lint` 成功。
- render: `npm run render` 成功。
- 最適化: `ffmpeg -c:v libx264 -crf 30 -c:a aac -b:a 96k` 実施。
- 正本候補: `video_study.mp4`
- duration: 200.064s
- size: 12278715 bytes
- bitrate: 490991 bps
- contact sheet: `/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2/units/unit02_genai_mechanism/remotion_video_study_20260606_172413/qa/unit02_optimized_midframe_contact_sheet.png`
- 中間フレームQA: 全8scene表示、黒画面/空白sceneなし、主要スライド見切れなし、下部カード/用語メモ読める、scene08下部「うのみにしない」確認。

### Drive
- [[Google Drive]]アップロードはユーザー指示により後回し。

関連: [[AIエージェント・ストラテジスト]] / [[Unit02]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]]

## 2026-06-13 Drive納品・正式完了検証
- 状態: `completed_drive_verified`
- Drive: https://drive.google.com/file/d/1b5g-LyEEW34R4J63hDU0LGE5TVkWdhf6/view?usp=drivesdk
- file ID: `1b5g-LyEEW34R4J63hDU0LGE5TVkWdhf6`
- MP4: `units/unit02_genai_mechanism/video_study.mp4`
- ffprobe: `1080x1920`, `h264/aac`, local size `12278715` bytes
- Drive readback: `mimeType=video/mp4`, size `12278715` bytes、local/Drive size一致
- permissions: owner only `shiomaruclaw@gmail.com`、public/domain共有なし
- final contact sheet: `qa/final_u01_u04_20260613/unit01_04_final_contact_sheet.jpg`
- blackdetect: `qa/final_u01_u04_20260613/blackdetect_summary.txt`（black_startなし）
関連: [[Unit02]] / [[Google Drive]] / [[動画QA]]
