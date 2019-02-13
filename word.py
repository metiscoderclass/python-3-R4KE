import os
import time
import random
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
    for wrd_file in glob.glob(os.path.join(parent_dir, '*.wrd')):
        menu_Line("• " + wrd_file)
    border_line()

    currentList = input("    :   ")
    while currentList != "":
        if not os.path.isfile(currentList):
            warning()
            clear_Screen()
            menu_Line("That list doesn't even exist bro!")
            border_line()
            menu_Line("Choose a list:")
            for wrd_file in glob.glob(os.path.join(parent_dir, '*.wrd')):
                menu_Line("• " + wrd_file)
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
    return worddict, currentList

def add_words(worddict, currentList):
    clear_Screen()
    print("Debug: " + str(worddict))
    menu_Line("Name the dutch word")
    border_line()
    keyChoice = input("    :   ")
    while keyChoice != "1":
        border_line()
        menu_Line("Name the english translation of '" + keyChoice + "'.")
        border_line()
        valueChoice = input("    :   ")
        worddict[keyChoice] = valueChoice
        clear_Screen()
        menu_Line("1 = exit")
        print("Debug: " + str(worddict))
        menu_Line("Name the dutch word")
        border_line()
        keyChoice = input("    :   ")
        file = open(currentList, 'a')
        file.write(keyChoice + "=" + valueChoice + "\n")
        file.close

def remove_words(worddict, currentList):
    clear_Screen()
    menu_Line("Type the key you want to remove")
    menu_Line("1 = save and go back")
    border_line()
    for item in worddict:
        menu_Line(item + " = " + worddict[item])
    border_line()
    keyChoice = input("    :   ")
    if keyChoice in worddict:
        del worddict[keyChoice]
    else:
        warning()
    while keyChoice not in ["1"]:
        clear_Screen()
        menu_Line("Type the key you want to remove")
        menu_Line("1 = save and go back")
        border_line()
        for item in worddict:
            menu_Line(item + " = " + worddict[item])
        border_line()
        keyChoice = input("    :   ")
        if keyChoice in worddict:
            del worddict[keyChoice]
        else:
            warning()
    return worddict

def show_menu_manage_list(worddict):
    clear_Screen()
    menu_Line("Do something with it.")
    border_line()
    menu_Line("1 = add words")
    menu_Line("2 = remove words")
    menu_Line("")
    menu_Line("3 = go back")
    border_line()
    choice = input("    :   ")
    return choice

def manage_List(worddict, currentList):
    choice = show_menu_manage_list(worddict)
    while choice != 3:
        if choice == "1":
            add_words(worddict, currentList)
        elif choice == "2":
            remove_words(worddict, currentList)
        elif choice == "3":
            break
        else:
            warning()
        choice = show_menu_manage_list(worddict)

def make_List():
    clear_Screen()
    menu_Line("Name the new list.")
    menu_Line("1 = go back")
    border_line()
    choice = input("    :   ")
    while choice != "":
        clear_Screen()
        menu_Line("Name the new list.")
        menu_Line("1 = go back")
        border_line()
        choice = input("    :   ")
        if choice != "1":
            newFile = open(choice +".wrd","w+")
        else:
            break

def start_Test(worddict):
    percentage = 100
    correct = 0
    incorrect = 0
    while percentage > 25:
        for item in worddict:
            clear_Screen()
            if not item == '':
                menu_Line("1 = Exit")
                border_line()
                menu_Line("Correct: " + str(correct))
                menu_Line("Incorrect: " + str(incorrect))
                menu_Line(str(round(percentage)) + "% is correct")
                border_line()
                menu_Line("Translate: " + item)
                guessInput = input("    :   ")
                if guessInput == worddict[item]:
                    correct += 1
                elif guessInput == "1":
                    return
                else:
                    print("Ded")
                    incorrect += 1
                if (correct + incorrect) >= 1:
                    percentage = (100.0*correct/(correct + incorrect))

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

def menu_Line(line):
    newLine = (("| {:" + str(screenWidth) + "} |").format(line))
    print(newLine)

def mainUI():
    clear_Screen()
    menu_Line("Welcome, select what you want to do.")
    border_line()
    menu_Line("1 = Start the test")
    menu_Line("2 = Manage lists")
    menu_Line("3 = Make new list")
    menu_Line("4 = quit")
    border_line()

def main():
    mainUI()
    choice = input("    :   ")
    while choice != "4":
        if choice in ["1", "2"]:
            worddict, currentList = select_list()
        if choice == "1":
            start_Test(worddict)
        elif choice == "2":
            manage_List(worddict, currentList)
        elif choice == "3":
            make_List()
        else:
            warning()
        mainUI()
        choice = input("    :   ")

main()
