#chap 2
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio.Seq import Seq

#create DNA segment object
dna_sequence = Seq("ATGCGTA")

#transcribe DNA to mRNA
mRNA_sequence = dna_sequence.transcribe()

#translate mRNA to a protein sequence
protein_sequence = mRNA_sequence.translate()

#output the protein sequence

print(f"Protein sequence: {protein_sequence}")