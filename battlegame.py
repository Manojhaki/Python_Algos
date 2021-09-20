wizard = "Wizard"
elf = "Elf"
human = "Human"

# Declare hp
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Declare damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

dargon_hp = 300
dargon_damage = 50
character = wizard, elf, human


while(True):  # Declare name

    count = 1
    for x in character:
        print(count, x)
        count += 1
    answer = input("Choose your character:")

    if(answer == "1"):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break

    if(answer == "2"):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage

        break

    if(answer == "3"):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    print("Unknown character")
print("You chose to be:", character)
print("Your health points:", my_hp)
print("Your Damage points:", my_damage)


while(True):
    dargon_hp = dargon_hp - my_damage

    print("The", character, "damaged the Dragon! Now the dragon has ", dargon_hp, "HP")
    if(dargon_hp == 0):
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp-dargon_damage

    print("The Dragon has damaged the", character,
          "! Now the", character, " has", my_hp, "HP")

    if(my_hp == 0):
        print("The", character, "has lost the battle")
        break
