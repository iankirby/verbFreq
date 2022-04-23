import re, subprocess, os, sys


def printOut(file_name):
    print(file_name)

name, path, file = sys.argv[1], sys.argv[2], sys.argv[3]

file_in=open(path+file,'r',encoding="utf8")
plain=file_in.read()
file_in.close()

plain=re.split("<body>",plain)
plain=plain[1]
plain=re.split("\n",plain)

print(len(plain))