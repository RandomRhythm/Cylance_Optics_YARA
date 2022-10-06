import clr
clr.AddReference('IronPython.StdLib')
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
print (os.path.dirname(os.path.realpath(__file__)))
clr.AddReference('libyara.NET.dll')
import libyaraNET

dirName = "c:\\"
def YARAscan(strFilePath):
    #print(strFilePath)
    file = "myrule.yara" #yara rule name included in the package
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)),file)
    #print(file)
    try:
        matches = libyaraNET.QuickScan.File(strFilePath, os.path.join(dirpath, file))

        for match in matches:
            print(str(strFilePath) + "|" + str(match))
            #unique name for each file copy
    except Exception as e:
        print >> sys.stderr, str(e) + "|" + strFilePath



for (dirpath, dirnames, filenames) in os.walk(dirName):
    for file in filenames:
        scanPath = os.path.join(dirpath, file)
        YARAscan(scanPath)

