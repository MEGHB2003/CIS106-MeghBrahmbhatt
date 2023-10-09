counter = 0
totalex1 = 0.0

response = input("Do you want to calculate the average exam score Yes or No")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter student last name")
  score1 = float(input("Enter exam score 1"))
  score2 = float(input("Enter exam score 2 "))
  avg = (score1 + score2) / 2
  print("last name" , lastname)
  print("Has an average of" ,avg)      
  totalex1 = totalex1 + score1 
  response = input("Do you want to calculate the average score Yes or No")

avgex1 = totalex1 / counter 
print("Number of students:", counter)
print("Average exam score 1", avgex1)