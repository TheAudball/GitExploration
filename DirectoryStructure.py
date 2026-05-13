import os
import sys

root = sys.argv[1] 
print(sys.argv[1])

def buildDirStruct(rootPath:str,optionFileName:str="options.txt"):
    dirstruct = {}
    dictList = []
    DirWalk = os.walk(rootPath)
    for path, dirs, files in DirWalk:
        subDict = {}
        if path == rootPath:
            subDict["name"] = "root"
            subDict["path"] = path
        else:
            subDict["name"] = path
        for name in dirs:
            subDict[name] = None
        for name in files:
            subDict[name] = os.path.join(path,name)
        dictList.append(subDict)
    return dictList


if __name__ == "__main__":
   DirStructure =  buildDirStruct(root)
   print(DirStructure)
