
#rose keenan section 2 lab 1

#function to verify input
def verify(num):
  if len(num) != 1:
    return False
  elif num in "12345":
    return True
  else:
    return False

#function to print one line --> if/elif/else
def christmasline(num):
  if num == 5:
   print("5 golden rings")
  elif num == 4:
   print("4 calling birds")
  elif num == 3:
   print("3 French hens")
  elif num == 2:
   print("2 turtle doves")
  elif num == 1:
   print("1 partridge in a pear tree")
  else:
   print("Error")

#function to print multiple lines --> if/else
def christmassong(num):
  print(num)
  if num == 5:
   print("5 golden rings")
  if num >= 4:
   print("4 calling birds")
  if num >= 3:
   print("3 French hens")
  if num >= 2:
   print("2 turtle doves")
  if num >= 1:
   print("1 partridge in a pear tree")
  else:
   print("Error")

#main program part a
num = input("Enter a number between 1 and 5: ")
if(verify(num)):
  num = int(num)
  print("")
  christmasline(num)
  print("")
else:
 print("")
 print("Invalid input. Must enter number between 1 and 5.")
 print("")

#main program part b
num = input("Enter a number between 1 and 5: ")
if(verify(num)):
  num = int(num)
  print("")
  christmassong(num)
  print("")
else:
  print("")
  print("Invalid input. Must enter number between 1 and 5.")
  print("")
