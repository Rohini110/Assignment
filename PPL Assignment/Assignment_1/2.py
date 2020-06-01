#dice rolling simulator

from random import randint

print("You can play again and again to get a number from dice ")
print("Start :")
while(1):
	number = randint(1,6)
	print("Value : " +str(number))
	print("Do you want to continue (y/n) ?")
	ans = input()
	if ans == 'y':
		continue
	if ans == 'n':
		break
	
