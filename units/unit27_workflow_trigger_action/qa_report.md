# [[Unit27]] QA report - ワークフロー設計：トリガーとアクション

## 結論
- Status: `completed_drive_verified`
- 動画: `video_study.mp4`
- Drive: https://drive.google.com/file/d/11qZWYVa4V4FLACKM8Bam5q-Z731id6yX/view?usp=drivesdk
- File ID: `11qZWYVa4V4FLACKM8Bam5q-Z731id6yX`

## 実行証跡
- TTS: `audio/scene01.mp3`〜`audio/scene10.mp3` を使用。
- Remotion: `npm run lint` / `npm run still` / `npm run render` 済みの成果物を確認。
- local MP4: `units/unit27_workflow_trigger_action/video_study.mp4`
- render MP4: `units/unit27_workflow_trigger_action/remotion_video_study_20260611_000000/out/video_study.mp4`

## メディア検証
- ffprobe: `1080x1920`, `h264/aac`, duration `108.821333s`, size `11430529` bytes, bit_rate `840315`
- blackdetect: exit `0`, black_startなし
- volumedetect: mean `-17.4 dB`, max `-3.6 dB`

## 目視QA
- final midpoint contact sheet: `remotion_video_study_20260611_000000/qa/midpoint_contact_sheet.jpg`
  - 10シーン順序表示、タイトル右上Step、GPT Image 2スライド、下部カード、進捗バーを確認。
  - 重大な見切れ・重なり・黒画面・下端フッター残存なし。
- lower card crop: `remotion_video_study_20260611_000000/qa/lower_card_crop_contact_sheet.jpg`
  - `おさえるべきポイント`表示、本文・用語メモの重大な見切れなし。
- progress crop: `remotion_video_study_20260611_000000/qa/progress_bar_crop_contact_sheet.jpg`
  - 進捗バー視認、下端フッター/制作ラベルなし。

## Drive検証
- Drive metadata readback: `mimeType=video/mp4`, size `11430529`
- Owner: `shiomaruclaw@gmail.com`
- Permissions: owner only / public共有なし

関連: [[Unit27]] / [[Google Drive]] / [[Remotion]] / [[GPT Image 2]]
