#!/bin/sh
#Make database
makeblastdb -in guian_ph.fasta -title guian_assembly -dbtype nucl -out db_guian/guian_assembly
#Extract scaffolds from assembly
xargs samtools faidx guian_ph.fasta< halfcoverage.txt > half_cov.fasta
#blast
blastn -db /global/scratch/aguilar-gomez/ pident length qstart qend" -max_hsps 1 -out halfcov_BLAST_hits -max_target_seqs 3 -num_threads 20
