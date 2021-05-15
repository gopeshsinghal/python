def leap(y):
    if y%400 == 0:
        print("year is leap year")
    elif y%100 == 0:
        print("year is not a leap year")
    elif y%4 == 0:
        print("year is leap year: ")
    else:
        print("year is not a leap year: ")
y = int(input("enter year: "))
leap(y)










"""
another way
def is_leap(l):
    if l%4 == 0:
        leap = True
    if l%100 == 0:
        leap = False
    if l%400 == 0:
        leap = True
    return leap
l = int(input())
print(is_leap(l))

"""