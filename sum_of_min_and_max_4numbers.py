def summ(l):
    lis = l.split()
    lis.sort()
    min = int(lis[0]) + int(lis[1]) + int(lis[2]) + int(lis[3])
    print(min)
    max = int(lis[-4]) + int(lis[-1]) + int(lis[-2]) + int(lis[-3])
    print(max)

l = input("enter numbers in list: ")
summ(l)
