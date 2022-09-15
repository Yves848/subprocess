import subprocess
import sys


class package:
    def __init__(self, line):
        self.name = line[iNom:iID]
        self.id = line[iID: iVersion]
        self.version = line[iVersion: iSource]
        # self.disponible = line[iDisponible: iSource]


def searchPackages(name):
    l = []
    scmd = f'winget search {name}'
    p = subprocess.run(scmd, capture_output=True, shell=True)
    out = p.stdout.decode('utf-8')
    sOut = out.split('\r')
    i = 0
    while not sOut[i].startswith('Nom'):
        i += 1

    # Déterminer les positions des champs
    global iNom
    iNom = sOut[i].index('Nom')
    global iID
    iID = sOut[i].index('ID')
    global iVersion
    iVersion = sOut[i].index('Version')
    # global iDisponible
    # iDisponible = sOut[i].index('Disponible')
    global iSource
    iSource = sOut[i].index('Source')

    i += 2

    while i < len(sOut)-2:
        s = sOut[i].replace('\n', '')
        aPackage = package(s)
        l.append(aPackage)
        i += 1

    return l


def getUpgradables():
    l = []
    p = subprocess.run(['winget', 'upgrade'], capture_output=True)
    out = p.stdout.decode('utf-8')
    sOut = out.split('\r')
    i = 0
    while not sOut[i].startswith('Nom'):
        i += 1

    # Déterminer les positions des champs
    global iNom
    iNom = sOut[i].index('Nom')
    global iID
    iID = sOut[i].index('ID')
    global iVersion
    iVersion = sOut[i].index('Version')
    global iDisponible
    iDisponible = sOut[i].index('Disponible')
    global iSource
    iSource = sOut[i].index('Source')

    i += 2

    while i < len(sOut)-2:
        s = sOut[i].replace('\n', '')
        aPackage = package(s)
        l.append(aPackage)
        i += 1

    return l


if __name__ == "__main__":
    # aList = getUpgradables()
    aList = searchPackages('notepad')
    for item in aList:
        print(item.id)
