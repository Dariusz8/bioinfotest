#chap 2
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio.PDB import PDBParser

#initialize a PDB parser
parser = PDBParser

#Parse the structure from a PDB file
structure = parser.get_structure("example","example.pdb")

#print out fist model's atoms
print(atom)

