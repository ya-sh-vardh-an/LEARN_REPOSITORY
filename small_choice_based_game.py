"""
creating a choice based game
"""
"""from pykeyboard import PyKeyboard
k = PyKeyboard()
k.tap_key(k.numpad_keys[1], n=1)""" # not wokring right now

def area_one(): # this is the starting area
    print("Welcome to Area 1: VOJOPOLIS")
    print("Here you will have to find the key to next room as well a 'Hidden treasure'")
    print("Oh wait.. there is something over there. \nWhat do you choose 'go' over there or 'stay'?")
    choice = input("> ")

    if "go" in choice: # I choose "in" for searching for the same string inside "choice" input if true then will proceed
        print("Be careful there is a Minataur over there.")
        print("The Minotaur looks calm and looking at something.")
        print("What do you wanna do?")
        choice = input("'Fight' or 'go where he is looking' at.. \n> ")

        if "fight" or "go where he is looking" in choice:
            end("You were killed by the Minataur")
        else:
            Minataur_scene()


    elif "stay" in choice:
        print("It's been past 12am. You can go to a new area now. Congrats")
        area_two()
    else:
        end("Uhhh... you died..")

def area_two():
    print("Welcome to Area 2: IOLO")
    print("Oh we have a visitor here who looks suspicious.")
    print("What do you wanna do? 'talk' to the stranger or 'ignore him'.")
    choice = input("> ")
    if "talk" in choice:
        print("Oh the stranger turns into a vampire and attacks you.")
        fight_scene()
    elif "ignore him" in choice:
        end("You ignored him and passed the game congrats")

def fight_scene():
    vampire_hp = 10000
    user_hp = 1200
    print(f"The vampire HP is: {vampire_hp}")
    print(f"Your HP is: {user_hp}")
    print("type 'f' on keypad to fight or type 'run' to run")
    choice = input("> ")
    defeat_vampire = False
    if "f" in choice:
        while True: # here is a while loop it will run till the  one dies
            if "f" in choice:
                vampire_hp = vampire_hp - 1000
                print(f"You attacked vampire the vampire HP now is: {vampire_hp}")
                user_hp = user_hp -20
                print(f"The vampire attacked you your HP now is: {user_hp}")
                choice = input("> ")
                if vampire_hp <= 0:
                    end("Congrats you win!")
                    defeat_vampire = True
                elif user_hp <= 0:
                    end("xp you died.")

    elif "run" in choice:
        end("The vampire caught you and sucked the life outta you!!!")


def Minataur_scene():
    print("Do you wish to return back to Area 1?")
    choice = ("> ")

    if "yes" in choice:
        print("ok..returning back")
        return_back(area_one)
    else:
        end("Staying.......and starving, you died.")

def return_back(towhere):
    towhere()

def end(message):
    print(message, "GOOD JOB!")
    print("Starting game again :)......")
    exit(0)

area_one() # starts from here
