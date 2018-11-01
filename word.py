import os
import time
import glob, os

screenWidth = 50;
parent_dir = ""

def clear_Screen():
    os.system('cls')

def select_list():
    # vraag gebruiker om naam van lijst
    clear_Screen()
    border_line()
    for txt_file in glob.glob(os.path.join(parent_dir, '*.txt')):
        menu_Line("• " + txt_file)
    border_line()
    currentList = input("Choose list: ")
    if not os.path.isfile(currentList):
        return
    wordFile = open(currentList)
    worddict = {}
    return worddict

def add_words(worddict):
    for item in worddict:
        print(item)
    newword = input("Add word: ")
    worddict.write(newword)
    worddict.close()

    #add or remove lists

def remove_words():
    for item in worddict:
        print(item)
    #add or remove lists

# functies = {"1": choose_list, }
# functies[choice]()
def manage_List(worddict):
    clear_Screen()
    border_line()
    menu_Line("1 = add list")
    menu_Line("2 = remove list")
    menu_Line("3 = add words")
    menu_Line("4 = remove words")
    menu_Line("5 = go back")
    border_line()
    choice = input("Choose an option: ")
    if choice == "3":
        add_words(worddict)
    elif choice == "4":
        remove_words()
    elif choice == "5":
        main()

def start_Test(worddict):
    #neem de lijst en overhoor
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

#print functie
def menu_Line(line):
    newLine = (("| {:" + str(screenWidth) + "} |").format(line))
    print(newLine)


def main():
    #show list
    clear_Screen()
    border_line()
    menu_Line("1 = Start the test")
    menu_Line("2 = Manage lists")
    menu_Line("3 = quit")
    border_line()
    choice = input("Choose an option: ")
    worddict = {}
    while choice != "4":
        if choice in ["1", "2"]:
            worddict = select_list()
        if choice == "1":
            start_Test(worddict)
        elif choice == "2":
            manage_List(worddict)
        choice = input("Choose an option: ")

main()
