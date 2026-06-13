# [[Unit16]] QA Report - ナレッジマネジメント：暗黙知・形式知・SECIモデル

## 結論
- status: `completed_drive_verified`
- 判定: 合格
- 完了時刻: 2026-06-07 20:42 JST
- Drive: https://drive.google.com/file/d/102G1TyQ_3WUF7lZGEUSluR29W23YIfUK/view?usp=drivesdk

## 成果物
- MP4: `video_study.mp4`
- [[Remotion]]作業ディレクトリ: `remotion_video_study_20260607_203140/`
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene10.png`
- TTS音声: `audio/scene01.mp3`〜`scene10.mp3`
- 画像contact sheet: `qa/unit16_image_contact_sheet.png`
- midpoint frame contact sheet: `remotion_video_study_20260607_203140/qa/unit16_midframe_contact_sheet.png`

## Remotion / Render
- `npm install`: 成功
- `npm run lint`: 成功
- `npm run still`: 成功（`qa/still.png`）
- `npm run render`: 成功（`out/video_study.mp4`）
- Unit直下配置: `video_study.mp4`

## Media probe
- container duration: `294.101333s`
- file size: `22741225` bytes
- format bit_rate: `618595`
- video: `h264`, `1080x1920`, `24fps`, duration `294.083333s`, bit_rate `295646`
- audio: `aac`, duration `294.101333s`, bit_rate `317375`
- blackdetect: `black_start` なし（1秒以上の黒画面検出なし）
- volumedetect: mean `-17.0 dB`, max `-3.5 dB`

## Visual QA
- still QA: 合格。見切れ、黒枠、不要フッター/進捗バー、下部カードはみ出しなし。
- midpoint contact sheet QA: 合格。10シーン順序通り、黒/空白フレームなし、Step表示はタイトルカード右上のみ、下部カード内Step非表示、不要なUnit番号/ページ番号/透かし/メールなし。
- [[SECIモデル]]の順序: 共同化 → 表出化 → 連結化 → 内面化 の循環として確認。

## Drive verification
- file ID: `102G1TyQ_3WUF7lZGEUSluR29W23YIfUK`
- link: https://drive.google.com/file/d/102G1TyQ_3WUF7lZGEUSluR29W23YIfUK/view?usp=drivesdk
- name: `2026-06-07_unit16_knowledge_seci_video_study.mp4`
- mimeType: `video/mp4`
- Drive size: `22741225`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only（公開 `anyone` 共有なし）
- metadata readback: `qa/drive_metadata_20260607.json`

関連: [[Unit16]] / [[ナレッジマネジメント]] / [[SECIモデル]] / [[Remotion]] / [[Google Drive]]
