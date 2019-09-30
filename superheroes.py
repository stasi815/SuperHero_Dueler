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
        Returns sum of all blocks."""
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
        """Current Hero will take turns fighting the opponent hero passed in."""
        if len(opponent.abilities) == 0 and len(self.abilities) == 0:
            return "Draw"
        else :     
            while self.is_alive() and opponent.is_alive() :
                if len(self.abilities) > 0 and len(opponent.abilities) == 0 :
                    opponent.take_damage(self.attack())
                elif len(opponent.abilities) > 0 and len(self.abilities) == 0 :
                    self.take_damage(opponent.attack())
                else :
                    self.take_damage(opponent.attack())
                    opponent.take_damage(self.attack())
        
        if self.is_alive(): 
            print(f"{self.name} won!")
        else :
            print(f"{opponent.name} won!")

class Weapon(Ability):
    def __init__(self, name, full_attack_value):
        """Create Instance Variables:
          name:String
          attack_strength: Integer
        """
        self.name = name
        self.full_attack_value = full_attack_value
    # Methods are defined as their own named functions inside the class
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # full_attack_value = 0
        weapon_attack = random.randint(self.full_attack_value//2, self.full_attack_value)
        return weapon_attack
        # TODO: Use what you learned to complete this method.

class Team(Hero):
    def __init__(self, name):
        """Initialize your team with its team name."""
        self.name = name
        self.heroes = []
    # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
    def add_hero(self, name):
        """Add Hero object to self.heroes."""
        self.heroes.append(name)

    def remove_hero(self, name):
        """Remove hero from heroes list.
        If Hero isn't found return 0."""
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        """Prints out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)


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

# test hero.is_alive()
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# test hero.fight() method 
# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero2.add_ability(ability1)
#     hero2.add_ability(ability2)
#     hero1.add_ability(ability3)
#     hero1.add_ability(ability4)
#     hero1.fight(hero2)

# test for ability.attack() in Ability class
# if __name__ == "__main__":
#     weapon1 = Weapon("big_sword", 50)
#     print(weapon1.name)
#     print(weapon1.attack())

# test for Team class
# if __name__ == "__main__":
#     team1 = Team("Super Dupers")
#     hero1 = Hero("Wonder Lady")
#     hero2 = Hero("Water Lady")
#     hero3 = Hero("Wind Lady")
#     team1.add_hero(hero1)
#     team1.add_hero(hero2)
#     team1.add_hero(hero3)  
#     team1.remove_hero("Wind Lady")
#     team1.view_all_heroes()




    

