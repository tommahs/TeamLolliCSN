## Here we will change the pincode ##
pincode = 1234



def changPinCode(pincode):
    inputOld = int(input('wat is uw oude pincode?: '))
    if inputOld == pincode:
        inputNew = int(input('Voer hier uw nieuwe pincode in: '))
        pincode = inputNew
        return pincode

    else:
        print ('Verkeerde pincode. Voer de goed pincode in.'),changPinCode()

chpincode = changPinCode(pincode)
print(chpincode)