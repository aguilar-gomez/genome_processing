# genome_processing

Assembly with supernova (10x Genomics)
1. Unzip reference
2. Rename scaffolds, index and make windows with  process_newgenome.sh
3. Map reads using bwa
4. Calculate coverage per window using sam2bamWin.sh
5. Identify half Coverage scaffold with script Coverage.py, which uses bwa alignments
6. Extract scaffolds from fasta and blast these scaffolds against the whole genome, for this, make the genome a blast database first with blast_halfcov.sh
7. Select which scaffold to remove using the blast results and script *remove_scaffolds.py*
8. Remove scaffolds from assembly using filter_fasta_by_list_of_headers.py. This last script was not written by me, I got it from bioinformatics stackexchange (https://bioinformatics.stackexchange.com/questions/3931/remove-delete-sequences-by-id-from-multifasta)
9. Check removal of half coverage scaffolds and remove manually if needed (see section CHECK REMOVAL OF HALF COV CAFFOLDS)
10. Remove scaffolds that are just N with removeNscaff.py 
11. Run BUSCO
