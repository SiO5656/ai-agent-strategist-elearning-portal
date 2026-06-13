# [[Unit18]] QA report

## 概要
- 対象: [[Unit18]] データの種類と特性：構造化・非構造化・メタデータ
- 状態: completed_drive_verified
- 検証日時: 2026-06-07 22:52 JST

## 生成状況
- 教材ファイル: 作成済み
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`assets_gptimage2/scene10.png` 採用済み
- [[ElevenLabs]] TTS: `audio/scene01.mp3`〜`audio/scene10.mp3` 作成済み
- [[Remotion]]: `remotion_video_study_20260607_224555/`
- MP4: `video_study.mp4`
- Drive link: https://drive.google.com/file/d/1W-tHBdLlQIsaSS4PqPImbwwEpq4Ecpag/view?usp=drivesdk
- Drive file ID: `1W-tHBdLlQIsaSS4PqPImbwwEpq4Ecpag`

## 実行QA
- raw image contact sheet: `qa/raw_image_contact_sheet.png` / Vision QA合格
- `npm run lint`: 成功
- `npm run still`: 成功 / `remotion_video_study_20260607_224555/qa/still.png`
- `npm run render`: 成功
- `ffprobe`: `h264/aac`, `1080x1920`, duration `308.352000s`, size `23075091` bytes, bitrate `598668`
- `blackdetect`: `black_start`なし
- `volumedetect`: mean `-16.9 dB`, max `-3.7 dB`
- final midpoint contact sheet: `remotion_video_study_20260607_224555/qa/final_midpoint_contact_sheet.png` / Vision QA合格
- Drive metadata / permissions: `mimeType=video/mp4`, size一致、owner `shiomaruclaw@gmail.com`、public sharing false

## QA判定
- 10シーン順序・固定テンプレート・見切れなし。
- Step表示はタイトルカード右上のみ、`Step NN/10`。
- 下部カード見出しは `おさえるべきポイント`、下部カード内Stepなし。
- 下端フッター・進捗バー・内部テンプレート文言なし。
- 画像内黒枠・透かし・メールアドレス・制作都合語なし。

## 証跡
- MP4: `projects/ai-agent-strategist-course/elearning_v2/units/unit18_data_types_metadata/video_study.mp4`
- raw contact sheet: `projects/ai-agent-strategist-course/elearning_v2/units/unit18_data_types_metadata/qa/raw_image_contact_sheet.png`
- final midpoint contact sheet: `projects/ai-agent-strategist-course/elearning_v2/units/unit18_data_types_metadata/remotion_video_study_20260607_224555/qa/final_midpoint_contact_sheet.png`
- Drive metadata: `projects/ai-agent-strategist-course/elearning_v2/units/unit18_data_types_metadata/drive_upload_unit18_metadata_20260607_225202.json`

関連: [[Unit18]] / [[QA]] / [[GPT Image 2]] / [[Remotion]] / [[Google Drive]]
