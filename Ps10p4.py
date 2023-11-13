def b_average (score1,score2,score3, handi):
    sum = score1 + score2 + score3
    average = (sum/3)
    haverage = (sum + handi)/ 3
    return average,haverage 






lastname = input("Enter bowlers last name")
score1 = float(input("Enter score 1 "))
score2 = float(input("Enter your score 2"))
score3 = float(input("Enter your score 3"))
handi = float(input("What is your handicap"))
average,haverage = b_average(score1,score2,score3,handi)
print("Your last name",lastname)
print("Your score average is" , average)
print("The haverage is ",haverage)