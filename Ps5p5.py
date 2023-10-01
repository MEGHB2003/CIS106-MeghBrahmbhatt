#inputphase
lastname = input("Your last name is")
salary =  float(input("Your Salary amount is"))
joblevel = float(input("What is your job level"))

#processphase
if joblevel>=10:
  bonusrate = 0.25
elif joblevel>=5:
  bonusrate = 0.20
else:
  bonusrate = 0.10

Bonus = (salary * bonusrate)

#outputphase
print("Your last name:" , lastname)
print("Your employee bonus is:" , Bonus)

