## Author : Keissy BOD
## Date : 2020-10-12
## Description : Password generator

## This programme require pyperclip module to work
## To install pyperclip module, run the following command in terminal:
## pip install pyperclip

import random
import string
import pyperclip


def main():
    choice = [True, True, True, True]
    menuInit(choice)
    lenghtChoice = setLenght()

    # required characters
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    required = [symbols, numbers, upper, lower]
    checkVar = [False, False, False, False]

    print("Generating password...")
    generatePassword(lenghtChoice, checkVar, required, choice)


def setLenght():
    # set password lenght
    lenghtChoice = 0
    while lenghtChoice < 12:
        lenghtChoice = int(input("Enter the lenght of the password: "))
    return lenghtChoice


def menuInit(choice):
    # display menu
    print("Welcome to the password generator!")
    choice[0] = input("1. Generate password with at least 1 symbol (e.g. !@#$%^&*()_+) [Y]/n")
    choice[1] = input("2. Generate password with at least 1 number (e.g. 1234567890) [Y]/n")
    choice[2] = input("3. Generate password with at least 1 uppercase letter (e.g. ABCDEFGHIJKLMNOPQRSTUVWXYZ) [Y]/n")
    choice[3] = input("4. Generate password with at least 1 lowercase letter (e.g. abcdefghijklmnopqrstuvwxyz) [Y]/n")

    # set choice array to False if user didn't enter Y or y (default value)
    for i in range(0, 4):
        if choice[i] == 'Y' or choice[i] == 'y' or choice[i] == "":
            choice[i] = True
        else:
            choice[i] = False

    # check if user entered at least one requirement
    if choice == [False, False, False, False]:
        print("You must enter at least one requirement!")
        menuInit(choice)

    return choice


def generatePassword(lenghtChoice, checkVar, required, choice):
    password = ""
    # generate password while it doesn't match the requirements of the user (choice)
    while len(password) < lenghtChoice:
        selectElement = random.randint(0, 3)
        if choice[selectElement]:
            checkVar[selectElement] = True
            password += random.choice(required[selectElement])

    checkConformity(checkVar, lenghtChoice, required, password, choice)


def checkConformity(checkVar, lenghtChoice, required, password, choice):
    # check if the password match the requirements of the user (choice)
    if checkVar != choice:
        checkVar = [False, False, False, False]
        generatePassword(lenghtChoice, checkVar, required, choice)
    else:
        printPassword(password)


def printPassword(password):
    # copy password to clipboard
    pyperclip.copy(password)
    # print password in red
    print("Password generated: \033[91m" + password + "\033[0m")
    print("Password copied to clipboard")


# run main function
main()
