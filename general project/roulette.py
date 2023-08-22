import random
import roulette_word

print(roulette_word.title)
print("Bienvenue in the roulette!")
number = int(input("Do it your game!\nWhat is the number?\n"))

if number >= 36 or number < -1:
    print("You type an invalid number, you lose!")
else:
    amount = int(input("how many money do you want put inside?\n"))
    colour = input(print("Would do you like to set the colour? R for red or B for black\n")).lower
    pair_unpair = input(print("Would do you like to set the pair or unpair? P for pair or U for unpair\n")).lower
    print("Rien ne va plus!")

game = random.randint(0, 36)
print(f"Computer choose: {game}")

plein = amount * 36
rouge =  amount * 2
noir = amount * 2
pair = amount * 2
dispair = amount * 2
manque = amount * 2
passe = amount * 2

pair = game % 2 == 0
dispair = game % 2 != 0

for num in game:
    if number == game:
        print("You Win!")
        print(f"Your winning prize is: {plein}")
    else:
        print("You Lose!")

for col in colour:
    if colour == "r" and game in roulette_word.red_number:
            print(f"Red number! you win: {rouge}")
            if colour == "b" and game in roulette_word.black_number:
                print(f"Black number! you win: {noir}")
    else:
        print("You Lose!")

for pair in pair_unpair:
    if pair_unpair == "p":
        if game == pair :
            print(f"Pair! You win: {pair}")
        elif game  == dispair:
            print(f"Unpair! You win: {dispair}")
        else:
            print("You Lose!")

if game == roulette_word.table:
    print("The number is 0. The table win all!")
# total_amount = plein + rouge + noir + pair + dispair + manque + passe 
# print(f"but if you set other gambling, you total amount is: {total_amount}")
