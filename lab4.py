class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

class Driver(Person):
    def __init__(self, name: str, surname: str, driving_experience: int):
        super().__init__(name, surname)
        self.driving_experience = driving_experience

class Engine:
    def __init__(self, power: int, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer

class Car:
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turnRight(self):
        print("Поворот направо")

    def turnLeft(self):
        print("Поворот налево")

    def toString(self):
        return f"Автомобиль {self.brand} класса {self.car_class}, весом {self.weight} кг, водитель {self.driver.name} {self.driver.surname}, мотор мощностью {self.engine.power} от {self.engine.manufacturer}"

class Lorry(Car):
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, cargo_capacity: int):
        super().__init__(brand, car_class, weight, driver, engine)
        self.cargo_capacity = cargo_capacity

    def toString(self):
        return super().toString() + f", грузоподъемностью {self.cargo_capacity} кг"

class SportCar(Car):
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, top_speed: int):
        super().__init__(brand, car_class, weight, driver, engine)
        self.top_speed = top_speed

    def toString(self):
        return super().toString() + f", предельная скорость {self.top_speed} км/ч"

driver = Driver("Иван", "Иванов", 5)
engine = Engine(200, "BMW")
car = Car("Audi", "B", 1500, driver, engine)
print(car.toString())

lorry_driver = Driver("Петр", "Петров", 10)
lorry_engine = Engine(300, "Volvo")
lorry = Lorry("Volvo", "C", 3000, lorry_driver, lorry_engine, 10000)
print(lorry.toString())

sportcar = SportCar("Ferrari", "Спортивный автомобиль", 1500, driver, engine, 300)
print(sportcar.toString())


