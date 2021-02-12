# Python コードの実行ファイル化 (PyInstaller)

PyInstaller の詳細: <https://pyinstaller.readthedocs.io/en/stable/>

> PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. PyInstaller supports Python 3.5 or newer, and correctly bundles the major Python packages such as numpy, PyQt, Django, wxPython, and others.
> PyInstaller is tested against Windows, Mac OS X, and GNU/Linux. However, it is not a cross-compiler: to make a Windows app you run PyInstaller in Windows; to make a GNU/Linux app you run it in GNU/Linux, etc. PyInstaller has been used successfully with AIX, Solaris, FreeBSD and OpenBSD but testing against them is not part of our continuous integration tests.

## Anaconda を利用した手順(例)

```sh
# Anaconda の仮想環境の作成
conda create -n hoge python=3.6
conda activate hoge

# PyInstaller と対象のコードの実行に必要となる Python パッケージを pip でインストールする。
pip install pyinstaller

# PyInstaller の実行
# --onefile: 1 ファイルにバンドルされた実行ファイルが作成される。
pyinstaller fuga.py --onefile
```
