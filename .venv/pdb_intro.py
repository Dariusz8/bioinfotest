#chap 2 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio.PDB import PDBParser

#initialize parser
parser = PDBParser

#parse structure from a PDB file
structure = parser.get("example_structure","example.pdb")

#iterate through the atoms in the structure
print(f"Atom: {atom.name}, Coordinates:{atom.cord}")