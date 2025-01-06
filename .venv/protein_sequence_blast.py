#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-6-2025
#Last mod: 1-6-2025

from Bio.Blast import NCBIWWW, NCBIXML

# Example protein sequence using Cholesterol 25-hydroxylase https://www.uniprot.org/uniprotkb/O95992/entry#sequences
protein_sequence = 'MSCHNCSDPQVLCSSGQLFLQPLWDHLRSWEALLQSPFFPVIFSITTYVGFCLPFVVLDILCSWVPALRRYKIHPDFSPSAQQLLPCLGQTLYQHVMFVFPVTLLHWARSPALLPHEAPELLLLLHHILFCLLLFDMEFFVWHLLHHKVPWLYRTFHKVHHQNSSSFALATQYMSVWELFSLGFFDMMNVTLLGCHPLTTLTFHVVNIWLSVEDHSGYNFPWSTHRLVPFGWYGGVVHHDLHHSHFNCNFAPYFTHWDKILGTLRTASVPAR'

# Perform BLAST search
result_handle = NCBIWWW.qblast('blastp', 'nr', protein_sequence)

# Parse BLAST output
blast_record = NCBIXML.read(result_handle)

# Close the result handle
result_handle.close()

# Examine top results
if blast_record.alignments:
    top_hit = blast_record.alignments[0]
    hsp = top_hit.hsps[0]  # Get the first high-scoring pair
    print("Alignment:")
    print(f"Sequence: {hsp.sbjct}")
    print(f"Length: {hsp.align_length}")
    print(f"E-value: {hsp.expect}")
else:
    print("No alignments found.")
