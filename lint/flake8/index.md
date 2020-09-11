# flake8

次の 3 つのパッケージのラッパーである。<https://pypi.org/project/flake8/>

- [PyFlakes](https://pypi.org/project/pyflakes/): Python コードのエラーをチェックするツール
- [pycodestyle](https://pypi.org/project/pycodestyle/): PEP8 に準拠しているか確認するツール
- [Ned Batchelder’s McCabe script](https://pypi.org/project/mccabe/): [循環的複雑度](https://en.wikipedia.org/wiki/Cyclomatic_complexity) を確認するツール

## インストール

デフォルトの Python にインストールする場合。

```sh
python -m pip install flake8
```

適切なバージョンの Python にインストールする必要がある。詳細は前述のドキュメントを参照のこと。

## VSCode の設定

設定の `python.linting.flake8Enabled` を有効にする必要がある。
`python.linting` の他の設定も確認すること。
