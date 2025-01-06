#chap 3 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-4-2025
#Last mod: 1-4-2025
# TODO: revisit possible issue

from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq

# Define the query sequence
query_seq = Seq("AAAGGCTGTCGTAAGCCTT")

# Perform BLAST search against the NCBI nucleotide database with BLASTN
result_handle = NCBIWWW.qblast("blastn", "nt", query_seq)

# Read BLAST results
blast_records = NCBIXML.parse(result_handle)

# Iterate through BLAST records
for blast_record in blast_records:
    print("Alignment:")
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print("Sequence:", alignment.title)
            print("Length:", alignment.length)
            print("E-value:", hsp.expect)
            print(hsp.query[0:75] + "...")
            print(hsp.match[0:75] + "...")
            print(hsp.sbjct[0:75] + "...")
