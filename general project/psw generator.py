import random
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g',
    'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 
    'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
    'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '£', '$', '%', '&', '/', '(', ')', '=', '?', '^', '*', '#', '@', '-', '+']

print("Welcome to the password generator")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

#easy level

password = ""
for char in range (1, nr_letter + 1):
    password += random.choice(letters)

for char in range (1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range (1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"The easy password is: {password}")
    
#hard level

password2 = []
for char in range (1, nr_letter + 1):
    password2 += random.choice(letters)

for char in range (1, nr_symbols + 1):
    password2 += random.choice(symbols)

for char in range (1, nr_numbers + 1):
    password2 += random.choice(numbers)

random.shuffle(password2)

password3 = ""
for char in password2:
    password3 += char
print(f"The hard password is: {password3}")