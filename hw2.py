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
}
def hero_damage():
    damage = hero['gun'] - robot['defence']
    if damage <= 0:
        return 'Damage is weak.Robot does not take damage.'
    else:
        modify_health(robot, -damage)
        return f'Robot take {damage} damage'
def check_probability():
    hit_probability = random.randint(1, 100)
    if hit_probability <= 75:
        return hero_damage()
    else:
        return 'Hero is missed!'
def robot_damage():
    hit_probability = random.randint(1, 3)
    if hit_probability == 1:
        damage = robot['gun'] + 0.3 * robot['gun'] - hero['defence']
        if damage <= 0:
            return 'Damage is weak.Hero does not take damage.'
        else:
            modify_health(hero, -damage)
            return f'Hero take {damage} damage'
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
    else:
        return 'Robot is not worked'
def display_hero_info():
    return f'Hero has {hero["hp"]} HP.'
def display_robot_info():
    return f'Robot has {robot["hp"]} HP.'
def step_hero():
    print(check_probability())
    print(display_robot_info())
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
        if hero['hp'] <= 0:
            print('Hero is dead')
            break
main()