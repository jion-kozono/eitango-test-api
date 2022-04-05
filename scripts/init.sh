# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
poetry config virtualenvs.in-project true #プロジェクト内に仮想環境作成
if [ -f pyproject.toml ]; then poetry install; fi