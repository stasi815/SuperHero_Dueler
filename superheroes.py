import random

class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    # Methods are defined as their own named functions inside the class
    def attack(self):
          return random.randint(0, self.max_damage)  
      # ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value. 
          

class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    # Methods are defined as their own named functions inside the class
    def block(self):
          return random.randint(0, self.max_block)  

class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = 100

    # Methods are defined as their own named functions inside the class
    def add_ability(self, ability):
        self.abilities.append(ability)
        return self.abilities
        
    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack() 
        return total
    #   '''Calculate the total damage from all ability attacks.
    #       return: total:Int
    #   '''
      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.
      # thanks @mdrame for clarity on what this function looks like
    
    def add_armor(self, armor):
        self.armors.append(armor)
        return self.armors

    def defend(self, incoming_damage):
        total_block = 0
        while len(self.armors) > 0 :
            for armor in self.armors:
                total_block += armor.block()
        return total_block
#   '''Runs `block` method on each armor.
#       Returns sum of all blocks
#   '''
# TODO: This method should run the block method on each armor in self.armors
# thanks @MackRoe for showing me how to account for no armor with len(self.armors)
    def take_damage(self, damage):
        return

    def is_alive(self):
        return

    def fight(self, opponent):
        return

if __name__ == "__main__":
    ability = Ability("invisibility", 1000)
    ability1 = Ability("stretch attack", 567)
    hero = Hero("Mystic Mayhem", 100)
    hero.add_ability(ability)
    hero.add_ability(ability1)
    print(hero.attack())
    great_big_helmut = Armor("gbh", 150)
    hero.add_armor(great_big_helmut)
    iron_shoes = Armor("iron shoes", 50)
    hero.add_armor(iron_shoes)
    print(hero.defend(78))


    

