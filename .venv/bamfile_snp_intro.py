#chap 4 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-5-2025
#Last mod: 1-5-2025

import pysam

#open BAM file
bamfile = pysam.AlignmentFile("example.bam","rb")

#iterate over reads and identify SNPs
alignments = read.get_aligned_pairs(matches_only=true,with_seq=True)
print(f"SNP detected:{ref_seq} to {read.query_sequence[query_pos]} at position {ref_pos}")