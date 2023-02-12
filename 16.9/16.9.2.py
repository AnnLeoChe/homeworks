class Rectangle:
    def __init__(self,  width, heigth):
        self.width = width
        self.heigth = heigth
    def get_area(self):
        return self.width * self.heigth #посчитаем площадь


width = int(input( "width = " )) #введем размеры прямоугольника
heigth = int(input( "heigth = " ))
rectangle = Rectangle(width, heigth) #применим класс
print("Площадь = ",rectangle.get_area()) #выведем площадь
