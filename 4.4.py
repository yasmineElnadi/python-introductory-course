class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2*(self.width + self.height)

rect_1 = Rectangle(4, 40)
rect_2 = Rectangle(3.5, 35.7)

print("For the first rectangle whose width is", rect_1.width," and height is", rect_1.height,
      "its Area is ", rect_1.getArea(),"and its Perimeter is",rect_1.getPerimeter(),
      " and for the second rectangle whose width is", rect_2.width, " and height is", rect_2.height,
      "its Area is ", rect_2.getArea(), "and its Perimeter is", rect_2.getPerimeter())
