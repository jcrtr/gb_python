# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} машина поехала'

    def stop(self):
        return f'{self.name} машина остановилась'

    def turn_right(self):
        return f'{self.name} машина повернула на право'

    def turn_left(self):
        return f'{self.name} машина повернула на лево'

    def show_speed(self):
        return f'Скорость машины Car {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины TownCar {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше 40'
        else:
            return f'Скорость {self.name} не выше 40'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость WorkCar {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Скорость WorkCar {self.name} выше 60'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полиция'
        else:
            return f'{self.name} не полиция'


wv = TownCar(30, 'White', 'WV', False)
ferrari = SportCar(100, 'Red', 'Ferrari', False)
audi = WorkCar(70, 'Black', 'Audi', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)


print(f'{wv.turn_right()},{ferrari.stop()}')
print(f'{audi.go()}, {audi.show_speed()}')
print(audi.turn_left())
print(f'{audi.name} {audi.color} цвета')
print(f'{ferrari.name} полиция? {ferrari.is_police}')
print(wv.show_speed())
print(ferrari.show_speed())
print(ford.police())
print(ford.show_speed())
