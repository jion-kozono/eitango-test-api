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

## spreadsheet設定

[ここ](https://drive.google.com/drive/folders/1IEy9B5pMT7GYvy83sqY5-pXqTZLsZGBa)から`client_secret.json`ファイルをダウンロードし、root直下に配置

## API の立ち上げ

- `sh scripts/run_api.sh`

## 追加パッケージのインストール

- `poetry add <package-name>}`

## API を heroku へデプロイ

```sh
heroku login
git add . # ディレクトリ直下のファイルをgitの管理対象に追加
git commit -m "コミットメッセージ" # ファイルの変更をgitに登録

heroku git:remote -a simple-eitango-test # Herokuとgitを関連づける
git push heroku master # HerokuにPython(FastAPI)アプリをデプロイ(配備)
```
