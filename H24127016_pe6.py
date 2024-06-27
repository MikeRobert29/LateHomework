import random

def displayHistogram(listOfTries) :

	tryRange = {"a - d" : "" , "e - h" : "", "i - l" : "", "m - p" : "", "q - t" : "", "u - x" : "", "y - z" : ""}

	for letter in listOfTries :
		for key in tryRange :
			if key[0] <= letter <= key[4] :
				tryRange[key] += "*"

	print("GUESS HISTOGRAM\n")
	
	for key, value in tryRange.items() :
			print(key, ":", value)

#-------------------------------------------------------------------------------------------------------------------------#

letter     = chr(random.randint(97, 122))
userLetter = ""
tries      = []

while userLetter != letter :

	userLetter = input("\nGuess the letter : ").lower()

	if userLetter < letter :
		print("The letter you are looking for is alphabetically higher\n")
	elif userLetter > letter :
		print("The letter you are looking for is alphabetically lower\n")

	tries.append(userLetter)

if len(tries) == 1 :
	print("Correct, it takes you only one try to find it!!!\n")
else :
	print("Congratulations, you guess the letter {} in {} tries!\n".format(letter, len(tries)))

displayHistogram(tries)