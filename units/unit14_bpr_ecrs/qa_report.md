# [[Unit14]] QA report

## 概要
- Unit: [[Unit14]] BPRとECRS：自動化前に業務を見直す
- 検証日時: 2026-06-07 16:49 JST
- ローカルMP4: `video_study.mp4`
- Remotion render dir: `remotion_video_study_20260607_162313/`

## 実行結果
- `npm run lint`: OK
- `npm run still`: OK (`remotion_video_study_20260607_162313/qa/still.png`)
- `npm run render`: OK
- `ffprobe`: `h264`, `1080x1920`, `236.352000s`, `19449446` bytes, bitrate `658321`
- audio: `aac`, `48000Hz`, `2ch`
- `blackdetect`: 0件
- `volumedetect`: mean `-17.3 dB`, max `-3.7 dB`

## 視覚QA
- raw image contact sheet: `qa/unit14_image_contact_sheet.png`
- final midpoint contact sheet: `qa/unit14_final_midframe_contact_sheet.png`
- [[GPT Image 2]]完成スライド: 10枚（scene01〜scene10）
- [[Remotion]]外側画像フレーム: あり
- [[GPT Image 2]]画像内の黒いページ枠/黒枠: なし
- Step: タイトルカード右上のみ、`Step NN/10` 一行
- 下部カード: Stepなし、見出し `おさえるべきポイント`
- 下端フッター/進捗バー: なし
- 見切れ/横溢れ/重大な文字化け: なし

## Drive検証
- Driveリンク: https://drive.google.com/file/d/1fVIDt9gPp2fEgJo6F5X7-cCVnf3hOBrW/view?usp=drivesdk
- File ID: `1fVIDt9gPp2fEgJo6F5X7-cCVnf3hOBrW`
- Drive保存先: `Exports/videos/2026/2026-06-07_unit14_bpr_ecrs_video_study.mp4`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner userのみ
- public sharing: なし

関連: [[Unit14]] / [[QA]] / [[Google Drive]] / [[Remotion]]
