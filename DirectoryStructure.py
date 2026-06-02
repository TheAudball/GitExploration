import os
import sys
import ast

DEFAULT_OPTIONS = {"dropdown": False, "order": ["*"], "title_level": 0, "ordered":False}


def buildDirStruct(rootPath:str,optionFileName:str="options.py"):
    dirstruct = {"name":rootPath}
    directory = os.scandir(rootPath)
    entryList = []
    for entry in directory:
        if entry.name == "__pycache__" or entry.name.startswith("."):
            continue
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

    optionsPath = os.path.join(rootPath, optionFileName)
    if os.path.exists(optionsPath):
        with open(optionsPath) as f:
            module = ast.parse(f.read())
        options = {}
        for node in module.body:
            if (isinstance(node, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == "options"
                            for t in node.targets)):
                options = ast.literal_eval(node.value)
        # fill in any keys missing from DEFAULT_OPTIONS without overriding
        # the values the file already defines, and persist if anything changed
        merged = {**DEFAULT_OPTIONS, **options}
        if merged != options:
            with open(optionsPath, "w") as f:
                f.write(f"options = {merged!r}\n")
        dirstruct["options"] = merged
    else:
        with open(optionsPath, "w") as f:
            f.write(f"options = {DEFAULT_OPTIONS!r}\n")
        dirstruct["options"] = dict(DEFAULT_OPTIONS)

    dirstruct["entries"] = OrderEntries(dirstruct["entries"],
                                        dirstruct["options"]["order"])

    return dirstruct

def OrderEntries(entryList,orderList):
    sortedList = []
    wildcardUsed = False
    for item in orderList:
        if item == '*':
            if wildcardUsed:
                continue
            wildcardUsed = True
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
