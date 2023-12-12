class Square:
    def area(self, side_length):
        return side_length ** 2

figure = Square()
side_length = int(input("Enter the length of the side of the square: "))
print(figure.area(side_length))