import os
import time
import glob, os

screenWidth = 10;
parent_dir = ""

def clear_Screen():
    os.system('cls')

def select_list():
    # vraag gebruiker om naam van lijst
    clear_Screen()
    for txt_file in glob.glob(os.path.join(parent_dir, '*.txt')):
        print (txt_file)
    currentList = input("Choose list: ")
    if not os.path.isfile(currentList):
        return
    wordFile = open(currentList)
    wordlist = {}
    #for item in wordFile:
    #    if not item == '':
    #        wordNL, wordENG = item.strip('\n').split("=")
    #        wordList[wordNL] = wordENG
    return wordlist

def change_list():
    print("test")
    #while loop om te checken als er een file geselect is anders: break
    # toevoegen of verwijderen?
    # bestand opslaa n

def add_Remove():
    print("test")
    #add or remove lists

# functies = {"1": choose_list, }
# functies[choice]()
def manage_List():
    clear_Screen()
    #print(currentList)
    menuLine("1 = select list")
    menuLine("2 = change list")
    menuLine("3 = remove/add list")
    menuLine("4 = go back")
    choice = input("Choose an option: ")
    if choice == "1":
        select_list()
    elif choice == "2":
        change_List()
    elif choice == "3":
        add_Remove()
    elif choice == "4":
        main()

def start_Test(wordlist):
    #neem de lijst en overhoor
    correct = 0
    incorrect = 0
    while True:
        for item in wordlist:
            if not item == '':
                wordNL, wordENG = item.strip('\n').split("=")
                input = input("Define: " + wordNL)
                if input == wordENG:
                    correct += 1
                    print("NICEEEEEE")
                    return
                else:
                    print("Ded")
                    incorrect += 1
                    return

def menuLine(line):
    #print functie
    newLine = (("| {:" + str(screenWidth - 3) + "}").format(line))
    print(newLine)


def main():
    #show list
    clear_Screen()
    menuLine("1 = Start the test")
    menuLine("2 = Select a list")
    menuLine("3 = Manage lists")
    menuLine("4 = quit")
    choice = input("Choose an option: ")
    wordlist = {}
    while choice != "4":
        if choice in ["1", "3"]:
            wordlist = select_list()
        if choice == "1":
            start_Test(wordlist)
        elif choice == "2":
            select_list()
        elif choice == "3":
            manage_List()
        choice = input("Choose an option: ")

main()
