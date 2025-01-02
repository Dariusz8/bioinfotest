#chap 2
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio import ExPASy
from Bio import SwissProt

#fetch the record for a given UniProt ID
accession = "P00533"
handle = ExPASy.get_sprot_raw(accession)
record = SwissProt.read(handle)

#print out the protein seq
print(f"Protein sequence for {accession}: {record.sequence}")