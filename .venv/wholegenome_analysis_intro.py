#chap 4 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-5-2025
#Last mod: 1-5-2025

import os

#define the command for read alignment usign BWA
bwa_command = "bwa mem -t 8 reference_genome.fasta read1.fastq read2.fastq > aligned_reads.sam"

#execute command
os.system(bwa_command)

#convert SAM to BAM, sort, and index using SAMtools
os.system("samtools view -Sb aligned_reads.sam > aligned_reads.bam")
os.system("samtools sort aligned_reads.bam -o sorted_aligned_reads.bam")
os.system("samtools index sorted_aligned_reads.bam")