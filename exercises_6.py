#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. 
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight:
    _color = ['red', 'yellow', 'green']

    def running(self):
        count = 0
        while count!= 3:
            print(TrafficLight._color[count])
            if count == 0:
                time.sleep(7)
            elif count == 1:
                time.sleep(2)
            elif count == 2:
                time.sleep(4)
            count += 1


T_light = TrafficLight()
T_light.running()

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса. 
# Атрибуты сделать защищенными. 
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. 
# Проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass =  int(self._width * self._length* self.weight * self.height / 1000) 
        print('This is asphalt mass a road : ', asphalt_mass)


road = Road(5000, 20)
road.asphalt_mass()

#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
# name, surname, position (должность), income (доход). 
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. 
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname,position, wage, bonus ):
        self.name = name 
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

        
    
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position(input('Enter name: '), input('Enter surname: '), input('Enter position: '), input('Enter wage'), input('Enter bonus: '))
print(p.get_full_name(), p.get_total_income())

#4. 4. Реализуйте базовый класс Car. 
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат. 

class Car:
    
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\n The {self.name} has stopped.'

    def turn(self, direction):
        return f'\n The {self.name} turned {direction}'

    def show_speed(self):
        return f'\n Your speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
      
        if self.speed > 60:
            return f'\n Your speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Your speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('Reno', 70, 'black', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('BMW', 170, 'blue', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

#5. Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def _draw(self):
        return f'Enter the drow'


class Pen(Stationery):
    def _draw(self):
        return f'Enter the drow {self.title}'


class Pencil(Stationery):
    def _draw(self):
        return f'Enter the drow {self.title}'


class Handle(Stationery):
    def _draw(self):
        return f'Enter the drow {self.title}'


pen = Pen('pen')
print(pen._draw())
pencil = Pencil('pencil')
print(pencil._draw())
handle = Handle('hadle')
print(handle._draw())


