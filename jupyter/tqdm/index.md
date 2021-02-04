# Jupyter notebook で プログレスバーを使う

`from tqdm import tqdm` とすると体裁が崩れるため。

```python
from tqdm.notebook import tqdm

for i in tqdm(range(100000000)):
    pass
```
