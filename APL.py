import io
from HelloWorld import HelloWorld

programs = [
HelloWorld()
]

def init():
    print("------------------------------------------")
    print("The programs that currently installed are:\n")
    print("------------------------------------------")
    counter = 0
    for program in programs:
        print("%d- %s\n" % (counter,program.name))
        counter += 1
    print("------------------------------------------")

def main():
    init()
    while(True):
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
