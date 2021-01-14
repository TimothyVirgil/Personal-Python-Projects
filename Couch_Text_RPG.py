#This program is a text-based RPG about sitting on the couch.



import random

play = 'y'

while play == 'y':

	print("You walk in the door from a hard day's work.\n")

	print("You are sitting on the couch. What is your name?\n")

	name = input()

	print(f'\n{name} is your name? Are you sure? (Y/N)\n')

	confirm = input()

	yes = 0

	while yes == 0:

		if confirm.lower() == 'y':

			print(f'\nOk. Wow. So {name} is sitting on the couch.\n')

			yes = 1

		elif confirm.lower() == 'n':

			print('\nWell, what the heck is your hecking name then?\n')

			name = input()

			print(f'\n{name} is your name? Are you sure this time?\n')

			confirm = input()

		else:

			print('\nEnter Y or N\n')

			confirm = input()

	print('\nWe need to figure out how long you can live. Roll for your hit points\n')

	go = input("Press Enter to roll for HP!")

	hp = random.randint(1,20)

	print(f'\nYour HP is {hp} points. Can you handle this? (Y/N)\n')

	confirm = input()

	yes = 0

	while yes == 0:

		if confirm.lower() == 'y':

			print(f'\nOk. So you have a paltry {hp} hit points. Great.\n')

			yes = 1

		elif confirm.lower() == 'n':

			print(f'\nToo flipping bad duck sauce. Your HP is {hp} whether you like it or not.\n')

			yes = 1

		else:

			print('\nEnter Y or N')

			confirm = input()

	print('\nWe need to figure out how strong you are. Press enter to roll for muscle power.\n')


	go = input()

	strength = random.randint(1,20)

	print(f"Your strength is {strength} muscle points. Don't bother trying to re-roll, weakling.\n")

	go = input('Press enter to proceed with the riveting adventure.\n')

	print(f'\nSo, {name} is ten feet from the couch. {name} has {hp} hit points and {strength} muscle points.\n')

	print('Enter a command.')

	curr_command = input()

	commands = ['walk', 'sit', 'look', 'touch', 'kiss', 'dispose', 'talk', 'eat']



	while curr_command.lower() not in commands:

		print('That is not a command. Type help for a list of commands.\n')

		curr_command = input()

		if curr_command.lower() == 'help':

			print(f'The commands are {commands[0]}, {commands[1]}, {commands[2]}, or {commands[3]}.\n')

			curr_command = input()


	if curr_command.lower() == 'walk':

		print("You have walked very close to the couch.\n")

		story = 'path_a'

	elif curr_command.lower() == 'sit':

		print("You are now sitting on the couch. Fun!")

	elif curr_command.lower() == 'look':

		print("You are looking at the couch. You are struck by its beauty.")

	elif curr_command.lower() == 'touch':

		print("You reach out and touch the couch. You feel something stir deep inside you.")



	if story == 'path_a':

		grem_hp = random.randint(1,10)

		print("There is a gremlin hiding in the couch! What will you do? (Run or attack?)")

		batt_command = input()

		while batt_command.lower() != 'run' and batt_command.lower() != 'attack':

			print('You must choose run or attack!\n')

			batt_command = input()

		while batt_command.lower() == 'attack':

			grem_hp -= strength

			if grem_hp <= 0:

				print(f'You did {strength} damage to the gremlin. The gremlin is dead!\n')

				break

			else:

				print(f'''You did {strength} damage to the gremlin. The gremlin
					has {grem_hp - strength} HP left.''')

				print('The gremlin attacks for 3 damage.')

				hp -= 3

				if hp <= 0:


					print("Unfortunately you are dead. Would you like to play again? (Y/N)")

					play = input().lower

					while play != 'y' or play != 'n':

						print('Type Y to play again or N to quit.')
						
					break


				print(f'You have {hp} health left. What will you do? (attack or run)')

				batt_command = input()

		print('''You have killed a gremlin. There's a gnarly corpse sitting on your couch. 
			What will you do with it? (eat, kiss, dispose, talk''')

		curr_command = input().lower()

		while curr_command not in commands:

			print("That is not in ")









