import pandas as pd
import numpy as np


chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alfa = 0.02
    return abs(x.mean() - y.mean()) <= alfa*y.mean() # Ваш ответ, True или False
