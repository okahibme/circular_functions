# 三角関数インタラクティブ教材：単位円と波

単位円の上を回る点と、sin・cos の波が連動して動く教材です。
Streamlit で `index.html`（HTML + JavaScript）を表示しています。
iPad などのタッチ操作にも対応しています。

## 画面の構成

| タブ | できること |
|---|---|
| **2D** | 単位円と波を並べて表示。円や波を指でなぞって角度を動かせる。4周（1440°）まで。 |
| **3D** | cos・sin を立体のカーブとして表示。ドラッグで回転。 |
| **クイズ** | 円を回して答えを探す。6問＋おまけ1問。ひらがな中心。 |

2D・3Dには、次の機能があります。

- **みかた**の切り替え：「かくど」（度数法）と「ながさ（こどほう）」（弧度法）。
  ながさでは、円周に長さ 1, 2, 3, … の目盛りを打ち、半周が π ≈ 3.14 であることを示します。
- スタート／ストップ、速度（1x・2x・4x）、17か所へのジャンプ（0〜360°）。
- 30°・45°の倍数に近いところで指をはなすと、その角度に吸い付きます。

## フォルダ構成

```
.
├── streamlit_app.py   # Streamlitのエントリーポイント
├── index.html         # 教材本体（HTML + JavaScript + Canvas）
├── requirements.txt   # Pythonの依存パッケージ（streamlitのみ）
└── README.md
```

`packages.txt`（apt-getで入れる外部ソフト用）は、このアプリでは不要なので置いていません。

## ローカルで動かす

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

`index.html` だけをブラウザで開いても動きます（下の「注意」を参照）。

## Streamlit Community Cloud にデプロイする

1. このフォルダの中身を、GitHub のリポジトリのルートに置いて push する。
2. <https://share.streamlit.io/> に GitHub アカウントでログインし、**Create app** を選ぶ。
3. リポジトリ・ブランチを選び、**Main file path** に `streamlit_app.py` を指定する。
4. **Advanced settings** で Python のバージョンを選ぶ（ローカルと同じ版にするのが安全）。
5. **Deploy** を押す。

デプロイ後は、GitHub に push するだけで自動的に更新されます。

## 注意

- **ネットワークが必要です。** `index.html` は、次の2つを CDN から読み込みます。
  - Tailwind CSS（`cdn.tailwindcss.com`、3.4.17 に固定）
  - KaTeX（`cdn.jsdelivr.net`、0.16.8 に固定）
- **iframeの高さ**は `streamlit_app.py` の `APP_HEIGHT` で調整します。画面が狭くてボタンが
  折り返し、下が切れるときは、大きくしてください。
- **iPad は横持ち**がおすすめです。縦持ちだと、円と波が窮屈になります。
- `st.components.v1.html` は Streamlit 1.56 で非推奨になりました。このアプリは `st.iframe`
  を優先して使い、古い版では自動で `components.html` に切り替えます。

## 調整できるところ（`index.html` の中）

| 設定 | 場所 | 意味 |
|---|---|---|
| `TOL` | クイズのコード | クイズで正解とみなす角度のはば（既定 ±5°） |
| `SNAP_TOL` | 2Dのコード | 指をはなしたときに、有名な角度へ吸い付くはば（既定 ±3°） |
| `QUESTIONS` | クイズのコード | 問題のデータ。ここに足せば、問題を増やせる |
