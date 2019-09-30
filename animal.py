class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
    
    def drink(self):
        print(f"{self.name} is drinking.")

class Dog(Animal):
    def bark(self):
        print(f"I'm {self.name} and I say Woof!")

if __name__ == "__main__":
    my_dog = Dog("Scruffy")
    my_dog.eat()
    my_dog.drink()
    my_dog.bark()
