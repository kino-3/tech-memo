# GitHub で数式を使用する方法

GitHub の README や issue で TeX の数式を使用する方法。

## 結論

- [CODECOGS](https://www.codecogs.com/latex/eqneditor.php) によって得られる画像を Markdown に埋め込む。
- 使用例

```md
![\sum_{n=1}^{N}a_n](https://latex.codecogs.com/gif.latex?\sum_{n=1}^{N}a_n)
```

と記述すると, 以下のような画像が埋め込まれる。

![\sum_{n=1}^{N}a_n](https://latex.codecogs.com/gif.latex?\sum_{n=1}^{N}a_n)

## 補足

- CODECOGS が使用できなくなった場合は他の方法に置換する必要がある。
- GitHub では, コードブロック内の数式はレンダリングされない。

```math
\sum_{n=1}^{N}a_n
```

- VSCode の拡張機能である [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/ja-jp/math) では, 上記の方法でレンダリングされる。

## 追記

`MathJax` 等のライブラリを使用することで, 以下のように `GitHub Pages` で数式を使用することができる。詳細は <https://github.com/kino-3/github-pages-template> を参照。

$$
{e}^{i\pi}=-1
$$
