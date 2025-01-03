#chap 2 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio.Seq import Seq

#crete Seq object
dna_sequence = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

#perform seq operation
print(f"Complement:{dna_sequence.complement()}")
print(f"Reverse Complement:{dna_sequence.reverse_complement()}")
print(f"RNA transcript:{dna_sequence.translate()}")