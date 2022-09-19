genome=$1
name=$2
samtools faidx $1
cut -f1-2 $genome.fai >$name.length
bedtools makewindows -g $name.length -w 100000 -s 10000 >${name}_windows.bed
