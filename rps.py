# Python project #1: Rock, Paper, Scissors 

import random
#set player and cpu scores to zero
ps = 0
cs = 0
outcomes = ["rock","paper","scissors"]

def game():
	global ps
	global cs
	random.shuffle(outcomes)
	c_input = random.choice(outcomes)
	p_input = input("Choose rock, paper or scissors ")
	if p_input in outcomes:
		print("You chose " +p_input)
	else:
		while p_input not in outcomes:
			p_input = input("Choose rock, paper or scissors ")
	print("CPU chose " +c_input)
	
	if p_input == c_input:
		print("Draw")
	elif ( p_input == "rock" and c_input == "paper"
		or  p_input == "paper" and c_input == "scissors"
		or  p_input == "scissors" and c_input == "rock"			
		):
			cs +=1
			print("You lose, computer wins")

	elif ( p_input == "rock" and c_input == "scissors"	
		or  p_input == "paper" and c_input == "rock"
		or  p_input == "scissors" and c_input == "paper"			
		):
			ps +=1
			print("You win, computer loses")
	print("CPU score: " ,cs)
	print("Your score: " ,ps)

	rep = input("Play again? (Y/N)")

	if rep == "N":
		print("Thank you for playing")
	if rep == "Y":
		game()

game()


