class GameCharacter:

    def __init__(self):
        self.__health = 100
        self.__energy = 50

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print("Attack performed!")
        else:
            print("Not enough energy!")

    def take_damage(self, amount):
        self.__health -= amount

        if self.__health < 0:
            self.__health = 0

    def heal(self, amount):
        self.__health += amount

        if self.__health > 100:
            self.__health = 100

    def rest(self):
        self.__energy += 20

        if self.__energy > 100:
            self.__energy = 100

    def get_status(self):
        return f"Health: {self.__health}, Energy: {self.__energy}"


# Test Code
hero = GameCharacter()

hero.attack()
hero.attack()
hero.take_damage(30)
hero.heal(20)
hero.rest()

print(hero.get_status())