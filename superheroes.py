import random

class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, attack_strength):
        """Create Instance Variables:
          name:String
          attack_strength: Integer
        """
        self.name = name
        self.attack_strength = attack_strength
    # Methods are defined as their own named functions inside the class
    def attack(self):
        """Return a value between 0 and the value set by self.attack_strength.
        """
        return random.randint(0, self.attack_strength)
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
        self.deaths = 0
        self.kills = 0

    # Methods are defined as their own named functions inside the class
    def add_ability(self, ability):
        """Add ability to abilities list."""
        self.abilities.append(ability)

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
        hero_armor = Armor(armor.name, armor.max_block)
        self.armors.append(hero_armor)

    def defend(self):
        """Runs `block` method on each armor.
        Returns sum of all blocks."""
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    # TODO: This method should run the block method on each armor in self.armors

    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense."""
        absorbed_damage = damage - self.defend()
        self.current_health -= absorbed_damage
        # self.current_health = self.current_health - damage - self.defend()
    # TODO: Create a method that updates self.current_health to the current
    # minus the the amount returned from calling self.defend(damage).

    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not."""
    # TODO: Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        """Update kills with num_kills"""
        self.kills += num_kills
        return self.kills
    # TODO: This method should add the number of kills to self.kills

    def add_deaths(self, num_deaths):
        """Update deaths with num_deaths"""
        self.deaths += num_deaths
        return self.deaths
    # TODO: This method should add the number of deaths to self.deaths

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive() is False:
            self.add_deaths(1)
            opponent.add_kill(1)
            print(f"{opponent.name} won!")
        else:
            self.add_kill(1)
            opponent.add_deaths(1)
            print(f"{self.name} won!")

    #TODO: Refactor this method to update the
    # number of kills the hero has when the opponent dies.>
    # Also update the number of deaths for whoever dies in the fight

    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""
        self.abilities.append(weapon)
        # return self.abilities
    # TODO: This method will append the weapon object passed in as an
    # argument to self.abilities.
    # This means that self.abilities will be a list of
    # abilities and weapons.


class Weapon(Ability):
    #     """Create Instance Variables:
    #       name:String
    #       attack_strength: Integer
    #     """
    # Methods are defined as their own named functions inside the class
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.attack_strength//2, self.attack_strength)
        # TODO: Use what you learned to complete this method.

class Team:
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

    def living_heroes(self):
        living_hero = []
        for hero in self.heroes:
            if hero.is_alive():
                living_hero.append(hero)
        return living_hero
# thanks to @NoblePrincelll for showing me how to incorporate living heroes

    def attack(self, other_team):
        """Battle each team against each other."""
        while len(self.living_heroes()) > 0 and len(other_team.living_heroes()) > 0:
            random_hero = random.choice(self.living_heroes())
            other_hero = random.choice(other_team.living_heroes())
            random_hero.fight(other_hero)

    # thank you @MackRoe and @mdrame for showing me how to get random hero from each team
    # TODO: Randomly select a living hero from each team and have
    # them fight until one or both teams have no surviving heroes.
    # Hint: Use the fight method in the Hero class.

    def revive_heroes(self, health=100):
        """Reset all heroes health to starting_health."""
        for hero in self.heroes:
            hero.current_health = health

    # TODO: This method should reset all heroes health to their
    # original starting value.

    def stats(self):
        """Print team statistics."""
        for hero in self.heroes:
            print("Super hero: " + hero.name)
            print("Number of kills: " + str(hero.kills))
            print("Number of deaths: " + str(hero.deaths))
    # TODO: This method should print the ratio of kills/deaths for each
    # member of the team to the screen.
    # This data must be output to the console.
    # Hint: Use the information stored in each hero.

class Arena:
    def __init__(self):
        """Instantiate properties:
            team_one: None
            team_two: None
        """
        # self.team_one = []
        # self.team_two = []
        self.team_one = Team("team one")
        self.team_two = Team("team two")

        # TODO: create instance variables named team_one and team_two that will hold our teams.

    def create_ability(self):
        """Prompt for Ability information.
        return Ability with values from user Input
        """
        user_ability = input("What ability do you want your hero to have? Enter it here: ")
        user_ability_value = int(input("What potency does this ability carry for the hero? Enter a number here: "))

        return Ability(user_ability, user_ability_value)


    # TODO: This method will allow a user to create an ability.
    # Prompt the user for the necessary information to create a new ability object.
    # return the new ability object.

    def create_weapon(self):
        """Prompt user for Weapon information
        return Weapon with values from user input.
        """
        user_weapon = input("Give your hero a bad-ass weapon. Enter the name of the weapon here: ")
        user_weapon_value = int(input("How bad-ass is this weapon? Enter a number value here: "))

        return Weapon(user_weapon, user_weapon_value)
    # TODO: This method will allow a user to create a weapon.
    # Prompt the user for the necessary information to create a new weapon object.
    # return the new weapon object.

    def create_armor(self):
        """Prompt user for Armor information
          return Armor with values from user input.
        """

        user_armor = input("Protect your hero! Name a piece of armor for your hero here: ")
        user_armor_value = int(input("How well does this armor protect? Add a number value here: "))

        return Armor(user_armor, user_armor_value)
    # TODO:This method will allow a user to create a piece of armor.
    #  Prompt the user for the necessary information to create a new armor
    #  object.
    #  return the new armor object with values set by user.

    def create_hero(self):
        """Prompt user for Hero information
          return Hero with values from user input.
        """
        user_hero_name = input("What is your super hero's name? Enter it here: ")
        self.hero_health = int(input("How much health is your super hero starting out with? Enter a number value here: "))
        hero = Hero(user_hero_name, self.hero_health)
        print("Please choose whether or not to give your hero abilities, weapons and/or armor.")

        user_wants_ability = True
        while user_wants_ability:
            user_ability_input = input("Please enter '1' to give your hero abilities. ").lower()
            if user_ability_input == '1':
                ability = self.create_ability()
                hero.add_ability(ability)
                more_abilities = input("Would you like to add another ability? (y/n) ")
                if more_abilities.lower() == "y":
                    user_wants_ability = True
                else :
                    user_wants_ability = False
            else:
                user_wants_ability = False
                print("Not one of the available choices. ")

        user_wants_weapon = True
        while user_wants_weapon:
            user_weapon_input = input("Please enter '2' to give your hero a weapon. ").lower()
            if user_weapon_input == '2':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                more_weapons = input("Would you like to add another weapon? (y/n) ")
                if more_weapons.lower() == "y":
                    user_wants_weapon = True
                else :
                    user_wants_weapon = False
            else:
                user_wants_weapon = False
                print("Not one of the available choices. ")

        user_wants_armor = True
        while user_wants_armor:
            user_armor_input = input("Please enter '3' to give your hero armor. ").lower()
            if user_armor_input == '3':
                armor = self.create_armor()
                hero.add_armor(armor)
                more_armor = input("Would you like to add another piece of armor? (y/n) ")
                if more_armor.lower() == "y":
                    user_wants_armor = True
                else :
                    user_wants_armor = False
            else:
                user_wants_armor = False
                print("Not one of the available choices. ")

        return hero

    # thank you @uyennguyen16900 for showing me how to include user's choice whether or not to have abilities, weapons, etc...
    # TODO: This method should allow a user to create a hero.
    # User should be able to specify if they want armors, weapons, and
    # abilities.
    # Call the methods you made above and use the return values to build
    # your hero.
    # return the new hero object

    def build_team_one(self):
        """Prompt the user to build team_one"""
        team_one_name = input("Give team one a name: ")
        self.team_one = Team(team_one_name)

        while True :
            num_heroes1 = input("How many heroes does team one have? ")
            if num_heroes1.isdigit() :
                break
        for i in range(int(num_heroes1)):
            self.team_one.add_hero(self.create_hero())



    # TODO: This method should allow a user to create team one.
    # Prompt the user for the number of Heroes on team one
    # call self.create_hero() for every hero that the user wants to add to team one.
    #
    # Add the created hero to team one.

    def build_team_two(self):
        """Prompt the user to build team_two"""
        team_two_name = input("Give team two a name: ")
        self.team_two = Team(team_two_name)

        while True:
            num_heroes2 = input("How many heroes does team two have? ")
            if num_heroes2.isdigit():
                break
        for i in range(int(num_heroes2)):
            self.team_two.add_hero(self.create_hero())
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.

    def team_battle(self):
        """Battle team_one and team_two together."""

        self.team_one.attack(self.team_two)

        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # Declare winning team
        if len(self.team_one.living_heroes()) > 0 :
            print(f"{self.team_one.name} wins the game!")
        elif len(self.team_two.living_heroes()) > 0 :
            print(f"{self.team_two.name} wins the game!")
        else:
            print("It's a tie")
        # Show both teams average kill/death ratio.
        self.team_one.stats()
        print("--------------------")
        self.team_two.stats()

# Unit Tests:

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
#     ability1 = Ability("Super Speed", 130)
#     ability2 = Ability("Super Eyes", 300)
#     ability3 = Ability("Wizard Wand", 20)
#     ability4 = Ability("Wizard Beard", 80)
#     hero1.add_ability(ability1)
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

# 2nd test for fight() method
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
#     print(hero1.deaths)

# test for .attack() and .stats() methods in Team class
# if __name__ == "__main__":
#     team1 = Team("Super Dupers")
#     other_team = Team("Stompers")
#     hero1 = Hero("Wonder Lady")
#     hero2 = Hero("Water Lady")
#     hero3 = Hero("Wind Lady")
#     other_team_hero1 = Hero("Winter Storm")
#     other_team_hero2 = Hero("Sand Storm")
#     other_team_hero3 = Hero("Tornado")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero2.add_ability(ability1)
#     other_team_hero2.add_ability(ability2)
#     hero2.add_ability(ability3)
#     other_team_hero1.add_ability(ability4)
#     other_team.add_hero(other_team_hero1)
#     other_team.add_hero(other_team_hero2)
#     other_team.add_hero(other_team_hero3)
#     team1.add_hero(hero1)
#     team1.add_hero(hero2)
#     team1.add_hero(hero3)
#     team1.attack(other_team)
#     team1.stats()
#     other_team.stats()

#test for .create_hero() in Arena class
# if __name__ == "__main__":
#     arena1 = Arena()
#     # arena1.create_ability()
#     # arena1.create_weapon()
#     # arena1.create_armor()
#     # print(arena1.abilities)
#     arena1.create_hero()

# test for hero.add_weapon()
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     sword = Weapon("Sword", 50)
#     hero.add_weapon(sword)
#     print(hero.name, hero.abilities)

# test for build_team_one(), build_team_two(), and final team battle functions
# if __name__ == "__main__":
#     arena1 = Arena()
#     arena1.build_team_one()
#     arena1.build_team_two()
#     arena1.team_battle()
#     arena1.show_stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()




