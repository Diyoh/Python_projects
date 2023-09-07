
def add(*agrs):
    sum = 0
    for n in agrs:
        sum += n
    return sum


print(add(5, 2, 3, 4))
add()


def calculate(n, **kwargs):
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n -= kwargs["subtract"]
    print(n)


calculate(22, add=3, subtract=7)

class car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = car(make = "Nissan", model="101")