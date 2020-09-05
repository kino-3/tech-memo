# markdownlint

markdown 用の lint ツール。
詳細は[作者のリポジトリ](https://github.com/DavidAnson/markdownlint)を参照のこと。

## インストール

```sh
npm install -g markdownlint-cli
```

## 設定

- 設定は `.markdownlint.json` などに記述する。設定ファイルが配置されたディレクトリと, そのサブディレクトリで有効である。
- ファイル中に `<!-- markdownlint-disable MD001 -->` などと記述すると, ファイル内のそれ以下で設定が反映される。

## その他

[VSCode の拡張機能](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)としても提供されている。

```sh
code --install-extension DavidAnson.vscode-markdownlint
```
