# Fetch.py
# This program is designed to fetch a certain type of files inside layrs of folders.
# Author: Amel Alhassan
# Date 4.12.2015

# call the program on the terminal by $: python Fetch.py foldername

import os
import sys
import numpy as np

filetype = '.npz'

def dirseq(x):
	"""This function takes a string of folder bath and returns a list of the directories sequence in the path each directory name as single element"""
	folderslist=[]
	indecies=[0]
	for i,c in enumerate(x):
		if "/"==c: indecies.append(i)
	for j in range(len(indecies)-1):
		if j==0:
			folderslist.append(x[indecies[j]:indecies[j+1]])
		else:
			folderslist.append(x[indecies[j]+1:indecies[j+1]])
	folderslist.append(x[indecies[-1]+1:])
	return folderslist



def fetchtype(x,y):
	""" This function finds pathes from a root folder to subfolders that contain cetrain files by their type
	iputs:
	x = file extention (string stating with".")
	y = name of the root folder
	output:
	list of 3D list for each folder containing target files (files with extention x):
	- The first element of the 3D list is the folder path starting from root directory to directory that contains the files of interest. 
	- The second element is a list of names of the folders squence in that path.
	- The third element is list of names of files in the timeline directory."""
	folders= []
	for root, dirs, files in os.walk(y):
		if len([f for f in files if f.endswith(x)  == True])>0:
			for f in files:
				if f.endswith(x)  == True:
					path=[]
					path.append(root)
					path.append(dirseq(root))
					path.append(f)
					folders.append(path)
	print folders,f
	return folders




#fetchtype(filetype, "TES/QE 2.2/QE2_1")
