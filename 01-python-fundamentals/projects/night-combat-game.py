"""
Nesta aula, vamos começar a trabalhar em um projeto de um jogo de combate em turno. 
O objetivo é criar as primeiras classes do jogo usando os conhecimentos sobre classes que aprendemos. 
Vamos começar com a classe "Personagem", que será a classe mãe e conterá atributos comuns a todos os personagens, como nome, vida e nível.
Em seguida, criaremos as classes "Herói" e "Inimigo", que herdarão da classe "Personagem". O herói terá um atributo adicional chamado "habilidade", enquanto o inimigo terá um atributo chamado "tipo". 
Também criaremos um método para exibir os detalhes do personagem, que mostrará o nome, vida, nível e habilidade (no caso do herói) ou tipo (no caso do inimigo).

"""


# Character - Main class
# Hero - controlled by the user
# Enemy - user's opponent


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


class Hero(Character):
   def __init__(self, name, life, level, skill):
      super().__init__(name, life, level)
      self.__skill = skill

   def get_skill(self):
      return self.__skill

   def show_details(self):
      return f"{super().show_details()}\nSkill: {self.get_skill()}\n"


class Enemy(Character):
   def __init__(self, name, life, level, type):
      super().__init__(name, life, level)
      self.__type = type

   def get_type(self):
      return self.__type


   def show_details(self):
      return f"{super().show_details()}\nType: {self.get_type()}\n"


hero = Hero(name="Hero", life=100, level=5, skill="Super Power")
print(hero.show_details())

enemy = Enemy(name="bat", life=50, level=3, type="flying")
print(enemy.show_details())