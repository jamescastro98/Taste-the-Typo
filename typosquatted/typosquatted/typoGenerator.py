import sys
import json

def generateTypos(site: str):
    # if len(sys.argv) < 2:         # not being used when being called from nodeConnection, replaced with similar
    #     print("missing website")
    #     sys.exit(0)

    addr = site
    typos = set()

    # 1) Missing-dot typo
    if (addr.startswith("www.")):
        typos.add(addr.replace(".","", 1))
    else:
        typos.add("www" + addr)
        addr = "www." + addr # if the website was entered without www. I add it

    # 2) Character-omission typos
    addrName = addr.split(".")[1]
    addrTopDomain = addr.split(".")[2]
    for i in range(0,len(addrName)):
        typos.add("www." + addrName[:i] + addrName[i+1:] + "." + addrTopDomain)

    # 3) Character-permutation typos
        for i in range(0,len(addrName) - 1):
            if (addrName[i] == addrName[i + 1]):
                continue
            typos.add("www." + addrName[:i] + addrName[i+1] + addrName[i] + addrName[i+2:] + "." + addrTopDomain)

    # 4) Character-replacement typos
    # adjacency dictonary
    adjacencyFile = open("adjacency.json")
    adjacencyDict = json.load(adjacencyFile)

    for i in range(len(addrName)):
        for j in adjacencyDict[addrName[i]]:
            typos.add("www." + addrName[:i] + j + addrName[i+1:] + "." + addrTopDomain)

    # 5) Character-insertion typos
    # the definition for this one was slightly unclear might need to be adjusted

    for i in range(len(addrName)):
        charsadded = []
        typos.add("www." + addrName[:i+1] + addrName[i] + addrName[i+1:] + "." + addrTopDomain)
        for j in adjacencyDict[addrName[i]]:
            charsadded.append(j)
            typos.add("www." + addrName[:i+1] + j + addrName[i+1:] + "." + addrTopDomain)
        if i+1 < len(addrName):
            for j in adjacencyDict[addrName[i+1]]:
                if not j in charsadded:  
                    typos.add("www." + addrName[:i+1] + j + addrName[i+1:] + "." + addrTopDomain)

    adjacencyFile.close()
    return list(typos)

#print(generateTypos(sys.argv[1]))
