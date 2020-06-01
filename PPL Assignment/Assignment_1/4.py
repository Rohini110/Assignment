#generating random numbers

from random import randint

number = randint(1,30)

chances = 5


for i in range(1,6):
	print("Guess and enter a number between 1 to 30 :")
	num = int(input())
	if num > number:
		print("The number u have guessed is greater than generated number\n")
	if num < number:
		print("The number u have guessed is less than generated number\n")
	if num == number:
		print("Congratulations ! You have guessed the correct number\n")
		break

print("The random number generated was :" + str(number))


