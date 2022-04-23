import re, subprocess, os, sys

def openDir(name,path):
    dir=os.listdir(path)
    
    if(name=="Greek" or name=="Latin"):
        i=0
        while(i<len(dir)):
            subprocess.call(['python','perseusRegex.py',name,path,dir[i]])
            i=i+1

    else:
        print("Still need to write English regexes")

def decidePath(var):
    if (var=="Greek" or var=="greek"):
        openDir("Greek","../pre/Greek/")
    elif (var=="Latin" or var=="latin"):
        openDir("Latin","../pre/Latin/")
        # print(title)
    elif(var=="Old English"):
        openDir(var,"../pre/OldEnglish")
    elif(var=="Middle English"):
        openDir(var,"../pre/MiddleEnglish")
    elif(var=="Early Modern English"):
        openDir(var,"../pre/EarlyModernEnglish")
    else:
        print("don't know")

if(len(sys.argv)<2):
    print("Forgot command line argument")
else:
    if(sys.argv[1]=="Old"):
        decidePath("Old English")
    elif(sys.argv[1]=="Middle"):
        decidePath("Middle English")
    else:
        decidePath(sys.argv[1])
        