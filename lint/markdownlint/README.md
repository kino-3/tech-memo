# markdownlint

markdown 用の lint ツールです。
詳細は[こちら](https://github.com/DavidAnson/markdownlint)を参照してください。

## インストール

Node.js のパッケージとして提供されています。

```sh
npm install -g markdownlint-cli
```

## 設定

- 設定は `.markdownlint.json` などに記述します。デフォルトでは, 設定ファイルが配置されたディレクトリと, そのサブディレクトリで有効です。
- また, ファイル中に `<!-- markdownlint-disable MD001 -->` などと記述すると, それ以下で記述した設定が反映されます。

## その他

[VSCode の拡張機能](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)としても提供されています。

```sh
code --install-extension DavidAnson.vscode-markdownlint
```
