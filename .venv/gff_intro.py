#chap 2 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

import gffutils

#create a database from the GFF file
db = gffutils.create_db("example.gff", dbfn="example.db",
    force=True, keep_order=True, merge_strategy="merge",sort_attribute_values=True)

print(f"Error parsing GFF file:{e}")
#query the databases for specific features
print(f"Gene:{gene.id},Start:{gene.start},End:{gene.end}")