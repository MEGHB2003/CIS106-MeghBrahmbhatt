file = open("data1.txt", "r")

Count = 0.0
totaltuition = 0.0

lastname = str(file.readline().rstrip('\n'))



while lastname != "":
  dcode = str(file.readline().rstrip('\n'))
  credits = float(file.readline())

  if dcode == "I\n":
    costpercredit = 250.00
  else:
    costpercredit = 500.00
    
  tuition = credits * costpercredit
  Count = Count + 1
  totaltuition = totaltuition + tuition
  print("Student last name is " , lastname)
  print("The total credits taken", credits)
  print("The total tuition is" , tuition)
  print("  ")

  lastname = file.readline()

file.close()
  
print("The number of students" , Count)
print("Total tuition owed" , totaltuition)
  

  
  

  
