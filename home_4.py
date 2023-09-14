class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed

    def bark(self):
        print(f"{self.get_name()} лает: Гав-гав!")

    def get_breed(self):
        return self.__breed

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def meow(self):
        print(f"{self.get_name()} мяукает: Мяу-мяу!")

    def get_color(self):
        return self.__color

dog = Dog("Рекс", 3, "Овчарка")
cat = Cat("Барсик", 2, "Серый")

print(f"{dog.get_name()} возраст {dog.get_age()}, порода {dog.get_breed()}")
dog.bark()

print(f"{cat.get_name()} возраст {cat.get_age()}, окрас {cat.get_color()}")
cat.meow()
