def minimum(ls):
    min = 10000000
    for i in ls:
        if i < min:
            min = i
    return min
ls = [3,6,5,9,0,7,6,1,4]
print(minimum(ls))