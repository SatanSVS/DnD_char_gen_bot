import numpy as np
import random
from array import *
from proplists import raceprop
racelist=(
'Лесной гном', 
'Скальный гном', 
'Горный дварф', 
'Холмовой дварф', 
'Драконорожденный', 
'Полуорк', 
'Коренастый полурослик', 
'Легконогий полурослик', 
'Полуэльф', 
'Тифлинг', 
'Человек', 
'Высший эльф', 
'Лесной эльф', 
'Темный эльф'
)
race=np.random.choice(racelist, size=1, p=raceprop)

