#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-7-2025
#Last mod: 1-7-2025

from pymol import cmd,util

#load the enzyme structure
cmd.load('enzyme_structure.pdb')

#highlight the active site residues
active_site_residues = [42,57,102,189] #example residue numbers

cmd.select('active_site', 'resi' + '+'.join(map(str,active_site_residues)))
util.cbac('active_site')

#load the subtrate structure
cmd.load('substrate.pdb','substrate')

#animate the substrate approaching the active site
cmd.mset('1x120')
cmd.frame(1)
cmd.translate([0,0,-20],'substrate')
cmd.mview('store',1)
cmd.frame(120)
cmd.translate([0,0,20],'substrate')
cmd.mview('store',120)
cmd.mplay()