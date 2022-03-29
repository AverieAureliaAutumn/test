import time
import Player
import Items

a = Items.Player()
#b = Items.Player()

#b.illness()
#a.illness()
def movementParser(input):
    input = input.lower()
    match input:
        case "forward":
             return "forward"
        case "backward":
             return "backward"
        case "left":
             return "left"
        case "right":
             return "right"
        case _:
             return "o"
def Inventory(items):
    items.gold = 100
    items.sword = 1
    items.potion = 5
    print("You have:", items.gold, "GOLD",",", items.sword, "METAL SWORDS",",", items.potion, "HEALTH POTIONS")


str = input("Welcome to the RPG Please enter your name : ")
print("Welcome", str, "Are you ready to begin? Press Y if yes Press N if no")
str = input("")
if str == "N":
    print("Program closing... You died")
    time.sleep(1)
    quit()
if str == "Y":
    print("Ok, Let us begin")
    time.sleep(5)
    while True:
        print("You wake up near a campfire, in a unfamiliar place. - You Have the following options:"
              " \n Sit up \n Sleep\n Inventory")

        str = input("")
        if str == "Sleep":
            print("You sleep until you die of old age. GAME OVER!")
            time.sleep(5)
            quit()
            break
        if str == "Inventory":
            Inventory(Items)

        if str == "Sit up":

            print("You sit up, In the distance you see a town or small village. ")
            break