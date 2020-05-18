import csv 
import sys 
import os
from datetime import datetime
from time import sleep
import shutil


#this loads the ID and points of each member
members = list(csv.reader(open("members.csv")))


#converts points column to int for iteration
for i in range(len(members)):
    members[i][1] = int(members[i][1])

def adddat(choice):
    #print("backing up previous list")
    writebak()
    done = set()
    print("adding points")
    ite=0
    datatoload = ""
    if choice == 1:
        ite=10
        datatoload="eventreg.csv"
    elif choice ==2:
        ite=20
        datatoload = "ctlist.csv"
    elif choice ==3:
        ite=10
        datatoload = "volunteers.csv"
    elif choice ==4:
        ite=15
        datatoload = "volunteers.csv"
    elif choice ==5:
        ite=15
        datatoload = "performers.csv"

    print("adding from",datatoload)
    newdat = list(csv.reader(open(f"{datatoload}")))
    for i in range(len(newdat)):
        for j in range(len(members)):
            if newdat[i][0] == members[j][0] and members[j][0] not in done:
                members[j][1] += ite
                done.add(members[j][0])

    print("Overwriting member points...")
    writedata()
    print("clearing list of finished IDs...")
    done.clear()
    print("Done!")
    sleep(3)
    os.system('cls')
    

def show(): #for debug purposes
    for i in range(len(members)):
        print(members[i][0],members[i][1])


def writebak(): #writes backup of current data
    baktm = datetime.now().strftime("%Y,%m-%d-%H;%M;%S")

    if not os.path.exists('backups'):
        os.makedirs('backups')

    backuppath=f"backups/members-{baktm}.csv"

    print("backing up current list...")
    with open(backuppath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(members)
    

#overwrites new updated file
def writedata():
    with open('members.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(members)

def main():
    mmchoice = 0
    while True:
        print("Welcome to the new AECES Merit Point Adding System!")
        print("Which group of people will you add to?")
        print("1: event goers               (+10 each)  eventreg.csv")
        print("2: core team members         (+20 each)  ctlist.csv")
        print("3: event volunteers(small)   (+10 each)  volunteers.csv")
        print("4: event volunteers(large)   (+15 each)  volunteers.csv")
        print("5: event performers          (+15 each)  performers.csv")
        print("0: exit")
        mmchoice=int(input())

        if mmchoice > 0 and mmchoice <6:
            adddat(mmchoice)
        
        elif mmchoice == 0:
            os.system('cls')
            quit()

if __name__ == "__main__":
    main()
   



