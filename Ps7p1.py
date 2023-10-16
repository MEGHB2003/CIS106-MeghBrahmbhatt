principleamt = 10000.00
intrate = 0.10
Year = 1
Endbalance = 0
print(principleamt)
print("Year, Beg Balance,End Balance")
Begbalance = principleamt
while Year <= 5:
  
    Endbalance = (Begbalance * intrate) + Begbalance 
    print(Year,Begbalance,Endbalance)
    Begbalance = Endbalance  
  
    Year = Year + 1

TotalInt = (Endbalance - principleamt)

print("The total interest is " , TotalInt)
    


