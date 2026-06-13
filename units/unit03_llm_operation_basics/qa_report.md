# Unit03 QA Report

## 初期作成
- 素材セットアップ完了。
- 画像生成は[[GPT Image 2]] / [[Codex CLI]]で1枚ずつ直列実行する。
- Driveアップロードはユーザー指示により後回し。

関連: [[Unit03]] / [[GPT Image 2]] / [[Remotion]]

## 2026-06-06 Unit03制作・レンダーQA

### 教材・音声
- `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` 作成済み。
- `audio/scene01.mp3`〜`audio/scene08.mp3` 生成済み。

### [[GPT Image 2]]スライドQA
- `assets_gptimage2/scene01.png`〜`scene08.png` 生成済み。
- scene01〜scene08: Vision QAで主要ラベル、見切れなし、番号バッジなし、透かしなし、個人情報なしを確認。
- scene06は「モデルルーティング」の小さい「ィ」字形が不安定だったため2枚不採用。最終スライドではタイトルを「モデルを振り分ける」に変更。
- 不採用画像:
  - `assets_gptimage2/rejected/scene06_title_glyph_20260606_182205.png`
  - `assets_gptimage2/rejected/scene06_title_glyph_second_20260606_182558.png`

### Remotion / MP4
- render dir: `/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2/units/unit03_llm_operation_basics/remotion_video_study_20260606_183921`
- lint: `npm run lint` 成功。
- render: `npm run render` 成功。
- 最適化: `ffmpeg -c:v libx264 -crf 30 -c:a aac -b:a 96k` 実施。
- 正本候補: `video_study.mp4`
- duration: 223.104s
- size: 12690861 bytes
- bitrate: 455065 bps
- contact sheet: `/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2/units/unit03_llm_operation_basics/remotion_video_study_20260606_183921/qa/unit03_optimized_midframe_contact_sheet.png`
- blackdetect: 0 lines（0.5秒以上の黒画面検出なし）
- 中間フレームQA: 全8scene表示、黒画面/空白sceneなし、主要スライド見切れなし、下部カード/用語メモ読める、Step表示は固定位置。上部の`Unit03`と`01/08`等はRemotionテンプレート側のヘッダー表示で、GPT Image 2スライド内への混入ではない。

### Drive
- [[Google Drive]]アップロードはユーザー指示により後回し。

関連: [[AIエージェント・ストラテジスト]] / [[Unit03]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]]

## 2026-06-13 Drive納品・正式完了検証
- 状態: `completed_drive_verified`
- Drive: https://drive.google.com/file/d/16KwbndOwo1olPit-HVSZHAOe6CBXvqHf/view?usp=drivesdk
- file ID: `16KwbndOwo1olPit-HVSZHAOe6CBXvqHf`
- MP4: `units/unit03_llm_operation_basics/video_study.mp4`
- ffprobe: `1080x1920`, `h264/aac`, local size `12690861` bytes
- Drive readback: `mimeType=video/mp4`, size `12690861` bytes、local/Drive size一致
- permissions: owner only `shiomaruclaw@gmail.com`、public/domain共有なし
- final contact sheet: `qa/final_u01_u04_20260613/unit01_04_final_contact_sheet.jpg`
- blackdetect: `qa/final_u01_u04_20260613/blackdetect_summary.txt`（black_startなし）
関連: [[Unit03]] / [[Google Drive]] / [[動画QA]]
