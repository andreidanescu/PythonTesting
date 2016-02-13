import webbrowser
import time

totalBreaks = 3
breakCount = 0

#for x in range(0, 4):
while(breakCount < totalBreaks):
    time.sleep(5)
    webbrowser.open("https://en.wikipedia.org/wiki/Giant_panda")
    breakCount = breakCount + 1

    
    

