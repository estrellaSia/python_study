################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()  # '2' 출력
print(f"enemies outside function: {enemies}") # '1' 출력

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)


# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)