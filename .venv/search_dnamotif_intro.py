#chap 3 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-3-2025
#Last mod: 1-3-2025

import re

#define a DNA sequence
dna_sequence = "ATGCGTAATAGCTAGTTTACATAGGGTAC"

#define motif patern
motif_patern = "TATA"

#search for the motif in the sequence
motif_locations = [match.start() for match in re.finditer(motif_patern, dna_sequence)]

#output motif locations
print("Motif found at positions:",motif_locations)