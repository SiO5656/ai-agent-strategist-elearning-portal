# [[Unit15]] QA Report - 業務可視化の4手法：IPOから業務フロー図まで

## 結論
- status: `completed_drive_verified`
- Drive: https://drive.google.com/file/d/1_H2oybLQ3WpD4oPNaDF-hmE4_Wn9MJd1/view?usp=drivesdk
- Drive file ID: `1_H2oybLQ3WpD4oPNaDF-hmE4_Wn9MJd1`
- local MP4: `video_study.mp4`

## Source / Assets
- Source pages: p.121-p.132
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene10.png`
- 画像寸法: scene01〜scene10 = `1024x1536`
- TTS音声: `audio/scene01.mp3`〜`scene10.mp3`
- TTS実測合計: `260.800s`
- Remotion: `remotion_video_study_20260607_192937/`

## Visual QA
- 画像contact sheet: `qa/unit15_image_contact_sheet.png`
- 画像QA: `qa/image_qa.md`
- still: `remotion_video_study_20260607_192937/qa/still.png`
- final midpoint contact sheet: `qa/unit15_final_midframe_contact_sheet.png`
- 10sceneすべて採用可。
- `Unit15` などviewer-facing Unit表記、ページ番号、スライド番号、透かしなし。
- scene10の1〜5丸数字はロードマップ内容番号であり、Unit/ページ/スライド番号ではないため許容。
- Remotion外側画像フレームあり、画像内黒枠なし。
- 下部カード内Step非表示、下端フッター/進捗バーなし。
- 下部カード文字見切れなし。

## Render QA
- `npm install`: success / vulnerabilities 0
- `npm run lint`: success
- `npm run still`: success / `1080x1920`
- `npm run render`: success
- ffprobe: `h264` + `aac`, `1080x1920`, duration `268.544000s`, size `21970226` bytes, bit_rate `654499`
- blackdetect: `black_start` 0行（0.5秒以上の黒画面なし）
- volumedetect: mean `-16.8 dB`, max `-3.6 dB`

## Drive metadata
- name: `2026-06-07_unit15_business_visualization_video_study.mp4`
- file ID: `1_H2oybLQ3WpD4oPNaDF-hmE4_Wn9MJd1`
- mimeType: `video/mp4`
- size: `21970226` bytes
- local size match: `true`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only `shiomaruclaw@gmail.com`
- public sharing: `false`
- parent: `Exports/videos/2026` (`1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`)
- verified_at: `2026-06-07T20:01:14+09:00`

関連: [[AIエージェント・ストラテジスト]] / [[Unit15]] / [[QA]] / [[Google Drive]] / [[Remotion]]
