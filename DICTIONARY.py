d = {"name":["gopesh","ghanisht",43], "followers":99999, "online":True, 34:"id"}
"""

keys: name,followers,online,34;

values: gopesh,99999,True,id;

"""

#for i in d.keys():
#    print(d[i])
#print(d)
#print(type(d))
#print(d.keys())
#print(d.values())
#print(d["name"][1]+" ty")
#print(d["name"][1]*3)
d["college"] = "JNU"
#print(d)
d.update({"department": {"btech":"CSE"}})
del d["department"]
print(d)