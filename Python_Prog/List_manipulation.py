ls=["jame",True,1234]

print(ls)
print(ls[-2])

ls[2] = "HR"
print(ls)

ls.append("id")
print(ls)

ls.insert(3,"1")
print(ls)
 
del(ls[2])
print(ls)

# ls.sort() """ cannot sort bool and str """
# print(ls)
