# genome_processing

Assembly with supernova (10x Genomics)
1. Unzip reference
2. Rename scaffolds, index and make windows with  *process_newgenome.sh*
3. Map reads using bwa
4. Calculate coverage per window using *sam2bamWin.sh*
5. Identify half Coverage scaffold with script *coverage.py*, which uses bwa alignment output
6. Extract scaffolds from fasta and blast these scaffolds against the whole genome, for this, make the genome a blast database first with *blast_halfcov.sh*
7. Select which scaffold to remove using the blast results and script *remove_scaffolds.py*
8. Do whole scaffold alignments with MUMmer *mum_removed_kept.sh*
9. Remove scaffolds from assembly using *filter_fasta_by_list_of_headers.py*. This last script was obtained from bioinformatics stackexchange (https://bioinformatics.stackexchange.com/questions/3931/remove-delete-sequences-by-id-from-multifasta)
10. Remove scaffolds that are just N with *removeNscaff.py* 
11. Run BUSCO
12. For submission to NCBI database they requested to trim all leading and traling Ns from all the sequences. They also have an option to indicate the size of the gap in terms of Ns. Supernova default output inserts 100 Ns in every gap, we replaced 100 Ns for 10 Ns because that is the maximum number that NCBI WGS submission allows. We used the script *supernova2NCBI.py* for this processing


Note: Most of the codes here do not take arguments, if somebody would want to use them, please submit and issue and I will make them more universal. You can also use them, but change the names of the files that it takes as an input.
