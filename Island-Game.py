# This is Open-Source code for the Island Game
# My first programming project
# Let me know if you have any suggestions or improvements

print("Welcome to the Island Game!")
print("You are stranded on a deserted island and need to find a way to survive.")
print("You will face various challenges and make choices that will affect your survival.")
print("\n*Note: this is a text-based game, so please type your choices as prompted.*")

while True:
    first_choice = input("You want to play the game? (yes/no): ").strip().lower()
    if first_choice == "yes" or first_choice == "y":
        print("Great! Let's get started.")
        exit()
    elif first_choice == "no":
        print("Okay, maybe next time. Goodbye!")
        exit()
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

print("\nYou wake up on a deserted island, you know you have an accident after a plane crash.")
print("You have no idea where you are but you must survive.")
while True:
    decision1 = input("You see a beach and a jungle. Where do you want to go? (beach/jungle): ").strip().lower()
    if decision1 == "beach":
        print("\nyou choose to go to the beach.")
        print("You found caves and a boat.")
        while True:
            decision2 = input("Do you want to explore the caves or take the boat? (caves/boat): ").strip().lower()
            if decision2 == "caves" or decision2 == "cave":
                print("\nYou choose to explore the caves and entry the cave.")
                print("You go deeper and deeper and found a lake.")
                while True:
                    decision3 = input("Do you want to search in the lake or continue explore deeper in the cave? (lake/deep): ").strip().lower()
                    if decision3 == "lake":
                        print("\nYou choose to search in the lake.")
                        print("Unfortunately, you found a shark and it attcked you.")
                        print("You died. Game over.")
                        exit()
                    elif decision3 == "deep":
                        print("\nYou continue to explore deeper in the cave.")
                        print("You found a light and you follow it.")
                        print("But before you reach the light, you found another ways to go deeper in the cave.")
                        while True:
                            decision4 = input("Do you want to go deeper or follow the light? (deeper/light): ").strip().lower()
                            if decision4 == "deeper":
                                print("\nYou still want to go deeper in the cave.")
                                print("At the end of the cave, you realize that you already in bunker, the cave was a bunker.")
                                print("You found a radio and note, the note says: Frequency 322 and SOS.")
                                while True:
                                    decision5 = input("What you want to call? (SOS/322): ").strip().lower()
                                    if decision5 == "sos":
                                        print("\nYou call SOS and got response from other people.")
                                        print("They said to wait inside the bunker")
                                        print("A few minutes later, you heard some sounds")
                                        print("You realize that's common sound of explosion")
                                        print("You try to escape but the bunker is already exploded")
                                        print("You died. Game over.")
                                        exit()
                                    elif decision5 == "322":
                                        print("\nYou call 322 and got no response.")
                                        print("You try it many times but still no response.")
                                        print("After that, you want to escape the bunker.")
                                        print("Suddenly, you heard some sounds from radio.")
                                        print("You come back to the radio and listen to it.")
                                        print("That's a voice from the radio, it says: 'Press button on the bottom of the table.'")
                                        print("You press the button and the voice says: 'Wait us'.")
                                        print("A few minutes later, you heard some sounds")
                                        print("You realize that's common sound of helicopter")
                                        print("You escaped the island and you are safe now.")
                                        print("Congratulations! You survived the island!")
                                        exit()
                                    else:
                                        print("\nInvalid input. Please type 'SOS' or '322'.")
                            elif decision4 == "light":
                                print("\nYou choose to follow the light.")
                                print("You running to the light and your emotions are high.")
                                print("But when you reach the light, you realize that's cliff")
                                print("You are want to go back but you heard some sounds from behind you.")
                                print("You are scared and lost balance, you fall off from cliff.")
                                print("You died. Game over.")
                                exit()
                            else:
                                print("\nInvalid input. Please type 'deeper' or 'light'.")
                    else:
                        print("\nInvalid input. Please type 'lake' or 'deep'.")
            elif decision2 == "boat":
                print("\nYou choose to take the boat.")
                print("You try to rowing the boat and you are far from the island.")
                print("But suddenly, you heard some sounds from the sea.")
                print("You look back and see big waves coming towards you.")
                print("You trying your best to rowing the boat but the waves reach you.")
                print("You are lost balance and fall off from the boat.")
                print("You are drowning and you can't move your body.")
                print("You died. Game over.")
                exit()
            else:
                print("\nInvalid input. Please type 'caves' or 'boat'.")
    elif decision1 == "jungle":
        print("\nYou choose to go to the jungle.")
        print("You walk through the jungle with slow pace.")
        while True:
            decision6 = input("You found a river and village. What do you want to do? (river/village): ").strip().lower()
            if decision6 == "river":
                print("\nYou choose to go to the river.")
                print("You are thrirsty and you want to drink some water.")
                print("You drink some water from the river and you feel better.")
                print("But you feel dizzy and suddenly you fall down.")
                print("You died. Game over.")
                exit()
            elif decision6 == "village":
                print("\nYou choose to go to the village.")
                print("This village is abandoned and you are alone.")
                print("You found a unique house and you want to enter it.")
                while True:
                    decision7 = input("Do you want to enter the house or leave it? (enter/leave): ").strip().lower()
                    if decision7 == "enter":
                        print("\nYou choose to enter the house.")
                        print("You realize this house is bigger than you thought.")
                        print("You heard some sounds from outside the house.")
                        print("You scared and hide in the room inside the house.")
                        print("You heard some footsteps and geting closer to your room.")
                        print("You searching around the room.")
                        print("You found hiding spot under the bed and clsoet")
                        while True:
                            decision8 = input("Where do you want to hide? (bed/closet): ").strip().lower()
                            if decision8 == "bed":
                                print("\nYou choose to hide under the bed.")
                                print("You are scared and your heart is beating fast.")
                                print("The door opened and you see a shadow.")
                                print("He is looking for you but didn't find you.")
                                print("He walked away from the room.")
                                print("You are relieved and want to escape the house.")
                                while True:
                                    decision9 = input("Do you want to still hide or get out of the room? (hide/out): ").strip().lower()
                                    if decision9 == "hide":
                                        print("\nYou choose to still hide under the bed.")
                                        print("After a few minutes, he come back to the room.")
                                        print("Just when you thought he left, he found you.")
                                        print("You got killed by him.")
                                        print("You died. Game over.")
                                        exit()
                                    elif decision9 == "out":
                                        print("\nYou choose to get out of the room.")
                                        print("You run away from the room and try to escape the house.")
                                        print("You heard some sounds from behind you.")
                                        print("You think he is chasing you.")
                                        print("You run as fast as you can and finally you reach the door.")
                                        print("You open the door and run away from the house.")
                                        print("You are safe now and you escaped the house.")
                                        print("Suddenly, you heard helicopter sound.")
                                        print("You screamed for help and they heard you.")
                                        print("You are rescued and you survived the island!")
                                        print("Congratulations! You survived the island!")
                                        exit()
                                    else:
                                        print("\nInvalid input. Please type 'hide' or 'out'.")
                            elif decision8 == "closet":
                                print("\nYou choose to hide in the closet.")
                                print("A few seconds later, he opened the door.")
                                print("You can see him through the closet's door.")
                                print("He is looking for you and approaching the closet.")
                                print("You clearly see his face and he is not human.")
                                print("He opened the closet and found you.")
                                print("You got killed by him.")
                                print("You died. Game over.")
                                exit()
                            else:
                                print("\nInvalid input. Please type 'bed' or 'closet'.")
                    elif decision7 == "leave":
                        print("\nYou choose to leave the house.")
                        print("You continue to explore the village.")
                        print("You heard something and someone calling you.")
                        print("You scared and run away.")
                        print("After that, you feel something behund your neck.")
                        print("Your vision is blurry and fade to black.")
                        print("You died. Game over.")
                        exit()
                    else:
                        print("\nInvalid input. Please type 'enter' or 'leave'.")            
            else:
                print("\nInvalid input. Please type 'river' or 'village'.")
    else:
        print("Invalid input. Please type 'beach' or 'jungle'.")

