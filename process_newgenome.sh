#!/bin/sh
#export samtools and bedtools
 
#$1=original_fasta_supernova_output.fasta 
#$2=new_fasta.fasta 
#$3=name 
 
#Rename chromosomes 
#awk '/^>/{print ">chr"++i;next}{print}'<$1>$2 
 
#Bwa index 
#bash bwa.index.sh  $2 
bwa index #2
 
#Samtools index, chr length, for windows 
samtools faidx $2 
cut -f1-2 $2.fai>$3.length 
bedtools makewindows -g $3.length -w 100000 -s 10000 > $3.windows.bed 
