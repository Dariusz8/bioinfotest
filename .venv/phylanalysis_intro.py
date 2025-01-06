#chap 3 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-4-2025
#Last mod: 1-4-2025

from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO

#load multiple sequence alignment file
alignment = AlignIO.read("example_msa.phy","phylip")

#calculate distance matrix
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)

#construct phylogenetic tree using UPGMA alogirthm
constructor = DistanceTreeConstructor()
upgma_tree = constructor.upgma(distance_matrix)

#visualize tree
Phylo.draw(upgma_tree)