heigth = int(input("If you want to mout on a rollercaster, you need to tell me how many heigth are you\nwhat is your heigth in cm?\n"))

bill = 0

if heigth >= 120:
    print("Ok you can pass!")
    age = int(input("and then I need to say how old are you????\ntell me correct age!!!!\n"))
    if age < 12:
        bill = 5
        print("you prize is 12 box!")
    elif age <= 18:
        bill = 16
        print("You are not a major man/woman, give me 16 box!")
    elif age <= 40:
        bill = 20
        print("You are OK please give me 20 box!")
    elif age <= 70:
        bill = 2100
        print("You are so old, can't ride the rollercaoaster!!!!")
    elif age >= 71 and age <= 100:
        bill = 0
        print ("Really want you come into the rollercaster? Good luck!!!\nIf you murder it's not own responsability")
    else:
        print("You prize is 18 box! Find a work!!!!")
    
    photo = input("whant you shot a photo? Y for yes! N for no!\n")
    if photo == "Y":
        bill += 3

    print(f"the new prize is {bill} box!")

else:
    print("You are a nano and can't pass!!")
#print("Are you happy for the game... and now ride!!!!!")





