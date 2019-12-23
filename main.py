import random
from array import *
from range_key_dict import RangeKeyDict
from statsgen import stats
from racegen import race
from sexgen import sex
from classgen import Pclass
from bggen import bg
from statsgen import stats


input("Нажмите Enter, чтобы сгенерировать персонажа")
print("Вы ".join(race), sex)
print("Класс:\n"+Pclass+"\n")
print("Характеристики:")
print("".join(stats))
print("".join(bg))
input("Нажмите Enter, чтобы завершить работу")
