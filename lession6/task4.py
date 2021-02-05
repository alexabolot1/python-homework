"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        # использовал super(), чтобы унаследовать метод из родительского класса, а не только переопределить его.
        if self.speed > 60:
            print(f'Внимание! Вы едете со скоростью {self.speed} км/ч - это выше допустимого значения, '
                  'рекомендуем ехать потише!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Внимание! Вы едете со скоростью {self.speed} км/ч - это выше допустимого значения, '
                  'рекомендуем ехать потише!')


class PoliceCar(Car):
    pass


town_car = TownCar(62, 'красня', 'Lada Priora', False)
work_car = WorkCar(39, 'чёрная', 'Renault Sandero', False)
sport_car = SportCar(160, 'хаки', 'Ferrari', False)
police_car = PoliceCar(90, 'синяя', 'Patriot', True)

town_car.show_speed()
work_car.show_speed()
sport_car.go()
sport_car.turn('налево')
sport_car.stop()
print(police_car.is_police)
