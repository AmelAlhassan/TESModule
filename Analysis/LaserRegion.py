# laser_region.py
# Author: Amel Alhassan
# date: 4.1.2016
# Description: This program reads the singles_Off files from a list and returns npz file contains the specifications of the 3_sigma region, event counts (total and inside the 3_sigma region) count ratios, correlation coifficients and comparisons of these parameters between different timelines, plus PI Vs PH Histogram for each timeline.
#This program is based on Noemie Bastidon's PHPI analysis. The modifications are: Transforming the solid script into functions, and allowing flexibility on choosing the PH and PI cuts

# Notes: This program works for laser data files. the 3 sigma region fails for non-laser data.




import inspect, os
import sys
import numpy as np
from math import degrees, atan
from scipy.optimize import leastsq
import time 
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Ellipse
import QEmodule
import PHnPI
from TestTimelines import PHPIhist

script_name = inspect.getfile(inspect.currentframe()) 
print "Starting script:", sys.argv[0]


def countevents(singlesfolder):
	TL = -15#input('Enter trigger level in mV: ')

	files = np.sort(os.listdir(singlesfolder)) # read event files within the timeline

	time_scaling = 1e6 #us
	voltage_scaling = 1e3 #mV



# initialize arrays for calculating PH and PI
	total_sum_raw = np.array([], dtype=float)
	total_peak_raw = np.array([], dtype=float)
	total_time_file = np.array([])


	for i, n in enumerate(files):
		data_in = os.path.join(singlesfolder, n) # data input: single events
		measind = singlesfolder[-3:]
		data = np.load(data_in)
		pulse = data['pulse'] # save voltage points in each event
		time_data = data['time'] # save time points in each event
		del data.f
		data.close()# del/close opened file

		time_bin = abs(time_data[1]-time_data[0]) # 50ns
		sum_raw = abs(np.sum(time_bin * pulse)) # PI
		peak_raw = np.min(pulse) # PH
		total_sum_raw = np.append(total_sum_raw, sum_raw) # save PI of this event to the timeline data
		total_peak_raw = np.append(total_peak_raw, peak_raw) # save PH of this event to the timeline data
		# end of data extraction for loop

#save the events charachterstics
	PH = total_peak_raw*voltage_scaling
	PI = total_sum_raw*time_scaling*voltage_scaling

# ******* COUNT TOTAL NBR OF TRIGGERED EVENTS ********

	count = 0 # Number of events below the TL
	for i in range(len(PH)):
		if (PH[i] < TL):
			count = count + 1
	ercount = sqrt(count) # the standard error in count
	return TL, PH, PI, count, ercount, measind


# ******* COUNT POINTS INSIDE AN ELLIPSE ********

def sigmaregion(TL,PH, PI, count):
	ph_lower_limit = input('Enter laser region lower PH limit in mV (negative): ') # make initial estimation for the laser region
	ph_higher_limit = input('Enter laser region higher PH limit in mV (negative): ')
	pi_lower_limit = input('Enter laser region lower PI limit in mV.us (positive): ')
	pi_higher_limit = input('Enter laser region higher PI limit in mV.us (positive): ')

	angle_scaling = 1e3 #mrad
	# PI vs PH laser box in measurement
	PH_region = np.array([], dtype = float)
	PI_region = np.array([], dtype = float)

	y = 'y'
	n='n'
	status = 'y'#input('Is the laser On? (y/n): ')
	if status == 'y' or 'Y':
		for i in range(len(PH)): # Laser 3 sigma region
			if float(ph_lower_limit) < PH[i] < float(ph_higher_limit) and float(pi_lower_limit)< PI[i] < float(pi_higher_limit):
				PH_region=np.append(PH_region,PH[i])
				PI_region=np.append(PI_region,PI[i])



		N = len(PH_region)
		data = np.vstack([PH_region, PI_region])
		mean = np.mean(data, axis=1)
		std = np.std(data, axis=1)
		corr_coeff = np.corrcoef(PH_region,PI_region)
		theta_1 = (2.*corr_coeff[0,1]*std[0]*std[1])/(std[0]**2-std[1]**2)# Compute angle from corr_coeff
		theta_2 = math.degrees(math.atan(theta_1))# find the angle in degrees
		correlation = corr_coeff[0,1]
		cov_matrix = np.cov(PH_region,PI_region)
		var_PH = cov_matrix[0,0]
		var_PI = cov_matrix[1,1]
		cov_PH_PI = cov_matrix[0,1]


		a = 3.*std[0] # Sigma PH (x)
		b = 3.*std[1] # Sigma PI (y)
		x = mean[0] # X coordinate for ellipse center = mean PH
		y = mean[1] # Y coordinate for ellipse center = mean PI
		angle_degree = (theta_2/2.) 
		angle_rad = (theta_2/2.) * np.pi/180. # Ellipse inclination angle
		angle_mrad = angle_rad * angle_scaling


	if status == 'n':
		a = input('Enter correspondent 3 sigma PH: ')
		b = input('Enter correspondent 3 sigma PI: ')
		x = input('Enter correspondent mu PH: ')
		y = input('Enter correspondent mu PI: ')
		angle_rad = input('Enter correspondent angle in rad: ')
		angle_degree = angle_rad / (np.pi/180.)
		angle_mrad = angle_rad * angle_scaling
		correlation = 0.0
		cov_PH_PI = 0.0


	countEllip = 0 # Count of events located in the 3 sigma region
	ptsX = []
	ptsY = []
	for i in range(len(PH)):
		if PHnPI.EllipFunc(PH[i],PI[i],x ,y,a,b,angle_rad) < 1.:
			countEllip = countEllip +1
			ptsX.append(PH[i])
			ptsY.append(PI[i])
	ercountEllip = sqrt(countEllip)
	ellip_total_ratio = float(countEllip) / float(count)

# Standard error on ellipse characteristics
	se_mu_PH = a/sqrt(N)
	se_mu_PI = b/sqrt(N)
	se_std_PH = sqrt((a**2)*sqrt(2./(N-1)))
	se_std_PI = sqrt((b**2)*sqrt(2./(N-1)))

	return x, y, a, b, angle_rad, angle_mrad, angle_degree, count, countEllip, ercountEllip, se_mu_PH, se_mu_PI, se_std_PH, se_std_PI, ellip_total_ratio, correlation, cov_PH_PI











def PIPHAnalysis(folderslist):
	""" Plot PI vs PH histograms for each timeline and makes npz file specifying the 3 sigma region parameters for all the timelines
	inputs:
	a list of pathes to timeline folders (the outputs of singles function)
	outputs:
	PI vs PH histograms .pdf file for each timeline, and
	one npz file contain the details of each timeline"""
	# initialize lisits for the output .npz file
	y = 'y'
	n = 'n'
	identifier = np.array([])
	Measure = np.array([],dtype = str)
	# counters
	Count = np.array([], dtype = float)
	Ercount = np.array([], dtype = float)
	CountEllip = np.array([], dtype = float)
	ErcountEllip = np.array([], dtype = float)
	Ellip_total_ratio = np.array([], dtype = float)
	# 3 sigma specifications
	mu_PH = np.array([], dtype = float)
	SE_mu_PH = np.array([], dtype = float)
	std_PH = np.array([], dtype = float)
	SE_std_PH = np.array([], dtype = float)
	mu_PI = np.array([], dtype = float)
	SE_mu_PI = np.array([], dtype = float)
	std_PI = np.array([], dtype = float)
	SE_std_PI = np.array([], dtype = float)
	angle = np.array([], dtype = float)
	angle_rad_raw = np.array([], dtype = float)
	rho = np.array([], dtype = float)
	covariance =  np.array([], dtype = float)



	for j in range(len(folderslist)):
		if j == 0 or folderslist[j][0] != folderslist[j-1][0]:
			print ('The current directiry is'), folderslist[j][0]
# get the 3 sigma region
			TL, PH, PI, count, ercount,measind = countevents(folderslist[j][0])
# plot histograms to see where the data falls
			details = ' '.join(folderslist[j][1]) 
			#PHPIhist(PH,PI,count,details)
			x, y, a, b, angle_rad,angle_mrad, angle_degree, count, countEllip, ercountEllip, se_mu_PH, se_mu_PI, se_std_PH, se_std_PI, ellip_total_ratio, correlation, cov_PH_PI = sigmaregion(TL, PH, PI, count)

# plot the PH vs PI histograms
			PHnPI.singlesout(folderslist[j][0],measind,TL,PH,PI,x,y,a,b,angle_rad,angle_degree,count,ercount,countEllip,ercountEllip,se_mu_PH,se_mu_PI,se_std_PH,se_std_PI)


#add values to lists
			identifier = np.append(identifier,np.vstack(folderslist[j][1]))
			Measure = np.append(Measure, measind)
			mu_PH = np.append(mu_PH, x)
			SE_mu_PH = np.append(SE_mu_PH, se_mu_PH)
			std_PH = np.append(std_PH, a)
			SE_std_PH = np.append(SE_std_PH, se_std_PH)
			mu_PI = np.append(mu_PI, y)
			SE_mu_PI = np.append(SE_mu_PI, se_mu_PI)
			std_PI = np.append(std_PI, b)
			SE_std_PI = np.append(SE_std_PI, se_std_PI)
			angle = np.append(angle, angle_mrad)
			angle_rad_raw = np.append(angle_rad_raw,angle_rad)
			Count = np.append(Count, count)
			Ercount = np.append(Ercount, ercount)
			CountEllip = np.append(CountEllip, countEllip)
			ErcountEllip = np.append(ErcountEllip, ercountEllip)
			Ellip_total_ratio = np.append(Ellip_total_ratio, ellip_total_ratio)
			rho = np.append(rho, correlation)
			covariance = np.append(covariance,cov_PH_PI)

			print ('3 sigma PH is : '), a
			print ('3 sigma PI: '),b
			print('mu PH: '), x
			print('mu PI: '),y
			print('angle in rad: '),angle_rad 



	save_name= input("Give a name to the npz file of these analysis: ")
	np.savez(save_name, identifier= identifier, Measure = Measure, mu_PH=mu_PH, SE_mu_PH=SE_mu_PH, std_PH=std_PH, SE_std_PH=SE_std_PH, mu_PI=mu_PI, SE_mu_PI=SE_mu_PI, std_PI=std_PI, SE_std_PI= SE_std_PI, angle= angle, Count=Count, Ercount=Ercount, CountEllip=CountEllip, ErcountEllip=ErcountEllip, Ellip_total_ratio =Ellip_total_ratio, rho =rho)

	print "output: ",save_name +".npz"


