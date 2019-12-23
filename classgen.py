import random
from array import *
from range_key_dict import RangeKeyDict
classlist={
1:'Бард', 
2:'Варвар', 
3:'Воин', 
4:'Волшебник', 
5:'Друид', 
6:'Жрец', 
7:'Колдун', 
8:'Монах', 
9:'Паладин', 
10:'Плут', 
11:'Следопыт',
12:'Чародей'
}
z=random.randint(1, 12)
Pclass=classlist.get(z)
