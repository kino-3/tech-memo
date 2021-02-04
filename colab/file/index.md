# Google Colaboratory のファイルのアップロード・ダウンロード

## PC 経由

```python
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]  # ファイル名を文字列として得る
files.download(file_name)
```

## Google Drive 経由

Google Drive の直下の `hoge` ディレクトリに移動する場合。

```python
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/"My Drive"/hoge
```
