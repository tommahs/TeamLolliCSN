## Here we will change the pincode ##
import csv


file = 'pincode.csv'

# Writing lockerFile
# def writeToFile(file, pincode):
#     try:
#         with open(file, 'w', newline='') as myCSVFile:
#             writer = csv.writer(myCSVFile, delimiter=';')
#             for pincode in file.items():
#                 writer.writerow((pincode))
#
#     except Exception as ex:
#         print(ex)

def readFromFile(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
           content = (row[0])
        return content



## Change pincode functie
def changPinCode(file):
    inputOld = (input('uw oude pincode?: '))
    content = readFromFile(file)
    if content == inputOld:
        inputNew = (str(input('Voer hier uw nieuwe pincode in: ')))

        with open(file, 'w', newline=inputNew) as f:
            writer = csv.writer(f)
            for inputNew in content:
                writer.writerow(inputNew)

    else:
        print ('Verkeerde pincode. Voer de goed pincode in.'),changPinCode(file)

changPinCode(file)

