# [[Unit13]] QA report

## 概要
- Unit: [[Unit13]] 業務ギャップ分析：改善候補を見極める
- 検証日時: 2026-06-07 15:30 JST
- ローカルMP4: `video_study.mp4`
- Remotion render dir: `remotion_video_study_20260607_151206/`

## 実行結果
- `npm run lint`: OK
- `npm run still`: OK (`remotion_video_study_20260607_151206/qa/still.png`)
- `npm run render`: OK
- `ffprobe`: `h264`, `1080x1920`, `306.112000s`, `23192285` bytes, bitrate `606112`
- `blackdetect`: 0件
- `volumedetect`: mean `-17.0 dB`, max `-3.6 dB`

## 視覚QA
- final midpoint contact sheet: `remotion_video_study_20260607_151206/qa/unit13_final_midframe_contact_sheet.png`
- [[Remotion]]外側画像フレーム: あり
- [[GPT Image 2]]画像内の黒いページ枠/黒枠: なし
- Step: タイトルカード右上のみ、`Step NN/09` 一行
- 下部カード: Stepなし、見出し `おさえるべきポイント`
- 見切れ/横溢れ/重大な文字化け: なし

## Drive検証
- Driveリンク: https://drive.google.com/file/d/1X_Ckkp8tpITApZAQi_woBBaY2f191BZ8/view?usp=drivesdk
- File ID: `1X_Ckkp8tpITApZAQi_woBBaY2f191BZ8`
- Drive保存先: `Exports/videos/2026/2026-06-07_unit13_business_gap_analysis_video_study.mp4`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner userのみ
- public sharing: なし

関連: [[Unit13]] / [[QA]] / [[Google Drive]] / [[Remotion]]
