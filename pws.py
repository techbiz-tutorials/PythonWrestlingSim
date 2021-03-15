# Randomly select 2 wrestlers from a roster
# Wrestlers have specific strengths and weakness
# Wrestlers roll to see who attacks
# Rock-Paper-Scissors type strategy
# Wrestler wins when opponent runs out of hp
from random import randint
import random
import time
print("******************************************")
print("Welcome to the Python Wrestling Simulator!")
print("******************************************")

# Wrestler attribute key ["Wrestler Name", HP, Off, Spd]
Thor = ["Thor Odinson",110, 110, 110 ]
Hulk = ["Hulk Hogan", 100,70,20]
Undertaker = ["The Undertaker", 80, 60, 20]
Sarge = ["Sgt. Slaughter", 80,50,50]
Giant = ["Andre the Giant", 100, 80, 20]
Mankind = ["Mankind", 80, 40, 40]
Dolph = ["Dolph Ziggler", 60, 70, 70]
Rock = ["The Rock", 60,60,60]
Bryan = ["Daniel Bryan", 60, 50, 60 ]
Mysterio = ["Mysterio", 20, 60, 100]
Glass = ["Glass Joe", 10, 10, 10]

roster = [Rock, Hulk, Sarge, Glass, Mysterio, Thor, Undertaker, Giant, Mankind, Dolph, Bryan ]

moves = ["punch", "kick", "spear","throw", "claymore", "full nelson","pile driver", "irish whip", "back breaker", "brain buster",
         "choke slam", "clothesline", "RKO", "face buster", "arm wringer", "atomic drop", "german suplex", "slap"]
moves2 = ["punched", "kicked", "speared","threw", "claymored", "full nelsoned","pile drove", "irish whipped", "back broke", "brain busted",
         "choke slammed", "clotheslined", "RKOed", "face busted", "arm wrang", "atomic dropped", "german suplexed", "slapped"]
result = ["pin", "submission", "disqualification", "knock-out"]

commentary = ["That's gonna leave a mark!", "This one is over!", "How is he still standing?", "Oh the humanity!",
              "Oh the fans loved that one!", "The fans are not happy about that one!"]

counter = 0

# Start the match
begin = input("Are you ready to begin? y or n?")
if begin.lower()== "y":
    print("Tonight's contest is between:")
    contestant1 = random.choice(roster)
    roster.remove(contestant1)
    contestant2 = random.choice(roster)
    print(contestant1[0],"vs.",contestant2[0])
    tie = ["The wrestlers circle each other.", "The wrestlers size each other up.", "Emotions are running high.",
           "Things are getting intense.", "Listen to that crowd!", "This match could go either way",
           contestant1[0] + " taunts " + contestant2[0], contestant2[0] + " taunts " + contestant1[0],
           contestant1[0]+" gets distracted", contestant1[0]+" argues with the official",
           contestant2[0]+" gets distracted", contestant2[0]+" argues with the official",
           contestant1[0]+" goes for the pin but "+contestant2[0]+" kicks out",
           contestant2[0]+" goes for the pin but "+contestant1[0]+" kicks out"]
    time.sleep(4)
    print("LET'S GET READY TO RUMBLE!!!")
    print("******************************************")
    time.sleep(4)

    # Combat loop
    while contestant1[1] > 0 and contestant2[1] > 0:
        contestant1roll = randint(0,3)
        contestant2roll = randint(0,3)
        # Contestant 1 attacks
        if contestant1roll > contestant2roll:
            contestant1roll = randint(0, contestant1[2])
            contestant2roll = randint(0, contestant2[3])
            # Contestant 1 successfully attacks
            if contestant1roll > contestant2roll:
                print(contestant1[0], random.choice(moves2), contestant2[0]+"!")
                contestant2[1] = (contestant2[1] - randint(1,10))
                print(random.choice(commentary))
                if contestant2[1] <= 0:
                    print("******************************************")
                    print(contestant1[0], "wins by", random.choice(result)+"!")
                    print("A winner is you!")
            # Contestant 1 unsuccessfully attacks
            else:
                print(contestant2[0], "countered", contestant1[0]+"'s",random.choice(moves)+"!")
                contestant1[1] = (contestant1[1] - randint(1, 5))
                print(random.choice(commentary))
                if contestant1[1] <= 0:
                    print("******************************************")
                    print(contestant2[0], "wins by", random.choice(result)+"!")
                    print("A winner is you!")
        # Contestant 2 attacks
        elif contestant2roll > contestant1roll:
            contestant1roll = randint(0, contestant1[3])
            contestant2roll = randint(0, contestant2[2])
            # Contestant 2 successfully attacks
            if contestant2roll > contestant1roll:
                print(contestant2[0], random.choice(moves2), contestant1[0]+"!")
                contestant1[1] = (contestant1[1] - randint(1,10))
                print(random.choice(commentary))
                if contestant1[1] <= 0:
                    print("******************************************")
                    print(contestant2[0], "wins by", random.choice(result)+"!")
                    print("A winner is you!")
            # Contestant 2 unsuccessfully attacks
            else:
                print(contestant1[0], "countered", contestant2[0]+"'s",random.choice(moves)+"!")
                contestant2[1] = (contestant2[1] - randint(1, 5))
                print(random.choice(commentary))
                if contestant2[1] <= 0:
                    print("******************************************")
                    print(contestant1[0], "wins by", random.choice(result)+"!")
                    print("A winner is you!")
        else:
            print(random.choice(tie))
        counter = counter+1
        time.sleep(2)

# Program has ended
if counter > 40:
    print("Wow, what an epic battle!")
elif counter > 5:
    print("We hope you enjoyed the match!")
elif counter > 1:
    print("Wow, that was over before it started!")
print("Please drive home safely.")
