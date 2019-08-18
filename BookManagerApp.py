from string import *
from Books import *
  

loop = "go"

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

    else :
        print("Wrong command try again")
