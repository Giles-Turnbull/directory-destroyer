import os
import time
import random

from numpy import full
import pywintypes, win32file, win32con, random

#pip install pywin32

def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)
    win32file.SetFileTime(winfile, wintime, None, None)
    winfile.close()

extensionTypes = ["aif", "au", "avi", "bat", "bmp", "java", "csv", "cvs", "dbf", "dif", "doc", "docx", "eps", "exe", "fm3", "gif", "hqx", "htm", "html", "jpg", "jpeg", "mac", "map", "mdb", "mid", "midi", "mov", "qt", "mtb", "mtw", "pdf", "p65", "t65", "png", "ppt", "pptx", "psd", "psp", "qxd", "ra", "rtf", "sit", "tar", "tif", "txt", "wav", "wk3", "wks", "wpd", "wp5", "xls", "xlsx", "zip"]
start_time, fol, storepaths, loop, count, folpathcount = time.time(), [], [], False, 0, -1
folpaths = ["C:/example/dir/"] #desried drive to destroy
storepaths.append(folpaths[0])
while loop != True:
    try: spath = folpaths[0]
    except: loop = True
    try:
        file = os.listdir(spath)
        for i in file:
            if "." not in i:
                folpaths.append(spath + i + "/")
                storepaths.append(spath + i + "/")
        try: del folpaths[0]
        except: loop = True
    except:
        try: del folpaths[0]
        except: loop = True
print(storepaths)
#--------------------------------------------------------------------------------
for path in storepaths:
    for i in range(10): #desired amount of files added
        NewFileName = ""
        for x in range(15): NewFileName = NewFileName + chr(random.randint(97, 122))  #extra bit of code for directory destroyer
        fileExtension = extensionTypes[random.randint(0, len(extensionTypes) - 1)]
        try: 
            fullPath = path + NewFileName + "." + fileExtension
            try: 
                woopie = open(fullPath, "w").close()
                newtime = random.randint(1000000000, 9999999999)
                os.utime(fullPath, (newtime, newtime))
                newtime = random.randint(1000000000, 9999999999)
                changeFileCreationTime(fullPath, newtime)
            except: print(fullPath + " - something went wrong with this file.")
        except: expen = "" #useless code
print("--- %s seconds ---" % (time.time()-start_time))
