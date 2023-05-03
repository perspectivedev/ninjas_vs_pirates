from classes.wookie import Wookie

class Pirate(Wookie):

    def __init__(self, name, strength, speed, health, moxie, agility, buff, special, has_growl=False, has_blaster=False, has_droid=False):
        super().__init__(name, strength, speed, health, moxie, agility, buff, special)
        self.has_growl = has_growl 
        self.has_blaster = has_blaster
        self.has_droid = has_droid

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nHook: {self.has_hook}\nPatch: {self.has_patch}\nParrot: {self.has_parrot}\n")

    def attack ( self , target ):
        super().cool_down()
        damage = self.strength
        msg = f"{self.name} attacks {target.name}."
        if self.has_growl:
            msg += f" Ghrrrr!"
            damage += 5
        if self.has_driod:
            msg += f" Beep-dot-doo!"
            damage += 3
        target.health -= damage
        return self

    def use_special(self, target):
        super().cool_down()
        if super().cool_down_amount > 0:
            return self
        if self.has_growl:
            msg += f"  Ghrrrr!"
            damage += 5
        if self.has_droid:
            msg += f" Beep-dot-doo!"
            damage += 3
        return self