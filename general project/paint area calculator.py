import math

def paint_calc(heigth, width, cover):
    number_of_cans = (heigth * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

test_h = int(input("heigth of the wall:\n"))
test_w = int(input("width of the wall:\n"))
coverage = 5
paint_calc(heigth=test_h, width=test_w, cover=coverage)