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