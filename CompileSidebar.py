import DirectoryStructure as ds

def MakeSideBar(root):
    pass

def GenerateLink(pageFile:str,repoName:str):
    pageName = pageFile.replace('.md','')
    webLink = f"github.com/{repoName}/wiki/{pageName}"
    displayName = pageName.replace('-',' ')
    markdownLink = f'[{displayName}]({webLink})'
    return markdownLink
