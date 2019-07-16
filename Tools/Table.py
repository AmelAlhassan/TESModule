#Author Amel Shamseldeen Ali Alhassan
# module for making tables


import numpy as np
import os
from math import *
import matplotlib.pyplot as plt
from matplotlib import patches
from scipy.optimize import leastsq
import matplotlib


#***************************************** Making Tables *************************************************#

#===============================
# making tables function
#===============================


def latex_table(tabledata,columnlabel,columnunit=None):
	"""This function data table and columns and units in one tabledata in latex format
	inputs:
	tabledate: """
	matplotlib.rc('text', usetex=True)
	table = r'\begin{table} \begin{tabular}{|'
	for c in range(len(columnlabel)):
		# add additional columns
		table += r'c|'
	table += r'} \hline '
	#provide column headers
	for i in range(len(columnlabel)-1):
		table += columnlabel[i]
		table += r'&'
	table += columnlabel[-1]
	table += r'\\ \hline '
	if columnunit:
		#provide units
		for u in range(len(columnunit)-1):
			if columnunit[u]:# write the unit of the coulumn has unit
				table += columnunit[u]
			else:#leave empty box if the coulumn has no unit
				table += r' '
			table += r'& '
		table += columnunit[-1]
		table += r'\\ \hline '
	#fill the table
	for raw in tabledata:
		for i, item in enumerate(raw):
			table += str(item)
			if i != len(raw)-1:
				table += r'&'
		table += r'\\ \hline '
	table += r'\end{tabular} \end{table} '
	return table






#==================
#make table in pdf
#==================

def mkpdftable(title,name,tabledata,columnlabel,columnunit=None):
	table = latex_table(tabledata,columnlabel,columnunit)
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
#	ax1.text(0,0,table, size=50)
	ax1.annotate(table, xy=(0.25, 1), xytext=(12, -12), va='top', xycoords='axes fraction', textcoords='offset points')
	ax1.axis('off')
	ax1.set_title(title)
	fig.savefig(name)
	print name
	plt.show()
