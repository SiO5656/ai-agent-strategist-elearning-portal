# [[Unit08]] MCP：エージェント接続標準を概念で理解する - QA Report

## 状態

- status: `completed`
- generated_at: 2026-06-07 09:04 JST
- 画像生成: [[GPT Image 2]] 完成スライド
- video template: [[Remotion]] vertical study video

## 成果物

- MP4: `video_study.mp4`
- render dir: `remotion_video_study_20260607_085542/`
- raw slide contact sheet: `qa/20260607_085420_ffmpeg_contact/unit08_gptimage2_scene_contact_sheet.png`
- final MP4 contact sheet: `remotion_video_study_20260607_085542/qa/video_frames_20260607_090132/unit08_video_sample_contact_sheet.png`
- ffprobe: `remotion_video_study_20260607_085542/qa/unit08_ffprobe_summary.json`
- blackdetect: `remotion_video_study_20260607_085542/qa/unit08_blackdetect.log`
- volumedetect: `remotion_video_study_20260607_085542/qa/unit08_volumedetect.log`

## MP4メタ情報

- size: `1080x1920`
- codec: `h264` / `aac`
- fps: `24`
- duration: `154.944000s`
- file size: `13307578` bytes
- bitrate: `687090`

## QA結果

- [[GPT Image 2]]スライド8枚生成・採用済み。
- raw slide contact sheetで見出し・主要ラベル・シーン意味の大ズレなしを確認。
- [[Remotion]] `npm run lint` 合格。
- 最終MP4から8シーンサンプルフレームを抽出し、contact sheetで順序・見切れ・下部カード・Step表示を確認。
- 上部役割バッジの長文改行をCSS修正後、再レンダー・再抽出QA済み。
- 右端切れ・下端切れ・透かし・ページ番号・制作都合語・個人情報なし。
- `blackdetect`: `black_start`なし。0.5秒以上の黒画面なし。
- `volumedetect`: mean `-17.3 dB` / max `-3.7 dB`。

## Drive

- file_id: `1wtfcmUjYlIslUP_l-yv1WrRr2UCPiWHr`
- webViewLink: https://drive.google.com/file/d/1wtfcmUjYlIslUP_l-yv1WrRr2UCPiWHr/view?usp=drivesdk
- parent: `Exports/videos/2026`
- parent_id: `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- mimeType verified: true (`video/mp4`)
- size verified: `13307578` bytes
- permissions verified: true
- sharing: owner only `shiomaruclaw@gmail.com`

関連: [[AIエージェント・ストラテジスト]] / [[Unit08]] / [[GPT Image 2]] / [[Remotion]] / [[Google Drive]]
