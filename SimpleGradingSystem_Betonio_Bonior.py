print("Please enter your details.")

print("Full name: ")
name = input()
print("ID Number: ")
id_number = input()
print("Course: ")
course = input()
print("Section: ")
section = input()

print("Input your 1st quarter grade:")
grade1 = eval(input())
print("Input your 2nd quarter grade:")
grade2 = eval(input())
print("Input your 3rd quarter grade:")
grade3 = eval(input())
print("Input your 4th quarter grade:")
grade4 = eval(input())

gwa = (grade1 + grade2 + grade3 + grade4) / 4

print("Your details:")
print("Full name: " + name)
print("ID Number: " + id_number)
print("Course: " + course)
print("Section: " + section)
print("Your grades: ")
print("1st quarter grade:", grade1)
print("2nd quarter grade:", grade2)
print("3rd quarter grade:", grade3)
print("4th quarter grade:", grade4)
print("Your GWA is:", gwa)
