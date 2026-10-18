# Variables
state = "escape"
bed_inspected = False
toilet_inspected = False
bars_inspected = False
cell_completed = False
guard_info = False
prisoner_info = False
helper_note_found = False
cell_block_intro_seen = False
yard_searched = False
door_found = False
code_entered = False
cameras_inspected = False
computer_inspected = False
security_panel_inspected = False
room_searched = False


#Chapter 1 - The first clue - the puzzle pieces are in your hands
while True:
    if state == "cell":
        print("\nYou open your eyes to a bright light above you.")
        print ("You sit up and realize you are in a jail cell and the only thing on your mind is to escape, and fast")
        print("You need to get out")
        print("\n\nYour options are:")

        print("\ninspect bed")
        print("inspect toilet")
        print("look through the bars")
        print("go to cell block")
        print("\n*hint: remember to keep note of your clues*")
        feeling = input("\nWhat do you want to do?").strip().lower()

        if feeling == "inspect bed":
            state = "inspect bed"
        elif feeling == "inspect toilet":
            state = "inspect toilet"
        elif feeling == "look through the bars":
            state = "look through the bars"
        elif feeling == "go to cell block":
            if bed_inspected and toilet_inspected and bars_inspected:
                cell_completed = True
                state = "cell block"
            else:
                print("\nYou are not ready to leave yet!")
                print("Inspect your bed, toilet, and bars first.")
        else:
            print("Invalid input. Please choose one of the options above.")




    # inspect bed
    elif state == "inspect bed":
        print("\nYou walk over to the bed and lift the thin mattress.")
        print("Underneath, you discover a loose floor tile.")
        print("You lift the tile and find a small piece of metal.")
        print("There is a triangle etched into the metal")
        print("It might be useful for escaping later.")
        print("You put the metal piece in your pocket.")

        bed_inspected = True
        feeling = input("Type 'return' to go back to your cell: ").strip().lower()

        if feeling == "return":
                state = "cell"
        else:
            print("Invalid input. Type 'return' to go back.")
            state = "inspect bed"

    # inspect toilet
    elif state == "inspect toilet":
        print("\nYou approach the toilet and inspect it carefully.")
        print("Something catches your eye near the base.")
        print("You find a tiny piece of paper folded behind it.")
        print("The paper has the number 1738 written on it.")
        print("You decide to remember the number. It could be a code.")

        toilet_inspected = True
        feeling = input("Type 'return' to go back to your cell: ").strip().lower()

        if feeling == "return":
            state = "cell"
        else:
            print("Invalid input. Type 'return' to go back.")
            state = "inspect toilet"

    #look through bars
    elif state == "look through the bars":
        print("\nYou carefully look through the bars of your cell.")
        print("You see a long hallway with several other cells.")
        print("You take a look and notice that there is a camera directly facing your cell.")
        print("You feel a bit uncomfortable, but you eventually shrug it off.")
        print("You need to be careful if you want to escape unnoticed.")

        print("Your Options are")
        print("return to cell")
        print("go to cell block")

        bars_inspected = True
        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "return to cell":
            state = "cell"

        elif feeling == "go to cell block":
            if bed_inspected and toilet_inspected and bars_inspected:
                cell_completed = True
                state = "cell block"
            else:
                print("You are not ready to leave yet!")
                print("You must inspect your bed and toilet first.")
                state = "cell"

        else:
            print("Invalid input. Please choose one of the options above.")


    elif state == "cell block":
        if cell_block_intro_seen == False:
            print("\nIt is dayroom time")
            print("Your cell is unlocked and you are free to move around")
            print("The noise levels increase and you begin to realize how packed the prison is")
            print("\nAs you roam around looking at guard and camera stations, a group asks you to join them")
            print("You hesitate, but the bigger prisoner comes closer towards you with a sharp object pointed at your stomach")
            print("You have no choice but to follow along.")
            print("\nThe 'leader' observes you")
            print("'You're new here, aren't you?' he asks.")
            print("You nod, wondering how he knows.")
            print("'Funny thing about this place is that the walls hide more than people realize.")
            print("You stare at him, unsure what he means.")
            print("\nHe takes a look towards the cameras before looking back at you.")
            print("'You must've seen the code. Hold it close.'")
            print("Your stomach drops. You never told anyone about the number.")
            print("'How do you know about that?' you ask.")
            print("He smiles slightly but doesn't answer.")
            print("\n'Listen carefully,' he continues.")
            print("'Not every locked door is meant to stay locked.'")
            print("Before you can ask what he means, a buzzer sounds.")
            print("The prisoners begin making their way towards the cafeteria.")
            print("'As he walks away, you watch him disappear into the crowd, wondering how much he knows.")
            print("You watch him disappear into the crowd, wondering how much he knows.")
            cell_block_intro_seen = True

        print("\nYour options are:")
        print("\nobserve guards")
        print("talk to prisoner")
        print("go to cafeteria")
        print("return to cell")


        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "observe guards":
            print("\nYou watch a guard walking past your cell block.")
            print("He looks back at you and stares.")
            print("You stare back and he walks away")
            print("You also notice the color of his uniform and the keys by his belt *keep that in mind'")
            guard_info = True

        elif feeling == "talk to prisoner":
            print("You approach a prisoner sitting by the wall.")
            print("'Be careful in the cafeteria,' he whispers.")
            print("'Not everyone there is on your side.'")
            prisoner_info = True

        elif feeling == "go to cafeteria":
            state = "cafeteria"

        elif feeling == "return to cell":
            state = "cell"

        else:
            print("Invalid input. Please choose one of the options above.")

    elif state == "cafeteria":
        print("\nYou enter the crowded prison cafeteria.")
        print("Prisoners sit at long metal tables while guards patrol the room.")
        print("You find an empty seat and place your food tray on the table.")
        print("A few seats away, an older prisoner sits alone.")
        print("He seems unusually calm compared to everyone else.")

        print("\nYour options are:")
        print("\ninspect food tray")
        print("observe older prisoner")
        print("return to cell block")
        print("go to visitation")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "inspect food tray":
            if helper_note_found == False:
                print("\nYou move your tray and notice a folded piece of paper underneath.")
                print("It reads '1738'. Remember this.")
                print("It's the second time you have seen this number, except it was given to you")
                print("You look around, wondering who left the message.")
                helper_note_found = True
            else:
                print("\nYou check beneath your tray again, but find nothing else.")

        elif feeling == "observe older prisoner":
            print("\nYou glance at the older prisoner sitting nearby.")
            print("He catches your eye, then calmly looks away.")
            print("A moment later, he stands and walks past your table.")
            print("'Stop looking around,' he whispers. 'You'll make yourself a target.'")
            print("Before you can ask what he means, he disappears into the crowd.")

        elif feeling == "go to visitation":
            state = "visitation"

        elif feeling == "return to cell":
            state = "cell"

        elif feeling == "go to cafeteria":
            state = "cafeteria"

        else:
            print("Invalid input. Please choose one of the options above.")

    elif state == "visitation":
        print("\nYou were called down to the visitation room.")
        print("You go in and see the room is empty, but there is a folder on the table.")
        print("You don't open it, but a couple minutes in silence keeps you curious.")
        print("In the folder it says: 'Check the laundry room.'")
        print("\n\nYour Options are:")
        print("go back to cell block")
        print("go to laundry room")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "return to cell block":
            state = "cell block"

        elif feeling == "go to laundry room":
            state = "laundry room"

        else:
            print("Invalid input. Please choose one of the options above.")

    elif state == "prison yard":
        print("\nYou step into the prison yard.")
        print("Prisoners walk around while guards watch from above.")
        print("You notice a tall fence and several buildings nearby.")
        print("\nWhat do you want to do?")
        print("search for a locked door")
        print("roam around the yard")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "search for a locked door":
            door_found = True
            print("\nYou discover a locked metal door")
            print("A keypad is attached to the wall.")

            code = input("Enter the four-digit code: ").strip()

            if code == "1738":
                code_entered = True
                print("\nThe keypad flashes green.")
                print("The door unlocks")
                print("You step inside the maintenance room.")
                state = "maintenance"

            else:
                print("The keypad flashes red.")
                print("Incorrect code. The door remains locked.")

        elif feeling == "roam around the yard":
            yard_searched = True
            print("\nYou walk around the yard, searching for anything useful.")
            print("You check the fences, benches, and corners of the yard.")
            print("Unfortunately, you find nothing that could help you escape.")
            print("You decide to keep searching the yard.")

        else:
            print("Invalid input. Please choose one of the options above.")
    # Both chapter 2 & 3 are in the same day.
    # Chapter 2
    elif state == "laundry room":
        print("\nYou enter the laundry room.")
        print("The machines are loud, and piles of prison uniforms cover the tables.")
        print("You remember the message from the folder in the visitation room.")
        print("You search through the uniforms and discover a guard uniform with keys.")
        print("You change into it and disguise as a worker at the prison.")
        print("There is a note in the pocket: ' find your way to the yard ")
        print("Type 'go to prison yard' to continue.")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "go to prison yard":
            state = "prison yard"

        else:
            print("Invalid input. Please choose one of the options above.")
    elif state == "maintenance":
        print("\nYou enter the maintenance room.")
        print("At the far end, there is a locked door leading to the control room.")
        print("A keypad beside the door asks you to enter a symbol.")
        print("\nYour options are:")
        print("triangle")
        print("square")
        print("circle")

        feeling = input("Which symbol do you choose? ").strip().lower()

        if feeling == "triangle":
            print("\nThe panel recognizes the symbol.")
            print("control room door unlocks.")
            print("You step inside.")
            state = "control room"

        elif feeling == "square":
            print("\nThe panel flashes red.")
            print("Incorrect symbol. The door remains locked.")

        elif feeling == "circle":
            print("\nThe panel flashes red.")
            print("Incorrect symbol. The door remains locked.")

        else:
            print("Invalid input. Please choose one of the symbols above.")
    elif state == "control room":
        print("\nYou are now in the Control Room")
        print("You enter the control room.")
        print("Monitors cover the walls, showing different parts of the prison")
        print("You need to find a way out.")

        print("\nInspect prison cameras")
        print("Inspect main computer")
        print("Inspect security panel")
        print("Search the room")
        print("Return to cell block")
        print("*you must inspect everywhere else before searching the room*")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "inspect prison cameras":
            print("\nYou scroll through the camera feeds.")
            print("You see the cafeteria, visitation room, and prison yard.")
            print("Then you find a camera feed showing your cell.")
            print("Someone has been watching you closely.")
            cameras_inspected = True

        elif feeling == "inspect main computer":
            print("\nThe computer displays prison records and camera logs.")
            print("You notice a section labelled 'RESTRICTED FILES'.")
            print("Access denied. You need further information.")
            computer_inspected = True

        elif feeling == "inspect security panel":
            print("\nThe panel controls the prison's security system.")
            print("You notice a strange symbol beside the controls.")
            security_panel_inspected = True

        elif feeling == "search the room":
            if cameras_inspected and computer_inspected and security_panel_inspected:
                print("\nYou search behind the monitors and under the desk.")
                print("You notice that the camera footage, computer records,")
                print("and security panel all point to the same wall.")
                print("You move a loose panel and discover a hidden doorway.")
                print("You have found the secret office.")
                state = "secret office"

            else:
                print("\nYou search the room but find nothing unusual.")
                print("You should inspect everything in the control room first.")

        elif feeling == "return to the cell block":
            state = "cell block"

        else:
            print("Invalid input. Please choose one of the actions described above.")

    # Chapter 3
    elif state == "secret office":
        print("You enter the hidden room.")
        print("Files cover the desks, and monitors line the walls.")
        print("One monitor shows a live camera feed of your cell.")
        print("Someone has been watching you this entire time.")
        print("\nYou can search the new room or gather information.")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "search the new room":
            print("\nYou search through the files and monitors.")
            print("You discover records of your movements throughout the prison.")
            print("The camera footage shows a mysterious figure entering your cell.")
            print("You find notes about the clues you discovered.")
            print("One note reads: 'You are closer than you think. Trust no one.'")
            print("\nWho has been helping you this whole time?")
            room_searched = True

        elif feeling == "gather information":
            if room_searched:
                print("\nYou gather the files, notes, and camera footage.")
                print("You discover a map showing a possible escape route.")
                print("Suddenly, you hear footsteps approaching.")
                print("You grab the files and hurry toward the exit.")
                state = "escape"

            else:
                print("You should search the room before gathering information.")

        elif feeling == "time to escape":
            state = "escape"

        else:
            print("Invalid input. Please choose one of the actions described above.")
    elif state == "escape":
        print("You follow the map through the prison's service passages.")
        print("You notice footsteps behind you and as you pass through, and it continues to get louder.")
        print("You finally reach a locked exit door.")
        print("\nYour options are:")
        print("inspect the door")
        print("attempt to escape")

        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "inspect the door":
            print("\nYou examine the door and notice a keypad.")
            print("Beside it is a message:")
            print("'You may be free but not for long.'")

        elif feeling == "attempt to escape":
            print("\nYou enter the code from your gathered information.")
            print("The door unlocks.")
            print("You step outside into the cold night air.")
            print("For the first time in what feels like forever,")
            print("you are no longer surrounded by prison walls.")
            print("\nSuddenly, a car pulls up and the windows go down.")
            print("'I've been waiting for you,' they say.")

            print("You recognize their voice.")
            print("Who has been helping you?")
            print("Can you really trust them?")

            print("\nType 'what now' to see where your freedom leads you")
            feeling = input("What do you want to do? ").strip().lower()
        # add an input
        if feeling == "what now":
            state = "what now"
        else:
            print("Invalid input. Please type the action given to you.")
            continue

    elif state == "what now":
        print("\nYou stand confused")
        print("The shadow in the car says you have two choices")
        print("\n'work for me'")
        print("go and be free")
        print("You know one is a lie but the options is in your hands")
        print("\nYour Options:")
        print("work for him")
        print("run away")
        feeling = input("What do you want to do? ").strip().lower()

        if feeling == "work for him":
            print("\nYou agree to do so")
            print("A bigger man comes behind you and from there everywhere goes black")
            print("You truly realize... you aren't free")
            print("\nTHE PLOT THICKENS")
            print("\nTO BE CONTINUED...")
            break
        elif feeling == "run away":
            print("\nAs you attempt to escape yet again")
            print("You hear a light chuckle, 'Fool' the shadow says")
            print("A gun cocks and  BOW")
            print("down you go...")
            print("\n\nYou were warned and here your 'freedom' ends")
            break
