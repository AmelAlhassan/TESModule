# addnoise.py
# Author: Amel Alhassan 
# Date: 4.1.2016
# Description: Add the voltage arrays of two equivalent (same length, i.e 1s) time lines. The first time line is for laser data (laser on) while the other one is noise( laser off).
# useage: study effect of noise in 3 sigma region

# you can use the program either by import addnoise then use the function as described, or 
# python addnoise.py datafile noisefile QE# name



import numpy as np
import sys



def addnoise(a,b,n=1,qe=None,name= None):
	"""Add the voltage arrays of two equivalent (same length, i.e 1s) time lines.
	inputs:
	two timelines, the first is the laser data.
	The second is the noise data (laser off and trigger level at zero),
	Quantum Effeciency index,
	and the output file name (without.npz).
	output:
	the laseron timeline with magnified (extra) noise"""
	data = np.load(a)
	voltage = data['pulse']
	time = data['time']
	del data.f
	data.close()

	data2 = np.load(b)
	prenoise = data2['pulse']
	noise = prenoise*int(n)
	del data2.f
	data2.close()

	new_voltage = voltage + noise

	if not name:
		name = 'Noise_'+n+'_'+b[-7:-4]+'_'+a[-7:-4]
	if qe:
		save_name = qe + name
	else:
		save_name = name

	np.savez(save_name, time = time, pulse = new_voltage)

	print 'The data from the noise file',b , 'is added to the voltage file', a
	print 'output file', save_name+'.npz'
	print len(new_voltage), len(time)





