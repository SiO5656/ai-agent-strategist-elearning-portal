# [[Unit11]] QA Report - 生成AIの発展トレンドを導入判断に結びつける

## 判定
- status: completed
- 完了日時: 2026-06-07 12:25 JST
- ローカルMP4: `units/unit11_genai_trends/video_study.mp4`
- Drive: https://drive.google.com/file/d/1TUCoH1g4U5cs9hgS4hLEm5elmQ-3pmJX/view?usp=drivesdk

## 生成物
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene09.png`
- TTS音声: `audio/scene01.mp3`〜`scene09.mp3`
- [[Remotion]] render dir: `units/unit11_genai_trends/remotion_video_study_20260607_120542`

## ffprobe
- video: h264, 1080x1920
- audio: aac, 48000Hz, stereo
- duration: 212.160000s
- size: 17872229 bytes

## blackdetect
- `qa/blackdetect.log`
- `black_start` 検出なし。0.5秒以上の黒画面なし。

## volumedetect
- `qa/volumedetect.log`
- mean_volume: -17.0 dB
- max_volume: -3.6 dB

## Visual QA
- raw slide contact sheet: `qa/unit11_raw_gptimage2_contact_sheet.png`
- final MP4 midpoint contact sheet: `qa/unit11_video_midpoints_contact_sheet.png`
- raw slide QA: 重大な崩れ、見切れ、透かし、メールアドレス、個人情報、ページ番号、Unit番号バッジ、制作都合語なし。
- final MP4 QA: タイトルカード側のみStep表示あり。下部カード内に `Step n / m` 表示なし。
- final MP4 QA: 下部カード見出しは全sceneで `おさえるべきポイント` に統一。下部カードは画像外側で、見切れ・横端切れなし。

## Drive metadata
- file ID: `1TUCoH1g4U5cs9hgS4hLEm5elmQ-3pmJX`
- mimeType: `video/mp4`
- size: `17872229`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only。公開共有なし。
- local size matches Drive metadata: true

関連: [[AIエージェント・ストラテジスト]] / [[Unit11]] / [[QA]] / [[Google Drive]]
