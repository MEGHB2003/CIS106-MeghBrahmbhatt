def nms(month, sales):
    forecastpercent = 0.0
    if month in ["jan", "feb", "mar"]:
      forecastpercent = 0.10
    elif month in ["apr", "may", "jun"]:
      forecastpercent = 0.15
    elif month in ["jul", "aug", "sep"]:
      forecastpercent = 0.20
    elif month in ["oct", "nov", "dec"]:
      forecastpercent = 0.25
    nms = sales * (1 + forecastpercent)
    return nms

r = input("Do you wish to run this program? (y/n) ")
while r == "y":
  lastname = input("Enter your last name: ")
  month = input("Enter the month: ")
  sales = float(input("Enter the sales: "))
  nextmonthsales = nms(month, sales)
  print("The next months sales are: ", nextmonthsales)
  r = input("Do you wish to run this program? (y/n) ")