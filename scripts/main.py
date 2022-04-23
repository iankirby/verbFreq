import re, subprocess, os, sys




def decidePath(var):
    if (var=="Greek" or var=="greek"):
        title="Greek"
        path="../Files/Greek/"
        # print(title)
    elif (var=="Latin" or var=="latin"):
        title="Latin"
        path="../Files/Latin/"
        # print(title)
    elif(var=="Old English"):



if(len(sys.argv)<2):
    print("Forgot command line argument")
else:
    if(sys.argv[1]=="Old"):
        var="Old English"
        decidePath()
    elif():
    var=sys.argv[1]
    decidePath(var)
        