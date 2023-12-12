#initialize game
import time
import os
import colorama
from colorama import Fore, Back, Style, init

init()  # Initialize colorama

# setup clear screen function
def Clear_Screen():
    os.system('cls')
    time.sleep(2)
    print("remaining health")
    print(str(lives))
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

os.system('cls')

# Initialize starting variables
inventory = ['Dagger', 'RumBottle', 'EMPTY']
lives = 3

# setup inventory function
def print_inventory():
    print('Slot1 =', inventory[0])
    print('Slot2 =', inventory[1])
    print('Slot3 =', inventory[2])

# death function
def Death_Outcome():
    if lives < 1:
        print('you have lost all health')
        time.sleep(3)
        ('you are in an awful condition')
        time.sleep(3)
        print(Fore.RED + 'YOU DIED')
        time.sleep(9999999)

# Title sequence
time.sleep(3)
print('A game by M7135')
time.sleep(3)
os.system('cls')
time.sleep(3)
print('Story by M7135')
time.sleep(3)
os.system('cls')
time.sleep(3)
print('Programmed using Python')
time.sleep(3)
os.system('cls')
time.sleep(3)
print('PizzaSlice Games presents...')
time.sleep(3)
os.system('cls')
time.sleep(3)
print(Fore.RED+'SURVIVE')
time.sleep(3)
os.system('cls')

# Introduction
print(Fore.WHITE+'You wake up on the floor of a dirty tavern.')
time.sleep(2)
print('The smell of death fills the air.')
time.sleep(2)
print('There is no one in sight...')
time.sleep(2)
print('Options:')
print('1. LEAVE THE TAVERN')
print('2. SEARCH')
print('3. INVENTORY')
print('Do not repeat the same command twice; the game will not work.')
choice = input('What do you do: ')

# Process player choice
if choice == 'INVENTORY':
    print_inventory()
    choice = input('What do you do: ')

if choice == 'SEARCH':
    print('You find a couple of arrows.')
    print('Which inventory slot would you like to replace?')
    print_inventory()
    inventory_swap = input('Slot1, Slot2, Slot3: ')

    if inventory_swap in ['Slot1', 'Slot2', 'Slot3']:
        inventory[int(inventory_swap[-1]) - 1] = 'arrows'
        print("You collected arrows.")
        time.sleep(2)
        print('Options:')
        print('1. LEAVE THE TAVERN')
        choice = input('What do you do: ')

if choice == 'LEAVE THE TAVERN':
    print('You leave the tavern.')
    time.sleep(2)
    print('It is dark, and you are afraid.')
    time.sleep(2)
    print('You venture on into the darkness and eventually stumble across a town.')
    time.sleep(3)
    print('The town is abandoned but provides a nice place to hold up for the night.')
    time.sleep(2)
    print('YOU SURVIVED NIGHT 1')
    time.sleep(2)

Clear_Screen()
Death_Outcome()

print('you wake up in the town\'s church, where you set up the previous night')
time.sleep(2)
print('you hear a noise outside and decide to investigate')
time.sleep(2)
print('you look out the window and see a large bear')
time.sleep(2)
print('it is grunting and looking for food')
time.sleep(2)
print('you have to get out of there')
time.sleep(2)
print('You see a bow about 5 meters away.')
time.sleep(2)
print('Which inventory slot would you like to replace?')
print_inventory()
inventory_swap = input('Slot1, Slot2, Slot3: ')

if inventory_swap in ['Slot1', 'Slot2', 'Slot3']:
    inventory[int(inventory_swap[-1]) - 1] = 'bow'
    print("You collected bow.")
    time.sleep(2)
    print('Options:')
    print('1. SHOOT THE BEAR')
    print('2. RUN OUT OF THE CHURCH')
    print('3. HIDE')
    choice = input('What do you do: ')

if choice == 'SHOOT THE BEAR':
    if 'bow' in inventory and 'arrows' in inventory:
        print('You aim your bow at the bear...')
        time.sleep(2)
        print('You release the arrow and hit the bear right in the heart.')
        time.sleep(2)
        print('The bear falls to the ground, defeated.')
        time.sleep(2)
        print('You survived the encounter with the bear.')
        time.sleep(2)
        print('Options:')
        print('2. EXPLORE THE TOWN')
        choice = input('What do you do: ')

    else:
        print('you do not have the required resources (bow + arrows)')
        time.sleep(2)
        print('Options:')
        print('1. RUN OUT OF THE CHURCH')
        print('2. HIDE')
        choice = input('What do you do: ')



# bear rips leg off scene
if choice == 'RUN OUT OF THE CHURCH':
    print('You run out of the church, hoping to escape the bear.')
    time.sleep(3)
    print('but the bear hears you running through the snow')
    time.sleep(3)
    print('the bear grasps your leg with its teeth')
    time.sleep(2)
    print('you kick and thrash but you can\'t get it off')
    time.sleep(2)
    print('the blood seeps through your pants into the snow')
    time.sleep(2)
    print('you manage to stab the bear in its eye with a stick')
    time.sleep(3)
    print('but as it pulls away you hear a bloody tear')
    time.sleep(3)
    print('your leg is gone')
    time.sleep(3)
    print('you scream in pain but no one can hear it')
    time.sleep(3)
    print('Options:')
    print('1. CRAWL TO A HOUSE')
    print('2. PATCH THE WOUND')
    choice = input('What do you do: ')
    if choice == 'CRAWL TO A HOUSE':
        print('you drag yourself to a nearby house')
        time.sleep(3)
        print('you know you won\'t make it')
        time.sleep(3)
        print('so you don\'t even try to survive')
        time.sleep(3)
        os.system('cls')
        print("YOU DIED")

    if choice == 'PATCH THE WOUND':
        print('you rip off your jacket and tie it around your bleeding waist ')
        time.sleep(3)
        print('the jacket is waterproof and stops the flow of blood')
        time.sleep(3)
        print('but you are now exposed to the cold')
        time.sleep(3)
        print('you crawl around and find a campfire starter kit')
        time.sleep(3)
        print('a nearby house would provide a great place to hold up')
        time.sleep(3)
        print('Options:')
        print('1. SLEEP IN HOUSE')
        choice = input('What do you do: ')

        if choice == 'SLEEP IN HOUSE':
            print('you drag yourself to a nearby house')
            time.sleep(3)
            print('after setting up the fire you find some pills to ease the pain')
            time.sleep(3)
            print('you are truly lucky to survive')
            time.sleep(3)
            print("YOU SURVIVED NIGHT 2")
            time.sleep(3)
            lives -= 2
            Clear_Screen()
            Death_Outcome()
            print('you wake up to the sound of voices')
            time.sleep(2)
            print('you crawl out the door to investigate')
            time.sleep(2)
            print('two hunters are walking into the town')
            time.sleep(2)
            print('weighing your options you decide to risk it and yell out to them')
            time.sleep(3)
            print('their heads snap towards you')
            time.sleep(2)
            print('they talk amongst themselves for a minute before beginning to walk over')
            time.sleep(3)
            print('you see bows and knives strapped to their backpack')
            time.sleep(3)
            print('Options:')
            print('1. DRAW DAGGER')
            print('2. WAIT')
            choice = input('What do you do: ')

            if choice == 'WAIT':
                print('they come over and ask if you are ok')
                time.sleep(3)
                print('you show them your leg, and they frantically pack up your things and carry you into the forest')
                time.sleep(4)
                print('you hear the whirring of helicopter blades from afar')
                time.sleep(3)
                print('you know you are saved')
                time.sleep(3)
                os.system('cls')
                print(Fore.GREEN + 'ENDING 1')
                time.sleep(9999999)

            if choice == 'DRAW DAGGER':
                print('you draw your dagger')
                time.sleep(3)
                print('they notice and draw their bows')
                time.sleep(3)
                print('quicker than you can blink, they shoot')
                time.sleep(3)
                os.system('cls')
                print(Fore.RED + 'YOU DIED')
                time.sleep(9999999)


if choice == 'HIDE':
    print('You find a hiding spot in the church and wait for the bear to leave.')
    time.sleep(2)
    print('but it doesn\'t seem to')
    time.sleep(2)
    print('you are starting to get cold')
    time.sleep(2)
    print('the cold has impaired your movement')
    time.sleep(2)
    print('due to the minor frostbite you acquired, you have lost a health')
    time.sleep(2)

    lives -= 1
    print("remaining health")
    print(str(lives))
    time.sleep(2)

    print('finally, you hear the bear leave')
    time.sleep(2)
    print('Options:')
    print('2. EXPLORE THE TOWN')
    choice = input('What do you do: ')

if choice == ('EXPLORE THE TOWN'):
    print('you venture into the town')
    time.sleep(2)
    print('suddenly you hear a howl')
    time.sleep(2)
    print('then you get a glimpse of a wolf in one of the houses windows')
    time.sleep(2)
    print('you need to leave this place')
    time.sleep(2)
    print('too many dangers')
    time.sleep(2)
    print('you gather a small firestarter kit from the village and head into the forest yet again')
    time.sleep(4)
    print('YOU SURVIVED NIGHT 2')
    time.sleep(3)

Clear_Screen()
Death_Outcome()

print('more story coming soon,')
time.sleep(2)
print('thanks for playing!')
time.sleep(2)
print(':)')

