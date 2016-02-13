import os


def renameFiles():
    # get file names
    fileList = os.listdir(r"C:\Users\Andrei\Desktop\prank")
    print(fileList)
    savePath = os.getcwd()
    print(savePath)
    os.chdir(r"C:\Users\Andrei\Desktop\prank")
    
    # rename filename
    for fileName in fileList:
        os.rename(fileName, fileName.translate(None, "0123456789"))
        

renameFiles()
