from os import walk
import os


if not os.path.exists(writePath):
    os.makedirs(writePath)

def clamp(input, LB, UB):
    val = input
    if (input < LB):
        val = LB
    elif (input > UB):
        val = UB
    return val
def getFiles(path, addition_to_path = ""):
    f = []
    d = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        d.extend(dirnames)
        print("Folder names = ", dirnames)
        print("Filenames = ", filenames)
        for i in range(len(dirnames)):
            newpath = (writePath + "\\" + addition_to_path + "\\" + d[i])
            if not os.path.exists(newpath):
                os.makedirs(newpath)
        for i in range(len(filenames)):

            fileObj = open(path + "\\"+filenames[i], mode="rb")
            filetext = fileObj.read()
            
            tempdata = list(filetext)
            #for j in range(len(tempdata)):
                #tempdata[j] = clamp(tempdata[j] + 5,0,255)
                #print(tempdata[j])
            filetext = bytes(tempdata)
            #filetext = fileObj.read()
            # Write to folder
            print("FN: " + writePath+addition_to_path+"\\"+filenames[i])

            writeObj = open(writePath+addition_to_path+"\\"+filenames[i],"wb")
            writeObj.write(filetext)

        break
    if (len(d) > 0):
        for i in range(len(d)):
            getFiles(path + "\\" + d[i], addition_to_path + "\\" +  d[i])
    
getFiles(mypath)
