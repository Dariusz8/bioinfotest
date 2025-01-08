#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-7-2025
#Last mod: 1-7-2025

from Bio import SeqIO
from pyteomics import fasta,parser

#read the genomic and transcriptomic sequences
genome_seqs = SeqIO.to_dict(SeqIO.parse('genome.fasta', 'fasta'))
transcript_seqs = SeqIO.to_dict(SeqIO.parse('transcripts.fasta','fasta'))

#create custom protein database
proteins = parser.cleave(str(transcript_seq.seq),parser.expasy_rules['trypsin'])
fasta.write(protein,output_file,header=transcript_id)