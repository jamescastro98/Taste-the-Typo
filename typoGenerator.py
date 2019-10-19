import sys
import json

if len(sys.argv) < 2:
    print("missing webiste")
    sys.exit(0)

addr = sys.argv[1]
typos = []

# 1) Missing-dot typo
if (addr.startswith("www.")):
    typos.append(addr.replace(".","", 1))
else:
    addr = "www." + addr # if the webiste was entered without www. I add it
    typos.append("www" + addr)

# 2) Character-omission typos
addrName = addr.split(".")[1]
addrTopDomain = addr.split(".")[2]
for i in range(0,len(addrName)):
    typos.append("www." + addrName[:i] + addrName[i+1:] + "." + addrTopDomain)

# 3) Character-permutation typos
    for i in range(0,len(addrName) - 1):
        if (addrName[i] == addrName[i + 1]):
            continue
        typos.append("www." + addrName[:i] + addrName[i+1] + addrName[i] + addrName[i+2:] + "." + addrTopDomain)

# 4) Character-replacement typos
# adjacency dictonary
adjacencyFile = open("adjacency.json")
adjacencyDict = json.load(adjacencyFile)

for i in range(len(addrName)):
    for j in adjacencyDict[addrName[i]]:
        typos.append("www." + addrName[:i] + j + addrName[i+1:] + "." + addrTopDomain)

# 5) Character-insertion typos
# the definition for this one was slightly unclear might need to be adjusted
for i in range(len(addrName)):
    typos.append("www." + addrName[:i+1] + addrName[i] + addrName[i+1:] + "." + addrTopDomain)
    for j in adjacencyDict[addrName[i]]:
        typos.append("www." + addrName[:i+1] + j + addrName[i+1:] + "." + addrTopDomain)
adjacencyFile.close()
print(typos)
