class ObservedConfiguration:
    def __init__(self, os):
        self.OS = os
        # This will hold the TCs this OC can mask
        self.masked = [os]


class TrueConfiguration:
    def __init__(self, name, os):
        self.name = name
        self.OS = os
        self.utility = 0


# This method is passed in the manual input from the command line
# This it reads the file and creates the appropriate TCs
def createNetwork(inputFile):
    systems = []
    with open(inputFile, 'r') as f:
        for line in f:
            attributes = line.split(',')
            # The last attribute will have a newline character at the end of it so we remove it
            attributes[-1] = attributes[-1].strip("\n").strip(" ")
            systems.append(createConfiguration(attributes))
    return systems


# This will create a configuration with the given attributes with the utility being scored by our miniMaxClass
def createConfiguration(attributes):
    return TrueConfiguration(attributes[0], attributes[1])


possibleOS = ['Windows', 'Ubuntu', 'Metasploitable', 'Fedora']
def createOSN():
    allOC = []
    portNums = [portnumber1, portnumber2, portnumber3]      #list of possible port numbers
    for os in possibleOS:
        myOC = ObservedConfiguration(os)
        allOC.append(myOC)
    return allOC


def networkToText(tsn, osn):
    return 0









