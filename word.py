import os
import time
import glob, os

screenWidth = 50;
delay = 0.1
parent_dir = ""

def clear_Screen():
    os.system('cls')

def select_list():
    clear_Screen()
    menu_Line("Type a existing list.")
    border_line()
    menu_Line("Choose a list:")
    for txt_file in glob.glob(os.path.join(parent_dir, '*.txt')):
        menu_Line("• " + txt_file)
    border_line()

    currentList = input("    :   ")
    while True:
        if not os.path.isfile(currentList):
            warning()
            clear_Screen()
            menu_Line("That list doesn't even exist bro!")
            border_line()
            menu_Line("Choose a list:")
            for txt_file in glob.glob(os.path.join(parent_dir, '*.txt')):
                menu_Line("• " + txt_file)
            border_line()
            currentList = input("    :   ")
        else:
            break
    wordFile = open(currentList)
    worddict = {}
    for item in wordFile:
        if not item == '':
            wordNL, wordENG = item.strip('\n').split("=")
            worddict[wordNL] = wordENG
    wordFile.close()
    return worddict

def add_words(worddict):
    clear_Screen()
    menu_Line("Name the dutch word")
    border_line()
    keyChoice = input("    :   ")
    clear_Screen()
    menu_Line("Name the english translation of '" + keyChoice + "'.")
    border_line()
    valueChoice = input("    :   ")

def remove_words(worddict):
    while True:
        clear_Screen()
        menu_Line("Type the key you want to remove")
        menu_Line("1 = save and go back")
        border_line()
        for item in worddict:
            menu_Line(item + " = " + worddict[item])
        border_line()
        keyChoice = input("    :   ")
        if keyChoice in worddict:
            del worddict[valueChoice]
        elif keyChoice == "1":
            manage_List(worddict)
        else:
            warning()

def manage_List(worddict):
    clear_Screen()
    print(worddict)
    menu_Line("Do something with it.")
    border_line()
    menu_Line("1 = make list")
    menu_Line("2 = delete list")
    menu_Line("")
    menu_Line("3 = add words")
    menu_Line("4 = remove words")
    menu_Line("")
    menu_Line("5 = go back")
    border_line()
    choice = input("    :   ")
    while choice != 5:
        if choice == "3":
            add_words(worddict)
        elif choice == "4":
            remove_words(worddict)
        elif choice == "5":
            break
        else:
            warning()

def start_Test(worddict):
    correct = 0
    incorrect = 0
    while True:
        for item in worddict:
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

def border_line():
    borderWidth = screenWidth + 4
    print("="*borderWidth)

def warning():
    clear_Screen()
    for i in range(2):
        menu_Line(" [!]  ERROR  [!]")
        border_line()
        time.sleep(delay)
        clear_Screen()
        time.sleep(delay/2)

#print functie
def menu_Line(line):
    newLine = (("| {:" + str(screenWidth) + "} |").format(line))
    print(newLine)

def main():
    #show list
    clear_Screen()
    menu_Line("Welcome, choose what you want to do.")
    border_line()
    menu_Line("1 = Start the test")
    menu_Line("2 = Manage lists")
    menu_Line("3 = quit")
    border_line()
    choice = input("    :   ")
    while choice != "3":
        if choice in ["1", "2"]:
            worddict = select_list()
        if choice == "1":
            start_Test(worddict)
        elif choice == "2":
            manage_List(worddict)
        else:
            warning()
        clear_Screen()
        menu_Line("Yo, choose what you want to do.")
        border_line()
        menu_Line("1 = Start the test")
        menu_Line("2 = Manage lists")
        menu_Line("3 = quit")
        border_line()
        choice = input("    :   ")

main()
