# python コードの時間計測(line_profiler)

<https://github.com/pyutils/line_profiler>
<https://pypi.org/project/line-profiler/>
<https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/01.07-Timing-and-Profiling.ipynb>

## インストール

```sh
pip install line_profiler
```

## サンプル

```python
import numpy as np

class Model():
  def __init__(self, count):
    a = np.arange(count) ** 2
    b = np.square(np.arange(count))

def func(count):
  a = [i**2 for i in range(count)]

def test():
  Model(int(1e6))
  func(int(1e6))


from line_profiler import LineProfiler

prof = LineProfiler()
prof.add_module(Model)
prof.add_function(func)
prof.runcall(test)
prof.print_stats()
```

以下のような結果が得られる。

```
Timer unit: 1e-06 s

Total time: 0.023689 s
File: <ipython-input-4-bac14ebd47f4>
Function: __init__ at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                             def __init__(self, count):
     5         1      17677.0  17677.0     74.6      a = np.arange(count) ** 2
     6         1       6012.0   6012.0     25.4      b = np.square(np.arange(count))

Total time: 0.404306 s
File: <ipython-input-4-bac14ebd47f4>
Function: func at line 8

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           def func(count):
     9         1     404306.0 404306.0    100.0    a = [i**2 for i in range(count)]
```
