import os
import time

screenWidth = 10;

def clear_Screen():
    os.system('cls')

def read_list():
    # vraag gebruiker om naam van lijst
    clear_Screen()
    currentList = input("Choose list: ")
    if not os.path.isfile(currentList):
        return
    wordFile = open(currentList)
    wordList = {}
    for item in wordFile:
        if not item == '':
            wordNL, wordENG = item.strip('\n').split("=")
            wordList[wordNL] = wordENG
    return wordList

def change_list():
    wordList = read_list()
    # toevoegen of verwijderen?
    # bestand opslaan

# functies = {"1": choose_list, }
# functies[choice]()
def manage_List():
    clear_Screen()
    print("| {:40} |".format("1 = choose list"))
    print("| {:40} |".format("2 = change list"))
    print("| {:40} |".format("3 = remove list"))
    print("| {:40} |".format("4 = go back"))
    choice = input("Choose an option: ")
    if choice == "1":
        read_list()
    elif choice == "2":
        change_List()
    else:
        manage_List()

def start_Test():
    correct = 0
    incorrect = 0
    while True:
        for item in wordList:
            if not item == '':
                wordNL, wordENG = item.strip('\n').split("=")
                print(wordNL + " = " + wordENG)
                input = input("Define: " + wordNL)
                if input == wordENG:
                    print("NICEEEEEE")
                else:
                    print("Ded")
                    return

def menuLine(line):
    newLine = (("| {:" + str(screenWidth - 3) + "}").format(line))
    print(newLine)


def main():
    #show list
    choice = input("Choose an option: ")
    while choice != "4":
        clear_Screen()
        menuLine("1 = start the test")
        print("| {:40} |".format("1 = start the test"))
        print("| {:40} |".format("2 = manage lists"))
        print("| {:40} |".format("3 = quit"))
        choice = input("Choose an option: ")
        if choice == "1":
            start_Test()
        elif choice == "2":
            manage_List()
        elif choice == "3":
            manage_List()


main()
