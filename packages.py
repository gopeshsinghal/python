def ping(t):
    if t%2 == 0:
        return True
    else:
        return False


def printing(num):
    val = ping(num)
    if val == True:
        print("number is even:")
    else:
        print("number is odd:")
        
        
number = int(input("Enter number:"))
printing(number)