# [[Unit25]] QA Report - 成功定義の3層フレームワーク

## 結論

- status: `completed_drive_verified`
- Drive: https://drive.google.com/file/d/1ILCM6pXTtiy2WDc3oJE7UuSQPDog7SY3/view?usp=drivesdk
- File ID: `1ILCM6pXTtiy2WDc3oJE7UuSQPDog7SY3`
- public sharing: `false`
- local/Drive size match: `true` (`27705628` bytes)

## 入力・構成

- 対象ページ: p.217〜p.228
- Scene数: 10
- Remotion dir: `units/unit25_success_three_layers/remotion_video_study_20260609_224259`
- Canonical MP4: `units/unit25_success_three_layers/video_study.mp4`

## GPT Image 2 スライドQA

- 生成/採用: 10枚
- dimensions: scene01=1086x1448, scene02=1086x1448, scene03=1086x1449, scene04=1086x1448, scene05=1086x1449, scene06=1086x1448, scene07=1086x1448, scene08=1086x1449, scene09=1086x1448, scene10=1086x1448
- 3:4 ratio check: `true`
- raw contact sheet: `units/unit25_success_three_layers/qa/raw_slide_contact_sheet.jpg`
- Vision確認: 重大な見切れ、黒枠、透かし/メール/ページ番号/Unit番号/Step表記、明らかな日本語崩れなし。全体の白ベース・青/シアン基調の統一感あり。

## Render QA

- `npm run lint`: pass
- `npm run still`: pass
- `npm run render`: pass
- ffprobe: `h264/aac`, `1080x1920`, `340.522667s`, `27705628` bytes, bitrate `650896`
- blackdetect: 黒画面0件（`blackdetect_has_black_start=false`）
- audio: mean `-16.9 dB` / max `-3.6 dB`

## Visual QA

- midpoint contact sheet: `units/unit25_success_three_layers/remotion_video_study_20260609_224259/qa/midpoint_contact_sheet.jpg`
- lower-card crop sheet: `units/unit25_success_three_layers/remotion_video_study_20260609_224259/qa/lower_card_crop_contact_sheet.jpg`
- progress-bar crop sheet: `units/unit25_success_three_layers/remotion_video_study_20260609_224259/qa/progress_bar_crop_contact_sheet.jpg`
- 確認結果:
  - 全10シーンで黒画面なし。
  - Step表示はタイトルカード右上で1行維持。
  - 下部カード内にStep重複なし。
  - 下端フッター、内部テンプレート名、制作ラベルなし。
  - 控えめな進捗バーは全10シーンで視認可能。
  - `おさえるべきポイント` と用語メモの下部カードで、文字の右端/下端はみ出しなし。
  - 進捗バーとの衝突なし。

## Drive QA

- metadata: `units/unit25_success_three_layers/qa/drive_metadata_verified.json`
- permissions: `units/unit25_success_three_layers/qa/drive_permissions_verified.json`
- mimeType: `video/mp4`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only
- public sharing: false
- local size: `27705628` bytes
- Drive size: `27705628` bytes

関連: [[Unit25]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]] / [[進捗バー]]
