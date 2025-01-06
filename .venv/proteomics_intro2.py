#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-6-2025
#Last mod: 1-6-2025

import pymzml

#path to mzML file
mzml_file_path = 'example.mzML'

#create an MS run object to iterate over spectra
run = pymzml.run.Reader(mzml_file_path)
if'MS:10005111' in spectrum: #filter for MS1 spectra
    #retrieve m/z intensity values
    mz_values = spectrum.mz
    intensity_values = spectrum.i

#perform peak detection (ex simple threshold method)
threshold = 1000
peaks = [(mz, intensity) for mz, intensity in zip(mz_values,intensity_values)if intensity>threshold]

#output detected peaks
print(f"Detected peaks in spectrum {spectrum['id']}:")
print(f"m/z: {m/z:.4f}, Intensity:{intensity:.2f}")

