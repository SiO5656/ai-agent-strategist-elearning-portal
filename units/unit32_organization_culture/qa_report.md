# [[Unit32]] QA Report

## 対象
- Unit: [[Unit32]] AIエージェント導入と組織文化の変革
- ローカルMP4: `units/unit32_organization_culture/video_study.mp4`
- [[Remotion]] project: `units/unit32_organization_culture/remotion_video_study_20260612_063342/`
- Drive: https://drive.google.com/file/d/1v6TiJxSxRamnSsex4y0o22VEqH9Vesht/view?usp=drivesdk

## 成果物検証
- [[GPT Image 2]]スライド: `scene01.png`〜`scene10.png`
- 画像寸法: 全10枚 `1086x1448` / 3:4 exact
- TTS音声: `scene01.mp3`〜`scene10.mp3`
- MP4: `1080x1920`, `353.194667s`, `27501880` bytes, `h264/aac`, fps `24/1`
- 音量: mean `-17.0 dB`, max `-3.6 dB`
- 黒画面検出: `0` events

## 目視QA
- 生スライド contact sheet: `units/unit32_organization_culture/qa/raw_slide_contact_sheet_10.jpg`
- 動画中間フレーム: `units/unit32_organization_culture/remotion_video_study_20260612_063342/qa/midpoint_contact_sheet.jpg`
- 進捗バーcrop: `units/unit32_organization_culture/remotion_video_study_20260612_063342/qa/progress_bar_crop_contact_sheet.jpg`
- 下部カードcrop: `units/unit32_organization_culture/remotion_video_study_20260612_063342/qa/lower_card_crop_contact_sheet.jpg`
- still: `units/unit32_organization_culture/remotion_video_study_20260612_063342/qa/still.png`

### 判定
- 白ベース・青/シアンアクセントで統一。
- スライド画像の大きな見切れ、黒枠、透かし、メール、ページ番号、購入者情報なし。
- `Step NN/10` は一行表示。下部カード内にStep重複なし。
- 下部カード見出し `おさえるべきポイント`、箇条書き、用語メモの見切れ・重なりなし。
- 進捗バーは全10シーンで表示され、左から右へ進行。

## Drive検証
- file ID: `1v6TiJxSxRamnSsex4y0o22VEqH9Vesht`
- name: `2026-06-12_unit32_organization_culture_video_study.mp4`
- mimeType: `video/mp4`
- local size: `27501880`
- Drive size: `27501880`
- size match: `True`
- public/domain permissions: `0`
- owner: `shiomaruclaw@gmail.com`
- verified: `True`

関連: [[Unit32]] / [[動画QA]] / [[Google Drive]] / [[Remotion]]
