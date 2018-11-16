#rose keenan lab 3 section 2
#within this program, there are five sections

#part a
#function for random number generator
import random
def randomnumbers():
  numList = []
  for number in range(10): 
    num = random.randrange(10, 21)
    numList.append(num)
  print(numList)
  ave = sum(numList)/len(numList)
  print("The average is:", ave)

#part b
#function for one horse, one race
#2 miles = 10560 feet
def onehorse():
  time = 0
  position = 0
  length = 10560
  while position < length:
    position = position + random.randrange(4, 41)
    time += 1
  print("The total number of seconds is:", time)

#part c
#function for one horse, 1000 races
def onehorsemanyrace():
  totalTime = 0
  for race in range(1000):
    time = 0
    position = 0
    length = 10560
    while position < length:
      position = position + random.randrange(4, 41)
      time += 1
    totalTime = time + totalTime 
  aveTime = totalTime/1000
  print("The average number seconds it takes for the horse to run 1000 races is:", aveTime)

#part d
#function for many horses
def manyhorses(horses):
  length = 10560
  distance = 0
  positionList = [0] * horses
  winner = 0
  while winner < length:
    for horse in range(horses):
      distance = random.randrange(4, 41)
      positionList[horse] += distance
#      print(positionList)
    winner = max(positionList)
    winHorse = positionList.index(winner) + 1
  print(positionList)
  print("The winner is horse number ", winHorse)

#part e
#entering names of however many horses
def namehorses():
  name = input("Enter the name of the horse: ")
  nameList = []
  while name.upper() != "XXX":
    nameList.append(name)
    name = input("Enter another horse name or enter 'xxx' to stop: ")
#  print(nameList)
  length = 10560
  distance = 0
  names = len(nameList)
  print("There are", names, "horses running in the race")
  positionList = [0] * names
#  print(positionList)
  winner = 0
  time = 0
  while winner < length:
    for horse in range(names):
      distance = random.randrange(4, 41)
      positionList[horse] += distance
#      print(positionList)
      time += 1
      if time % 10 == 0:
        for horse in range(names):
          print("At", time, "seconds", nameList[horse], "is at", positionList[horse], "feet!")
    winner = max(positionList)
    winHorse = positionList.index(winner)
    winHorseNumber = winHorse + 1
  winName = nameList[winHorse]
  print("The winner is horse number", winHorseNumber, ",", winName,"!")


#main program
randomnumbers()
onehorse()
onehorsemanyrace()
horses = eval(input("Enter the number of horses: "))
manyhorses(horses)
namehorses()
