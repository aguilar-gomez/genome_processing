# genome_processing

Assembly with supernova (10x Genomics)
1. Unzip reference
2. Rename scaffolds, index and make windows with  *process_newgenome.sh*
3. Map reads using bwa
4. Calculate coverage per window using *sam2bamWin.sh*
5. Identify half Coverage scaffold with script *coverage.py*, which uses bwa alignment output
6. Extract scaffolds from fasta and blast these scaffolds against the whole genome, for this, make the genome a blast database first with *blast_halfcov.sh*
7. Select which scaffold to remove using the blast results and script *remove_scaffolds.py*
8. Remove scaffolds from assembly using *filter_fasta_by_list_of_headers.py*. This last script was obtained from bioinformatics stackexchange (https://bioinformatics.stackexchange.com/questions/3931/remove-delete-sequences-by-id-from-multifasta)
9. Remove scaffolds that are just N with *removeNscaff.py* 
10. Run BUSCO


Note: Most of the codes here do not take arguments, if somebody would want to use them, please submit and issue and I will make them more universal. You can also use them, but change the names of the files that it takes as an input. Sorry for the inconviniences (and lazy coding).
