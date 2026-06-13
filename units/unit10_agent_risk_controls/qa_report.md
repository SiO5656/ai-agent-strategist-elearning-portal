# [[Unit10]] QA Report - AIエージェントのリスクと対策：4カテゴリで整理する

## 判定
- status: completed
- 完了日時: 2026-06-07 11:25 JST
- ローカルMP4: `units/unit10_agent_risk_controls/video_study.mp4`
- Drive: https://drive.google.com/file/d/1yhEhBEFEaBYKLSA0wd09IthdDgBlStwk/view?usp=drivesdk

## 生成物
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene10.png`
- TTS音声: `audio/scene01.mp3`〜`scene10.mp3`
- [[Remotion]] render dir: `units/unit10_agent_risk_controls/remotion_video_study_20260607_111457`

## ffprobe
- video: h264, 1080x1920
- audio: aac, 48000Hz, stereo
- duration: 230.869333s
- size: 19671333 bytes

## blackdetect
- `qa/blackdetect.log`
- `black_start` 検出なし。0.5秒以上の黒画面なし。

## volumedetect
- `qa/volumedetect.log`
- mean_volume: -17.0 dB
- max_volume: -3.6 dB

## Visual QA
- raw slide contact sheet: `qa/unit10_raw_gptimage2_contact_sheet.png`
- final MP4 midpoint contact sheet: `qa/unit10_final_mp4_midpoints_contact_sheet.png`
- raw slide QA: 重大な崩れ、見切れ、透かし、メールアドレス、個人情報、ページ番号、Unit番号バッジ、制作都合語なし。
- final MP4 QA: 重大な見切れ、横端切れ、黒画面、下部カード崩れなし。
- 下部カード見出し: 全sceneで `おさえるべきポイント` に統一確認。

## Drive metadata
- file ID: `1yhEhBEFEaBYKLSA0wd09IthdDgBlStwk`
- mimeType: `video/mp4`
- size: `19671333`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only。公開共有なし。

関連: [[AIエージェント・ストラテジスト]] / [[Unit10]] / [[QA]] / [[Google Drive]]
