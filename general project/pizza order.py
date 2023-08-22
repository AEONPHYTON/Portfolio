print("Welcome to the pizza delivery!\nYou can order here!\n")
size = input("what size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want a pepperoni? Y or N\n")
extra_cheese = input("Do you want a extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 4

if extra_cheese == "Y":
    bill += 1

print(f"your total amount is: {bill}$")
        


