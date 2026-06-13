# [[Unit33]] QAレポート

## 成果物
- ローカルMP4: `units/unit33_organization_models/video_study.mp4`
- Drive: https://drive.google.com/file/d/19cmgtMphBCY-d1PsOpUhEQl_2EL4DaCw/view?usp=drivesdk
- ファイル名: `2026-06-12_unit33_organization_models_video_study.mp4`

## レンダー検証
- [[Remotion]] render: 成功
- 解像度: `1080x1920`
- FPS: `24`
- 動画codec: `h264`
- 音声codec: `aac`
- 長さ: `346.944` 秒
- サイズ: `27774054` bytes
- SHA256: `8c41353345b58b5f87f5998196dba8d3b55bf8547fe3fd68c70db83e95dfc594`

## QA
- TypeScript: `npm run lint` 成功
- still生成: `qa/still.png` 成功
- 画像QA: `qa/image_qa.md` / contact sheet `qa/raw_slide_contact_sheet_10.jpg`
- 動画QA: `qa/video_contact_sheet_10.jpg`
- blackdetect: `black_start` 0件
- volumedetect: mean `-17.1 dB`, max `-3.6 dB`
- 目視QA: 右端切れ、下部カード欠け、黒画面、透かし、ページ番号、メール混入は見当たらず

## Drive検証
- fileId: `19cmgtMphBCY-d1PsOpUhEQl_2EL4DaCw`
- mimeType: `video/mp4`
- owner: `shiomaruclaw@gmail.com`
- public permissions: 0
- Drive size: `27774054`
- local size: `27774054`
- size match: true

関連: [[Unit33]] / [[動画QA]] / [[Google Drive]] / [[Remotion]]
