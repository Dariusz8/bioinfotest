#chap 4 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-5-2025
#Last mod: 1-5-2025

from goatools import obo_parser
from goatools.base import download_go_basic_obo
from goatools.goea.go_enrichment_ns import GOEnrichmentStudyNS
from goatools.anno.genetogo_reader import Gene2GoReader

#download latest version of the Go basic obo file
obo_fname = download_go_basic_obo()

#read obo file
go_obo = obo_parser.GODag(obo_fname)

#read gene2go annotation
objanno = Gene2GoReader('gene2go',taxids=[9606])

#mapping of gene IDS to GO terms
ns2assoc = objanno.get_ns2assc()

#list of differentially expressed genes
my_gene_list = ['geneA','geneB','geneC',...]
#example gene identifiers

#initialize GOEA object
goeaobj = GOEnrichmentStudyNS(methods=['fdr_bh'])

#run GOEA on the gnee list and print results
goea_results_all = goeaobj.run_study(my_gene_list)
goeaobj.print_results(goea_results_all)