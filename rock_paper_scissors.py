import random

play = ['paper', 'scissors', 'rock']
Continue = True
invalidInput = True
invalidOption = True
comScore = 0
plaScore = 0
while Continue:
	while invalidInput:
		invalidOption = True
		print('Make a move!(r/s/p)')
		player = input()
		if player == 'r':
			plaInt = 2
			invalidInput = False
		elif player == 's':
			plaInt = 1
			invalidInput = False
		elif player == 'p':
			plaInt = 0
			invalidInput = False
		else:
			print('Invalid input! Please enter again...')

	comInput = random.randint(0, 2)
	print('You chose', play[plaInt], 'and the computer chose', play[comInput])
	result = comInput - plaInt
	if result == 1 or result == -2:
		print('You win!')
		plaScore += 1
	elif result  == 0:
		print('Draw!')
	else:
		print('You lose!')
		comScore += 1

	while invalidOption:
		invalidInput = True
		print('Do you want to play again? (Y/N)')
		option = input()
		if option == 'n':
			Continue = False
			invalidOption = False
		elif option == 'sc':
			print('human: ', plaScore)
			print('computer: ', comScore)
		elif option == 'y':
			invalidOption = False
		else:
			print('Invalid input! Please enter again...')
print('Thanks bye!')
	
			

