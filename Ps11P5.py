def loadarrays(lastname, avg):
  with open("myfile.txt", "r") as f:
    for i in range (0,10,1):
      ln = f.readline()
      ln = ln.rstrip("\n")
      lastname.append(ln)
      s = f.readline()
      s = s.rstrip("\n")
      avg.append(s)
  f.close()
def printarrays(lastname, avg):
  for i in range (0,10,1):
    print(lastname[i],"Has a avg of:", avg[i])

def searchname(lastname, avg, name):
  for i in range (0,10,1):
    if lastname[i] == name:
      print(name,"Has a avg of:", avg[i])
      return
  print("Name not found")

lastname = []
avg = []
loadarrays(lastname, avg)

r = input("Do you want to search a last name (y or n)?: ")
while r == "y":
  name = input("Enter last name: ")
  searchname(lastname, avg, name)
  r = input("Do you want to search a last name (y or n)?: ")