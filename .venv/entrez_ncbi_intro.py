#chap 2 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio import Entrez
from Bio import SeqIO

#provide email to NCBI to use services
Entrez.email = "dariusz.czeczuk@hotmail.com"

#fetch seq from NCBI using an accession number
handle = Entrez.efetch(db="nucleotide", id="NC_005816",rettype="fasta",retmode="text")
record = SeqIO.read(handle,"fasta")
handle.close()
print(record)