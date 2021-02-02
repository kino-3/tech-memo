# PC のアクティブ状態を維持するスクリプト

- 一定時間ごとに画面を上下にスクロールすることで, PC のアクティブ状態を維持するコード。
- Google Colaboratory のセッションが 90 分で切れることの回避などを想定している。
- requirement: `pip install pyautogui`

```python
import time
import random
import pyautogui

while True:
    base_sec = 20
    scroll_size = 10
    rand = random.random()
    time.sleep(base_sec + base_sec*rand)
    pyautogui.scroll(scroll_size)
    time.sleep(1)
    pyautogui.scroll(-scroll_size)
    # クリックも必要な場合
    # x, y = pyautogui.position()
    # print(x, y, rand)
    # pyautogui.click(x,y)
```
