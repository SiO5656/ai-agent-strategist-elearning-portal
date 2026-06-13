# [[Unit23]] QA Report - AIプロジェクトの進め方：PoC中心の導入初期設計

## 判定
- status: `passed_drive_verified`
- completed_at: `2026-06-09T00:17:23+09:00`
- Drive link: https://drive.google.com/file/d/1rmTGXzeX03AXcDpvj3NRIcN9FPc_oZ9m/view?usp=drivesdk
- Drive file ID: `1rmTGXzeX03AXcDpvj3NRIcN9FPc_oZ9m`
- 共有範囲: owner only `shiomaruclaw@gmail.com`（public sharing false）

## 成果物
- MP4: `units/unit23_ai_project_poc/video_study.mp4`
- Remotion: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/`
- raw slide contact sheet: `units/unit23_ai_project_poc/qa/raw_slide_contact_sheet.jpg`
- raw slide manifest: `units/unit23_ai_project_poc/qa/raw_slide_manifest.json`
- still: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/still.png`
- final midpoint contact sheet: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/midpoint_contact_sheet.jpg`
- progress bar contact sheet: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/progress_bar_crop_contact_sheet.jpg`
- ffprobe: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/ffprobe_video_study.json`
- blackdetect: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/blackdetect.log`
- volumedetect: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/volumedetect.log`
- media summary: `units/unit23_ai_project_poc/remotion_video_study_20260608_125444/qa/qa_media_summary.json`

## メディア仕様
- format: `1080x1920` vertical MP4
- video codec: `h264` / pixel format `yuvj420p`
- audio codec: `aac` / sample rate `48000`
- duration: `287.274667s`
- size: `21814169` bytes
- bitrate: `607479`
- scenes: `10`
- fps: `24`
- Remotion versions: `4.0.473` / all packages correct

## 実行QA
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功
- `ffprobe`: `1080x1920` / `h264` / `aac` / local size `21814169` bytes
- `blackdetect`: `black_start` なし（検出0件）
- `volumedetect`: mean `-17.0 dB`, max `-3.6 dB`
- raw slide dimensions: 10枚すべて `1086x1448`、`all_ratio_3_4=true`
- 進捗バーコードQA: `src/StudyVideo.tsx` に `progressFooter` / `progressFill`、`src/style.css` に `.progressFooter` / `.progressFill` が存在（`true`）

## 目視QA
- raw slide contact sheet: [[GPT Image 2]]完成スライド10枚を確認。白ベース図解、3:4縦スライド、安全マージンあり。スライド番号、Unit番号、透かし、メール、購入者情報、制作都合語は見えない。
- still/final midpoint contact sheet: 10シーン順序OK。黒画面/空白なし。Step表示はタイトルカード右上のみ。下部カード内Step重複なし。下端フッター/内部テンプレート名/制作ラベルなし。
- 進捗バーQA: `progress_bar_crop_contact_sheet.jpg` で10シーンすべてに控えめな全体進捗バーを視認。[[Unit19]]指摘後の `bottom:150px` / `height:11px` 方針を維持。

## Drive検証
- file ID: `1rmTGXzeX03AXcDpvj3NRIcN9FPc_oZ9m`
- name: `2026-06-09_unit23_ai_project_poc_video_study.mp4`
- mimeType: `video/mp4`
- Drive size: `21814169` bytes（ローカルMP4と一致）
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only
- public sharing: `false`

## 補足
- 初回画像QAで2:3画像混入とRemotion `src/scenes.json` staleを検知したため、対象8枚を3:4で直列再生成し、Unit23用 `scenes.json` を再構築してからレンダーした。
- 再発防止記録: `kakotora/2026-06-08_unit23-aspect-ratio-and-stale-scenes-json.md`

関連: [[AIエージェント・ストラテジスト]] / [[Unit23]] / [[PoC]] / [[Remotion]] / [[Google Drive]]
