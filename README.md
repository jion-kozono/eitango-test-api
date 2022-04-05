# 簡易英単語アプリ

## url

<https://share.streamlit.io/jion-kozono/eitango-test/main>

## poetry による Python 環境のセットアップ

- ローカルに poetry をインストール(Poetry version 1.1.13)

  - `pip3 install poetry`
  - or

  ```sh
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  ```

- バージョン確認

  ```sh
  $ poetry -V
  Poetry version 1.1.13
  ```

## 仮想環境のセットアップ

- poetry でライブラリをインストール (pyproject.toml が既にある場合)
  - `sh scripts/init.sh`
  - ルートディレクトリに仮想環境`.venv`フォルダが作られる。

## 環境変数設定

- direnv推奨
- `.env`ファイルを作成し、`.env.default`の内容をコピー
- [ここ](https://drive.google.com/drive/folders/1IEy9B5pMT7GYvy83sqY5-pXqTZLsZGBa)から`client_secret.json`ファイルの中の情報を取得し、`.env`に追記
- `direnv allow .`

## API の立ち上げ

- `sh scripts/run_api.sh`

## 追加パッケージのインストール

- `poetry add <package-name>}`

## API を heroku へデプロイ

- github actionsでpush時にデプロイされる
