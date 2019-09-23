import random

class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = 1000
    # Methods are defined as their own named functions inside the class
    def attack(self):
          return random.randint(1,1000)  
      # ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value. 
          

class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = 1000

    # Methods are defined as their own named functions inside the class
    def block(self):
          return random.randint(1,1000)  

class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = 100
        self.current_health = 100

    # Methods are defined as their own named functions inside the class
    def add_ability(self):
        return
    def attack(self, ability):
        return

    def defend(self, incoming_damage):
        return

    def take_damage(self, damage):
        return

    def is_alive(self):
        return

    def fight(self, opponent):
        return

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 1000)
    print(ability.name)
    print(ability.attack())
    armor = Armor("Lustrous Shield", 1000)
    print(armor.name)
    print(armor.block())
    my_hero = Hero("Mystic Mayhem", 100)
    print(my_hero.name)
    print(my_hero.current_health)
