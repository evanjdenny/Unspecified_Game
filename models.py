from random import randint

class Damage:
    """Damage system."""
    def __init__(self, MIN, MAX):
        self.MIN = MIN
        self.MAX = MAX
        self.RANGE = (self.MIN, self.MAX)
        self.roll = None

    def roll_dice(self):
        """Randomly select the final damage between the MIN and MAX."""
        self.roll = randint(self.RANGE[0], self.RANGE[1])
        return self.roll

class Heal(Damage):
    pass

class Player:
    """Player model."""
    def __init__(self, name: str):
        self.name = name
        self.health = 50
        self.max_health = 50
        self.mana = 25
        self.max_mana = 25
        self.level = 0
        self.unarmed_damage = Damage(1, 5)
        self.alive = True

    def check_alive(self):
        """Check if health is <= 0 and set alive attribute to False
        if this is the case."""
        if self.health <= 0:
            self.alive = False

    def take_damage(self, damage: Damage):
        """Subtract damage from Player health."""
        self.health -= damage.roll_dice()
        self.check_alive()

    def use_mana(self, spell_name: str, mana: int):
        if self.mana >= mana:
            self.mana -= mana
            print(f'You cast {spell_name} using {mana} mana.')

    def heal(self, amount: int):
        ### EDIT TO INCORPORATE HEAL CLASS ###
        if self.health+amount > self.max_health:
            self.health += (self.health+amount)-self.max_health
        elif self.health+amount <= self.max_health:
            self.health += amount

    def 