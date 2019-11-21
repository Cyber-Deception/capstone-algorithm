class ObservedConfiguration:
    def __init__(self, os, ports):
        self.OS = os
        self.Ports = ports
        # This will hold the TCs this OC can mask
        self.masked = [os]

class TrueConfiguration:
    def __init__(self, name, os, ports):
        self.name = name
        self.OS = os
        self.Ports = ports
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
    #print(systems)
    return systems

# This will create a configuration with the given attributes with the utility being scored by our miniMaxClass
def createConfiguration(attributes):
    VMName = attributes[0]
    OSName = attributes[1]
    listOfPorts = attributes[2:len(attributes)]
    listOfPorts = list(map(int, listOfPorts))
    #print(listOfPorts)
    return TrueConfiguration(VMName, OSName, listOfPorts)



possibleOS = ['Windows', 'Ubuntu', 'Metasploitable', 'Fedora']
possiblePorts = [5,80,443,21,22,110,995,143,993,25,26,587,3306] #list of common ports
def createOSN():
    allOC = []
    idx = 0;
    for os in possibleOS:
        #print(os)
        myOC = ObservedConfiguration(os,possiblePorts[idx])
        allOC.append(myOC)
        idx = idx+1
        #print(myOC)
    return allOC


def networkToText(tsn, osn):
    return 0









