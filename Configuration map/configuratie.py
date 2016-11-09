import xmltodict

def readxml():
    global configxml
    docFile = open("config.xml", "r")
    read = docFile.read()
    xmlDict = xmltodict.parse(read)
    configxml = xmlDict['data']
    # print(configxml)
    # print(type(configxml))
    return configxml


# def writexml():


def getknipper(xml):
    global knipper, Kort, Lang
    knipper = xml['knipper']
    print(knipper)

def getcode(xml):
    global code
    code = xml['code']
    print('de code is :', code)

loop =1
while loop == 1:
    configxml = readxml()
    getknipper(configxml)
    getcode(configxml)
    loop = 0