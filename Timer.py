#████████╗██╗███╗   ███╗███████╗██████╗ ██╗
#╚══██╔══╝██║████╗ ████║██╔════╝██╔══██╗██║
#   ██║   ██║██╔████╔██║█████╗  ██████╔╝██║
#   ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝
#   ██║   ██║██║ ╚═╝ ██║███████╗██║  ██║██╗
#   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝
                                        
import time    # Imports the time module, this is an essential component of the code.
from tkinter import *
root = Tk()
root.mainloop()

my_time = int(input("Enter the time in seconds > "))    # Uses the user input to define the "my_time" variable, this variable is essential to the code.
txtfld=Entry(window, text="This is Entry Widget", bg='black',fg='white', bd=5)

for x in range(my_time, 0, -1):    # Loops the below section 

    seconds = x % 60    # Defines the seconds

    minutes = int(x / 60) % 60    # Defines the minutes, essentially the second value x60

    hours = int(x / 3600)    # Defines the hours, essentially the second value x3600

    window.title(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")    # Prints the time using the above equation, the "02" adds padding to numbers below 10 eg. "1" will become "01",
                                                               # the \r at the end refreshes the previous line so the terminal dosent become flooded with lines of each number.

    time.sleep(1)    # Waits one second before looping the script, changing this value will change the speed that the script runs at

print("Times Up!")    # Displays a message when the loop completes