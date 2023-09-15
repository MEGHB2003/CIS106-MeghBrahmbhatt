#input phase
PPS = float(input("Enter price per share"))
CS = float(input("Enter current stock price"))
QS = float(input("Enter quantity of stock"))

#process phase
Value = (CS - PPS) * QS

#output phase
print("total value price" , Value)
