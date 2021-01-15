#!/usr/bin/env python3 
#I honeslty cannot remember if I coded this or if someone gave me this code, so author is unknown/uncertain
 
from Bio import SeqIO 
import sys 
 
INPUT  = sys.argv[1] 
OUTPUT = sys.argv[2] 
 
def main(): 
    records = SeqIO.parse(INPUT, 'fasta') 
    filtered = (rec for rec in records if any(ch != 'N' for ch in rec.seq)) 
    SeqIO.write(filtered, OUTPUT, 'fasta') 
 
if __name__=="__main__": 
    main() 
