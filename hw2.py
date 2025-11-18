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
        damage = robot['gun'] * 0,3 - hero['defence']
        modify_health(hero, damage)
    if hit_probability == 2:
        chance = random.randint(1, 2)
        if chance == 1:
            damage = robot['gun'] - hero['defence']
            modify_health(hero, damage)
        else:
            return 'Robot missed!'
    else:
        return 'Robot is not worked'
def display_hero_info():
    return f'Hero is {hero["hp"]} HP.'
def display_robot_info():
    return f'Robot has {robot["hp"]} HP.'
def step_hero():
    check_probability()
    display_hero_info()
def step_robot():
    robot_damage()
    display_robot_info()
def modify_health(person,hp_change):
    person['hp'] += hp_change
    if person['hp'] <= 0:
        person['hp'] = 0
def main():
    while robot['hp'] > 0:
        input("Press Enter to continue to next step...")
        step_hero()
    print('Robot is dead')
main()