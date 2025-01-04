#chap 3 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-3-2025
#Last mod: 1-3-2025

from Bio import AlignIO

#read alignment file in PHYLIP format
alignment = AlignIO.read("examply.phy","phylip")

#inspect alignment
print(alignment)