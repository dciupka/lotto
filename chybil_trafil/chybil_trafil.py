import random
import numpy as np

# Base list for draw
numbers_base = [x for x in range(1,50)]
print(numbers_base)
print(10*'------')

# Drawing numbers

drawing_count = int(input('podaj liczbe losowan:' ))
x = 0
while  x<drawing_count:
	x+=1
	drawed = []
	count = 48
	for i in range(1,7):
		drawed.append(numbers_base.pop(random.randint(0,count)))
		count-=1
	print(drawed)

# Analitics
#jezeli element tabliy powtarza sie wiecej niz 10 raz wypisz te elemen


print(10*'---' + ' END ' + 10*'---')

