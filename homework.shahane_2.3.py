list = [[0] * 4 for i in range(4)]
print("List before modification\n",list)
for i in range(len(list)):
    list[i][i] = 1

print("List after modification\n",list)
