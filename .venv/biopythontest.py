#Trying and looking into pandas while learning about bioinformatics
#Dariusz Czeczuk
#Start date: 11-02-2024
#Last mod: 11-02-2024

from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
from collections import Counter
import matplotlib.pyplot as plt


# Reading sequences from a FASTA file
sequences = [record.seq for record in SeqIO.parse('data/gene.fna', 'fasta')]

# Find the minimum sequence length
min_length = min(len(seq) for seq in sequences)

# Trim all sequences to the minimum length
sequences = [seq[:min_length] for seq in sequences]

# Create motif object and search for common motifs
motif_finder = motifs.create(sequences)
consensus = motif_finder.consensus

print(f"The consensus sequence is: {consensus}")

#find all instances of the consensus sequence within our set of sequences

instances = [str(sequence).count(str(consensus))for sequence in sequences]
frequencies = Counter(instances)

print(f"Frequencies of the consensus motif:{frequencies}")

#plot the frequency distribution of consensus motifs occurences
plt.bar(frequencies.keys(),frequencies.values())
plt.xlabel('Number of Occurences')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Consensus Motif Occurences')
plt.show()