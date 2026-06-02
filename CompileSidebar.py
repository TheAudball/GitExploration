import DirectoryStructure as ds
import MarkdownTools as md

RepoName = ''
# 4 spaces per nesting level — renders as a nested list on GitHub wikis
# more reliably than tabs (and stays under the indented-code-block threshold)
INDENT = '    '

def MakeSideBar(root:str,optionFileName:str="options.py"):
    directory = ds.buildDirStruct(root,optionFileName)
    sidebar = ''
    for item in directory["entries"]:
        if isinstance(directory.get(item), dict):
            subDict = directory[item]
            titleLvl = 1
            if subDict["options"]["title_level"] == 0:
                pass
            else:
                titleLvl = subDict["options"]["title_level"]
            sidebar += ('#' * titleLvl) + ' '
            if subDict.get("page"):
                title = md.GenerateLink(subDict["page"], RepoName)
            else:
                title = item
            sidebar += title + '\n'
            sidebar += MakeSection(directory[item])
            sidebar += '\n\n'
    return sidebar




def MakeSection(sectionDict:dict,indentLvl:int=0):
    indent = INDENT * indentLvl
    section = ''
    ordered = sectionDict["options"]["ordered"]
    if ordered:
        bullet = '1.'
    else:
        bullet = '-'
    for entry in sectionDict["entries"]:
        if isinstance(sectionDict.get(entry), dict):
            subDict = sectionDict[entry]
            if subDict["options"]["dropdown"]:
                if subDict.get("page"):
                    title = md.HtmlLink(subDict["page"], RepoName)
                else:
                    title = entry
                section += md.GenerateDropdown(title,MakeSection(sectionDict[entry], 0))
            else:
                if subDict.get("page"):
                    title = md.GenerateLink(subDict["page"], RepoName)
                else:
                    title = entry
                section += f'{indent}{bullet} {title}\n'
                section += MakeSection(sectionDict[entry], indentLvl + 1)
        else:
            section += f'{indent}{bullet} {md.GenerateLink(entry, RepoName)}\n'
    return section
