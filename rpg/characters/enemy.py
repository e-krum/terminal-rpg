import random
from rpg.actions.action import Action
from rpg.characters.entity import Entity

class Dog(Entity):
    def __init__(self):
        actions = [Action.ATTACK, Action.DODGE]
        health = random.randint(1,4) + 1
        print('*GRRRR* *WOOOOF WOOF*')
        super().__init__(f'Dog', actions, health, 4, 4, 0, 0)

    def kill(self):
        print('''*Dog dies*\n*whimper*''')
    
    def act(self, target=0):
        action = super().act()
        if action == Action.ATTACK: return (action, self.attack(), 0)
        else: return (action, self.mitigate(), target)

class Bandit(Entity):
    def __init__(self):
        actions = [Action.ATTACK, Action.BLOCK, Action.HEAL]
        health = random.randint(1,6) + 2
        print('Well, well, wot do we have \'ere')
        super().__init__(f'Bandit', actions, health, 4, 4, 1, 2)

    def kill(self):
        print('''*Bandit dies*\nAuugh!! Ye'll p-pay... for this...''')

    def act(self, target=0):
        action = super().act()
        if action == Action.ATTACK: return (Action.ATTACK, self.attack(), 0)
        elif action == Action.BLOCK: return (Action.BLOCK, self.mitigate(), target)
        else: return (Action.HEAL, self.healing(), target)

class Ranger(Entity):
    def __init__(self):
        actions = [Action.ATTACK, Action.DODGE]
        health = random.randint(1,4) + 1
        print('*Craaaack* So much for the surprise')
        super().__init__(f'Ranger', actions, health, 6, 4, 0, 0)

    def kill(self):
        print('''*Ranger dies*\nThought was... more 'idden than... that''')

    def act(self, target=0):
        action = super().act()
        if action == Action.ATTACK: return (action, self.attack(), 0)
        else: return (action, self.mitigate(), target)

class Chief(Entity):
    def __init__(self):
        actions = [Action.ATTACK, Action.BLOCK, Action.HEAL]
        health = random.randint(2,12) + 2
        potions = random.randint(1,2)
        print('Look \'hos tryin\' be a \'ero ')
        super().__init__('Chief', actions, health, 8, 6, potions, 4)

    def kill(self):
        print('''*Chief dies*\nY... Ye tink... ye've won? That damned town wi... will burn soon 'enough.''')

    def act(self, target=0):
        action = super().act()
        if action == Action.ATTACK: return (Action.ATTACK, self.attack(), 0)
        elif action == Action.BLOCK: return (Action.BLOCK, self.mitigate(), target)
        else: return (Action.HEAL, self.healing(), target)