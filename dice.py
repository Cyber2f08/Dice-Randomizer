import random
import psutil
import pyfiglet
import pyautogui
import colorama
from colorama import Fore, Back, Style
from mdl import banner
from time import sleep
from termcolor import colored
colorama.init(autoreset=True)

## If syntax an error maybe this python file has a bug or different python Version
# Dont forget to read the license file! 
# Credit Cyber2f08!
# ----------------------------->

char = '123456'
a = 1
b = 2
c = 3
l = random.choice(char)

def main(b):
    if a in range(c):
        from mdl import banner
        sleep(1)
        return main(a)
        
def main(a):
    if a in range(c):
        print(colored("{=} Generating..", 'green'))  ## colored = is when you gonna chance color
        sleep(1)
        print(colored("[+] Printing /x32 Value!", 'green'))
        sleep(1)
        print(colored("[+] Writing CPU Block ", 'green'))
        sleep(2)
        print(colored("[=] Success: ", 'green'))
        sleep(1)
        print(colored("Hey You Got the Lucky Dice of mark:  ", 'green'))

        ascii_banner = pyfiglet.figlet_format(l)
        print(colored(ascii_banner, 'green'))
        k = "Thank you! Your dice is :"
        print(colored(k ,'green'))
        print(colored(l ,'green'))
        sleep(6)
        print("Please\n")
        sleep(1)
        print("Kill\n")
        sleep(1)
        print("ME\n\nIF\n")
        sleep(3)
        print("U\n")
        sleep(1)
        print("CAN\n\n\n\n\n\n\n\n\n")
        sleep(2)
        answer = input(colored("-> Are you want to dice this again? ", 'yellow'))
    if answer == "yes":
        print('OK, FINDING QUERYS!')
        sleep(5)
        return main(b)
    if answer == "no":
        print(colored('OK DESTROYING COMPUTER', 'red'))
        sleep(10)
        exit()
# PLEASE END ME
    
p1 = main(a)
print(p1)