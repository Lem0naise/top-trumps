import random
from time import *
import os, subprocess

read_map = {
	"b":"Bravery",
	"i":"Intelligence / Power",
	"h":"Height",
	"g":"Goodness / Loyalty"
}
choice_map = {
	"b":1,
	"i":2,
	"h":3,
	"g":4
}
rev_choice_map = {
	1:"b",
	2:"i",
	3:"h",
	4:"g"
}


play_cards = []
ai_cards =[]

menu_art = [
	r"  _______            _______ ",
	r" |__   __|          |__   __|  ",
	r"    | | ___  _ __      | |_ __ _   _ _ __ ___  _ __  ___ ",
	r"    | |/ _ \| '_ \     | | '__| | | | '_ ` _ \| '_ \/ __|",
	r"    | | (_) | |_) |    | | |  | |_| | | | | | | |_) \__ \\",
	r"    |_|\___/| .__/     |_|_|   \__,_|_| |_| |_| .__/|___/",
	r"            | |                               | |      ",
	r"            |_|                               |_|    ",

]

intro_art = [
	r"  _______            _______ ",
	r" |__   __|          |__   __|  ",
	r"    | | ___  _ __      | |_ __ _   _ _ __ ___  _ __  ___ ",
	r"    | |/ _ \| '_ \     | | '__| | | | '_ ` _ \| '_ \/ __|",
	r"    | | (_) | |_) |    | | |  | |_| | | | | | | |_) \__ \\",
	r"    |_|\___/| .__/     |_|_|   \__,_|_| |_| |_| .__/|___/",
	r"            | |                               | |      ",
	r"            |_|                               |_|    ",
	r" ",    
	r"               _____",
	r"              |A .  | _____",
	r"              | /.\ ||A ^  | _____",
	r"              |(_._)|| / \ ||A _  | _____",
	r"              |  |  || \ / || ( ) ||A_ _ |",
	r"              |____V||  .  ||(_'_)||( v )|",
	r"                     |____V||  |  || \ / |",
	r"                            |____V||  .  |",
	r"                                   |____V|"
]    


def menu():
	for i in range(30):
		for each in intro_art:
			print((" "*i) + each)
		sleep(0.001)
		os.system("clear")

	for each in menu_art:
			print((" "*30) + each)


	
	print("\n\n\n")
	print(" "*45 + "1: Start Harry Potter game\n")
	print(" "*45 + "2: Start Star Wars game\n")
	print(" "*45 + "3: Start Lord of the Rings game\n")
	print(" "*45 + "4: Quit game\n")
	choice = input("")
	if choice.strip().lower() == "1":
		return "potter.txt"
	if choice.strip().lower() == "2":
		return "wars.txt"
	if choice.strip().lower() == "3":
		return "rings.txt"
	elif choice.strip().lower() == "4":
		sleep(0.5)
		quit()
	else:
		menu()
	

global characters
characters = []
	

choice_temp = menu()

with open (choice_temp) as chars:
	temp_chars = chars.readlines()
	for each in temp_chars:
		temp = [s.strip() for s in each.split(",")]
		for i in range(1, len(temp)):
			try:
				temp[i] = float(temp[i])
			except ValueError:
				os.system("clear")
				print("An error has occured when reading from the text file. Either redownload it or reconfigure it yourself. The format should be: 'Name, Bravery, Int/Power, Height, Goodness/Loyalty'")
				sleep(2)
				quit()
		characters.append(temp)

def deal():

	print("\n\n\nGame starting...")
	sleep(1)
	global player_turn
	player_turn = True
	random.shuffle(characters)
	for each in range(len(characters)):
		if each <((0.5)*len(characters)):
			play_cards.append(characters[each])
		else:
			ai_cards.append(characters[each])

#true is player, false is ai


def turn():
	global player_turn
	os.system("clear")
	print("Player Turn:")
	print("You have {cards_1} cards, and the AI has {cards_2} cards.\n\n".format(cards_1 = len(play_cards), cards_2 = len(ai_cards)))
	if len(ai_cards) == 0:
		os.system("clear")
		print("You have won! The AI has run out of cards. ")
		sleep(1)
		quit()
	try:
		temp_char = play_cards[0]
	except IndexError:
		os.system("clear")
		print("You have lost! You have run out of cards. ")
		sleep(1)
		quit()

	temp_name = "Your character is " + temp_char[0] + "."
	temp_bra = "Bravery: " + str(temp_char[1]) 
	temp_int = "Intelligence / Power: " + str(temp_char[2])
	temp_he = "Height: " + str(temp_char[3])
	temp_goo = "Goodness / Loyalty: " + str(temp_char[4])
		
	print("""
	 __| |____________________________________________| |__
	(__   ____________________________________________   __)
	   | |                                            | |
	   | |{name}| |
	   | |         Their stats are as follows:        | |
	   | |                                            | |
	   | |                                            | |
	   | |{bra}| |
	   | |{int}| |
	   | |{he}| |
	   | |{goo}| |
	   | |                                            | |
	 __| |____________________________________________| |__
	(__   ____________________________________________   __)
	   | |                                            | |
   """.format(name=f"{temp_name:^44}", bra=f"{temp_bra:^44}", int=f"{temp_int:^44}", he =f"{temp_he:^44}", goo=f"{temp_goo:^44}"))


	choice = input("Pick a stat: (B/I/H/G): ").strip().lower()
	if choice not in read_map:
		print("Incorrect input.\n\n")
		sleep(0.5)
		return

	try:
		other_char = ai_cards[0]
	except IndexError:
		print("You have won! The AI has run out of cards. ")
		quit()


	if temp_char[choice_map[choice]] > other_char[choice_map[choice]]:
		print("\n\n\n\nYou won!\n{name}'s {stat} of {num_1} beat {other_name}'s {stat} of {num_2}.".format(name = temp_char[0], stat=read_map[choice], other_name= other_char[0], num_1=temp_char[choice_map[choice]], num_2 = other_char[choice_map[choice]]))
		play_cards.append(other_char)
		play_cards.append(play_cards.pop(0))
		ai_cards.pop(ai_cards.index(other_char))
		return True

	elif temp_char[choice_map[choice]] < other_char[choice_map[choice]]:
		print("\n\n\n\nYou lost!\n{other_name}'s {stat} of {num_2} beat {name}'s {stat} of {num_1}.".format(name = temp_char[0], stat=read_map[choice], other_name= other_char[0], num_1=temp_char[choice_map[choice]], num_2 = other_char[choice_map[choice]]))
		play_cards.pop(play_cards.index(temp_char))
		ai_cards.append(ai_cards.pop(0))
		ai_cards.append(temp_char)
		return False

	else:
		print("\n\n\nYou drew!\n{other_name}'s {stat} of {num_2} drew with {name}'s {stat} of {num_1}.".format(name = temp_char[0], stat=read_map[choice], other_name= other_char[0], num_1=temp_char[choice_map[choice]], num_2 = other_char[choice_map[choice]]))
		play_cards.append(play_cards.pop(0))
		ai_cards.append(ai_cards.pop(0))
		return player_turn



def ai_turn():
	os.system("clear")
	if len(ai_cards) == 0:
		print("You have won! The AI has run out of cards. ")
		sleep(1)
		quit()
	try:
		temp_char = play_cards[0]
	except IndexError:
		print("You have lost! You have run out of cards. ")
		sleep(1)
		quit()

	print("AI turn:")
	print("You have {cards_1} cards, and the AI has {cards_2} cards.\n\n".format(cards_1 = len(play_cards), cards_2 = len(ai_cards)))

	temp_name = "Your character is " + temp_char[0] + "."
	temp_bra = "Bravery: " + str(temp_char[1]) 
	temp_int = "Intelligence / Power: " + str(temp_char[2])
	temp_he = "Height: " + str(temp_char[3])
	temp_goo = "Goodness / Loyalty: " + str(temp_char[4])
		
	print("""
	 __| |____________________________________________| |__
	(__   ____________________________________________   __)
	   | |                                            | |
	   | |{name}| |
	   | |         Their stats are as follows:        | |
	   | |                                            | |
	   | |                                            | |
	   | |{bra}| |
	   | |{int}| |
	   | |{he}| |
	   | |{goo}| |
	   | |                                            | |
	 __| |____________________________________________| |__
	(__   ____________________________________________   __)
	   | |                                            | |
   """.format(name=f"{temp_name:^44}", bra=f"{temp_bra:^44}", int=f"{temp_int:^44}", he =f"{temp_he:^44}", goo=f"{temp_goo:^44}"))
	input("Press enter to continue...")

	try:
		other_char = ai_cards[0]
	except IndexError:
		print("You have won! The AI has run out of cards. ")
		quit()

	if other_char[3] > 3:
		ai_choice = "h"
	else:
		temp_biggest = 0
		for each in range(1, len(other_char)):
			if other_char[each] > temp_biggest:
				temp_biggest = each
		ai_choice = rev_choice_map[temp_biggest]


	if temp_char[choice_map[ai_choice]] > other_char[choice_map[ai_choice]]:
		print("\n\n\n\nYou won!\n{name}'s {stat} of {num_1} beat {other_name}'s {stat} of {num_2}.".format(name = temp_char[0], stat=read_map[ai_choice], other_name= other_char[0], num_1=temp_char[choice_map[ai_choice]], num_2 = other_char[choice_map[ai_choice]]))
		play_cards.append(other_char)
		play_cards.append(play_cards.pop(0))
		ai_cards.pop(ai_cards.index(other_char))
		return True

	elif temp_char[choice_map[ai_choice]] < other_char[choice_map[ai_choice]]:
		print("\n\n\n\nYou lost!\n{other_name}'s {stat} of {num_2} beat {name}'s {stat} of {num_1}.".format(name = temp_char[0], stat=read_map[ai_choice], other_name= other_char[0], num_1=temp_char[choice_map[ai_choice]], num_2 = other_char[choice_map[ai_choice]]))
		play_cards.pop(play_cards.index(temp_char))
		ai_cards.append(ai_cards.pop(0))
		ai_cards.append(temp_char)
		return False

	else:
		print("\n\n\nYou drew!\n{other_name}'s {stat} of {num_2} drew with {name}'s {stat} of {num_1}.".format(name = temp_char[0], stat=read_map[choice], other_name= other_char[0], num_1=temp_char[choice_map[choice]], num_2 = other_char[choice_map[choice]]))
		play_cards.append(play_cards.pop(0))
		ai_cards.append(ai_cards.pop(0))
		return player_turn


deal()

print("\n\nYou have {cards_1} cards, and the AI has {cards_2} cards.\n\n".format(cards_1 = len(play_cards), cards_2 = len(ai_cards)))

while True:

	if player_turn:
		player_turn = turn()
		
		sleep(4)
	elif not player_turn:
		player_turn = ai_turn()
		sleep(2)
		
