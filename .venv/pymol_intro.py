#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-6-2025
#Last mod: 1-6-2025

#pymol script to visualize predicted protein structure
from pymol import cmd.\.venv\Scripts\activate

#load the predicted model
cmd.load('predicted_model.pdb')

#visualize protein with a cartoon representation
cmd.show('cartoon','predicted_model')

#color secondary structure
cmd.color('red','ss h')
cmd.color('yellow','ss s')
cmd.color('cyan','ss 1+')

#display the molecular surface
cmd.show('surface','predicted_model')
cmd.set('transparency',0.5)