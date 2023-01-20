class Rectangle():
    def __init__(self,l,w):
       self.length=l
       self.width=w

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
l1=float(input("Enter the length of first rectangle"))
l2=float(input("Enter the length of second rectangle"))
b1=float(input("Enter the width of first rectangle"))
b2=float(input("Enter the width of second rectangle"))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("Area of rectangle 1 is {} and perimeter is{}:".format(rect1.area(),rect1.perimeter()))
print("Area of rectangle 2 is {} and perimeter is{}:".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())


