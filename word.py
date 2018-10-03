import os
import time

def clear_Screen():
    os.system('cls')

def read_list():
    # vraag gebruiker om naan van lijst
    wordList = {}
    currentList = input("Choose list: ")
    if not os.path.isfile(currentList):
        return
    wordFile = open(currentList)
    for item in wordFile:
        if not item == '':
            wordNL, wordENG = item.strip('\n').split("=")
            print(wordNL + " = " + wordENG)
            #{"hallo" : "hello"}
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
        readList()
    elif choice == "2":
        change_List()

def start_Test():
    for item in wordList:
        if not item == '':
            wordNL, wordENG = item.strip('\n').split("=")
            print(wordNL + " = " + wordENG)
            input = input("Define: " + wordNL)
            if input == wordENG:
                print("dipp")

def main():
    #show list
    clear_Screen()
    print("| {:40} |".format("1 = start the test"))
    print("| {:40} |".format("2 = manage lists"))
    print("| {:40} |".format("3 = quit"))
    choice = input("Choose an option: ")
    if choice == "1":
        start_Test()
    elif choice == "2":
        manage_List()


main()
