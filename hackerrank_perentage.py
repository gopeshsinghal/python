stu_num = int(input())
d = {}
for i in range(stu_num):
    p = input().split()
    name = p[0]
    line = p[1:]
    scores = list(map(float, line))
    d[name] = scores
    #print(d)
x = input("choose student: ")
s = 0
for i in d[x]:
    s+=i
k = len(d[x])
s = s/k
print(s)




"""

exact output
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s = 0
    for i in student_marks[query_name]:
        s+=i
    k = len(student_marks[query_name])
    s = s/k
    print("{0:.2f}".format(s))
    
"""