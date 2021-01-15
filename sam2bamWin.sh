#!/bin/sh
#Export samtools 
for sam in *sam 
do 
    name=${sam%%_*} 
    echo $name 
    samtools view -Sb $sam |samtools sort - $name.sort 
    samtools index $name.sort.bam 
    samtools bedcov file.windows.bed $name.sort.bam > ${name}_window 
done 
