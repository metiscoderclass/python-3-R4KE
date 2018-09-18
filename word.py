import os

screenWidth = 25;

def clear_Screen():
    os.system('clear')
    
def read_Words(wordList):
    wordList = open(wordList)
    for item in wordList:
        if not item == '':
            word1, word2 = item.strip('\n').split("=")
            #print(word1 + " = " + word2)

def new_List():
    newList = input("Name the new list: ")
    return newList

def test_Dat_Ass():
    #test

def main():
    #show list
    clear_Screen()
    print("1 = add list")
    print("2 = chooce list")
    print("3 = add words")
    print("4 = test dat ass")
    print("5 = quit")
    choice = input("Choose an option!")
    while choice != 5:
        if choice == 1:
            new_List()
        elif choice == 2:
            #choocelist
        elif choice == 3:
            #add words
        elif choice == 4:
            #test dat ass
            
read_Words("wordList.txt")
main()
