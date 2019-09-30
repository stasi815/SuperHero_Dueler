import random

class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_attack_strength):
        """Create Instance Variables:
          name:String
          attack_strength: Integer
        """
        self.name = name
        self.max_attack_strength = max_attack_strength
    # Methods are defined as their own named functions inside the class
    def attack(self):
        """Return a value between 0 and the value set by self.max_attack_strength.
        """
        return random.randint(0, self.max_attack_strength)  
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value. 
          

class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        """Instantiate instance properties.
        name: String
        max_block: Integer
        """
        self.name = name
        self.max_block = max_block

    # Methods are defined as their own named functions inside the class
    def block(self):
        return random.randint(0, self.max_block)  

class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        """Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        """
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        self.damage = 0

    # Methods are defined as their own named functions inside the class
    def add_ability(self, ability):
        """Add ability to abilities list."""

        self.abilities.append(ability)
        return self.abilities
        
    def attack(self):
        """Calculate the total damage from all ability attacks.
          return: total:Int
        """
        total = 0
        for ability in self.abilities:
            total += ability.attack() 
        return total

      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.
      # thanks @mdrame for clarity on what this function looks like
    
    def add_armor(self, armor):
        """Add armor to self.armors
        Armor: Armor Object
        """
        self.armors.append(armor)

    def defend(self, incoming_damage):
        """Runs `block` method on each armor. 
        Returns sum of all blocks.""""
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block 

# TODO: This method should run the block method on each armor in self.armors

    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense."""
        incoming_damage = 0
        self.current_health = self.current_health - damage + self.defend(incoming_damage)


  # TODO: Create a method that updates self.current_health to the current
  # minus the the amount returned from calling self.defend(damage).

    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not."""
  # TODO: Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else:
            return False


    def fight(self, opponent):
        return

# test for ability.attack() in Ability class
# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())

# test for armor.block() in Armor class
# if __name__ == "__main__":
#     armor = Armor("Debugging shield", 20)
#     print(armor.name)
#     print(armor.block())

# first test for Hero class
# if __name__ == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

# test for hero.add_ability
# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     print(hero.abilities)

# test for hero.attack()
# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())

# test for hero.add_armor
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     armor = Armor("fight shoes", 20)
#     armor2 = Armor("hard gloves", 30)
#     hero.add_armor(armor)    
#     hero.add_armor(armor2)    
#     print(hero.armors)

# test for hero.add_armor
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     armor = Armor("fight shoes", 20)
#     armor2 = Armor("hard gloves", 30)
#     hero.add_armor(armor)    
#     hero.add_armor(armor2)    
#     print(hero.defend(50))

# test for hero.defend()
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     armor = Armor("Debugging shield", 20)
#     armor2 = Armor("hard gloves", 1300)
#     hero.add_armor(armor)
#     hero.add_armor(armor2)
#     print(hero.defend(40))

# test for hero.take_damage()
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())





    

