#rose keenan lab 2 section 2
#purpose of program: assign letter grade based off of input values and average of total grades


#function to get average
def findave(scores):
  ave = sum(scores)/len(scores)
  return ave

#function to assign grades
def assigngrades(id, score, ave):
  grades = []
  for score in scores:
    if score > ave + 10.0:
      grade = 'A'
    elif score > ave + 5.0:
      grade = 'B'
    elif score > ave - 5.0:
      grade = 'C'
    elif score > ave - 10.0:
      grade =  'D'
    else:
      grade = 'F'
    grades.append(grade)
  return grades

#function to print summary
def printsummary(ids, scores, grades):
  print("ID   SCORE   GRADE")
  print("===================")
  n = len(ids)
  for i in range(n):
    print(ids[i], "   ",  scores[i], "     ", grades[i])

#main program
scores = []
ids = []
id = input("Enter an ID:")
while int(id) != -1:
  ids.append(id)
  score = eval(input("Enter a score:"))
  scores.append(score)
  id = eval(input("Enter another ID (or -1 to exit):"))
average = findave(scores)
summary = assigngrades(ids, scores, average)
printsummary(ids, scores, summary)
