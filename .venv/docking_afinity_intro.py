#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-7-2025
#Last mod: 1-7-2025

import os
from vina import vina

#initialize the vina docking object
vina = Vina(sf_name='vina')

#set the protein and ligand file
vina.set_receptor('protein.pdbqt')
vina.set_ligand_from_file('ligand.pdbqt')

#define the search space around the active site
vina.compute_vina_maps(center=[15.0,58.2,22.5],box_size=[20,20,20])

#configure the vina object for docking
vina.score_only = False
vina.optimize = True
vina.exhaustviness = 8
vina.nu,_modes = 20

#dock the ligand
vina.dock(log_file='docking.log',out_pdbqt='docked_ligand.pdbqt')

#parse results
best_pose = vina.best_pose()
print(f"Best pose affinity: {best_pose.affinity} kcal/mol")