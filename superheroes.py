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
          

# class Armor:
#     # Required properties are defined inside the __init__ constructor method
#     def __init__(self, name, max_block):
#         self.name = name
#         self.max_block = int(max_block)

#     # Methods are defined as their own named functions inside the class
#     def block(self):

# class Hero:
#     # Required properties are defined inside the __init__ constructor method
#     def __init__(self, name, starting_health):
#         self.name = name
#         self.starting_health = 100

#     # Methods are defined as their own named functions inside the class
#     def add_ability(self):
#     def attack(self, ability):
#     def defend(self, incoming_damage):
#     def take_damage(self, damage):
#     def is_alive(self):
#     def fight(self, opponent):

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 1000)
    print(ability.name)
    print(ability.attack())
