def GenerateLink(pageFile:str,repoName:str):
    pageName = pageFile.replace('.md','')
    webLink = f"https://github.com/{repoName}/wiki/{pageName}"
    displayName = pageName.replace('-',' ')
    markdownLink = f'[{displayName}]({webLink})'
    return markdownLink

def HtmlLink(pageFile:str,repoName:str):
    pageName = pageFile.replace('.md','')
    webLink = f"https://github.com/{repoName}/wiki/{pageName}"
    displayName = pageName.replace('-',' ')
    htmlLink = f'<a href="{webLink}">{displayName}</a>'
    return htmlLink

def GenerateList(entryList:list[str],title:str='',Lvl:int=0,ordered:bool=False):
    markdownList = ''
    if title != '':
        markdownList = ('    ' * Lvl) + title + '\n'
        Lvl += 1
    if ordered:
        bullet = '1.'
    else:
        bullet = '-'
    for item in entryList:
        line = ('    ' * Lvl) + bullet + item + '\n'
        markdownList = markdownList + line
    return markdownList

def GenerateDropdown(title:str,content:str):
    htmlDropdown = f'<details><summary>{title}</summary>\n\n{content}\n</details>\n\n'
    return htmlDropdown
