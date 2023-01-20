#Remove short sequences taken from  BioStars
$1=200
$2=input.fasta
$3=output.fasta

awk -v min=$1 'BEGIN {RS = ">" ; ORS = ""} length($2) >= min {print ">"$0}' $2 > $3
