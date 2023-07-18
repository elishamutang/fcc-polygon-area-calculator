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
        lines = []
        for j in range(0, self.height, 1):
            if j <= self.height+1:
                line += "\n"
            else:
                pass

            for i in range(0, self.width, 1):
                if i <= self.width+1:
                    line += "*"
                else:
                    line += " "
        lines.append(line)

        return lines

    def get_amount_inside(self, shape):
        pass
    