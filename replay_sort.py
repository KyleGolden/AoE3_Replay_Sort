import os
import glob
import time
import sys
import getpass as gp

"""
AOE3 Replay Sort

Age of Empires 3 replays are saved to generic default names (Save Game 1.age3rec) which make it difficult
to find replays.

After I play a game I can run this script to rename the file

"""

#Globals
ORIG = "Record Game 1.age3rec"
DATE_TIME = time.strftime("%m-%d-%Y-%H.%M.%S")
PATH = "C:\\Users\\" + gp.getuser() + "\\Documents\\My Games\\Age of Empires 3\\Savegame"

if __name__ == '__main__':
    #handle arg
    try:
        rename = sys.argv[1]
    except IndexError:
        print("\n[ ERROR ]   :: Useage: %s <new name>" % __file__)
        sys.exit(1)


    #Go to directory
    try:
        os.chdir(PATH)
    except Exception:
        print(PATH)
        print("\n[ ERROR ]   :: The directory: %s does not exist" % PATH)
        sys.exit(1)


    #look for Record Game 1
    replays = glob.glob("*.age3rec")
    print("\n[ LOG ]     :: Replays contained in %s\n" % os.getcwd())    


    for r in replays:
        print("\t\t- %s\n" % r)


    if ORIG not in replays:
        print("[ ERROR ]   :: There are no recently recorded game to be found")
        sys.exit(1)

    #change to new name and save
    new_file = rename + "_" + DATE_TIME
    os.rename(ORIG, new_file)
    print ("[ SUCCESS ] :: " + ORIG + " has been renamed to " + new_file + ".age3rec")
