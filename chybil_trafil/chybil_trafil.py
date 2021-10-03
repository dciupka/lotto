import random
from sys import stdout
from time import sleep
from timeit import default_timer as timer

while True:
	numbers_of_drawings = int(input('podaj liczbe losowan: '))
	repeted_num = int(input('ile razy ma sie powtorzyc zaklad w losowaniach: '))
	list_of_sets_drawed = []
	start = timer()
	for i in range(0,numbers_of_drawings):
		# Base list for draw
		numbers_base = [x for x in range(1,50)]
		#print(numbers_base)
		#print(10*'------')
		# Drawing numbers
		drawed_numbers = []
		n=50
		for drawing_num in range(1,7):
			n-=1
			index_number = random.choice(range(0,n))
			drawed_number = numbers_base.pop(index_number)
			drawed_numbers.append(drawed_number)

		set_list = set(drawed_numbers)
		list_of_sets_drawed.append(set_list)
		#print(sorted(set_list), len(set_list))

	# Analitics
	new_list_sets = []
	e=0
	for each in list_of_sets_drawed:
		count =  list_of_sets_drawed.count(each)
		e+=1
		if count >repeted_num:
			if each not in new_list_sets:
				new_list_sets.append(each) 
		else:
			stdout.write("\r%d" % e)
			stdout.flush()
			sleep(0.00000000000000000000000000001)
			#print(f'numer losowania: {e}',end=' ',flush=True)
		#stdout.write('\n') # Move cursor to the next line

	if not new_list_sets:
		print('\nWpisz wieksza probe losowan')
		print('\n')
		print(10*'* * ')
		print('time: ',timer()-start, ' s')
		print(10*'* * ')
		continue
	else: 
		print(10*'* * ')
		print(f'\nProponowane liczby: {new_list_sets}')
		print(10*'- -  ')
		print('time: ',timer()-start, ' s')
		print(10*'* * ')
		print(10*'---' + ' END ' + 10*'---')
		break
	

