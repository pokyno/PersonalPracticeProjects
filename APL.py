import io
import os
import sys
import importlib

programsFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Programs")
programs = []

def importPrograms():
    print("-----------------------------------------")
    print("Loading programs in the Programs folder:")
    print("-----------------------------------------")

    print("Reading the files------------------------")
    filenames = next(os.walk(programsFolder))[2]
    sys.path.append(programsFolder) #add to the pathenv

    for f in filenames:
        try:
            f = f.split(".")[0]
            print("Loading %s" % f)

            imported = importlib.import_module(f)
            programs.append(imported.classStart())

            print("%s loaded" % f)
        except:
            print("module %s failed to load" % f)

    sys.path.pop()
    print("-----------------------------------------\n")

def printPrograms():
    print("------------------------------------------")
    print("The programs that currently installed are:\n")
    print("------------------------------------------")
    counter = 0
    for program in programs:
        print("%d- %s\n" % (counter,program.name))
        counter += 1
    print("------------------------------------------")

def main():
    importPrograms()
    while(True):
        printPrograms()
        print("Enter the desired program number(-1 to exit):")
        userInput = 0
        try:
            userInput = int(input())
        except:
            print("Please enter a existing option")
            continue

        if userInput == -1: #user wants to exit the program
            print("Program closing")
            break

        if 0 <= userInput and userInput < len(programs):
            programs[userInput].start() #start the application

main()
