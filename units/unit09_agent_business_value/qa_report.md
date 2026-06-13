# [[Unit09]] QA Report - AIエージェント導入価値：ROI・TCO・定性価値

## 結果

- Status: completed
- Local MP4: `units/unit09_agent_business_value/video_study.mp4`
- Render dir: `units/unit09_agent_business_value/remotion_video_study_20260607_103200/`
- Drive file ID: `1uayj0f0g6EqqkDa3SbAZ5WWaU8MvukWl`
- Drive link: https://drive.google.com/file/d/1uayj0f0g6EqqkDa3SbAZ5WWaU8MvukWl/view?usp=drivesdk

## ffprobe

- Video: `h264`, `1080x1920`, `24/1`, pix_fmt `yuvj420p`
- Audio: `aac`, `48000 Hz`, `stereo`
- Duration: `179.989333s`
- Size: `15051650` bytes
- Bitrate: `669001`

## QA証跡

- raw slide contact sheet: `units/unit09_agent_business_value/qa/raw_slide_contact_sheet.png`
- MP4 midpoint contact sheet: `units/unit09_agent_business_value/qa/mp4_midpoints_contact_sheet.png`
- ffprobe JSON: `units/unit09_agent_business_value/qa/ffprobe_video_study.json`
- blackdetect log: `units/unit09_agent_business_value/qa/logs/blackdetect.log`
- volumedetect log: `units/unit09_agent_business_value/qa/logs/volumedetect.log`

## 判定

- [[GPT Image 2]]スライド8枚: 採用。禁止要素（Unit番号バッジ、ページ番号、スライド番号、透かし、メールアドレス、購入者情報、制作都合語）なし。
- Remotion lint/still/render: 成功。
- Vision QA: raw slide / final MP4 contact sheetともに通過。左右端揃い、上下余白、見切れなし。
- blackdetect: `black_start` なし。0.5秒以上の黒画面なし。
- volumedetect: mean `-17.5 dB`, max `-3.6 dB`。
- Drive metadata: `mimeType=video/mp4`, `size=15051650`。
- Drive permissions: owner only `shiomaruclaw@gmail.com`、public共有なし。

関連: [[AIエージェント・ストラテジスト]] / [[Unit09]] / [[QA]] / [[Google Drive]] / [[Remotion]]
