#chap 2
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

from Bio import Entrez

#set the email to be used for NCBI Entrez
Entrez.email = "dariusz.czeczuk@hotmail.com"

#search for a genomic record using an accession number
accession = "NC_000852"
search_handle = Entrez.esearch(db="nucleotide",term=accession,retmax="1")
search_results = Entrez.read(search_handle)
search_handle.close()

#fetch the record from the search result
id_list = search_results["IdList"]
fetch_handle = Entrez.efetch(db="nucleotide",id=id_list,rettype="fasta",retmode="text")

#read and print fetched data
genomic_data = fetch_handle.read()
fetch_handle.close()
print(genomic_data)