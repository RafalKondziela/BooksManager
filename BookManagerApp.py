from string import *
from Books import *
  

loop = "go"
library = {0:"test"}

while(loop == "go"):
    key = input("Hello in Book Manager type command to perform action or 'help' to get list of commands \n\n")
    if(key == "help"):
        print("Avaliable commands: ")
        print("exit - exits application")
        print("list - library of written books")
        print("add - add book to library")
        print("--------------------------------------------------------")
        
        
    elif(key == "exit"):
        print("Bye")
        break

    elif(key == "list"):
        print(library)

    elif(key =="add"):
        length = len(library)
        book = Book(
        str(input("Add Author: ")),
        str(input("Add Title: ")),
        int(input("Add number of pages: ")))
        book.addBook(library, length, book) 
        

    else :
        print("Wrong command try again")
