#-------------------------------#
#    Made by sauce (å&#9109)    #
#-------------------------------#

import pymem
import re
import os
import time
import pyautogui

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NORMAL = '\033[30m'

# Defines the clearConsole() function
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Loading (useless but fun)
time.sleep(1.4)
l = "Loading"
for i in range(100):
    print(l, i, "%")
    clearConsole()

# Gets memory codes
pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle, 'GameAssembly.dll')

# Sets the booleans to false
slap = False
jump = False
kb = False
sprint = False

# Patches anti cheat
print("Before we start, do you want to disable the Cheat Engine bypass? (recommended)\n")
print("If you do, type 'yes' in the input box below, else type 'no' (both are case insensitive)")

answer = str(input()).upper()

if answer == "YES":
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x40\x53\x48\x83\xEC\x20\x48\x8B\xD9\x48\x85\xC9\x74\x71', clientModule).start()
    pm.write_bytes(address, b"\xC3\x90", 2)
    print("\nOkay! The cheat engine bypass has been activated.")
    time.sleep(1)
    clearConsole()
elif answer == "NO":
    print("\nOkay! The cheat engine bypass has not been activated.")
    time.sleep(1)
    clearConsole()
    
# Defines addresses for 2 other hacks
    '''
    removed due to them being defined later on in the program
    '''

# GUI
print(bcolors.OKCYAN + "Created by sauce / buy wadbot @ wadbot.lol\n")
print("Choose one of the cheats available:\n")
print("1. Slap cooldown remover\n")
print("2. Air jump/Double jump\n")
print("3. Anti Knockback\n")
print("4. Constant sprint (not recommended, in development, very buggy)\n")
print(bcolors.WARNING + "/!\ Important: to choose a cheat simply input the number of the cheat below", "\n")
print("For example: to choose the slap cooldown remove hack, simply type '1' below! Enjoy :)\n")
print(bcolors.BOLD + "To close this window, type 'disable' when prompted to choose a game \n(important: you still have to restart the game to remove the hacks!)")
print(bcolors.NORMAL + " ")

go = True
while go:
    t = input("Choose a cheat to activate (ex: 1): ")
    
    if int(t) == 1:
        if not slap:
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\xC6\x43\x24\x00\x48\x8B\xCB', clientModule).start() + 3
            pm.write_uchar(address, 1)

            slap = True
            print("Success! The slap cooldown remover has been activated! To disable all hacks, simply type 'disable' below (case insensitive)\n")

        else:
            print("The slap cooldown remover is already enabled! To disable all hacks, simply type 'disable' below (case insensitive)\n")
                
    elif int(t) == 2:
        if not jump:
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x80\xBB.....\x74\x09\x80\xBB.....', clientModule).start()
            pm.write_bytes(address, b"\x90\x90\x90\x90\x90\x90\x90\x90\x90", 9)

            jump = True
            print("Success! The air jump hack has been activated! To disable all hacks, simply type 'disable' below (case insensitive)\n")
        else:
            print("The double jump hack is already enabled! To disable all hacks, simply type 'disable' below (case insensitive)\n")

    elif int(t) == 3:
        if not kb:
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x48\x89\x5C\x24.\x48\x89\x74\x24.\x57\x48\x83\xEC.\x80\x3D.....\x48\x8B\xF2\x48\x8B\xD9\x75.\x48\x8D\x0D....\xE8....\x48\x8D\x0D....\xE8....\xC6\x05.....\x48\x8B\x7B', clientModule).start()
            pm.write_bytes(address, b"\xC3\x90\x90\x90\x90", 5)

            kb = True
            print("Success! The anti knockback hack has been activated! To disable all hacks, simply type 'disable' below (case insensitive)\n")
        else:
            print("Anti Knockback is already enabled! To disable all hacks, simply type 'disable' below (case insensitive)\n")

    elif int(t) == 4:
        if not sprint:
            print("Constant sprint has succesfully been activated! To disable all hacks, simply type 'disable' below (case insensitive)\n")
            while True:
                pyautogui.keyDown("shift")
        else:
            print("Constant sprint is already enabled! To disable all hacks, simply type 'disable' below (case insensitive)\n")
            
    elif int(t) > 4:
        print("Please enter a valid value ranging from 1 to 4!")    
        
    elif t.upper() == "DISABLE":
        go = False
        pm.close_process()
        exit()

