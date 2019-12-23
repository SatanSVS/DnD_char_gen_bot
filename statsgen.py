import random
from racegen import race

def dice():
	x=random.randint(1, 6)
	y=random.randint(1, 6)
	z=random.randint(1, 6)
	o=random.randint(1, 6)
	stat=[x, y, z, o]
	stat.remove(min(stat))
	r=sum(stat)
	return r

stre=dice()
agi=dice()
stam=dice()
intel=dice()
mudr=dice()
har=dice()

stats_work=[
stre,
agi,
stam,
intel,
mudr,
har
]

def rand_stat():
        x=int()
        y=int()
        x=random.randint(0, 5)
        y=random.randint(0, 5)
        stats_work[x]+=1
        stats_work[y]+=1
        
if race=='Лесной гном':
	agi+=1
	intel+=2
elif race=='Скальный гном':
	stam+=1
	intel+=2
elif race=='Горный дварф':
	stam+=2
	stre+=2
elif race=='Холмовой дварф':
	stam+=2
	mudr+=1
elif race=='Драконорожденный':
	stre+=2
	har+=1
elif race=='Полуорк':
	stam+=1
	stre+=2
elif race=='Коренастый полурослик':
	agi+=2
	stam+=1
elif race=='Легконогий полурослик':
	agi+=2
	har+=1
elif race=='Полуэльф':
	rand_stat()
elif race=='Тифлинг':
	intel+=1
	har+=1
elif race=='Человек':
	stre+=1
	agi+=1
	stam+=1
	intel+=1
	mudr+=1
	har+=1
elif race=='Высший эльф':
	agi+=2
	intel+=1
elif race=='Лесной эльф':
	agi+=2
	mudr+=1
elif race=='Темный эльф':
	agi+=2
	har+=1


stats=(
"Сила:"+str(stre)+"\n",
"Ловкость:"+str(agi)+"\n",
"Телосложение:"+str(stam)+"\n",
"Интелект:"+str(intel)+"\n",
"Мудрость:"+str(mudr)+"\n",
"Харизма:"+str(har)+"\n"
)



