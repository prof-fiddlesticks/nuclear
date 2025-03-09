import time

print("Late")
print("A comedy game by Nuclear Technologies")
print()
print("Loading game....")
time.sleep(2)
print()
print("""You wake up in the morning and see that it is 9:55 AM,
        you were supposed to be in the office at 9:00 AM but 
        you partied last night in the club and slept at 1:00 AM.
        You ride your Subaru to the office at 10:11 AM and reach 
        the office at 10:24 AM, your boss asks you why you were
        1 hour and 24 minutes late.""")
print()
print("You have two options, enter 1 or 2")
print("Option 1  Lie to him and say that there was a lot of traffic | Option 2  Tell him the truth")
option1=input("Enter your option: ")
print()
print("Calculating...")
time.sleep(2)
print()

if option1=="1":
  print("""He accepts the excuse and goes back to playing
           War of Thunder on his phone while pretending to
           do work, you sit down and start working. You feel
           a bit thirsty and want to get a drink.""")
  print()
  print("You have two options, enter 1 or 2")
  print("Option 1  Get cofee | Option 2  Get tea")
  option2=input("Enter your option: ")
  print()
  print("Calculating...")
  time.sleep(2)
  print()
  if option2=="1":
    print("""You drink cofee and immidiately feel an energy rush.
                               GAME OVER""")
  elif option2=="2":
      print("""You drink tea and feel refreshed, you go back to 
               your seat and work more, you end up finishing the
               work, you go to your boss and ask him what you 
               should do, he gives you one more task to do, he isn't
               careful and you see that he is playing mobile games, you
               confront him, he gives you $500 and says that you don't have
               to come to work for the whole week if you tell no one.""")
      print()
      print("You have two options, enter 1 or 2")
      print("Option 1  Get the bribe and go home | Option 2 Tell on him")
      option3=input("Enter your option: ")
      print()
      print("Calculating...")
      time.sleep(2)
      print()
      if option3=="1":
        print("""You go home and watch national tv, the USA is preparing
                 for world war 3, boring. You watch a reality show 
                 instead, boring. You decide to watch a movie.
                 When you go to the office after a week, you 
                 blackmail the boss again, this time he gives
                 you a pay raise and a one month leave where you will
                 still be paid.""")
        print()
        print("You have two options, enter 1 or 2")
        print("Option 1  Get the bribe and go home | Option 2  Blackmail him for $100,000")
        option4=input("Enter your option: ")
        print()
        print("Calculating...")
        time.sleep(2)
        print()
        print("The game has stopped here, we are working on coding more.")
      elif option3=="2":
       print("""You tell on him and the boss gets fired, you realize
               that you lost out on a big blackmail oppurtunity.
                                     GAME OVER""")
elif option1=="2":
  print("""The boss fires you and goes back to playing war of thunder
           on his phone while pretending to do work.
                                 GAME OVER""")
