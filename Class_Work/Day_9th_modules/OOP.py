'''defining a class to perform operation on rectangles'''
class Rectangle:
    length = 0
    width = 0
    def initialise(self, length, width):
        self.length = length
        self.width = width
        def dispay(self):
            print("Length:", self.length)
            print("Width:", self.width)
#Step 2: object creation'''obj name = object of class Rectangle
# it gives a memory to the class Rectangle and the memory is assigned to the object name obj'''obj will work outside the class Rectangle and it can access the attributes and methods of the class Rectangle
rect = Rectangle()
rect.initialise(5, 10)
rect.display_data()