# block scope : 블록({}) 내부에서 선언된 변수는 해당 블록에서만 접근 가능함
# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)