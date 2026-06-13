# [[Unit22]] QA Report - 社内データをAI活用資産に変える実践

## 判定
- status: `passed_drive_verified`
- completed_at: `2026-06-08T10:16:33+09:00`
- Drive link: https://drive.google.com/file/d/1JGzoq68CizqWhb5E8kJj1798UEyG9BI4/view?usp=drivesdk
- Drive file ID: `1JGzoq68CizqWhb5E8kJj1798UEyG9BI4`
- 共有範囲: owner only `shiomaruclaw@gmail.com`（public sharing false）

## 成果物
- MP4: `units/unit22_data_asset_practice/video_study.mp4`
- Remotion: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/`
- raw slide contact sheet: `units/unit22_data_asset_practice/qa/raw_slide_contact_sheet.png`
- still: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/qa/still.png`
- final midpoint contact sheet: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/qa/final_midpoint_contact_sheet.png`
- ffprobe: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/qa/ffprobe.json`
- blackdetect: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/qa/blackdetect.log`
- volumedetect: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/qa/volumedetect.log`
- media summary: `units/unit22_data_asset_practice/remotion_video_study_20260608_094816/qa/qa_media_summary.json`

## メディア仕様
- format: `1080x1920` vertical MP4
- video codec: `h264` / pixel format `yuvj420p`
- audio codec: `aac` / sample rate `48000`
- duration: `259.114667s`
- size: `19915979` bytes
- bitrate: `614893`
- scenes: `10`
- fps: `24`
- Remotion versions: `4.0.473` / all packages correct

## 実行QA
- `npm install`: 成功
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功
- `ffprobe`: `1080x1920` / `h264` / `aac` / local size `19915979` bytes
- `blackdetect`: `black_start` なし（検出0件）
- `volumedetect`: mean `-16.9 dB`, max `-3.6 dB`
- 進捗バーコードQA: `src/StudyVideo.tsx` に `progressFooter` / `progressFill`、`src/style.css` に `.progressFooter` / `.progressFill` が存在

## 目視QA
- raw slide contact sheet: [[GPT Image 2]]完成スライド10枚を確認。白ベース図解、安全マージンあり、短い日本語ラベル中心。スライド番号、Unit番号、透かし、メール、購入者情報、制作都合語は見えない。
- still/final midpoint contact sheet: 10シーン順序OK。黒画面/空白なし。Step表示はタイトルカード右上のみ。下部カード内Step重複なし。下端フッター/内部テンプレート名/制作ラベルなし。
- 進捗バーQA: final midpoint contact sheetで各シーン下端に控えめな全体進捗バーを視認。[[Unit19]]で指摘された進捗バー消失はUnit22では再発なし。

## Drive検証
- file ID: `1JGzoq68CizqWhb5E8kJj1798UEyG9BI4`
- name: `2026-06-08_unit22_data_asset_practice_video_study.mp4`
- mimeType: `video/mp4`
- Drive size: `19915979` bytes（ローカルMP4と一致）
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only
- public sharing: `false`

関連: [[AIエージェント・ストラテジスト]] / [[Unit22]] / [[AI活用資産]] / [[Remotion]] / [[Google Drive]]
