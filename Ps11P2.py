lastname = ["name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8", "name9", "name0"]
score = ["100", "95", "90", "85", "80", "75", "70", "80", "90", "100"]
def displayarrays(lastname, score):
    for i in range(0, 10, 1):
        print(lastname[i], "Has a score of:" , score[i])
displayarrays(lastname, score)