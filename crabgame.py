import pymem
import re

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

# Gets memory codes
pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle,'GameAssembly.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)

# Patches anti cheat
address = client.lpBaseOfDll + re.search(rb'\x40\x53\x48\x83\xEC\x20\x48\x8B\xD9\x48\x85\xC9\x74\x71', clientModule).start()

pm.write_bytes(address, b"\xC3\x90", 2)

# Defines addresses for 2 other hacks
address1 = client.lpBaseOfDll + re.search(rb'\xC6\x43\x24\x00\x48\x8B\xCB', clientModule).start() + 3
address2 = client.lpBaseOfDll + re.search(rb'\x80\xBB.....\x74\x09\x80\xBB.....',clientModule).start()

# GUI
print("Open source hack forked by sauce -_- buy wadbot @ wadbot.lol\n")
print("Choose one of the cheats available:\n")
print("1. Slap cooldown remover\n")
print("2. Air jump/Double jump\n")
print(bcolors.WARNING + "/!\ Important: to choose a cheat simply input the number of the cheat below\n")
print(bcolors.UNDERLINE + "For example: to choose the slap cooldown remove hack, simply type '1' below! Enjoy :)")

go = True
while go:
    t = input()  
    if t == 1:
        pm.write_uchar(address1, 1)
        print("Success! The slap cooldown remover has been activated! To disable all hacks, simply type 'disable' below (case insensitive)")
        t1 = input()
        if t1 == "DISABLE":
            go = False
            pm.close_process()
            exit()
    elif t == 2:
        pm.write_bytes(address2, b"\x90\x90\x90\x90\x90\x90\x90\x90\x90", 9)
        print("Succes! The air jump hack has been activated! To disable all hacks, simply type 'disable' below (case insensitive)")
        t1 = input().upper()
        if t1 == "DISABLE":
            go = False
            pm.close_process()
            exit()






