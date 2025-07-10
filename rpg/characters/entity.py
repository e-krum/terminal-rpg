import random
from rpg.actions.action import Action

class Entity:
    def __init__(self, name, actions, health, damage, mit, potions, heal):
        self.name = name
        self.actions = actions
        self.health = health
        self.damage = damage
        self.mit = mit
        self.potions = potions
        self.heal = heal
        self.max_health = health

    def act(self):
        return self.actions[random.randint(0, len(self.actions)-1)]
    
    def mitigate(self):
        return random.randint(1, self.mit)

    def attack(self):
        return random.randint(1, self.damage)
    
    def healing(self):
        return random.randint(1, self.heal)
    
    def heal_self(self, heal):
        self.health = min(self.health + heal, self.max_health)
        self.potions -= 1
        
        if self.potions <= 0: self.actions.remove(Action.HEAL)
    
    def take_damage(self, damage):
        self.health -= damage

    def alive(self):
        return self.health > 0
    
    def kill(self):
        print(f'{self.type} has been slain.')

    def status(self):
        print(f'{self.name}: {self.health}/{self.max_health}HP')
    
    def resolve(self, *args):
        if len(args) == 0: pass

        damage = 0
        mit = 0
        heal = 0

        for action in args:
            if action[0] == Action.ATTACK: damage = action[1]
            elif action[0] in [Action.BLOCK, Action.DODGE]: mit = action[1]
            else: heal = action[1]
        
        actual_dam = damage - mit
        if actual_dam > 0: 
            self.take_damage(actual_dam)
            print(f'{self.name} hit for {actual_dam}HP')
        elif mit > 0 and damage > 0: print(f'{self.name} mitigated {damage} damage')

        if self.alive() and heal > 0: 
            self.heal_self(heal)
            if self.health != self.max_health: print(f'{self.name} healed {heal}HP')
        elif not self.alive(): self.kill()