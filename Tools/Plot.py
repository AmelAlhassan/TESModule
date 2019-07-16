#Author Amel Shamseldeen Ali Alhassan
# module for plotting 1,2 or 3 functions in a single plot

import numpy as np
import inspect, sys
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from matplotlib.patches import Ellipse

# ******************************************   PLOTTING   *************************************************




#--------------------------------- Plotting Functions -----------------------------


#------------------
# One diagram plot
#------------------
 

def dia(title, name, xlab, ylab, a, era, mua, x1,la,lmua,c,shape = 'o'):
	'''Plot a digrams in a single frame
	parameters:
	-----------
	title: written on top of the graph
	name: used to save the file
	xlab: the x- axis label (str)
	ylab: the y- axis label (str)
	a: y axis parameter 
	era: erroe in a
	mua: a mean value (arithmatic mean)
	x1:  x in the a vs x plot

	extras:
	-------
	la: label of a 
	lmua: label of mean a
	'''
	mina= min(a)
	maxa= max(a)
	c1 = ('%s: min. = %.3f, Max. = %.3f' %(la,mina,maxa))
	fig = plt.figure(figsize=(15,9))  # Create an empty figure
	plt.errorbar(x1, a, yerr=era, marker=shape, color=c,ls='None',label=la) 
	plt.axhline(y=mua, ls='--', color= c,label=lmua+' = %.3f' %mua) 
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(title)
	plt.margins(0.05, 0.15)
	plt.legend(loc='best')
	plt.annotate(c1, xy=(0, 1), xytext=(12, -12), va='top', xycoords='axes fraction', textcoords='offset points')
	# save figure
	save_name = name 
	plt.savefig(save_name)
	print save_name






#------------------------------------------------------------------------


#------------------
# Two diagrams plot
#------------------


def dia2(title, name, xlab, ylab, a, era, mua, x1, b, erb, mub, la, lb, lmua, lmub, x2):
	'''Plot 2 digrams in a single frame
	parameters:
	-----------
	title: written on top of the graph
	name: used to save the file
	xlab: the x- axis label (str)
	ylab: the y- axis label (str)
	a: first parameter
	era: erroe in a
	mua: a mean value (arithmatic mean)
	x1:  x in the a vs x plot
	b: second parameter
	erb: error in b
	mub: b mean value

	extras:
	-------
	x2: x in the b vs x plot
	la: label of a 
	lb: label of b
	lmua: label of mean a
	lmub: label of mean b
	'''
	mina= min(a)
	maxa= max(a)
	minb= min(b)
	maxb= max(b)
	c1 = ('%s: min. =%.3f, Max. =%.3f$ \n %s: min. =%.3f, Max. =%.3f' %(la,mina,maxa,lb,minb,maxb))
	fig = plt.figure(figsize=(15,9))  # Create an empty figure
	plt.errorbar(x1, a, yerr=era, marker='o', color='b',ls='None',label=la) 
	plt.errorbar(x2, b, yerr=erb, marker='o', color='r',ls='None',label=lb) 
	plt.axhline(y=mua, ls='--', color='b',label=lmua+' = %.3f' %mua) 
	plt.axhline(y=mub, ls='--', color='r',label=lmub+' = %.3f' %mub)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(title)
	plt.margins(0.05, 0.15)
	plt.legend(loc='best')
	plt.annotate(c1, xy=(0, 1), xytext=(12, -12), va='top', xycoords='axes fraction', textcoords='offset points')
	# save figure
	save_name = name 
	plt.savefig(save_name)
	print save_name


#-----------------------------------------------------------------------------
#This section defines the functions used in this program

#------------------
# Three diagrams plot
#------------------


def dia3(title, name, xlab, ylab, a, era, mua, x1, b, erb, mub, c, erc, muc, la, lb, lc, lmua, lmub, lmuc, x2, x3):
	'''Plot 2 digrams in a single frame
	parameters:
	-----------
	title: written on top of the graph
	name: used to save the file
	xlab: the x- axis label (str)
	ylab: the y- axis label (str)
	a: first parameter
	era: erroe in a
	mua: a mean value (arithmatic mean)
	x1:  x in the a vs x plot
	b: second parameter
	erb: error in b
	mub: b mean value
	c: Thisrd parameters
	erc: error in c
	muc: c mean value

	extras:
	-------
	x2: x in the b vs x plot
	x3: x in c vs x plot
	la: label of a 
	lb: label of b
	lc: label of c
	lmua: label of mean a
	lmub: label of mean b
	lmuc: label of mean c
	'''
	mina= min(a)
	maxa= max(a)
	minb= min(b)
	maxb= max(b)
	minc= min(c)
	maxc= max(c)
	c1 = ('%s: min. =%.3f, Max. =%.3f$ \n %s: min. =%.3f, Max. =%.3f \n %s: min. %.3f Max.  %.3f' %(la,mina,maxa,lb,minb,maxb,lc,minc,maxc))
	fig = plt.figure(figsize=(15,9))  # Create an empty figure
	plt.errorbar(x1, a, yerr=era, marker='o', color='m',ls='None',label=la) 
	plt.errorbar(x2, b, yerr=erb, marker='o', color='g',ls='None',label=lb) 
	plt.errorbar(x3, c, yerr=erb, marker='o', color='k',ls='None',label=lc) 
	plt.axhline(y=mua, ls='--', color='m',label=lmua+' = %.3f' %mua) 
	plt.axhline(y=mub, ls='--', color='g',label=lmub+' = %.3f' %mub)
	plt.axhline(y=muc, ls='--', color='k',label=lmuc+' = %.3f' %muc)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(title)
	plt.margins(0.01, 0.15)
	plt.legend(loc='best')
	plt.annotate(c1, xy=(0, 1), xytext=(12, -12), va='top', xycoords='axes fraction', textcoords='offset points')
	# save figure
	save_name = name 
	plt.savefig(save_name)
	print save_name




















