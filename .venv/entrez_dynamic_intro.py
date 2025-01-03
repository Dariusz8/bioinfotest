#chap 2 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio import Entrez
from Bio import SeqIO

#define a list of NCBI accession numbers
accession_numbers = ["NM_001200014", "NM_001202473", "NM_002074"]

#set email
Entrez.email = "dariusz.czeczuk@hotmail.com"

#create an empty list to store sequences
sequences = []

#loop over the accession numbers to retrieve the sequences
for accession in accession_numbers:
    handle = Entrez.efetch(db="nucleotide",id=accession,rettype="fasta",retmode="text")
    record = SeqIO.read(handle,"fasta")
    handle.close()
    sequences.append(record)

for seq_record in sequences:
    print(f">{seq_record.id}")
    print(seq_record.seq)