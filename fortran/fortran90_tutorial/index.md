# 文法(数値計算用)

Fortran90 の概要メモ
「数値計算のための Fortran90/95 プログラミング 第1版」 3.8節まで

## gfortran によるコンパイル(省略版)

```bash
gfortran hoge.f90 fuga.f90 # 依存関係に注意すること
./a.exe # 実行ファイルへのパスを書く
```

## コメント

```Fortran
call hoge() ! 複数行のコメントは存在しない
```



## 変数名

- 先頭は 英字
- 以降は 英数字と_

## 主プログラム (program ~ end)

```Fortran
program hoge        ! プログラム名は省略してもよい(書いたほうが良い)
    implicit none   ! 暗黙の変数の型に関する規約を無効にするため, 変数宣言する前に使用する。
    integer i       ! 宣言文を実行文よりも上に書く
    i = 0           ! 代入前の変数は不定値        
    write(*,*) i
end program hoge
```

## ループ処理

### do - enddo
```Fortran
integer counter         ! 変数宣言必要
do counter = 1, 100     ! 制御変数(do変数)はかならず整数型変数を用いる。制御変数を省略して `do` のみ書いた場合は無限ループとなる。
    ! counter は 1, 2, ..., 100
    ! 内部で制御変数を書き換えてはならない。
    ! do counter = 1,100,2 -> 1,3,5,...,99
    ! do counter = 100,1,-2 -> 100,98,96,...,2
enddo
```

### 離脱処理
- `exit` : いわゆるbreak文
- `cycle` : いわゆるcontinue文
- `goto 123` : 文番号(行頭の数字)が123の行に移動する。多重ループなどやむを得ないときに使用。
- `continue` : 何もしない文 (`123 continue` のように使う)

## 条件式

```Fortran
if (論理式) then
    !
else if (論理式) then
    !
else
    !
endif
```

## 変数型
- `real(8) dx, dy`: 8バイトの倍精度実数。数値計算ではこちらを用いる。(`real` は4バイトの基本実数)
- `1.5d-1` : 倍精度実数0.15 (0なら`0.0d0`とする) (基本実数なら`d`ではなく`e`)
- `1/2` の計算結果は 0 になる。(整数で不用意に除算をしない)
- 基本的に演算時の型は統一する。
- 複素数型
    - 宣言: `complex(8) e`
    - 2つの実数を実引数とするcmplx関数の戻り値が複素数
    - 出力: `(1.,1.5)` のようになる

## 変数宣言
- `integer :: i, j = 0` : j に初期値0を代入している。
- `::` を型の後に書くべき場合
    - 初期値を使うとき
    - 属性を付するとき

## 入出力
### 基本
- `write()` は2つ引数を取り, 続いて出力対象となる変数などを列挙する。
    - 第1引数: 装置識別子(ファイル番号)
        - `*`: 標準出力
    - 第2引数: 書式識別子(フォーマット)
        - `*`: 並び出力
        - `a\`: 改行されない。
    - 実際の値は 空白 または タブ 区切り
    - ベクトル, 行列(メモリ順一次元並びになる) も可
    - 出力対象変数の個数 < 実際の値の個数 のとき、余分な値は破棄されて次の行に進む
    - 出力対象変数の個数 > 実際の値の個数 のとき、読み込みは次の行に進んで代入が続く。
- `read()` も `write()` 同様。

### ファイル操作
```Fortran
integer :: ina, inb, iv, is, iost, fi = 10, fo = 11
                                        ! 0以上の整数。数字は5,6 は標準入出力なので良くない。
open(fi, file = "inputFilename", action = "read", iostat = is)
                                        ! action はオプション(無指定の場合は"readwrite")
                                        ! iostat はオプション(openに成功するとisには0が代入される。失敗すると非0が代入される。)
open(fo, file = "outputFilename", position = "append")
                                        ! ファイルがあれば上書き。なければ新規作成。
                                        ! append は追記するためのオプション
read(fi, *) ina, inb                    ! 並び出力でファイルを読み込む(入力ファイルに合わせる)
do                                      ! 入力が何行あるかわからん時
    read(fi, *, iostat = iost) iv       
    if (iost < 0) exit                  ! 代入により終端に達するとiostは負になる。
endif      
close(fi)
write(fo,*) "hoge"                      ! 何回writeを呼び出してもよい。(追記される)
close(fo)
```
### 書式
- `5i6` 文字数6文字の整数5個以下。変数が5個より多いときは複数行になる。
- `10e12.4` 小数点以下4桁の12文字小数が10個

## ベクトルと行列
### 基本(配列の上下限が自明である)
- 要素アクセス: v(2),m(3,1) 添え字は整数または整数型変数。上下限を超えたアクセスは不可。
- 行列の「行」は第1成分で、第1成分を優先的に変化させる。(メモリ的にm(1,1)の次はm(2,1))
- 宣言： 
    - `real(8) v(3)` は要素数倍精度実数配列(`real(8) v(1:3)`に同じ)
    - `integer(8) v(-1:1)` の添え字は　-1, 0, 1
- 代入: 
    - 要素に代入: `vi(2) = 7`
    - 定数配列の代入: `vi(1:2) = (/ 3, 5 /)`
    - 一括代入:  `vi(1:3) = 0`, `integer :: i(4) = 0`
    - `vi(:) = 4` のように上下限は省略可能
- 並び
    - `(u(i), i = 1, 3)` : u(1) u(2) u(3) の並び
    - `(/ (i, i = 1, 5, 2) /)` : do型反復。`(/ 1, 3, 5 /)` と同じ。
- m(3:3) は要素数1の(部分)配列, m(3) はスカラ
- 演算
    - abs, sqrt 等は配列を引数にとり, 各要素に演算する。
    - 配列 * 配列 は配列の形状が同じなら各要素ごとに演算
    - スカラ * 配列 はNumPyのブロードキャストのようになる。
    - `dot_product(1次元配列, 1次元配列)`: 内積計算の組み込み関数
    - 行列積: 組み込み関数 matmul
        - 引数として(ベクトル, 行列) or (行列, ベクトル) or (行列, 行列) をとる。
    - 行列の転置: transpose 
### その他
- 配列の宣言
    - 宣言時に配列の寸法を「数値」で定める。
    - 宣言時に配列の寸法を「定数」で定める。
        - 定数: `integer, parameter :: i = 3` のように parameter 属性を持つ変数。実行時に代入不可。
    - 割付け配列(ランタイムに寸法が定まる配列)
```Fortran
implicit none
real(8), allocatable :: u(:), v(:,:)
                ! この時点で上下限は不明だが, 次元は固定。未割り付けの状態では使用出来ない。
integer i, is
read(*, *) i
allocate (u(i)) ! 複数なら allocate (u(i), v(i,i))
deallocate (u)  ! 複数なら allocate (u, v)
allovate (u(-i:i), stat = is) ! 異なる寸法で再割り付け可能。割付が成功するとisに0が代入される。
```
- 部分配列: `v(1:5:2)` は v(1) v(3) v(5) を要素とする配列(添字三つ組)
    - ストライドを省略した時は 1
    - 始値 > 終値 のときは実行されない
    - 部分配列を書き換えると元の配列も書き換わる。

## 副プログラム (programに対して)
- 大別: モジュール副プログラム, 外部副プログラム
### モジュール副プログラム
```Fortran
module hoge
    implicit none               ! 以下 end module 内で有効(プログラム単位ごとに行う)
contains                        ! containsより前に書いた宣言は全域で有効
                                ! 以下 subroutine と function を書く
    subroutine hoge_sub(a, b)   ! a, b は仮引数。引数無しの時は括弧も不要。
        integer a, b            ! 実引数と仮引数で型を一致させる必要がある
        integer tmp             ! 局所変数で(useしたとしても)このsubroutine内で有効
        return                  ! return が呼び出されるとその時点で subroutine を離脱する
    end subroutine hoge_sub     ! return が呼び出されないと end subroutine まで
    function hoge_func(a, b) result(c)  
        real, intent(in) :: a,b ! 普通仮引数には intent(in) を与える。
        integer c                  ! resultの要素は必ず単一で intent(out) 不要
    end function hoge_func
end module hoge

program fuga
    use hoge                    ! module の使用宣言。使用するモジュールは先に定義する。
    implicit none               ! use はこれより上に書く。以下 end program 内で有効
    integer v1, v2
    real e1, e2
    call hoge_sub(v1, v2)       ! subroutineの呼び出し(実引数を参照渡しする)
    v1 = hoge_func(e1, e2)      ! call 不要
end program fuga
```
#### subroutine の属性
- subroutine の局所変数の save 属性
    - `real, save :: i` とすると, subroutine 呼び出し後も変数が保存される。
    - `real :: i = 0` のように初期化した場合は自動的に save 属性となる。
        - 初期化は 1回目のsubroutine呼び出し時のみ有効で2回目以降は初期化されない。
        - 毎回初期化したいなら代入すべし。
    - 局所配列にも save 属性を与えることは可能
- subroutine の仮引数の intent 属性
```Fortran
subroutine hoge_sub2(a, b, c)
    real, intent(in) :: a, b    ! プログラム中で書き換え不可
    real, intent(out) :: c      ! プログラム中で代入必須(書き換えたいやつ)
```
#### モジュール副プログラムで配列を引数にする(function も同様)
- 形状明示仮配列
```Fortran
subroutine hoge_sub3(a, n)
    integer, intent(in) :: n    ! 配列の寸法も仮引数として与えて
    real, intent(in) :: a(n,n)  ! 仮配列定義時に寸法も与える
!
call hoge_sub(mat, mat_n)       ! 呼び出し時の実引数 mat は呼び出し時点で形状が自明
```

- 形状引継ぎ配列
```Fortran
subroutine hoge_sub3(a)
    real, intent(in) :: a(:,:)  ! 次元のみ指定する。各要素数は呼び出しの実引数にあわされる。
                                ! 形状明治仮配列の省略版なのでallocate属性は不要
!
call hoge_sub(mat)              ! 呼び出し時の実引数 mat は呼び出し時点で形状が自明
call hoge_sub(mat(2:4,2:4))     ! 部分配列として小行列を引数にすることもできる。
```

- **未割り付け**の割付配列を引数とする(実引数がallocatableだが**allocateされていない**)
```Fortran
subroutine hoge_sub4(a)
    real, allocatable, intent(out) :: a(:,:)    ! 仮引数にも allocatable 属性をつける(この時点で形状不明)
    integer :: n = 10
    allocate (a(n,n))
!
real, allocatable :: a(:,:)
call hoge_sub4(a)                               ! 呼び出し時の実引数 a は呼び出し時点で未割り付け
```

- 注意
    - 形状明示仮配列・形状引継ぎ配列では形状のみ引き継がれるため, 仮配列の下限値は1となる。
    そのため, `real, intent(in) :: a(d:d+n-1,e:e+n-1)`・`real, intent(in) :: a(d:,e:)` 等で指定する必要がある。
    - 形状明治仮配列(と非推奨であるが形状引継ぎ配列)では, 実配列を要素数の同じ違う形状の仮配列で受け取れる。(メモリ順は不変)
    - 実引数を配列の要素(スカラ―)として, 仮引数を形状明示仮配列とすることは可能(実引数の先頭要素のメモリから形状明示仮配列の要素数分だけメモリ順に読みだされる)
#### 局所配列としての自動割付配列
- 仮引数による
```Fortran
subroutine hoge_sub5(n)
    integer tmp(n)          ! 数値や定数の代わりに仮引数を寸法として与える。
```
- 他のモジュールによる
```Fortran
module params
    implicit none
    integer :: n = 2
end module params

module hoge
    implicit none
contains
    subroutine fuga
        use params
        integer tmp(n)
    ends subroutine fuga
end module hoge
```
#### 配列を返すモジュール関数
```Fortran
function hoge_func2(v) result(nv)
    real(8), intent(in) :: v(:)     ! 形状引継ぎ配列
    real(8) nv(size(v, 1))          ! 自動割付配列?
    nv = 2 * v
end function hoge_func2
```
### モジュールによる変数の共有
#### グローバル変数モジュール(プログラム単位間で共有したい変数)
```Fortran
module global_params                    ! use global_params とかで使用宣言する
    implicit none
    integer, params :: global_i = 1     ! 定数なので書き換え不可能
    integer, save :: global_j           ! 書き換えて記憶させるやつは save 属性
end module global_params
```
## その他文法

- 文字列はシングルクォートまたはダブルクォート
- 日本語文字は文字列とコメントのみ可
- 複数行にまたがるときは, 先行する行の行末に `&` をつける。
- (; で区切ると1行に複数の実行文が書ける)
- 文字列を除いて, 大文字小文字の区別はない
- べき乗は `**` で優先度は乗除より高い。指数は極力整数を用いる。
- 等しい, 等しくないは `==`, `/=`
- `stop "プログラムを停止してこの文字列を出力する"`
- 円周率は`2.0d0*acos(0.0d0)`または`acos(-1.0d0)`等を用いる。
- 乱数: まず `call random_seed` で乱数の初期値を設定して, そのあと `call random_number(hoge)` とする。hogeはスカラや配列で, 配列の場合は各要素が[0,1)の数となる。
