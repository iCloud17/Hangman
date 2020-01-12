import random
import os


words = ["APEX", "PLYWOOD", "RYTHM", "ALPHABET", "PYTHON", "XYLOPHONE", "FLOCK", "HANGMAN", "COMPUTER"]
vowels = ['A', 'E', 'I', 'O', 'U']	
guessed = list()
spellWord = list()
play = True
r = -1
prev = -2
oldPrev = -3

def randomNumber(r, prev, oldPrev):
	oldPrev = prev
	prev = r
	while (r == prev) or (r == oldPrev):
		r = random.randint(0,(len(words)-1))
	return r

def printWord():
	i=0
	while i < len(words[r]):
		if (words[r][i] in vowels) or (words[r][i] in guessed):
			print(words[r][i], end=' ')
		else:
			print('_', end=' ')
		i += 1


def printMan(n):
	switcher = {
		0:"",
		1:'o',
		2:"o-",
		3:"o->",
		4:"o->-",
		5:"o->-< Last Chance! Your guy's about to die...he's suffocating!",
		6:"o->-< Too bad. Your dude's dead. :( :/"
	}
	print("State of your man: " + switcher.get(n,""))
	print("Strikes left: ", end='')
	print(6-strike)
	print("")


while play:
	os.system('cls')
	r = randomNumber(r, prev, oldPrev)
	strike = 0
	alive = True
	guessed.clear()
	spellWord.clear()
	print("HANGMAN")
	printMan(strike)
	i = 0
	while i < len(words[r]):
		if (words[r][i] not in spellWord) and (words[r][i] not in vowels):
			spellWord.append(words[r][i])
		if words[r][i] in vowels:
			print(words[r][i], end=' ')
		else:
			print('_', end=' ')
		i += 1
	while alive:
		print("\n\nGuessed letters: ")
		print(guessed)
		g = input("\nWhat's your guess(not case sensitive)?? ")	
		while (not g.isalpha()) or len(g) != 1:
			g = input("Invalid guess!\nReenter your guess: ")
		g = g.upper()
		os.system('cls')
		print("HANGMAN")

		if g in guessed:
			printMan(strike)
			printWord()
			print("\nYou've already guessed this!")
		elif g in vowels:
			printMan(strike)
			printWord()
			print("\nAll the vowels are already given!")
		else:
			guessed.append(g)
			if g in spellWord:
				spellWord.remove(g)
				printMan(strike)
				printWord()					
				if len(spellWord) == 0:
					print("\nGood job! You Won!")
					alive = False
				else:
					print("\nGood guess!!")
			else:
				strike += 1
				printMan(strike)
				printWord()
				if strike == 6:
					print("\nGame Over!")
					print("The actual word was " + words[r])
					alive = False
				else:
					print("\nWrong guess!")

	c = input("Good game! Would you like to play again?\nEnter y for yes and n for no(not case sensitive): ")
	c = c.upper()
	while c != 'Y' and c != 'N':
		c = input("Invalid input entered. Please enter y or n: ")
		c = c.upper()
	if(c == 'N'):
		play = False

	print("")
	os.system('pause')