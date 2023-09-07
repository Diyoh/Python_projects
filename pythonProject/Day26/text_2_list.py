R1 = open("file1.txt")
lst_1 = []
for c in R1:
  lst_1.append([int(n) for n in c.split()])
list_1 = [x[0] for x in lst_1]

R2 = open("file2.txt")
lst_2 = []
for b in R2:
  lst_2.append([int(y) for y in b.split()])
list_2 = [y[0] for y in lst_2]

result = [n for n in list_1 if n in list_2]
print(list_2)
print(list_1)
# Write your code above 👆

print(result)

# or we can use the following to convert the data read to a list

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()
results = [int(n) for n in file_1_data if n in file_2_data]
