total = int(input("How many total marks for each subject? "))
math = int(input("Enter math grade: "))
science = int(input("Enter science grade: "))
eng = int(input("Enter english grade: "))
percentage = ((math + science + eng)/(total*3))*100
print(percentage)