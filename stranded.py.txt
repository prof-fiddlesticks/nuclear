#
import time
import random
print("Welcome to the text adventure game, try to survive. Have fun!")
print("This program is made by GEANIUS GAEMES™")
print("Press enter to start playing")
start = input()
inventory = []
if start== "":
    print("Entering World...")
    time.sleep(1)
    print("You are on a distant island and you see nothing except a few trees, fallen logs, and brushes.")
    print("Choice 1: Make a shelter | Choice 2: Gather food")
    choice1 = input("Enter 1 or 2: ")
    if choice1 == "1":
        print("You start to gather some fallen wood and leaves for the shelter and start a fire. You see some berries in the bushes.")
        print("Choice 1: Eat the berries | Choice 2: Starve in the night")
        choice2 = input("Enter 1 or 2: ")
        if choice2 == "1":
            print("You eat the berries and immediately feel bad, you try to rest but die of poisoning.")
            print("Game Over")
        elif choice2 == "2":
            print("You starve in the night and die of starvation.")
            print("Game Over")

    elif choice1 == "2":
        print("You try to catch fish with your bare hands, you end up catching two small tropical fish, you eat one of it and keep the other in your inventory.")
        inventory.append("Tropical fish")
        print(f"Your inventory: {inventory}")
        print("You see a hut in the distance with its lights on")
        print("Choice 1: Go to the hut | Choice 2: Sleep on top of a tree")
        choice3 = input("Enter 1 or 2: ")
        if choice3 == "1":
            print("You go to the hut and find an old lady, she turns out to be a witch, she casts a spell and you are suddenly in the clouds. You are in heaven, the witch killed you.")
            print("Game Over")
        elif choice3 == "2":
            print("You survived the night uneventfully.")
            print("Choice 1: Explore the island | Choice 2: Try to swim to some land")
            choice4 = input("Enter 1 or 2: ")
            if choice4 == "2":
                print("You swim really far and see no sight of land, run out of energy and drown.")
                print("Game Over")
            elif choice4 == "1":
                print("You find an abandoned hut and a cave.")
                print("Choice 1: Go to the hut | Choice 2: Go to the cave")
                choice5 = input("Enter 1 or 2: ")
                if choice5 == "1":
                    print("You go to the hut and find some food and water. You start to eat and drink to your content and keep some in your inventory.")
                    inventory.append("Food")
                    inventory.append("Water")
                    print(f"Your inventory: {inventory}")
                    print("You suddenly see a ship coming in from the ocean.")
                    print("Choice 1: Go to the ship in hope of civilization | Choice 2: Hide in the forest")
                    choice6 = input("Enter 1 or 2: ")
                    if choice6 == "1":
                        print("You go to the ship and realize that it is a pirate ship, they walk you off the plank and the sharks eat you.")
                        print("Game Over")
                    elif choice6 == "2":
                        print("You hide in the forest while the ship comes closer, you realize that it was a pirate ship all along. Lucky you! It starts to become night.")
                        print("Choice 1: Explore the island more in the night | Choice 2: Sleep in the trees")
                        choice8 = input("Enter 1 or 2: ")
                        if choice8 == "1":
                            print("A lot of demons start to arise in the night, they immediately see you and kill you.")
                            print("Game Over")
                        elif choice8 == "2":
                            print("You sleep in the trees during the night uneventfully. You wake up and think that you can get home with a raft.")
                            print("Choice 1: Try to build a raft | Choice 2: Explore more")
                            choice12=input("Enter 1 or 2:")
                            # make more choices here
                elif choice5 == "2":
                    print("You go to the cave and find extremely rare jewels.")
                    print("Choice 1: Steal the jewels | Choice 2: Go deeper into the cave for more jewels")
                    choice7 = input("Enter 1 or 2: ")
                    if choice7 == "1":
                        print("You steal the jewels and keep them in your inventory while escaping the cave.")
                        inventory.append("Jewels")
                        print(f"Your inventory: {inventory}")
                        print("It starts to become night time")
                        print("Choice 1: Sleep on the trees | Choice 2: Explore the island a bit more in the night")
                        choice9 = input("Enter 1 or 2: ")
                        if choice9 == "2":
                            print("A lot of demons start to arise in the night, they immediately see you and kill you.")
                            print("Game Over")
                        elif choice9 == "1":
                            print("You sleep on the trees and wake up. You find that a monkey stole all your jewels. You lose the jewels from your inventory")
                            inventory.remove("Jewels")
                            print(f"Your inventory: {inventory}")
                            print("The monkey can talk and asks for 20 bananas in return of the precious jewels.")
                            print("Choice 1: Get the bananas | Choice 2: Kill the monkey for the jewels")
                            choice10=input("Enter 1 or 2: ")
                            if choice10=="1":
                              print("You find a banana tree forest about 5 miles away. You also see that a banana guardian is guarding it.")
                              print("Choice 1: Make some weapons to fight the guardian | Choice 2: Try to sneak in | Choice 3: Ask him for bananas")
                              choice11=input("Enter 1,2, or 3: ")
                              if choice11=="1":
                                print("You sharpen some fallen wood logs to damage the guardian and think you are ready. You add them to your inventory.")
                                inventory.append("Sharp Logs")
                                print(f"Your inventory: {inventory}")
                                print("Choice 1 : Go to the banana forest and fight | Choice 2: Get more supplies like armour ")
                                choice12=input("Enter 1 or 2: ")
                                if choice12=="1":
                                  print("You head over to the forest and try to fight him but find that he is much stronger than you. You underprepared")
                                  print("Game over")
                                elif choice12=="2":
                                    print("You pull some bark from the tree and get some sap. You stick them together and make a full set of armour. You add them to your inventory.")
                                    inventory.append(" Bark Armour")
                                    print(f"Your inventory: {inventory}")
                                    print("Choice 1 : Go to the banana forest and fight | Choice 2: Turn on the monkey and kill him because you are currently stronger")
                                    choice13=input("Enter 1 or 2: ")
                                    if choice13=="1":
                                      print("You head over the the forest and get some good hits on him, but he wounds you severly and you retreat.")
                                      print("You need some better weapons and a shield to fight him.")
                                      print("Choice 1: Go back to the guardian and see if you can kill him | Choice 2: Get more gear")
                                      choice14=input("Enter 1 or 2: ")
                                      if choice14=="1":
                                        print("You go back to fight but he immediately kills you.")
                                        print("Game Over")
                                      elif choice14=="2":
                                        print("You make an axe and mine some wood. You make a shield out of wood as its material. You add it to your inventory")
                                        inventory.append("Wood Axe")
                                        inventory.append("Wood Shield")
                                        print(f"Your inventory: {inventory}")
                                        print("""You go back to the forest and fight him, this time more prepared. You hit him with your sharp logs but he breaks them.
                                        You lost your sharp logs. Then you use your wood axe and you barely end up beating him and get the bananas. You add them to your inventory.""")
                                        inventory.append("20 Bananas")
                                        inventory.remove("Sharp Logs")
                                        print(f"Your inventory: {inventory}")
                                    if choice13=="2":
                                      print("You decide to go over to the monkeys now that you are stronger and try to get the jewels back")
                                      print("You head to the monkey's base.")
                                      print("You reach their base and when you enter they immediately suround you on all sides.")
                                      print("You prepare to fight thenm when you hear a dull thunk.")
                                      print("A monkey ")
                              elif choice11=="2":
                                print("You try to sneak in and steal 20 bananas for the monkeys but the guardian hears you and kills you.")
                                print("Game over")
                              elif choice11=="3":
                                  print("You ask the man for 20 bananas. He replies back and asks for a trade. What could you trade?")
                                  print(f"You inventory: {inventory}")
                                  print("Press T to trade with the man.")
                                  print("Press anything else to not trade with him")
                                  trade1=input("Trade:")
                                  if trade1.upper()=="T":
                                    print("You traded your Tropical Fish with the man and he happily gives you more than enough bananas. 10 extra!")
                                    inventory.remove("Tropical fish")
                                    inventory.append("30 Bananas")
                                    print(f"You inventory:{inventory}")
                                    print("Choice 1 : Should you go back to the monkeys and give them 20 of your bananas | Choice 2 : Look for someone else you can trade your bananas with for something else")
                                    choice15=input("Choose 1 or 2")
                                    #add more choices here
                                  else:
                                    print("You decide not to trade with the man. You refuse the trade and walk away.")
                                    print("")
                            if choice10=="2":
                              print("You try to kill some of the monkeys but then 400 monkeys come upon you and drop you off a cliff. ")
                              print("GAME OVER")
                    elif choice7 == "2":
                        print("You go deeper and see a beast protecting it. You try to run away but he kills you.")
                        print("Game Over")
#Ishaan you imported random but never used it