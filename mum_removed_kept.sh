#!/bin/sh
#$1= name
#$2= fasta file assembly
#$3= outdir
nucmer -t 6 -c 1000 -l 50  -p $1 removed_versicolor_scaffolds.fasta kept_versicolor_scaffolds.fasta
delta-filter -i 90 -l 1000 $1.delta > $1.filter90.delta
mummerplot --png --large -p $1 $1.filter90.delta

