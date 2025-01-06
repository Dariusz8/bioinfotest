#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-6-2025
#Last mod: 1-6-2025

from pyteomics import mzml,parser

#load and read the mzML file
path_to_mzml_file = 'example.mzml'
mz_values = spectrum['m/z array']
intensity_values = spectrum['intensity array']
#more processing ....

#peptide modification parsing
modified_peptide = 'R.HSApSTGVK.T' #phosphorylation ex.
parser.parse_modifications(modified_peptide)
print(f"Identified modifications: {modifications}")