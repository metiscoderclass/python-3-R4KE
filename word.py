import os
import time

screenWidth = 25;

def clear_Screen():
    os.system('cls')

def read_Words(wordList):
    wordList = open(wordList)
    for item in wordList:
        if not item == '':
            word1, word2 = item.strip('\n').split("=")
            #print(word1 + " = " + word2)
            return(word1, word2)

def new_List():
    clear_Screen()
    newList = input("Name the new list: ")
    read_Words(newList)
    return newList

def choose_List():
    clear_Screen()
    currentList = input("Choose list: ")
    if os.path.isfile(currentList):
        read_Words(currentList)
        return(currentList);
        manage_List()
    else:
        print("ewa nee bro")

def manage_List():
    clear_Screen()
    print("1 = choose list")
    print("2 = make list")
    print("3 = remove list")
    print("4 = go back")
    choice = input("Choose an option: ")
    if choice == "1":
        choose_List()
    elif choice == "2":
        new_List()

def start_Test():
    print("test")
    print(word1 + " = " + word2)

def main():
    #show list
    while True:
        clear_Screen()
        print("1 = start the test")
        print("2 = manage lists")
        print("3 = quit")
        choice = input("Choose an option: ")
        if choice == "1":
            start_Test()
            break
        elif choice == "2":
            manage_List()
            break


main()
