def paint_calc(height, width, cover):
  quantity = round((height*width)/cover)
  if quantity > 1:
    print(f"You need {quantity} cans for the job")
  else:  
    print(f"You need {quantity} can of paint for the job")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


