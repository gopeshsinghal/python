"""
rough work....just tried an approach
s = input()
s = s.split()
#print(s)
#print(s[0][0])
#print(len(s))
for i in range(len(s)):
    t = s[i][0]
    #print(t.upper())
    s[i][0] = list(t.upper())
     #print(type(s[i][0]))
print(s)

"""
"""
another function
def capital(s):
    t = s.split()
    string = ""
    for i in t:
        string = string + i.capitalize()
        string += " "
    return string
"""

def capital(s):
    string = ""
    for i in range(len(s)):
        if i == 0:
            string += s[i].capitalize()
            continue
        if s[i-1] == " ":
            string += s[i].capitalize()
            continue
        else:
            string+=s[i]
    return string

s = input()
print(capital(s))