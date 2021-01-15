#!/usr/bin/env python3
# coding: utf-8
# Author : Diana Aguilar

import pandas as pd 
import warnings 
warnings.filterwarnings('ignore')
 
'''Read data
halfcov_BLAST_hits: a tabular file that contains blast hits with the columns "reference","query","identity","length","qstart","qend"
assembly_scaffold.length: a tabular file that contains the scaffold names and the lengths
'''
blast2=pd.read_table("halfcov_BLAST_hits",header=None) 
blast2.columns=["reference","query","identity","length","qstart","qend"]  
chrs=pd.read_table("assembly_scaffold.length",header=None) 
chrs.columns=["chr","length"] 

#Dictionary of scaffolds and lengths
dic_chr=chrs.set_index('chr').T.to_dict() 
 
#Remove hits of scaffolds to itself. We are interested in hits of different scaffolds that might be duplicated 
blast_filter2=blast2[blast2["reference"]!=blast2["query"]]
 
#Get lengths of scaffolds 
blast_filter2["qlength"]=[dic_chr[x]["length"] for x in blast_filter2["query"]] 
blast_filter2["rlength"]=[dic_chr[x]["length"] for x in blast_filter2["reference"]]
 
#Percent of scaffold covered by the alignment 
blast_filter2["qpercent"]=blast_filter2.length/blast_filter2.qlength*100 
blast_filter2["rpercent"]=blast_filter2.length/blast_filter2.rlength*100
 
#Select if identity is more that %99 
blast_identity=blast_filter2[blast_filter2["identity"]>99]
 
#Find scaffolds to remove, the ones that are shorter: 
#Select query when shorter than reference 
remove_sca2=blast_identity[blast_identity.qlength<blast_identity.rlength]["query"].unique() 
#Select reference when is shorter than query 
rem2=blast_identity[blast_identity.qlength>blast_identity.rlength]["reference"].unique() 
#Join lists of all the scaffold we are going to delete
remove2=list(set(list(rem2)+list(remove_sca2)))
 
thefile = open('removescaffolds.txt', 'w') 
 
for item in remove2: 
    print(item) 
    thefile.write(item+"\n") 
    
thefile.close()
 
