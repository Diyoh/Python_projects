# # row_map = {row:"" for row in range(3)}
# # print(row_map)
#
# class Zigzag:
#     def solution(self, s:str, num_of_rows:int):
#         if num_of_rows == 1:
#             return s
#         row_count = {rows:"" for rows in range(num_of_rows)}
#         rows = 0
#         moving_up = True
#         for letter in s:
#             row_count[rows].append (letter)
#             if (rows ==0) or ((rows < num_of_rows) and moving_up):
#                 rows += 1
#                 moving_up = True
#             else:
#                 rows -= 1
#                 moving_up = False
#             print(rows)
#
#
# Zigzag.solution( 9, "SHILOH", 9)
int main()
x,y = 67.80
x,y,z = 1,2,3
print (x,y,z)
