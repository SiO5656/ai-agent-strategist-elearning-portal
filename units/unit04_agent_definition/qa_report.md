# Unit04 QAレポート

## 対象
- Unit: [[Unit04]] AIエージェントとは何か：チャットボットとの違い
- Unit dir: `units/unit04_agent_definition/`
- Manifest範囲: p.26〜p.30
- 実参照ファイル: `../extracted_text/pages/page_026.txt`〜`page_030.txt`

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

関連: [[AIエージェント・ストラテジスト]] / [[Unit04]] / [[GPT Image 2]] / [[Google Drive]]
## 2026-06-06 Unit04素材生成開始
- 教材: `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` / `prompts_gptimage2/scene01.txt`〜`scene08.txt` 作成済み。
- ソース範囲: p.26〜p.30を参照し、原文丸写しではなく講義用に再構成。
- サニタイズ検索: `t.shio` / `gmail.com` / `盭目` / `剛` は生成教材内0件。
- 音声: `audio/scene01.mp3`〜`scene08.mp3` 生成済み。
- 音声合計: 約219.28秒。

関連: [[AIエージェント・ストラテジスト]] / [[Unit04]] / [[TTS]] / [[GPT Image 2]]
## 2026-06-06 Unit04制作・レンダーQA

### 教材・音声
- `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` 作成済み。
- `audio/scene01.mp3`〜`audio/scene08.mp3` 生成済み。
- 音声合計: 約219.28秒。

### [[GPT Image 2]]スライドQA
- `assets_gptimage2/scene01.png`〜`scene08.png` 生成済み。
- scene01〜scene08: Vision QAで主要ラベル、見切れなし、番号バッジなし、透かしなし、不要フッターなし、個人情報なしを確認。
- 生成は同時投入せず、1枚ずつ直列実行。TooManyRequestsなし。

### Remotion / MP4
- render dir: `/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2/units/unit04_agent_definition/remotion_video_study_20260606_233906`
- lint: `npm run lint` 成功。
- render: `npm run render` 成功。
- 最適化: `ffmpeg -c:v libx264 -crf 30 -c:a aac -b:a 96k` 実施。
- 正本候補: `video_study.mp4`
- duration: 235.434s
- size: 13829945 bytes
- bitrate: 469938 bps
- contact sheet: `/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2/units/unit04_agent_definition/remotion_video_study_20260606_233906/qa/unit04_optimized_midframe_contact_sheet.png`
- blackdetect: 0 lines（0.5秒以上の黒画面検出なし）
- 中間フレームQA: 全8scene表示、黒画面/空白sceneなし、主要スライド見切れなし、下部カード/用語メモ読める、Step表示は固定位置。上部の`Unit04`と`01/08`等はRemotionテンプレート側のヘッダー表示で、GPT Image 2スライド内への混入ではない。

### Drive
- [[Google Drive]]アップロードはgws再認証後に後回し。

関連: [[AIエージェント・ストラテジスト]] / [[Unit04]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]]

## 2026-06-13 Drive納品・正式完了検証
- 状態: `completed_drive_verified`
- Drive: https://drive.google.com/file/d/1xCgwNzRMTLslvfUEYf_M9v7wmMtSHAzb/view?usp=drivesdk
- file ID: `1xCgwNzRMTLslvfUEYf_M9v7wmMtSHAzb`
- MP4: `units/unit04_agent_definition/video_study.mp4`
- ffprobe: `1080x1920`, `h264/aac`, local size `13829945` bytes
- Drive readback: `mimeType=video/mp4`, size `13829945` bytes、local/Drive size一致
- permissions: owner only `shiomaruclaw@gmail.com`、public/domain共有なし
- final contact sheet: `qa/final_u01_u04_20260613/unit01_04_final_contact_sheet.jpg`
- blackdetect: `qa/final_u01_u04_20260613/blackdetect_summary.txt`（black_startなし）
関連: [[Unit04]] / [[Google Drive]] / [[動画QA]]
