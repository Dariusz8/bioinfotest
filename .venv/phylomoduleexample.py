#ending chapter 1 bioinfo practical approach
#Dariusz Czeczuk
#Start date: 1-1-2025
#Last mod: 1-1-205
from copyreg import constructor

from scipy.spatial import distance_matrix
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo

#calculate the distance matrix
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)

#construct phylogenetic tree
constructor = DistanceTreeConstructor()
phylo_tree = constructor.upgma(distance_matrix)

#visualize a tree
Phylo.draw(phylo_tree)

