# Python から C++ を使う(pybind11)

## Google Colaboratory での動作確認

参考にしたサイト: <https://buildersbox.corp-sansan.com/entry/2019/12/09/110000>

1. `$ pip install pybind11`

1. `sample.cpp` を用意する。

    ```cpp
    #include <pybind11/pybind11.h>
    #include <string>

    std::string concat(std::string a, std::string b){
        return a + b;
    }

    PYBIND11_MODULE(sample, m)
    {
        m.doc() = "sample module";
        m.def("concat", &concat, "concatenate two strings");
    }
    ```

1. コンパイルして共有ライブラリを作成する。

    ```sh
    g++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` sample.cpp -o sample`python3-config --extension-suffix`
    ```

1. Python から作成したライブラリを利用する。

    ```py
    import sample
    sample.concat("hoge", "fuga")
    ```
