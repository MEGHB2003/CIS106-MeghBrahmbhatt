def calctuition(credhours, distcode):
  if distcode == "I":
      return 250 * credhours
  elif distcode == "0":
    return 550 * credhours
  else:
    return 0

students = []
totaltuition = 0

while True:
  name = input("Enter student name: ")
  if name == "":
    break
  credhours = int(input("Enter credit hours: "))
  distcode = input("Enter district code (I for in-district, O for out-of-district): ")
  tuitionowed = calctuition(credhours, distcode)
  totaltuition += tuitionowed
  students.append((name, credhours, distcode, tuitionowed))

print("\nStudent Data:")
for student in students:
  name,tuitionowed = student
  print(f"{name} owes ${tuitionowed}")

print("total tuition owed:" , totaltuition)
