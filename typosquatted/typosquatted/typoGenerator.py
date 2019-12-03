import sys
import json

def generateTypos(site: str):
    # if len(sys.argv) < 2:         # not being used when being called from nodeConnection, replaced with similar
    #     print("missing website")
    #     sys.exit(0)

    addr = site
    typos = set()


    if len(addr.split(".")) < 3:
        addr = "www." + addr
    
    addrSubDomains = ".".join(addr.split(".")[0:-2]) + "."
    addrName = addr.split(".")[-2]
    addrTopDomain = "." + addr.split(".")[-1]
    addrName += addrTopDomain
    # 1) missing dot typos
    typos.add(addrSubDomains[:-1] + addrName) 
    # 2) Character-omission typos 
    for i in range(0,len(addrName)):
        typos.add(addrSubDomains + addrName[:i] + addrName[i+1:])

    # 3) Character-permutation typos
        for i in range(0,len(addrName) - 1):
            if (addrName[i] == addrName[i + 1] or addrName[i] == '.'):
                continue
            typos.add(addrSubDomains + addrName[:i] + addrName[i+1] + addrName[i] + addrName[i+2:])

    # 4) Character-replacement typos
    # adjacency dictonary
    adjacencyFile = open("adjacency.json")
    adjacencyDict = json.load(adjacencyFile)

    for i in range(len(addrName)):
        if not addrName[i] in adjacencyDict.keys():
            continue
        for j in adjacencyDict[addrName[i]]:
            typos.add(addrSubDomains + addrName[:i] + j + addrName[i+1:])

    # 5) Character-insertion typos
    # the definition for this one was slightly unclear might need to be adjusted

    for i in range(len(addrName)):
        charsadded = []
        typos.add(addrSubDomains + addrName[:i+1] + addrName[i] + addrName[i+1:])
        if addrName[i] in adjacencyDict.keys():
            for j in adjacencyDict[addrName[i]]:
                charsadded.append(j)
                typos.add(addrSubDomains + addrName[:i+1] + j + addrName[i+1:])
        if i+1 < len(addrName) and addrName[i+1] in adjacencyDict.keys():
            for j in adjacencyDict[addrName[i+1]]:
                if not j in charsadded:  
                    typos.add(addrSubDomains + addrName[:i+1] + j + addrName[i+1:])

    adjacencyFile.close()
    return list(typos)

print(generateTypos(sys.argv[1]))
