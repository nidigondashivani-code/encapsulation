class GameCharacter:
    def __init__(self,health=100,energy=50):
        self.__health=health
        self.__energy=energy
    
    def attack(self):
        if self.__energy>=10:
            self.__energy-=10
            print("Attacking with power")
        else:
            print("Not enough energy to attack.")

    def take_damage(self,amount):
        self.__health -= amount
        if self.__health<0:
            self.__health=0
    def get_status(self):
        return f"Health:{self.__health},{self.__energy}"
    
    def get_energy(self):
        return self.__energy
    
    def get_health(self):
        return self.__health
    
    def set_energy(self,energy):
        self.__energy=energy

    def set_health(self,health):
        self.__health=health

class Warrior(GameCharacter):

    def attack(self):
        super().attack()
        print("Warrior's attack is powerful!")
class Mage(GameCharacter):
    def attack(self):
        if self.get_energy()>=20:
            self.set_energy(self.get_energy()-20)
            print("Mage's attack is magical!")
        else:
            print("Not enough energy to attack.")
    def heal(self,amount):
        new_health=self.get_health()+amount

        if new_health>100:
            new_health=100
        self.set_health(new_health)

w=Warrior()
m=Mage()
w.attack()
m.attack()
w.take_damage(30)
m.heal(20)
print(w.get_status())
print(m.get_status())
