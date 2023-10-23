def calc_mpg(miles, gallons):
    if gallons == 0:
        return 0
    else:
        return miles / gallons


trips = []
count = 0

while True:
    destcity = input("Enter destination city")
  
    miles = float(input("Enter miles driven: "))
    gallons = float(input("Enter gallons of gas used: "))
    mpg = calc_mpg(miles, gallons)
    trips.append([destcity, miles, gallons, mpg])
    count += 1
    if count == 3:
        break
print("\nTrip Data:")
for trip in trips:
    destination, miles, mpg = trip
  
    print(f"{destination}: {miles} miles, {mpg} mpg")
