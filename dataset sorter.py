f = open("groceries.txt", "r")
lines = f.read().splitlines()
newlist = []
for line in lines:
    new_line = line.replace('"', '')  # Remove double quotes from the line
    newlist.append(new_line)

print("\n".join(newlist))
newData = "\n".join(newlist)
f.close()

f = open("updatedgroceries.txt", 'w')
f.writelines(newData)
f.close()
