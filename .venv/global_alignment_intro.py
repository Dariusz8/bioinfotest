#chap 3 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-3-2025
#Last mod: 1-3-2025

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq

#define two sequences to be aligned
seq1 = "AGTTGTTAGTCTACGT"
seq2 = "CGTTGCATGTCGTACG"

#perform global alignment
alignments = pairwise2.align.globalxx(seq1,seq2)

#print first alignment
print(format_alignment(*alignments[0]))

print("PART 2")

seq3 = Seq("ACCGT")
seq4 = Seq("ACG")

#peform global alignment using default parameters
alignments = pairwise2.align.globalxx(seq3,seq4)

#print best alignment
best_alignment = alignments[0]
print(pairwise2.format_alignment(*best_alignment))