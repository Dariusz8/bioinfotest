#chap 3 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-3-2025
#Last mod: 1-3-2025

from Bio import Align

#initialize the aligner
aligner = Align.PairwiseAligner()
aligner.mode = 'global'

#define 2 sequences
seq1 = "GACTTAC"
seq2 = "CGTGAATTCAT"

#perform global alignment
alignment = aligner.align(seq1,seq2)

#print the best global alignment
print(alignment[0])

#initialize local aligner
local_aligner = Align.PairwiseAligner()
local_aligner.mode = "local"

#perform local alignment
local_alignment = local_aligner.align(seq1,seq2)

#print best local alignment
print(local_alignment[0])