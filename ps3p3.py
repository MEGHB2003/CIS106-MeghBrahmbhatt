#input phase
totalmealcost = (float(input("Your total meal cost is")))

#process phase
tip1 = (0.15 * totalmealcost)
totalwithtip1 = (totalmealcost + tip1)
tip2 = (0.18 * totalmealcost)
totalwithtip2 = (totalmealcost + tip2)
tip3 = (0.20 * totalmealcost)
totalwithtip3 = (totalmealcost + tip3)

#output phase
print("Your total meal cost will be", totalmealcost)
print("Your tip 1 is" ,tip1) 
print("total with tip1" , totalwithtip1)
print("Your tip 2 is" , tip2)
print("total with tip 2" , totalwithtip2)
print("Your tip 3 is" , tip3)
print("total with tip3" , totalwithtip3)


