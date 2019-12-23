import numpy as np
from bgmod import *
from classgen import Pclass
from proplists import *
import random
from array import *
bglist=(
acolyte(),
charlatan(),
criminal(),
artist(),
hero(),
craftsman(),
hermit(),
noble(),
outlander(),
sage(),
sailor(),
soldier(),
urchin()
)

if Pclass=='Бард':
	bg=np.random.choice(bglist, size=1, p=bardprop)
elif Pclass=='Варвар' or Pclass=='Следопыт':
	bg=np.random.choice(bglist, size=1, p=barbprop)
elif Pclass=='Воин':
	bg=np.random.choice(bglist, size=1, p=fighprop)
elif Pclass=='Волшебник':
	bg=np.random.choice(bglist, size=1, p=sorcprop)
elif Pclass=='Друид' or Pclass=='Монах' or Pclass=='Чародей':
	bg=np.random.choice(bglist, size=1, p=druiprop)
elif Pclass=='Жрец':
	bg=np.random.choice(bglist, size=1, p=clerprop)
elif Pclass=='Колдун' or Pclass=='Плут':
	bg=np.random.choice(bglist, size=1, p=warlprop)
elif Pclass=='Паладин':
	bg=np.random.choice(bglist, size=1, p=paldprop)
