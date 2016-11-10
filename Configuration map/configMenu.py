#this is going to be a configuration code for Code, short or long blinks

## import
from changePinCode import changPinCode(file), readFromFile(file)

## Main screen
def mainScreen():
    def main(input_value):

        if input_value is 1:
            print ('Het alarm systeem is afgesloten')
        if input_value is 2:
            print ('Configuratie scherm open'), config()

        if inputValue is 5:
            print ('u sluit nu het appraat af')
            exit(0)

    while True:
        print('\n '
            'Keuze menu\n',
            'Kies 1 voor Alarm systeem uti zetten.\n',
            'Kies 2 voor Configuratie scherm.\n')
        inputValue = int(input('Wat is uw keuze?: '))
        main(inputValue)

## Config Screen
def config():
    def configuration(inputValue):
        if inputValue is 1:
            configLed()
        if inputValue is 2:
            menuPinCode()
        if inputValue is 3:
            mainScreen()
    while True:
        print('\n'
            'Keuze menu configuratie scherm','\n',
            'Kies 1 om knipperen van het rode alarm licht aan te passen. \n',
            'Kies 2 om de beveilings pincode aan te passen. \n',
            'Kies 3 om terug te gaan naar het hoofd scherm. \n')
        inputValue = int(input('wat is uw keuze?: '))
        configuration(inputValue)

## change the pincode
def menuPinCode():
    def menuPinCode(inputValue):
        if inputValue is 1:
            changPinCode()
        if inputValue is 2:
            config()
    while True:
        print('\n',
            'Keuze menu Pincode. \n',
            'Kies 1 om pincode te weizigen. \n',
            'Kies 2 om terug naar het configuratie scherm te gaan')
        inputValue = int(input('wat is uw keuze?: '))
        menuPinCode(inputValue)

## Led configuration Screen
def configLed():
    def configLight(inputValue):
        if inputValue is 1:
            print('Alarm led zal nu snel & kort knipperen. \n')
        if inputValue is 2:
            print('Alarm led zal een langezaam knipperen')
        if inputValue is 3:
            mainScreen()

    while True:
        print('\n','Keuze menu configuratie led knipper. \n',
              'Kies 1 om de rode led kort en snel knipperen. \n',
              'Kies 2 om de rode led langzaam te laten knipperen. \n',
              'Kies 3 om terug naar het hoofdscherm te gaan. \n')
        inputValue = int(input('wat is uw keuze?: '))
        configLight(inputValue)

## Starting program
mainScreen()