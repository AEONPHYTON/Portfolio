weigth = int(input("what is your weigth in kilos?\n"))
heigth = float(input("what is your heigth in meter?\n"))

bmi = round(weigth / (heigth ** 2))

if bmi < 18:
    print(f"your BMI is {bmi}, you are underweigth.")
elif bmi < 25:
    print(f"your BMI is {bmi}, you are normal weigth.")
elif bmi < 30:
    print(f"your BMI is {bmi}, you are overweigth.")
elif bmi < 35:
    print(f"your BMI is {bmi}, you are obese.")
else:
    print(f"your BMI is {bmi}, you are clinically obese.")