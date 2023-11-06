def compassessedvalue(county, marketvalue):
  if county == "cook":
    avpercent = 0.90
  elif county == "dupage":
    avpercent = 0.80
  elif county == "mchenry":
    avpercent = 0.75
  elif county == "kane":
    avpercent = 0.60
  else:
    avpercent = 0.70
    
  assessedvalue = marketvalue * avpercent
  return assessedvalue

summarketvalue = 0.0
sumassessedvalue = 0.0
r = input("Do you wish to run this program? (y/n) ")
while r == "y":
  county = input("Enter the county name: ")
  marketvalue = float(input("Enter the market value of home: "))
  assessedvalue = compassessedvalue(county, marketvalue)
  print("The assessed value is: ", assessedvalue)
  summarketvalue = summarketvalue + marketvalue
  sumassessedvalue = sumassessedvalue + assessedvalue
  r = input("Do you wish to run this program? (y/n) ")
  
print("The total of all market values is: ", summarketvalue)
print("The total of all assessed values is: ", sumassessedvalue)
  