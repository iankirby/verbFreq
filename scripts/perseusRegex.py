import re, subprocess, os, sys

name, path, file = sys.argv[1], sys.argv[2], sys.argv[3]

file_in=open(path+file,'r',encoding="utf8")
plain=file_in.read()
file_in.close()

plain=re.split("<body>",plain)
plain=plain[1]
plain=re.split("\n",plain)

print("Length:\t"+str(len(plain)))

i=0

str=""

while (i<len(plain)):
# while (i<10):
    curr=plain[i]
    if (re.search("postag=\"v",curr)):
      
        form=re.search("form=\"[^\"]*\"",curr)
        form=form.group()
        # form=re.search("\"[^\"\]*\"",form)
        # form=form.group()
        

        lemma=re.search("lemma=\"[^\"]*\"",curr)
        lemma=lemma.group()
        # lemma=re.search("\"[^\"]*\"",lemma)
        # lemma=lemma.group()

        postag=re.search("postag=\"[^\"]*\"",curr)
        postag=postag.group()
        # postag=re.search("\"[^\"]*\"",postag)
        # postag=postag.group()

        relation=re.search("relation=\"[^\"]*\"",curr)
        relation=relation.group()
        # relation=re.search("\"[^\"]*\"",relation)
        # relation=relation.group()

        str=str+"\n"+lemma+", "+form+", "+postag+", "+relation+", "+file+", "+curr

    i=i+1
str="lemma, form, tag, relation, file, full_line"+str
fl_out=open("../Files/"+name+".txt",'a+',encoding="utf8")
fl_out.write(str)
fl_out.close()