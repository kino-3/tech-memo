# Jupyter notebook で anaconda の仮想環境を使用する方法

```sh
conda create --name=hoge python=3.6 jupyter # jupyter 込みの仮想環境を作成
conda activate hoge
ipython kernel install --user --name=hoge # $ jupyter kernelspec list で追加を確認できる
jupyter notebook
# ブラウザで
# 1. notebook の選択
# 2. Kernel タブ > Change Kernel > hoge

# 補足: kernelspec からの uninstall
jupyter kernelspec uninstall hoge
```
