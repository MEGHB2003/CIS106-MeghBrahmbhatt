def exam_average(ex1,ex2,ex3):
  sum = ex1 + ex2 + ex3
  total = 300
  percentage = (sum/total)* 100
  average = (sum/3)
  points = ex1 + ex2 + ex3
  return average,points
  



lastname = (input("Enter lastname"))
ex1 = float(input(" Enter your exam score 1 "))
ex2 = float(input(" Enter your exam score 2 "))
ex3 = float(input(" Enter your exam score 3 "))
average,points = exam_average(ex1,ex2,ex3)
print("Your last name", lastname)
print("Your exam score average", average)
print("Your exam points", points)