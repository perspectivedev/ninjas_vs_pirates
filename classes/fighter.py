import random

class Fighter:
    
    def __init__(self, name, strength, speed, health, moxie=1, agility=1, buff=None, special=None, cool_down_amount=0):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
        self.moxie = moxie
        self.agility = agility
        self.buff = buff
        self.special = special
        self.cool_down_amount = cool_down_amount
    
    # define attack
    def attack(self, target):
        print(f'{self.name} attacks {target.name}')
        target.defend(self.strength)
        return self
    # define defend
    def defend(self, amount):
        if self.dodge() == True:
            print(f'{self.name} avoided the attack')
            return self
        
        damage = amount - (self.defense)
        if damage < 0:
            self.health -= damage
        return self
    
    # refactor to @classmethod | @staticmethod
    # define dodge
    def dodge(self):
        coin_flip = random.randint(1,2)
        return coin_flip == 1
    # define use_buff
    def use_buff(self):
        raise NotImplementedError
    # define use_special
    def use_special(self, target):
        raise NotImplementedError
    # define heal
    def heal(self):
        self.health += self.moxie * (5)
        return self
    # define cool_down
    def cool_down(self):
        if self.cool_down_amount > 0:
            self.cool_down_amount -= 1 
        return self
    
    # list of trash talk phrases:
    phrases = [
        "You missed me!",
        "You think that hurt?",
        "I must break you",
        "Momma said knock you out!",
        "Dems' fightin wurdz!",
        "Is it hot in here",
        "I smell toast",
        "Your Daddy can't save you!",
        "Billy, don't be a hero",
        "My grannie hits harder than you!",
    ]
    # define trash_talk
    def trash_talk(self):
        rand = random.randint(0, len(self.phrases) - 1)
        self.health += rand
        print(f'{self.phrases[rand]}')
        return self