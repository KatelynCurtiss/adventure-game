# Katelyn Curtiss
# 25 November 2024
# Adventure Game

#Variables
from time import sleep 
lives = 3
score = 0

rucksack = ["key", "duck", "brush"]

def lives_score():
    print("**********")
    print("You have",lives,"lives left")
    print("Your score is:",score)
    print("**********")

#Welcome

name = input("What is your name:")

print("Welcome",name,"to the adventure!")
print()
print()
lives_score()
print()
sleep(2.0)

#scene1
print("""You awake to the sound of an old crone cooking in her pot.""")
print()   
sleep(1.0)  
print("She is singing an old song about.")
print()
sleep(1.0)
print("....I think she is about to cook you!")

choice1 = input("Press r to run away or e to use magic:")

if choice1 == "r":
    print("The olfd crone catches you and puts you in a the pot")
    lives = lives - 1 #lose a life
else:
    print("You cast a spell on her and she explodes!!")
    score = score + 5 #add 5 to score


    lives_score()

#scene2
print("""You move further into the forest. It is full of strange and worrying noises. What other strange creatures might you encounter?""")
sleep(2.0)
print()

print("You hear a scratching noise")
sleep(2.0)
print()

print("It's getting closer...!")
sleep(2.0)
print()

print("Oh phew! It's just a cute fluffy bunny!")
print()
print()

#choice2

choice2 = input("Press s to stroke it, press k to kill it or press r to run away.")

if choice2 == "s":
    print("The bunny reveals ENORMOUS fangs and bites your head off!")
    lives = lives - 1 #lose a life
elif choice2 == "k":
    print("The bunny reveals ENORMOUS fangs, but you kill it before it can bite you!")
    score = score + 5 # add 5 points
else:
    print("""the bunny is quicker than it looks...
          and before you know it, it hops onto you....
          reveals ENORMOUS fangs and bites your head off! """)
    lives = lives - 1

#scene3
print("Behind you, in the forest, there is a great ROAR!")
print()
sleep(2.0)
print("You begin to run very quickly - fearing for your life")
print()
sleep(1.0)
print("""Up ahead you see anouther house. Unlike the old crone's cottage, it is warm, inviting and rather homely. """)
print()
sleep(1.0)
print("You try the door, but it is locked!")
print()
sleep(1.0)
print("The roaring and footsteps are right behind you. You need to make a quick decision!")
print()
print("Perhaps there is something in your bag which can help?")
print("You look in your rucksack and find:",rucksack)

#choice3

choice3 = input("Press k to use the key, d to release the duck to buy you some time, or b to to throw the brush at the monster")

if choice3 == "k":
    print("To your great luck, the key fits the door, and you fell into the house in the nick of time.")
    score = score + 5 # add 5 to score
    rucksack.remove("key")
elif choice3 == "d":
    print("The duck quaks nervously as you pull it from the bag, but it seems to distract the terrible monster following you")
    score = score + #add 2 to score
    rucksack.remove("duck")
else: 
    print("You throw the brush at the monster, but it bounces off its head and it gobbles you up instead.")
    lives = lives - 1 #lose a life
    rucksack.remove("brush")

    lives_score()

