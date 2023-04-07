import pandas as pd
import numpy as np


chat_id = 469912664 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 74
    x = x*2.0/t/t
    div = np.std(x)
    print(div)
    return x.mean() # Ваш ответ
