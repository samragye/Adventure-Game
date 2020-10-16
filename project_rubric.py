import time
import random


def print_sleep(string):
    print(string)
    time.sleep(2)


def ending():
    possible_endings = ["Congrats you made it!", "Yoohoo! Way to go!!",
                        "You rock!"]
    print_sleep(random.choice(possible_endings))


def intro():
    print_sleep("You find yourself in strange, strange place."
                " You are also very weak and severly dehydrated")
    print_sleep("The only thing you can trust is your instinct to survive")
    print_sleep("You can hear a stream nearby")
    print_sleep("You also hear strange howling")
    print_sleep("You also spy a nutritous bush of berries")


def stream(items):

    print_sleep("You are a real survivor! Your first instinct"
                "is absolutely right about finding a clean water source!")
    if "water" in items:
        print_sleep("You have already drunk a lot of water. Remember too"
                    "much water isn't good either!")
    else:
        print_sleep("You drink some clean water and instantly "
                    "feel much much better.")
        items.append("water")
    survive(items)


def berries(items):

    print_sleep("You have now reached the berry bush.")
    if "water" in items:
        print_sleep("You pick the berries and start eating them. "
                    "They are very delicious!")
        items.append("berries")
        survive(items)

    elif "berries" in items:
        print_sleep("Over consuming these berries might not be the "
                    "brightest idea!")
    else:
        print_sleep("You are too parched to swallow any food!")
        survive(items)


def wolf(items):

    print_sleep("You have decided to stare at the face of danger. "
                "Are you prepared?")
    if "water" in items:
        print_sleep("You now are hydrated! But do you have the strength"
                    " to beat the wolf?")
        if "berries" in items:
            print_sleep("Yes you have eaten those powerful berries! "
                        "You defeat the bad wolf! Now you can finally "
                        "focus on how to get home!")
            ending()
            play_again()
        else:
            print_sleep("You are much to weak to kill the wolf!")
            survive(items)
    else:
        print_sleep("You are much to weak to kill the wolf!")
        survive(items)


def survive(items):
    choice = input("Where would you like to go?\n").lower()
    if "stream" in choice:
        stream(items)
    elif "bush" in choice:
        berries(items)
    elif "wolf" in choice:
        wolf(items)
    else:
        print_sleep("I'm sorry, I didn't understand...Try again!")
        survive(items)


def play_again():
    play_again = input("Would you like to play again? "
                       "Please say 'yes' or 'no'.\n").lower()
    if 'no' in play_again:
        print("OK, goodbye!")
        time.sleep(2)
    elif 'yes' in play_again:
        print("Here we go again!")
        time.sleep(2)
        play_game()


def play_game():
    items = []
    intro()
    survive(items)


play_game()
