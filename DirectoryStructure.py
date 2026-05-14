import os
import sys


def buildDirStruct(rootPath:str,optionFileName:str="options.txt"):
    dirstruct = {"name":rootPath}
    directory = os.scandir(rootPath)
    entryList = []
    for entry in directory:
        if entry.is_dir():
            dirstruct[entry.name] = buildDirStruct(os.path.join(rootPath,entry.name),optionFileName)
        entryList.append(entry.name)
    dirstruct["entries"] = entryList
    return dirstruct


if __name__ == "__main__":
    root = sys.argv[1] 
    DirStructure =  buildDirStruct(root)
    print(DirStructure)
