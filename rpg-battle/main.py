from classes.game import Person, bcolors
from classes.magic import Spell

#black magic

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("thunder", 10, 100, "black")
blizzard = Spell("blizzard", 10, 100, "black")
meteor = Spell("meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")


#white magic

cure = Spell("Cure", 12, 120, "white")
redemption = Spell("Redemption", 18, 200, "white")


## basic damage list but now commented because it will be inside player/enemy classes

# magic = [{"name": "Fire", "cost": 10, "dmg": 100},
#         {"name": "Thunder", "cost": 10, "dmg": 1240},
#         {"name": "Blizzard", "cost": 10, "dmg": 100}]


player = Person(460, 65 , 60, 34, [fire, thunder, blizzard, meteor, cure, redemption])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
# while running:
#     print("Lets overflow this stack.", i)
#     i += 1

#attacks and stats
while running:
    print("===============")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1


        #basic and long 
        # magic_dmg = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_mp_cost(magic_choice)
    #### NEW #####
        spell = player.magic[magic_choice]
        # magic_dmg = player.magic[magic_choice].generate_damage() THIS IS THE LONG TYPE
        magic_dmg = spell.generate_damage()


        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.Fail + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)


    enemy_choice = 1

    #display stats

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg,)

    print("---------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
    # running = False
# print(player.generate_spell_damage(0))
# print(player.generate_spell_damage(1))



# print(player.generate_damage())
# print(player.generate_damage())
# print(player.generate_damage())