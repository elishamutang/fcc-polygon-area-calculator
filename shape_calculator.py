class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
        return new_width

    def set_height(self, new_height):
        self.height = new_height
        return new_height

    def get_area(self):
        area = self.width*self.height
        return area
    