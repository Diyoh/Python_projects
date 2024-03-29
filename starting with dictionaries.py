student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for score in student_scores:
  if (int(student_scores[score])) > 90 and (int(student_scores[score])) < 100:
    student_grades[score] = "outstanding"
  if (int(student_scores[score])) > 80 and (int(student_scores[score])) < 90:
    student_grades[score] = "Exceeds Expectation"

  if (int(student_scores[score])) > 70 and (int(student_scores[score])) < 80:
    student_grades[score] = "Acceptable"
  if (int(student_scores[score])) <= 70:
    student_grades[score] = "Fail"
print(student_grades)



#or use this code

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for score in student_scores:
  score = student_scores[score]
  if score > 90:
    student_grades[score] = "outstanding"
  if score > 80:
    student_grades[score] = "Exceeds Expectation"

  if score > 70:
    student_grades[score] = "Acceptable"
  if score <= 70:
    student_grades[score] = "Fail"
print(student_grades)













