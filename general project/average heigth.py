student_heigths = input("input a list of student heigths\n").split()
for n in range (0, len(student_heigths)):
    student_heigths[n] = int(student_heigths[n])
    #print(student_heigths)

total_heigth = 0 
for eigth in student_heigths:
    total_heigth += eigth
#print(total_heigth)

number_of_students = 0
for student in student_heigths:
    number_of_students += 1
#print(number_of_students)

print(round(total_heigth / number_of_students))