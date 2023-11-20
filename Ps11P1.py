lastname = ["name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8", "name9", "name10"]
def displayarrays(lastname):
    for i in range(0, 10, 1):
        print(lastname[i])

def displayarraysrev(lastname):
    for i in range(9, -1, -1):
        print(lastname[i])

displayarrays(lastname)
print("In reverse:")
displayarraysrev(lastname)