import os
import time

screenWidth = 25;

def clear_Screen():
    os.system('cls')

def read_Words(wordList):
    wordList = open(wordList)
    return wordList

def new_List():
    clear_Screen()
    newList = input("Name the new list: ")
    read_Words(newList)
    return newList

def choose_List():
    while True:
        clear_Screen()
        currentList = input("Choose list: ")
        if os.path.isfile(currentList):
            wordList = read_Words(currentList)
            return(currentList);
            break
            manage_List()
        else:
            print("NOOO")

def manage_List():
    clear_Screen()
    print("| {:40} |".format("1 = choose list"))
    print("| {:40} |".format("2 = make list"))
    print("| {:40} |".format("3 = remove list"))
    print("| {:40} |".format("4 = go back"))
    choice = input("Choose an option: ")
    if choice == "1":
        choose_List()
    elif choice == "2":
        new_List()

def start_Test():
    wordList = read_Words(currentList)
    for item in wordList:
        if not item == '':
            word1, word2 = item.strip('\n').split("=")
            print(word1 + " = " + word2)
            input = input("Define: " + word1)
            if input == word2:
                print("dipp")

def main():
    #show list
    while True:
        clear_Screen()
        print("| {:40} |".format("1 = start the test"))
        print("| {:40} |".format("2 = manage lists"))
        print("| {:40} |".format("3 = quit"))
        choice = input("Choose an option: ")
        if choice == "1":
            start_Test()
            break
        elif choice == "2":
            manage_List()
            break


main()
