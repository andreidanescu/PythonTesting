import urllib

def readText():
    quotes = open("C:\Python27\TestCodeADR\Movies.txt")
    contentOfFile = quotes.read()
    #print(contentOfFile)
    quotes.close
    checkProfanity(contentOfFile)


def checkProfanity(textToCheck):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=friend"+textToCheck)
    output = connection.read()
    print(output)
    connection.close()
    #if "true" in output:
    #   print("ProfanityAllert")
    #elif "false" in output:
    #    print("This document is clean")
    #else:
    #    print("Could not scan document") 


readText()
