# [[Unit07]] RPAとAIエージェントの違い：使い分けと組み合わせ - QAレポート

## 状態

- status: `completed_local_rendered`
- 最終MP4: `video_study.mp4`
- render dir: `remotion_video_study_20260607_081317/`

## 生成素材

- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene08.png`
- TTS音声: `audio/scene01.mp3`〜`scene08.mp3`
- スライドcontact sheet: `qa/unit07_gptimage2_scene_contact_sheet.png`

## Remotion / MP4メタ情報

- composition: `StudyVideo`
- size: `1080x1920`
- fps: `24/1`
- duration: `282.197333s`
- file size: `21204370` bytes
- video codec: `h264`
- audio codec: `aac`

## QA結果

- `npm run lint`: 合格。
- `npm run still`: 合格。ヘッダー右の折返しを修正済み。
- midpoint contact sheet Vision QA: 合格。
- `blackdetect`: `black_start`なし。0.5秒以上の黒画面なし。
- `volumedetect`: mean `-17.4 dB` / max `-3.7 dB`。
- 8シーン順番通り。中央スライド、下部カード、用語メモ、Step表示、進捗バーに大きな見切れ・重なりなし。
- 制作都合語、余計なページ番号、フッター、透かし、個人情報混入なし。

## 証跡

- MP4: `units/unit07_rpa_vs_agent/video_study.mp4`
- ffprobe: `units/unit07_rpa_vs_agent/remotion_video_study_20260607_081317/qa/unit07_ffprobe_summary.json`
- midpoint contact sheet: `units/unit07_rpa_vs_agent/remotion_video_study_20260607_081317/qa/unit07_mp4_midpoints_contact_sheet.png`
- blackdetect: `units/unit07_rpa_vs_agent/remotion_video_study_20260607_081317/qa/unit07_blackdetect.log`
- volumedetect: `units/unit07_rpa_vs_agent/remotion_video_study_20260607_081317/qa/unit07_volumedetect.log`

## Drive

- mp4_file_id: `1AAbhhsjpNxuzQzDiQcw8fO1IENVueq6u`
- mp4_view_link: https://drive.google.com/file/d/1AAbhhsjpNxuzQzDiQcw8fO1IENVueq6u/view?usp=drivesdk
- mimeType: `video/mp4`
- size: `21204370` bytes
- permissions: owner only `shiomaruclaw@gmail.com`

関連: [[AIエージェント・ストラテジスト]] / [[Unit07]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]]
