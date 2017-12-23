from pipeline import *

choice = input('Is this first time running? Y/N\n')

while choice:
	if choice.upper() == 'Y':
		try:
			DB_create()
			get_update()
			choice = False
		except:
			print('You have Existing DB Instance...Skipping Creation Now')
			get_update()
			choice = False
	elif choice.upper() == 'N':
		try:
			get_update()
			choice = False
		except:
			print('Database Not Found. Creating database')
			DB_create()
			get_update()
			choice = False
	else:
		print('Invalid Input! Please enter Valid Input')
		choice = input('Is this first time running? Y/N\n')

get_updateInterval()