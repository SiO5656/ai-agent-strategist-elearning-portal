# [[Unit21]] QA Report - AIが読みやすいデータ設計：区切り・表記・検索性

## 判定
- status: `passed_drive_verified`
- completed_at: `2026-06-08T09:28:47+09:00`
- Drive link: https://drive.google.com/file/d/1GvGk2_9drNhEsbPYSYtH5OkPJnt9tunL/view?usp=drivesdk
- Drive file ID: `1GvGk2_9drNhEsbPYSYtH5OkPJnt9tunL`
- 共有範囲: owner only `shiomaruclaw@gmail.com`（public sharing false）

## 成果物
- MP4: `units/unit21_ai_readable_data_design/video_study.mp4`
- Remotion: `units/unit21_ai_readable_data_design/remotion_video_study_20260608_091950/`
- raw slide contact sheet: `units/unit21_ai_readable_data_design/qa/raw_slide_contact_sheet.png`
- still: `units/unit21_ai_readable_data_design/remotion_video_study_20260608_091950/qa/still.png`
- final midpoint contact sheet: `units/unit21_ai_readable_data_design/remotion_video_study_20260608_091950/qa/final_midpoint_contact_sheet.png`
- ffprobe: `units/unit21_ai_readable_data_design/remotion_video_study_20260608_091950/qa/ffprobe.json`
- blackdetect: `units/unit21_ai_readable_data_design/remotion_video_study_20260608_091950/qa/blackdetect.log`
- volumedetect: `units/unit21_ai_readable_data_design/remotion_video_study_20260608_091950/qa/volumedetect.log`

## メディア仕様
- format: `1080x1920` vertical MP4
- video codec: `h264` / pixel format `yuvj420p`
- audio codec: `aac` / sample rate `48000`
- duration: `268.736000s`
- size: `22020243` bytes
- bitrate: `655520`
- scenes: `10`
- fps: `24`

## 実行QA
- `npm install`: 成功
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功
- `ffprobe`: `1080x1920` / `h264` / `aac` / local size `22020243` bytes
- `blackdetect`: `black_start` なし（検出0件）
- `volumedetect`: mean `-17.4 dB`, max `-3.6 dB`
- 進捗バーコードQA: `src/StudyVideo.tsx` に `progressFooter` / `progressFill`、`src/style.css` に `.progressFooter` / `.progressFill` が存在

## 目視QA
- raw slide contact sheet: [[GPT Image 2]]完成スライド10枚を確認。白ベース図解、安全マージンあり、短い日本語ラベル中心。明らかな見切れ、メール、透かし、ページ番号、Unit番号バッジなし。
- still/final midpoint contact sheet: 10シーン順序OK。黒画面/空白なし。Step表示はタイトルカード右上のみ。下部カード内Step重複なし。下端フッター/内部テンプレート名/制作ラベルなし。
- 進捗バーQA: 各シーン下端に控えめな全体進捗バーを視認。[[Unit19]]で消えた進捗バーはUnit21では維持済み。

## Drive検証
- file ID: `1GvGk2_9drNhEsbPYSYtH5OkPJnt9tunL`
- name: `2026-06-08_unit21_ai_readable_data_design_video_study.mp4`
- mimeType: `video/mp4`
- Drive size: `22020243` bytes（ローカルMP4と一致）
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only
- public sharing: `false`

関連: [[AIエージェント・ストラテジスト]] / [[Unit21]] / [[AI Readyデータ]] / [[RAG]] / [[Remotion]] / [[Google Drive]]
