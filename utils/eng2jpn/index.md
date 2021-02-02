# 英語(論文)の日本語翻訳

## Google 翻訳を用いる方法

コピーした文章の行末に改行文字が入ると正しく Google 翻訳出来ないため, 以下の前処理が必要である。

```sh
# コピーした文章を hoge.txt にコピーする。
# 以下のコマンドで, 成形された文章が fuga.txt として出力される。
cat hoge.txt | tr '\r\n' ' ' | sed 's/([^)]*)/()/g' | sed 's/\. /\.\r\n/g' > fuga.txt
```

## pdf の英語論文翻訳翻訳ツール

以下の記事を参考にした。

- https://qiita.com/kimisyo/items/916f58ac6571815851ff
- https://qiita.com/tanabee/items/c79c5c28ba0537112922

1. ツールのダウンロード

    - [pdf2text.py](./pdf2text.py)
    - [cfg.py](./cfg.py)

1. requirements

    ```sh
    pip install pdfminer.six tqdm
    ```

1. Google Apps Script の作成

[Google Apps Script](https://script.google.com/home) にアクセスして, 「APPS SCRIPT を作成」し, 下のコードを保存する。
その後, デプロイ > 新しいデプロイ > (種類の選択)ウェブアプリ > 完了 > URL をコピー の手順を行う。

    ```gs
    function doGet(e) {
        var p = e.parameter;
        var translatedText = LanguageApp.translate(p.text, p.source, p.target);
        return ContentService.createTextOutput(translatedText);
    }
    ```

1. URL の登録

`cfg.py` の `api` のリストに URL を文字列として追加する。

1. 実行

```sh
python pdf2text.py hoge.pdf
```
