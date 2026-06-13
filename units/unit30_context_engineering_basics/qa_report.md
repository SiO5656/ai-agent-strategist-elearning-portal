# [[Unit30]] QA Report - コンテキストエンジニアリング概論

## 結論
- 判定: 合格 / [[Google Drive]]検証済み
- Drive: https://drive.google.com/file/d/1UbioM-5RKNMpUTv694rcYzZQUh7D1QM3/view?usp=drivesdk
- file ID: `1UbioM-5RKNMpUTv694rcYzZQUh7D1QM3`

## 成果物
- MP4: `units/unit30_context_engineering_basics/video_study.mp4`
- Remotion: `units/unit30_context_engineering_basics/remotion_video_study_20260611_235900/`
- still: `units/unit30_context_engineering_basics/remotion_video_study_20260611_235900/qa/still.png`
- midpoint contact sheet: `units/unit30_context_engineering_basics/remotion_video_study_20260611_235900/qa/midpoint_contact_sheet.jpg`
- progress-bar contact sheet: `units/unit30_context_engineering_basics/remotion_video_study_20260611_235900/qa/progress_bar_crop_contact_sheet.jpg`
- lower-card contact sheet: `units/unit30_context_engineering_basics/remotion_video_study_20260611_235900/qa/lower_card_crop_contact_sheet.jpg`

## MP4検証
- codec: h264 / aac
- 解像度: 1080x1920
- 尺: 245.909333s
- ローカルサイズ: 19551186 bytes
- blackdetect: `black_start` 0件
- volumedetect: mean -17.0 dB / max -3.4 dB

## Remotion / QA
- `storyboard.json`: 10 scenes
- `assets_gptimage2/sceneNN.png`: 10件
- `audio/sceneNN.mp3`: 10件
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功

## Vision QA
- midpoint contact sheet: 10シーンすべて[[Unit30]]内容（コンテキストエンジニアリング、プロンプトとの違い、目的・制約・例・出力形式・評価基準、ノイズ、RAG等）。前Unit残存、黒/空白フレーム、フッター/透かし/制作都合語なし。
- progress-bar contact sheet: 10シーンすべて下部進捗バー表示あり。下端すぎず視認可能。
- lower-card contact sheet: 下部カード内にStep重複なし、文字見切れなし、フッター/制作メタ/内部ラベル混入なし。

## Drive検証
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- mimeType: `video/mp4`
- Drive size: 19551186 bytes
- local size: 19551186 bytes
- size一致: True
- owner: `shiomaruclaw@gmail.com`
- public/domain共有: 0

関連: [[Unit30]] / [[コンテキストエンジニアリング]] / [[Remotion]] / [[Google Drive]]
