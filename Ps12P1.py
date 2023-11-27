# 1. Prompt the user for a number and create a list
num_items = int(input("Enter the number of items for the list: "))
user_list = []

for _  in range(num_items):
    user_input = int(input("Enter an integer: "))
    user_list.append(user_input)

# Display the list
print("User List:", user_list)

# 2. Insert the score of 99 at position 1
user_list.insert(1, 99)
print("Updated List after inserting 99 at position 1:", user_list)

# 3. Replace the value of 99 with 100
user_list[user_list.index(99)] = 100
print("Updated List after replacing 99 with 100:", user_list)

# 4. Create a second list and extend the first list
second_list = [500, 600, 700, 800, 900]
print("Second List:", second_list)

user_list.extend(second_list)
print("First List after extending with Second List:", user_list)

# 5. Remove the value 800 from the first list
user_list.remove(800)
print("First List after removing 800:", user_list)

# 6. Remove the third item from the first list
del user_list[2]
print("First List after removing the third item:", user_list)

# 7. Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

# 8. Display the count of the number of A grades
count_a_grades = grades.count("A")
print("Number of A grades:", count_a_grades)

# 9. Display the index of the first B grade
index_b_grade = grades.index("B")
print("Index of the first B grade:", index_b_grade)

# 10. Look for grade of F in the grades list
if "F" not in grades:
    print("F is not in the list.")

# 11. Clear the second list of integers
second_list.clear()
print("Second List after clearing:", second_list)

# 12. Delete the second list (will generate an error if trying to display)
del second_list
# Uncommenting the line below would result in an error:
# print("Second List after deleting:", second_list)

# 13. Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14. Sort the list of players
players.sort()
print("Sorted List of Players:", players)

# 15. Make a copy of the list of players called players2
players2 = players.copy()
print("Copy of List of Players (players2):", players2)

# 16. Reverse the order of players2
players2.reverse()
print("Reversed List of Players (players2):", players2)
