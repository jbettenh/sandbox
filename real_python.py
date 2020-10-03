
import os

with os.scandir('C:\Users\jbettenh\Documents') as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)