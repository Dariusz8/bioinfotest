#chap 4 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-5-2025
#Last mod: 1-5-2025

from Bio import SeqIO
import matplotlib.pyplot as plt

#read genomic DNA sequence from FASTA file
record = SeqIO.read("example.fasta","fasta")
sequence=  record.seq

#calculate GC content
gc_content = (sequence.count('G') + sequence.count('C'))/len(sequence)*100

#create plot of GC content
plt.figure(figsize=10,2)
plt.plot(range(len(sequence)),[gc_content]*len(sequence),label='GC Content')
plt.legend()
plt.title(f'GC Content of {record.id}')
plt.xlabel('Position in sequence')
plt.ylabel('%GC Content')
plt.show()