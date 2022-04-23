#!/usr/bin/env Rscript
args=commandArgs(trailingOnly=TRUE)

library(plyr)
library(stringr)

lang=args[1]
# lang=str_sub(lang,2,-1)

file_name=paste("../Files/",lang,".csv",sep='')

x <-read.csv(file_name, header=TRUE)

y=ddply(x, .(lemma,tag))
y= y[y$lemma!='form',]
y=y[y$lemma!=' form',]
out_name1=paste("../Files/",lang,"_full_aggr.csv",sep='')
write.csv(y, file=out_name1)

z=ddply(x, .(lemma,tag), summarize, Total=sum(lemma!=''))
out_name2=paste("../Files/", lang,"_summarized.csv",sep='')
z=z[z$lemma!='form',]
z=z[z$lemma!=' form',]
write.csv(z,file=out_name2)


if (args[1]=="Latin"){
volo_all=y[y$lemma=='lemma=volo1',]
write.csv(volo_all, file="../Files/volo_all.csv")

volo_summarized=z[z$lemma=='lemma=volo1',]
write.csv(volo_summarized, file="../Files/volo_summarized.csv")
}
