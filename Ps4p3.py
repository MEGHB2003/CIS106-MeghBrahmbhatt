NOB = float(input("Enter number of books to order"))
CPB = float(input("Enter cost per book"))

total = (NOB * CPB)
if total> 50.00:
  sc = 0

if total<50.00:
  sc = 25.00

print("Number of books", NOB)
print("Cost per book", CPB)
print("order total", total)
print("Shipping charge cost",sc)
