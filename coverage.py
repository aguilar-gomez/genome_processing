#!/usr/bin/env python3
# coding: utf-8
# Author : Diana Aguilar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
 
def file2df(file):
    meanWindow=pd.read_table(file, header=None)
    #Keep scaffolds that have at least x windows >10Kb
    counts=meanWindow[0].value_counts()
    df=meanWindow[meanWindow[0].isin(counts[counts>10].index)]
    return df
#Read file, structure: chr, start, end, cov
guian=file2df("../../guian_fastq/new_pseudohap/guian_window")
chrs=guian.groupby([0])[1].max()+10000
a=chrs.index.to_series().str.rsplit('chr').str[-1].astype(int).sort_values()
chrs = chrs.reindex(index=a.index)

#Sort original data
guian["length"]=chrs[guian[0]].values
guian=guian.sort_values(["length",1],ascending=[False,True])

#Plot to see which is the range of half coverage
plt.rcParams["figure.figsize"] = (15,5)
ini=0
whiteandblue = ["white", "blue"]
wb = cycle(whiteandblue)
for len_ in chrs:
    len_+=ini
    plt.axvspan(ini/10000, len_/10000, facecolor=next(wb), alpha=0.1)
    ini=len_
plt.ylabel(r"$log_2$"+"(coverage per window)",size=20)
plt.scatter(range(len(guian)),guian[3],c="red",alpha=.1,s=1)
plt.title("Genome fixed pseudohap, reads used for assembly mapped",size=20)
plt.axis([0,len(guian),-4,1e6])
plt.show()
 
#Get Median of each scaffold (chr)
half_cov_remcon=guian.groupby([0])[3].median().between(2e5,5e5)
halfcoveragemore=chrs[half_cov_remcon].index
#Write file
thefile = open('halfcoverage.txt', 'w')
for item in halfcoveragemore:
    thefile.write(item+"\n")    
thefile.close()
