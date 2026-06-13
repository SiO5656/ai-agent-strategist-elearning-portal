# Unit12 QAレポート

## 対象
- Unit: [[Unit12]] 業務の構造的理解：As-IsからTo-Beへ
- Unit dir: `units/unit12_business_as_is_to_be/`
- Manifest範囲: p.93〜p.101
- 実参照ファイル: `../extracted_text/pages/page_094.txt`〜`page_102.txt`（紙面ページ番号との差分を確認済み）

## 完成成果物
- 教材: `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json`
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene09.png`
- 音声: `audio/scene01.mp3`〜`scene09.mp3`
- 正式動画: `video_study.mp4`
- [[Google Drive]]: https://drive.google.com/file/d/1Dt_zAG7cFQvnjZxqub2YK1-pvRqe_rqe/view?usp=drivesdk

## 画像生成チェック
- 生成経路: [[GPT Image 2]] via [[Codex CLI]] `$imagegen`
- 生成方法: `TooManyRequests` 回避のため、1枚ずつ直列生成。scene04〜scene09は10分間隔キューで完了。
- 寸法確認:
  - scene01 / scene02 / scene04 / scene07 / scene09: `1086x1448`
  - scene03 / scene05 / scene06 / scene08: `1024x1536`
- Contact sheet: `qa/unit12_gptimage2_contact_sheet_3x3_current.png`
- Vision QA: 9枚とも白ベース・青シアン系で統一。見切れ、透かし、個人情報、不要フッター、ページ番号なし。順序は導入→定義→分解→As-Is→収集→To-Be→部品→順序→まとめで自然。

## Remotion / MP4検証
- Remotion作業ディレクトリ: `remotion_video_study_20260606_090543/`
- 実行:
  - `npm install`: 成功、脆弱性0件
  - `npm run lint`: 成功
  - `npm run still`: 成功、`qa/still.png`
  - `npm run render`: 成功、テンプレートロック版 `out/video_study.mp4 23.2 MB`
- 正本MP4: `video_study.mp4`
- ffprobe:
  - video: `h264`, `1080x1920`, `24fps`
  - audio: `aac`, stereo
  - duration: `318.186667s`
  - size: `23248596` bytes
- ffprobe JSON: `video_study_ffprobe.json`

## 最終フレームQA
- 各Scene中間点contact sheet: `remotion_video_study_20260606_090543/qa/unit12_locked_template_mp4_midpoints_contact_sheet.png`
- 追加still QA: `remotion_video_study_20260606_090543/qa/unit12_locked_template_stills_contact_sheet.png`
- Vision QA:
  - Scene 1〜9の順序は正しい。
  - 全Sceneで[[GPT Image 2]]スライド本体の見切れなし。
  - [[Remotion]]側の中央スライド枠、ヘッダー枠、下部解説カード、用語メモカード、Step表示、プログレスバーの座標はシーン間で固定されている。
  - `slideShell` / `slideImg` のdrift・scale演出を削除し、外枠がシーンごとに動かないテンプレートロック版にした。
  - 黒画面なし。
  - 制作都合語、不要フッター、ページ番号、手書き装飾の混入なし。

## 2026-06-07 フレーム訂正QA
- きっかけ: しおの訂正「画像の外枠は必要。不要なのは画像そのものの黒い枠」。
- 正しい視覚契約: 中央画像は[[Remotion]]外側表示フレームあり、[[GPT Image 2]]画像そのものの内側黒枠/ページ枠なし。
- Remotion更新: `src/StudyVideo.tsx` / `src/style.css` / `src/scenes.json`。
- 再render: `npm run render` exit code 0、`video_study.mp4` を再生成。
- `npm run lint`: OK
- `npm run still`: OK
- `npm run render`: OK
- `ffprobe`: `h264`, `1080x1920`, `318.186667s`, `23190145` bytes, bitrate `583057`
- `blackdetect`: 0件
- `volumedetect`: mean `-17.0 dB`, max `-3.5 dB`
- final MP4 contact sheet: `remotion_video_study_20260606_090543/qa/unit12_frame_correction_midpoints_contact_sheet.png`
- Vision QA: 全Sceneで右上Stepは `Step NN/09` 一行、下部カード内Stepなし、下部見出しは `おさえるべきポイント`、[[Remotion]]外側表示フレームあり、画像内黒枠/ページ枠なし。

## Google Drive検証
- File ID: `1Dt_zAG7cFQvnjZxqub2YK1-pvRqe_rqe`
- Link: https://drive.google.com/file/d/1Dt_zAG7cFQvnjZxqub2YK1-pvRqe_rqe/view?usp=drivesdk
- name: `2026-06-06_unit12_business_as_is_to_be_video_study.mp4`
- mimeType: `video/mp4`
- size: `23190145`
- parent: `Exports/videos/2026`
- permissions: owner only `shiomaruclaw@gmail.com`
- public sharing: なし
- 更新内容: 同一File IDへ再アップロード（タイトルカードStepを`Step NN/09`一行固定、下部カード内Step削除、下部見出しを`おさえるべきポイント`へ統一、中央画像は外側表示フレームあり・画像内黒枠/ページ枠なし）
- 検証日時: 2026-06-07 15:30 JST

## QA判定
- [[Unit12]] は動画教材として完了。
- 正式MP4・Driveリンク・メタデータ・共有範囲を確認済み。
- 2026-06-07の追加指摘を受け、外側画像フレームあり・画像内黒枠なしの再レンダー版をDrive上の同一MP4リンクへ反映済み。

関連: [[AIエージェント・ストラテジスト]] / [[Unit12]] / [[GPT Image 2]] / [[Google Drive]] / [[Remotion]]
