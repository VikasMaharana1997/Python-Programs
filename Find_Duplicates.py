#find duplicatres values
my_list = ['a','b','c','b','n','z','n']
duplicates = []
for i in my_list:
    if my_list.count(i)>1:
        duplicates.append(i)
print(tuple(set(duplicates)))