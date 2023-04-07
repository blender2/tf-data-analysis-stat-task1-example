import pandas as pd
import numpy as np


chat_id = 469912664 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 74
    n = len(x)
    z = np.random.laplace(0, 1, n)
    x = x - z
    D = 2.0/t/t
    return D*x.mean() # Ваш ответ
