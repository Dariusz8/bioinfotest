#trying to compare pt and ref seq
#Dariusz Czeczuk
#Start date: 1-1-2025
#Last mod: 1-1-205

from Bio import SeqIO, AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
import subprocess

# Load patient gene sequence and reference sequence
patient_seq = SeqIO.read("data/NC_000001.11[161222091..161223827](-).fa", "fasta").seq
reference_seq = SeqIO.read("data/NC_060925.1[160359547..160361277](-).fa", "fasta").seq

# Write sequences to a temporary file for alignment
with open("sequences.fasta", "w") as seq_file:
    seq_file.write(f">patient\n{patient_seq}\n")
    seq_file.write(f">reference\n{reference_seq}\n")

print("[LOG] Temporary sequence file 'sequences.fasta' created.")
with open("sequences.fasta", "r") as file:
    print(file.read())  # Log the content of the sequence file

# Perform sequence alignment between patient and reference sequences
clustalomega_cline = ClustalOmegaCommandline(
    infile="sequences.fasta",
    outfile="aligned.fasta",
    verbose=True,
    auto=True
)

# Execute the command using subprocess
cmd = str(clustalomega_cline)  # Convert the command-line object to a string
process = subprocess.run(cmd, shell=True, text=True, capture_output=True)

# Check for errors
if process.returncode != 0:
    print("Error running Clustal Omega:")
    print(process.stderr)
    exit(1)

print("[LOG] Clustal Omega alignment completed successfully.")
if process.stdout:
    print("[LOG] Clustal Omega output:")
    print(process.stdout)

# Inspect the alignment file
print("[LOG] Content of the alignment file 'aligned.fasta':")
with open("aligned.fasta", "r") as file:
    print(file.read())

# Read the alignment
alignment = AlignIO.read("aligned.fasta", "fasta")

# Identify sequences in alignment
patient_alignment = None
reference_alignment = None

for record in alignment:
    print(f"[LOG] Found sequence in alignment: ID={record.id}, Length={len(record.seq)}")
    if record.id == "patient":
        patient_alignment = record.seq
    elif record.id == "reference":
        reference_alignment = record.seq

if patient_alignment is None or reference_alignment is None:
    print("Error: Patient or reference sequence not found in alignment.")
    exit(1)

# Identify mutations
mutations = []
for idx, (ref_nuc, pat_nuc) in enumerate(zip(reference_alignment, patient_alignment)):
    if ref_nuc != pat_nuc and ref_nuc != '-' and pat_nuc != '-':
        mutations.append((idx, ref_nuc, pat_nuc))

# Output the identified mutations
print(f"[LOG] Identified mutations: {mutations}")
