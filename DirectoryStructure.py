import os
import sys


def buildDirStruct(rootPath:str,optionFileName:str="options.py"):
    dirstruct = {"name":rootPath}
    directory = os.scandir(rootPath)
    entryList = []
    for entry in directory:
        if entry.is_dir():
            dirstruct[entry.name] = buildDirStruct(os.path.join(rootPath,entry.name),
                                                   optionFileName)
        if entry.name == optionFileName:
            dirstruct["options"] = entry.name
        elif entry.name == (os.path.basename(rootPath) + ".md"):
            dirstruct["page"] = entry.name
        else:
            entryList.append(entry.name)
    dirstruct["entries"] = entryList
    return dirstruct

def OrderEntries(entryList,orderList):
    sortedList = []
    for item in orderList:
        if item == '*':
            for entry in entryList:
                if entry in orderList:
                    pass
                else:
                   sortedList.append(entry)
        elif item not in entryList:
            pass
        else:
            sortedList.append(item)
    for entry in entryList:
        if entry not in sortedList:
            sortedList.append(entry)
    return sortedList
            




if __name__ == "__main__":
    root = sys.argv[1] 
    DirStructure =  buildDirStruct(root)
    print(DirStructure)
