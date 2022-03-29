import time
import Player
Sword = Player.Items()
Potion = Player.Items()
Gold = Player.Items()
death = False
str = input("Welcome to the RPG Please enter your name : ")
print("Welcome", str, "Are you ready to begin? Press Y if yes Press N if no")
str = input("")
if str == ("N"):
    print("Program closing... You died")
    time.sleep(1)
    quit()
if str == ("Y"):
    print("Ok, Let us begin")

    time.sleep(5)
    print("You wake up near a campfire, in a unfamiliar place. - You Have the following options: \n Sit up \n Sleep\n Inventory")
    str = input("")
    if str == ("Sleep"):
        print("You sleep until you die of old age. GAME OVER!")
        time.sleep(5)
        quit()
    if str == ("Sit up"):
        print("You sit up, In the distance you see a town or small village. ")

    if str == ("freestuff"):
        Player.Items.gold = 100
        Player.Items.sword = 1
        Player.Items.potion = 5

        print("You have entered the secret passkode. You have: ",Player.Items.gold, "Gold")
    if str == ("Inventory"):
        print("You have:",Player.Items.gold, "gold", Player.Items.sword, Player.Items.potion)


