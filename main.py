import CalArea # import file in the same dir
from Area.rectangle import rectangle # import from folder in dir

radius = 3.5

area = CalArea.calculate_cricle_area(radius)

# print(area)

rectangle_area = rectangle.calculate_area(4, 5)
print(f'area of rectangle: {rectangle_area}')
print(f'area of cricle: {area}')

print("______________________________")

from class_person.person import Person

myPerson = Person('adam', 45, 1997)
myPerson.greeting()

infor = myPerson.getInfor()
print(infor)