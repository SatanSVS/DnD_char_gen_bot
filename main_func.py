import random
from array import *
from range_key_dict import RangeKeyDict
from statsgen import stats
from racegen import race
from sexgen import sex
from classgen import Pclass
from bggen import bg
from statsgen import stats


gen_char="Вы ".join(race)+sex+"\nКласс:\n"+Pclass+"\n"+"\nХарактеристики\n:"+"".join(stats)+"".join(bg)

