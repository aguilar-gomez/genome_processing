#!/usr/bin/env python
# coding: utf-8


from Bio.Seq import Seq
from Bio import SeqIO
import sys 
 
INPUT  = sys.argv[1] 
OUTPUT = sys.argv[2] 


allseq=[]
for seq_record in SeqIO.parse(INPUT, "fasta"):
    #Strip any Ns at the beginning or end of the sequence
    seq_record.seq=seq_record.seq.strip("N")
    #Replace 100 Ns with 10 Ns
    seq_record.seq=Seq("N"*10).join(seq_record.seq.split("N"*100))
    #Save all sequences
    allseq.append(seq_record)
#Write new file
SeqIO.write(allseq, OUTPUT, "fasta")

