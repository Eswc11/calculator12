import random
robot = {
    'hp' : 1300,
    'defence' : 120,
    'gun' : 300
}
hero = {
    'hp' : 2000,
    'defence' : 100,
    'gun' : 250,
    'protective_field' : 150,
    'has_shield' : False,
    'adrenaline' : 1,
    'action' : ""
}
def hero_damage():
    damage = hero['gun'] - robot['defence']
    if damage <= 0:
        return 'Damage is weak.Robot does not take damage.'
    else:
        modify_health(robot, -damage)
        return f'Robot take {damage} damage'
def block_hero():
    hero['defence'] += hero['protective_field']
    print('Protective Field is now ON')
def equip_shield():
    if not hero['has_shield']:
        hero['has_shield'] = True
        block_hero()
def remove_shield():
    if hero['has_shield']:
        hero['has_shield'] = False
        hero['defence'] -= hero['protective_field']
        print('Protective Field is now OFF')
def check_probability():
    hit_probability = random.randint(1, 100)
    if hit_probability <= 75:
        return hero_damage()
    else:
        return 'Hero is missed!'
def robot_damage():
    hit_probability = random.randint(1, 4)
    if hit_probability == 1:
        damage = robot['gun'] + 0.3 * robot['gun'] - hero['defence']
        if damage <= 0:
            return 'Damage is weak.Hero does not take damage.'
        else:
            modify_health(hero, -damage)
            return f'Hero take {damage} damage on rocket.'
    if hit_probability == 2:
        chance = random.randint(1, 2)
        if chance == 1:
            damage = robot['gun'] - hero['defence']
            if damage <= 0:
                return 'Damage is weak.Robot does not take damage.'
            else:
                modify_health(hero,-damage)
                return f'Hero take {damage} damage'
        else:
            return 'Robot missed!'
    elif hit_probability == 3:
        damage = robot['gun'] * 2
        if hero['action'] == 'defence':
            return 'Hero block grenade with shield'
        else:
            modify_health(hero, -damage)
            return f'Hero take {damage} damage on grenade.'
    else:
        return 'Robot is not worked'
def display_hero_info():
    return f'Hero has {hero["hp"]} HP and {hero["defence"]} defence.'
def display_robot_info():
    return f'Robot has {robot["hp"]} HP.'
def step_hero():
    choice_hero = ['attack', 'defence','adrenaline', 'pass']
    while True:
        action = input(f'Enter command what do you want to do({choice_hero}) : ').lower().strip()
        if action not in choice_hero:
            print("Invalid command! Try again.")
            continue
        hero['action'] = action
        if action == "attack":
            print(check_probability())
            print(display_robot_info())
            break
        elif action == "defence":
            equip_shield()
            print(display_hero_info())
            break
        elif action == "adrenaline":
            if hero['adrenaline'] > 0:
                modify_health(hero, 500)
                hero['adrenaline'] -= 1
                print("Hero used adrenaline!+500 for HP")
                print(display_hero_info())
                break
            else:
                print('No adrenaline left.Change action.')
                continue
        elif action == "pass":
            print("Hero skipped the turn.")
            break
def step_robot():
    print(robot_damage())
    print(display_hero_info())
def modify_health(person,hp_change):
    person['hp'] += hp_change
    if person['hp'] <= 0:
        person['hp'] = 0
def main():
    while robot['hp'] > 0 and hero['hp'] > 0:
        input("Press Enter to hero step...")
        step_hero()
        if robot['hp'] <= 0:
            print('Robot is dead')
            break
        input("Press Enter to robot step...")
        step_robot()
        remove_shield()
        if hero['hp'] <= 0:
            print('Hero is dead')
            break
main()
int