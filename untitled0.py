from random import randint
#print(randint(1,30))

avengers = ['Iron Man' ,'spider man','Captain America', 'Hulk', 'Thor', 'Black Widow' , 'Hawkeye', 'Ant Man', 'Scarlet Witch', 'Winter Soldier']
l = len(avengers)
k = randint(0,l-1)
t =avengers[k]
word = ""
for i in t:
    if i == " " or i == "a"or i == "e"or i == "i"or i == "o"or i == "u":
        word += i
    else:
        word += "_"
        
print(word)
    
    
