"""
Project: Turn-Based Combat Game (Version 1.000)

Description:
This script implements an Object-Oriented turn-based battle game. It simulates a combat 
system between a player-controlled Hero and an Enemy, orchestrating the mechanics through 
a continuous battle loop.

Architecture & Mechanics:
- Character (Base Class): Encapsulates common attributes (name, life, level). It handles 
  core combat mechanics like receiving damage and executing standard attacks. Damage is 
  calculated dynamically using the 'random' library based on the character's level.
- Hero (Child Class): Inherits from Character, adding a 'skill' attribute and a 
  'special_attack' method that yields higher randomized damage.
- Enemy (Child Class): Inherits from Character, adding a 'type' attribute.
- Game (Orchestrator Class): Manages the battle flow. It presents a menu for the user 
  to choose their attack type, processes the enemy's counter-attack, and loops until 
  one of the characters' life points reaches exactly 0.000.
"""

import random

class Character:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name

  def get_life(self):
      return self.__life

  def get_level(self):
     return self.__level

  def show_details(self):
     return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"

  def come_under_attack(self, damage):
     self.__life -= damage
     if self.__life < 0:
        self.__life = 0

  def attack(self, target):
     damage = random.randint(self.get_level() * 2, self.get_level() * 4) # based on the level 
     target.come_under_attack(damage)
     print(f"{self.get_name()} attacked {target.get_name()} and caused {damage} of damage!")


class Hero(Character):
   def __init__(self, name, life, level, skill):
      super().__init__(name, life, level)
      self.__skill = skill

   def get_skill(self):
      return self.__skill

   def show_details(self):
      return f"{super().show_details()}\nSkill: {self.get_skill()}\n"


   def special_attack(self, target):
      damage = random.randint(self.get_level() * 5, self.get_level() * 8) # Damage increased
      target.come_under_attack(damage)
      print(f"{self.get_name()} used special skill {self.get_skill()} in {target.get_name()} and caused {damage} of damage!")
      


class Enemy(Character):
   def __init__(self, name, life, level, type):
      super().__init__(name, life, level)
      self.__type = type

   def get_type(self):
      return self.__type


   def show_details(self):
      return f"{super().show_details()}\nType: {self.get_type()}\n"



class Game:
   """ Game orchestrator class """

   def __init__(self) -> None:
      self.hero = Hero(name="Hero", life=100, level=5, skill="Super Power")
      self.enemy = Enemy(name="bat", life=100, level=5, type="flying")

   def start_batlle(self):
      """ Manage the turn-based battle """
      print("Starting the battle!")

      while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
         print("\nCharacteres Details:")
         print(self.hero.show_details())
         print(self.enemy.show_details())

         input("Press enter to attack...")
         choice = input("Choose (1 - Normal Attack, 2 - Especial Attack):")


         if choice == '1':
            self.hero.attack(self.enemy)

         elif choice == '2':
            self.hero.special_attack(self.enemy)

         else:
            print("You entered an invalid option! Try again.")


         if self.enemy.get_life() > 0:
            # Enemy attacks Hero
            self.enemy.attack(self.hero)



      if self.hero.get_life() > 0:
         print("\nCongratulations, you won the battle!")
      else:
          print("\nYou lost!")



# Create the game instance and start the battle
game = Game()
game.start_batlle()

