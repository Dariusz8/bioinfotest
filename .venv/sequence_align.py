#chap 2
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

#create sequence records
record1 = SeqRecord(Seq("ATGCGTA"),id="seq1")
record2 = SeqRecord(Seq("ATGCGT-"),id="seq2")
record3 = SeqRecord(Seq("ATGGGTA"),id="seq3")

#align sequences
alignment = MultipleSeqAlignment([record1, record2, record3])

#display alignment
print(alignment)
