class GameCharacter:

    def __init__(self):
        self.__health = 100
        self.__energy = 50

    # Protected methods for child classes
    def _get_health(self):
        return self.__health

    def _set_health(self, health):
        self.__health = health

    def _get_energy(self):
        return self.__energy

    def _set_energy(self, energy):
        self.__energy = energy

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
        else:
            print("Not enough energy!")

    def take_damage(self, amount):
        self.__health -= amount

        if self.__health < 0:
            self.__health = 0

    def get_status(self):
        return f"Health: {self.__health}, Energy: {self.__energy}"


class Warrior(GameCharacter):

    def attack(self):
        super().attack()
        print("Warrior performs a heavy attack!")


class Mage(GameCharacter):

    def attack(self):
        if self._get_energy() >= 20:
            self._set_energy(self._get_energy() - 20)
            print("Mage casts a spell!")
        else:
            print("Not enough energy for spell!")

    def heal(self, amount):
        new_health = self._get_health() + amount

        if new_health > 100:
            new_health = 100

        self._set_health(new_health)


# Test Code
w = Warrior()
m = Mage()

w.attack()
m.attack()

w.take_damage(30)
m.heal(20)

print(w.get_status())
print(m.get_status())