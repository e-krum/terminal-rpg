import random
from rpg.characters.enemy import Dog, Bandit, Ranger, Chief
from rpg.characters.player import Player

def game_loop():
    rounds = random.randint(4,6)
    name = input('Your name, traveler, what is your name? ')
    print(f'\nThe woods are filled with danger, {name}.\nBe prepared for what is to come...')
    separator('_', 15)

    player = create_player(name)
    enemies = []

    while rounds > 0:
        rounds -= 1
        weights = [0.5, 0.5]

        if rounds == 0: enemies.append(create_chief())
        else: 
            random.choices([1,2], weights=weights)
            count = max(1, random.randint(1,2))
            enemies = draw_enemies(count)

        print(f'{len(enemies)} {'enemies' if len(enemies) > 1 else 'enemy'} appeared out of the woods...\n')

        while player != None and len(enemies):
            [enemy.status() for enemy in enemies]
            player.status()

            separator('-', 7)
            is_valid = False
            actions = {}
            while not is_valid:
                is_valid = get_player_action(player, enemies, actions)
            
            for index, enemy in enumerate(enemies):
                enemy_action(actions, index, enemy)
            
            resolve_actions(actions, player, enemies)
            separator('_', 12)
        
        if rounds > 0:
            choice = int(input(f'Encounter cleared.\n1) Rest\n2) Continue\nChoose: '))
            if choice == 1: 
                player.rest()
                weights = calculate_enemy_weighting()
        else: print('*Looks like the leader is dead now. Time to head back to the village*')

# Player and enemy creation
def create_player(name): 
    return Player(name)

def create_chief():
    return Chief()

def draw_enemies(count):
    enemies = []
    for i in range(count):
        enemy_type = random.choices([1,3], weights=[0.45,0.25,0.3])
        if enemy_type == 1: enemies.append(Dog())
        elif enemy_type == 2: enemies.append(Bandit())
        else: enemies.append(Ranger())
    return enemies

# Player and enemy actions
def enemy_action(actions, index, enemy):
    enemy_action = [enemy.act(index + 1)]
    if enemy_action[0][2] == 0:
        actions[0] = actions[0] + enemy_action if actions.get(0) is not None else enemy_action
    else:
        actions[index + 1] = actions[index + 1] + enemy_action if actions.get(index + 1) is not None else enemy_action

def get_player_action(player, enemies, actions):
    player_action = int(input('Your Actions:\n1. Attack\n2. Block\n3. Heal\n'))
    print()
    if player_action == 1: 
        target = get_target(len(enemies)) if len(enemies) > 1 else 1
        actions[target] = [player.act(player_action, target)]
        return True
    elif player_action == 2: 
        actions[0] = [player.act(player_action, 0)]
        return True
    elif player_action == 3: 
        if player.potions <= 0: print('Out of potions')
        else: 
            actions[0] = [player.act(player_action, 0)]
            return True
    else: 
        print('Invalid option')
        return False
    
# Determine player target if more than one enemy
def get_target(count): 
    is_valid = False
    while not is_valid:
        [print(i, end=' ') for i in range(1, count+1)]
        target = int(input('\nWhich target? '))
        print()
        if target >= 1 and target <= count: return target
    
# Resolve actions taken by player and enemies
def resolve_actions(actions, player, enemies): 
    player.resolve(*actions.get(0, []))

    [enemy.resolve(*actions.get(index + 1, [])) for index, enemy in enumerate(enemies)]
    dead = list()
    [dead.append(index) if not enemy.alive() else print() for index, enemy in enumerate(enemies)]
    for index in dead: del enemies[index]

def calculate_enemy_weighting(rested):
    return [0.5, 0.5] if rested else [0.35, 0.65]

def separator(char, count):
    print(char * count)
    print()