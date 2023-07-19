import shape_calculator

rect = shape_calculator.Rectangle(3, 6)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(5)
print(sq.get_area())
sq.set_side(2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
print(sq)

rect.set_height(3)
rect.set_width(7)
print(rect.get_amount_inside(sq))