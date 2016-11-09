## Here we will change the pincode ##
import csv


file = 'pincode.csv'


List= []



def readFromFile(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
           content = (row[0])
        return content

# def writeFromFile(file):
#     with open(file, 'w', newline='') as f:
#         writer = csv.writer(f)
#         content = readFromFile()
#         for inputNew in content:
#             writer.writerow(inputNew)

## Change pincode functie
def changPinCode(file):
    inputOld = (input('uw oude pincode?: '))
    content = readFromFile(file)
    if content == inputOld:
        inputNew = ((input('Voer hier uw nieuwe pincode in: ')))
        pincodeFile = open(file, 'w')
        writer = csv.writer(pincodeFile)
        ##   \/ \/ \/ \/ \/ \/  ##
        writer.writerow(inputNew)
        ##^^^^^^^^^^^^^^^^^^^^^^^ is het problem

        # with open(file, 'w', newline='') as f:
        #     writer = csv.writer(f)
        #     for inputNew in content:
        #         writer.writerow(inputNew)

    else:
        print ('Verkeerde pincode. Voer de goed pincode in.'),changPinCode(file)

changPinCode(file)

