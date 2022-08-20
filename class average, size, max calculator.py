student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max = student_scores[0]
total_mark = 0
number_of_students = 0
for n in range(0, len(student_scores)):
  total_mark += student_scores[n]
  number_of_students += 1
  if max < student_scores[n]:
    max = student_scores[n]
  elif max == student_scores[n]:
    max = student_scores[n]
  else:
    max = max
average = round(total_mark/number_of_students)
print(f" The hoghest score in the class is: {max}")
print(len(student_scores))
print(f"total mark is: = {total_mark}")
print(f"number of students = {number_of_students}")
print(f" The class average is: {average}")

 



