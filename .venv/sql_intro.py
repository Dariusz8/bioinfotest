#chap 2
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

import sqlite3

# Connect or create SQLite database
conn = sqlite3.connect("genomic.db")
cursor = conn.cursor()

# Create table to store gene annotations
cursor.execute('''CREATE TABLE IF NOT EXISTS gene_annotations (
    gene_id TEXT PRIMARY KEY,
    gene_name TEXT,
    organism TEXT,
    chromosome TEXT,
    start INTEGER,
    "end" INTEGER
)''')

# Insert a gene annotation into the table
annotation_data = ("ATG0001", "ExampleGene", "Arabidopsis thaliana", "1", 12345, 67890)
cursor.execute("INSERT INTO gene_annotations VALUES (?,?,?,?,?,?)", annotation_data)

# Commit changes and close the connection
conn.commit()
conn.close()
