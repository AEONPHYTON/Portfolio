import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(",")

num_items = len(names)
randon_choice = random.randint(0,num_items -1 )
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} pay the bill!!")