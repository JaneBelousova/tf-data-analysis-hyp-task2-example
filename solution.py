import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alfa = 0.02
    p = anderson_ksamp([x, y]).pvalue
    return p < alfa # Ваш ответ, True (отклонить Но, не однородны) или False (не отклонять Но, однородны)
