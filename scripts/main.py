import re, subprocess, os, sys, csv

def openEng(name,path):
    out_name="../Files/"+name+".txt"
    # print(out_name)
    fl_out=open(out_name,'r+',encoding="utf-8")
    fl_out.truncate(0)
    fl_out.close()

    dir=os.listdir(path)
    # print(dir)
    
    i=0
    while(i<len(dir)):
        subprocess.call(['perl','oe.pl',name, path, dir[i]])
        # i=i+1
        break

def getVolo():
    out_name="../Files/Volo.txt"

#For greek and latin
def openGreekLatin(name,path):
    
    #truncuate the file first
    out_name="../Files/"+name+".txt"
    fl_out=open(out_name,"r+",encoding="utf8")
    fl_out.truncate(0)
    fl_out.close()

    dir=os.listdir(path)

    i=0
    while(i<len(dir)):
        subprocess.call(['python','perseusRegex.py',name,path,dir[i]])
        i=i+1
    subprocess.call(['bash','../Files/toCSV.sh',out_name])


#Which path it goes through
def decidePath(var):
    if (var=="Greek" or var=="greek"):
        openGreekLatin("Greek","../pre/Greek/")
    elif (var=="Latin" or var=="latin"):
        openGreekLatin("Latin","../pre/Latin/")
        # print(title)
    elif(var=="Old English"):
        openEng(var,"../pre/OldEnglish/")
    elif(var=="Middle English"):
        openEng(var,"../pre/MiddleEnglish/")
    elif(var=="Early Modern English"):
        openEng(var,"../pre/EarlyModernEnglish/")
    else:
        print("don't know")

if(len(sys.argv)<2):
    print("Forgot command line argument")
else:
    if(sys.argv[1]=="Old"):
        decidePath("Old English")
    elif(sys.argv[1]=="Middle"):
        decidePath("Middle English")
    elif(sys.argv[1]=="Latin" and sys.argv[2]=="volo"):
        getVolo()
    else:
        decidePath(sys.argv[1])
        