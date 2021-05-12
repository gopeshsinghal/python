def length(ls):
    count = 0
    for i in ls:
        count+=1
    #print(count)
    return count
ls = [1,5,3,8,2,5,7,4,0]
for i in range(length(ls)):
    print(ls[i])