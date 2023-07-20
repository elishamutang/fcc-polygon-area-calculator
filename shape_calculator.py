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
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height **2) ** .5)
    
    def get_picture(self):
        lines = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(0, self.height, 1):
                line = "*" * self.width + "\n"
                lines += line
            return lines
                        

    def get_amount_inside(self, shape):
        self.shape = shape #Polygon object
        amt_inside = 0
        if self.get_area() >= shape.get_area():
            amt_inside = self.get_area() // shape.get_area() # // rounds down the value from 8.0 to 8
            return amt_inside
        else:
            return "Not enough"
    
    def __repr__(self) -> str:
        """Return a string representation of the object"""
        return f"Rectangle(width={self.width}, height={self.height})"
        
        
        

class Square(Rectangle):

    def __init__(self, side_length):
        self.side_length = side_length
        self.width = side_length
        self.height = side_length

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, sq_width):
        self.width = sq_width
        self.height = sq_width

    def set_height(self, sq_height):
        self.width = sq_height
        self.height = sq_height
    
    def __repr__(self) -> str:
        return f"Square(side={self.width})"