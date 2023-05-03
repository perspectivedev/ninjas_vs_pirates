from classes.fighter import Fighter

class Pirate(Fighter):

    def __init__(self, name, strength, speed, health, moxie, agility, buff, special, has_hook=False, has_patch=False, has_parrot=False):
        super().__init__(name, strength, speed, health, moxie, agility, buff, special)
        self.has_hook = has_hook
        self.has_patch = has_patch
        self.has_parrot = has_parrot

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nHook: {self.has_hook}\nPatch: {self.has_patch}\nParrot: {self.has_parrot}\n")

    def attack ( self , target ):
        super().cool_down()
        damage = self.strength
        msg = f"{self.name} attacks {target.name}."
        if self.has_hook:
            msg += f" My hook will get you!"
            damage += 5
        if self.has_parrot:
            msg += f" Squack!"
            damage += 3
        target.health -= damage
        return self

    def use_special(self, target):
        super().cool_down()
        if super().cool_down_amount > 0:
            return self
        if self.has_hook:
            msg += f" My hook will get you!"
            damage += 5
        if self.has_parrot:
            msg += f" Sqwak!"
            damage += 3
        return self