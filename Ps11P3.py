def loadarrays(lastname, score):
  f = open("myfile.txt", "r")
  for i in range (0,10,1):
      ln = f.readline()
      ln = ln.rstrip("\n")
      lastname.append(ln)
      s = f.readline()
      s = s.rstrip("\n")
      score.append(s)
  f.close()
def printarrays(lastname, score):
for i in range (0,10,1):
    print(lastname[i],"Has a score of:", score[i])
def hilow(lastname, score):
hisco = 0.0
hisub = 0
losco = 100.0
lossub = 0
for i in range (0,10,1):
  if float(score[i]) > hisco:
    hisco = float(score[i])
    hisub = i
  if float(score[i]) < losco:
    losco = float(score[i])
    lossub = i
print("The highest score is:", hisco, "and the student with the highest score is:", lastname[hisub])
print("The lowest score is:", losco, "and the student with the lowest score is:", lastname[lossub])

lastname = []
score = []
loadarrays(lastname, score)
printarrays(lastname, score)
hilow(lastname, score)