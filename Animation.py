#                 _                 __  _           
#    ____ _____  (_)___ ___  ____ _/ /_(_)___  ____ 
#   / __ `/ __ \/ / __ `__ \/ __ `/ __/ / __ \/ __ \         @
#  / /_/ / / / / / / / / / / /_/ / /_/ / /_/ / / / /        /|\
#  \__,_/_/ /_/_/_/ /_/ /_/\__,_/\__/_/\____/_/ /_/   1.0   / \           




import time,os,sys,colorama
os.system('clear')

tme = 0.5 # time between frames

Loop_Amount=4 # variable for amount of full loops

def F(Symbols): # makes frames cleaner and easier to understand
    print(Symbols)

def Clearlines(): # function to refresh the screen
    sys.stdout.write('\033[3A')  # Move cursor up one line
    sys.stdout.write('\033[3K')  # Clear the line
    sys.stdout.flush()

x=0 # variable used to start and stop loops
while True:


    F(" @  ") #each frame is stored in 3 F functions, F stands for frame and prints a line of the frame!
    F("/|\ ")
    F("/ \ ")
    Clearlines()
    time.sleep(tme)
    F("  @ ")
    F("  | ")
    F("  | ")
    Clearlines()
    time.sleep(tme)
    F("   @  ")
    F("  /|\ ")
    F("  / \ ")
    Clearlines()
    time.sleep(tme)
    F("    @ ")
    F("    | ")
    F("    | ")
    Clearlines()
    time.sleep(tme)
    F("     @  ")
    F("    /|\ ")
    F("    / \ ")
    Clearlines()
    time.sleep(tme)
    F("      @ ")
    F("      | ")
    F("      | ")
    Clearlines()
    time.sleep(tme)
    F("       @  ")
    F("      /|\ ")
    F("      / \ ")
    Clearlines()
    time.sleep(tme)

    F(" " * 10) # this block of code is required if you want your animation to run in a smooth loop,
    F(" " * 10) # because the clear lines function doesnt clear the frame before beginning to draw a new one
    F(" " * 10)
    Clearlines()
    time.sleep(tme)

    x += 1
    if x>=Loop_Amount:
        break
x=0 # at the end of the animation x is set back to 0
