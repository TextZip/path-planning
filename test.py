potential_list = [[1,1],[1,0],[-1,0],[0,-1]]
print(potential_list)

for item1,item2 in potential_list:
    if item2 < 0:
        potential_list.remove([item1,item2])

for item1,item2 in potential_list:
    if item1 < 0:
        potential_list.remove([item1,item2])

print(potential_list)