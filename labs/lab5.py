#rose keenan section 2 lab 5
#this program plays a game that guesses a number between 1-100 :)

import random

#main program
times = eval(input("How many times would you like to play? "))
print("Think of a number between 1 and 100.")
totalCounter = 0
for games in range(times):
  counter = 1
  answer = ""
  high = 101
  low = 1
  guess = random.randint(low, high)
  answer = input(print("Is your number", guess, "? Enter < is your number is smaller, > if your number is bigger, and = if the number is correct."))
  while answer != "=":
    if answer == ">":
      low = guess + 1
      guess = random.randint(low, high)
      answer = input(print("Is your number", guess, "? Enter < is your number is smaller, > if your number is bigger, and = if the number is correct."))
      counter += 1
#      print(counter)
    if answer == "<":
      high = guess - 1
      guess = random.randint(low, high)
      answer = input(print("Is your number", guess, "? Enter < is your number is smaller, > if your number is bigger, and = if the number is correct."))
      counter += 1
#      print(counter)
  totalCounter += counter 
  print("Yay! I guessed right! Your number is", guess,"! Let's play again!")
average = totalCounter//times #using integer division so that the number of guesses is a whole number
print("The average amount of guesses is about", average, "times.")
