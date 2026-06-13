# [[Unit29]] QA Report - 変数と条件分岐

## 結論
- 判定: 合格 / [[Google Drive]]検証済み
- Drive: https://drive.google.com/file/d/1U3GXypzMTWpxPnNoNVZUuG5EYMZk1yc4/view?usp=drivesdk
- file ID: `1U3GXypzMTWpxPnNoNVZUuG5EYMZk1yc4`

## 成果物
- MP4: `units/unit29_workflow_variables_conditions/video_study.mp4`
- Remotion: `units/unit29_workflow_variables_conditions/remotion_video_study_20260611_231821/`
- still: `units/unit29_workflow_variables_conditions/remotion_video_study_20260611_231821/qa/still.png`
- midpoint contact sheet: `units/unit29_workflow_variables_conditions/remotion_video_study_20260611_231821/qa/midpoint_contact_sheet.jpg`
- progress-bar contact sheet: `units/unit29_workflow_variables_conditions/remotion_video_study_20260611_231821/qa/progress_bar_contact_sheet.jpg`

## MP4検証
- codec: h264 / aac
- 解像度: 1080x1920
- 尺: 183.829333s
- ローカルサイズ: 14782791 bytes
- blackdetect: `black_start` 0件
- volumedetect: mean -17.2 dB / max -3.7 dB

## 画像・音声・Remotion整合
- `storyboard.json`: 10 scenes
- `assets_gptimage2/sceneNN.png`: 10件、3:4 portrait比率確認済み
- `audio/sceneNN.mp3`: 10件、音声尺から `src/scenes.json` を再生成済み
- `public/scene_NN.png` / `public/scene_NN.mp3`: 10件ずつ同期済み
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功

## Vision QA
- still: 見切れ・黒帯・空白なし。`Step 01/10` 表示、下部カード可読、フッター/透かし/制作都合語なし。
- midpoint contact sheet: 10シーンすべて[[Unit29]]内容（変数・条件分岐・If/Else・フィルタ・ルーティング）。前Unit残存、黒/空白フレーム、フッター/透かし/制作都合語なし。
- progress-bar contact sheet: 10シーンすべて下部進捗バー表示あり。下端すぎず視認可能。

## Drive検証
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- mimeType: `video/mp4`
- Drive size: 14782791 bytes
- local size: 14782791 bytes
- size一致: True
- owner: `shiomaruclaw@gmail.com`
- public/domain共有: 0

関連: [[Unit29]] / [[AIエージェント・ストラテジスト]] / [[Remotion]] / [[Google Drive]]
