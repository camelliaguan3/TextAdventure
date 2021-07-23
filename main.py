#Text Adventure
print('Created by Camellia and Alondra @ GWC Summer Immersion Program')
start = ''

while start != 'yes':
    start = input('Welcome to the game. Would you like to begin? (yes or no)\n')

    if start == 'yes':
        print('\nAlright, here we go.')
        print('You are standing in a forest. You don\'t know where you are, and the forest stretches infinitely in all directions.')

        choice = input('Type \'left\' to go left and \'right\' to go right.\n')

        while choice != 'left' and choice != 'right':
            choice = input('')

        if choice == 'left':
            print('\nYou go towards your left.')
            print('After walking for a long time, you finally see something other than trees and shrubbery. You come to an ancient ruin that happens to have a doorway to the underground.')

            choice = input('Type \'go inside\' or \'leave\'\n')

            while choice != 'go inside' and choice != 'leave':
                choice = input('')

            if choice == 'go inside':
                print('\nYou walk through the doorway.')
                print('There is a long hallway in front of you and two doorways. One is very bright, and the other is dim.')

                choice = input('Type \'dim\', \'bright\', or \'hallway\'.\n')

                while choice != 'bright' and choice != 'dim' and choice != 'hallway':
                    choice = input('')

                if choice == 'bright':
                    print('\nYou walk into the bright room.')
                    print('As you step through the door, you feel an immense heat. It feels as if your skin is peeling.')
                    print('You have died.\n\n\n\n\n')


                elif choice == 'dim':
                    print('\nYou walk into the dim room.')
                    print('As you step through the door, you see a table with two objects on it: a cup and a plate.')

                    choice = input('Type \'cup\' or \'plate\' to pick it up.\n')

                    while choice != 'cup' and choice != 'plate':
                        choice = input('')

                    if choice == 'cup':
                        print('\nYou pick up the cup.')
                        print('Inside is a silvery liquid. You lift the cup to your lips and take a sip. You feel dizzy and everything gets blurry. Then you feel the cool air around you. You open your eyes, and you are lying down on your bed.')
                        print('You have escaped your dream.\n\n\n\n\n')

                    elif choice == 'plate':
                        print('\nYou pick up the plate.')
                        print('On the plate is a bread roll. You take a bite and immediately your throat closes up. Turns out, you\'re allergic.')
                        print('You have died.\n\n\n\n\n')

                elif choice == 'hallway':
                    print('You continue down the hallway.')
                    print('Seems as if it goes on forever. You continue walking down, and when you realize that the hallway does indeed never end, you try to turn back. Turns out, your legs want to continue walking down.')
                    print('You have died?\n\n\n\n\n')

            elif choice == 'leave':
                print('\nYou decide not to walk through the doorway.')
                print('Instead, you decide to wander around, but you never find your way out of the forest.')
                print('You have died?\n\n\n\n\n')


        elif choice == 'right':
            print('\nYou go towards your right.')
            print('You go deeper into the woods, and it starts to get really creepy. You feel the goosebumps running up and down your arm. You look straight down the path and see a spooky castle. You decide to go towards it. Curiosity gets the best of you and you invite yourself in. You walk around a hallway and see a room that interests you.')

            choice = input('Type \'walk in\' to go inside or \'leave\'.\n')

            while choice != 'walk in' and choice != 'leave':
                choice = input('')

            if choice == 'leave':
                print('\nYou decide to go inside anyways.')

            elif choice == 'walk in':
                print('')

            print('You take a look around and find a bunch of fun treasures. One item in particular catches your eye. An apple, but not just any apple. This is the shiniest, most scrumptious looking apple you\'ve ever seen in your short life. This just reminds you of how hungry you have been the entire time.')

            choice = input('Type \'eat\' or \'don\'t eat \'.\n')

            if choice == 'eat':
                print('\nYou decide to eat the apple.')
                print('You\'re so hungry, you eat it in 3 bites. Wow! That sure was filling. You start to feel a bit funny. You feel like you are floating. You\'re not feeling so good. You slowly start to come back. You appear in the room again. This time, everything looks a bit off. The walls look like they\'re caving in. You look at the floor. There is a random egg in the corner of the room.')

                choice = input('Type \'pick up\' or \'don\'t pick up\'.\n')

                while choice != 'pick up' and choice != 'don\'t pick up':
                    choice = input('')

                if choice == 'pick up':
                    print('\nYou pick up the egg.')
                    print('How random. Who would leave this random egg on the floor? You stare at the egg in your hand. It starts to move. A strange buzzing sound starts to come out of the egg. It\'s only getting worse! You start to panic. You put the egg down out of fear. It begins to crack. How peculiar. The top of the egg cracks off and a small head pops out. It\'s not your ordinary chick. It\'s way weirder than that. It\'s purple and it has...TEN HEADS?! It starts to move and you scream like a pansy. It runs out of the room and you foolishly decide to follow it. You follow it outside and back into the forest, and eventually, you arrive at a door. Just a regular door in the middle of the woods. You walk around the door, which somehow is just standing there. What is this creature thinking? The ten headed creature of madness chirps at you using all of its heads. This is the most terrifying moment of your life. It uses its claws to nudge the door open.')
                    print('It looks at you then looks back at the door.')

                    choice = input('Type \'go in\' or \'stay\'.\n')

                    while choice != 'go in' and choice != 'stay':
                        choice = input('')

                    if choice == 'go in':
                        print('\nYou decide to walk in.')
                        print('When you take your first step into the door, you step on empty air. The floor is gone. You shouldn\'t have listened to that egg. You fall into a well. You drop to the bottom of the well and fall to your death.')
                        print('You have died.\n\n\n\n\n')

                    elif choice == 'stay':
                        print('\nYou decide to stay where you are.')
                        print('The creature starts to change color. It becomes a dark red and starts to flash. Suddenly, it starts to grow in size, and you hear a hissing noise. You feel an explosion, but you are able to avoid it. The aftermath of the blast makes you black out.')
                        print('You open your eyes, and you are on your bed. Turns out, it was just a dream.\n\n\n\n\n')

                elif choice == 'don\'t pick up':
                    print('\nYou decide not to pick up the egg.')
                    print('You exit the castle and enter the woods once again. You spend the rest of your life wondering, just what would have happened if you had picked up the egg?')
                    print('You have many regrets and perish.\n\n\n\n\n')

            elif choice == 'don\'t eat':
                print('\nYou decide it\'s wise not to eat the tempting apple.')
                print('You feel your insides start to twist up in a knot. It\'s not a great feeling. You pass out on the floor and you start to black out.')
                print('You have starved to death.\n\n\n\n\n')


    elif start == 'no':
        print('\nOk, bye.')

    else:
        print('\nTry Again.')