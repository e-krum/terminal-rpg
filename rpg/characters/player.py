import random
from rpg.actions.action import Action
from rpg.characters.entity import Entity

class Player(Entity):
    def __init__(self, name):
        actions = [Action.ATTACK, Action.BLOCK, Action.HEAL]
        self.rests = 3
        health = random.randint(2,12) + 5
        potions = random.randint(1,4) + 1
        super().__init__(name, actions, health, 6, 6, potions, 4)

    def kill(self):
        if (self.health <= 0):
            print('''I... I may have failed... but ano- another will finish... what I've started...''')
        else: print('Heh... well, seems like this job is done now, pay better be worth it')

    def rest(self):
        if self.rests > 0:
            print(f'{self.name} rests for a moment before continuing on...')
            self.health = self.max_health
            self.rests -= 1
        else: print("No time to rest, must keep moving...")

    def act(self, action, target=0):
        action = Action(action)
        if action == Action.ATTACK: return (Action.ATTACK, self.attack(), target)
        elif action == Action.BLOCK: return (Action.BLOCK, self.mitigate(), target)
        else: return (Action.HEAL, self.healing(), target)

    def status(self):
        print(f'{self.name}: {self.health}/{self.max_health}HP Potions: {self.potions}')