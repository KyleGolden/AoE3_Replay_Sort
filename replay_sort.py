import os
import glob
import time
import sys

"""
AOE3 Replay Sort

Age of Empires 3 replays are saved to generic default names (Save Game 1.age3rec) which make it difficult
to find replays.

After I play a game I can run this script to rename the file

(originally wanted to scrap the replay files for playername, civ used, map name etc..
but the rec files are unreadable i a text editor)

"""

#Globals
ORIG = "Record Game 2.age3rec"
DATE_TIME = time.strftime("%d_%m_%Y")
PATH = r"C:\Users\Kyle\Documents\My Games\Age of Empires 3\Savegame"

if __name__ == '__main__':
    #handle arg
    try:
        rename = sys.argv[1]
    except IndexError:
        print "[ERROR]: useage: replay_sort.py <new filename>"
        sys.exit(1)

    #Go to directory
    try:
        os.chdir(PATH)
    except Exception:
        print "That directory does not exist"
        sys.exit(1)

    #look for Record Game 1
    replays = glob.glob("*.age3rec")
    if ORIG not in replays:
        print "There is no recently recorded game to be found  (Record Game 1.age3rec)"
        sys.exit(1)

    #change to new name and save
    new_file = rename + "_" + DATE_TIME
    os.rename(ORIG, new_file)
    print "[SUCCESS]: " + ORIG + " has been renamed to " + new_file + ".age3rec"
