#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-6-2025
#Last mod: 1-6-2025

from pyteomics import mzml
import matplotlib.pyplot as plt

#open mzMl file containing the MS data & plot MS/MS spectrum\
plt.figure()
plt.stem(spectrum['m/z array'], spectrum['intensity'],markerfmt="",basefmt="")
plt.xlabel('m/z')
plt.ylabel('Intensity')
plt.title(f"Spectrum ID: {spectrum['id']}")
plt.show()

#.....