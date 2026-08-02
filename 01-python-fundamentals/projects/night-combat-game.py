"""
Nesta aula, vamos começar a trabalhar em um projeto de um jogo de combate em turno. 
O objetivo é criar as primeiras classes do jogo usando os conhecimentos sobre classes que aprendemos. 
Vamos começar com a classe "Personagem", que será a classe mãe e conterá atributos comuns a todos os personagens, como nome, vida e nível.
Em seguida, criaremos as classes "Herói" e "Inimigo", que herdarão da classe "Personagem". O herói terá um atributo adicional chamado "habilidade", enquanto o inimigo terá um atributo chamado "tipo". 
Também criaremos um método para exibir os detalhes do personagem, que mostrará o nome, vida, nível e habilidade (no caso do herói) ou tipo (no caso do inimigo).

"""


"""
Continuamos trabalhando no projeto do jogo. Criamos a classe "Jogo" para orquestrar a gestão do jogo. 
Adicionamos um método para iniciar a batalha, que acontece em turnos. Utilizamos um loop "while" para continuar a batalha enquanto o herói e o inimigo estiverem vivos. 
Exibimos os detalhes dos personagens e permitimos ao usuário escolher entre um ataque normal ou especial do herói. A batalha continua até que um dos personagens tenha sua vida zerada. 
"""

"""
continuamos a trabalhar na mecânica de combate do jogo. Já implementamos a escolha do usuário entre ataque normal e ataque especial, mas agora precisamos fazer com que esses ataques causem dano ao inimigo e ao herói. 
Para isso, criamos o método "atacar" na classe mãe do personagem, que recebe o alvo como parâmetro. Dentro desse método, calculamos o dano com base no nível do personagem e exibimos uma mensagem informando quem atacou quem e o dano causado.
No entanto, ainda não implementamos o método para decrementar a vida do alvo. Além disso, precisamos implementar a mecânica do inimigo atacando o herói. 
Continuaremos a trabalhar nesses aspectos nas próximas aulas.
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

  def come_under_attack(self, damage):
     self.__life -= damage
     if self.__life < 0:
        self.__life = 0

  def attack(self, target):
     damage = self.__level * 2
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
      self.enemy = Enemy(name="bat", life=50, level=3, type="flying")

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
         else:
            print("You entered an invalid option! Try again.")


      if self.hero.get_life() > 0:
         print("\nCongratulations, you won the battle!")
      else:
          print("\nYou lost!")



# Create the game instance and start the battle
game = Game()
game.start_batlle()

