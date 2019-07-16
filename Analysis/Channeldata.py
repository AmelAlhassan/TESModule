import numpy as np
import inspect, sys
import matplotlib.pyplot as plt
#from TESModule.Analysis import QEmodule
import math
import matplotlib as mpl
from matplotlib.patches import Ellipse


#make a class for extracting data tables from PH vs PI histograms npz file
class Dataset(object):

	def add(self,datatable):
		"""Extract 3 sigma region specifications from npz file"""
		CH = np.load(datatable)
		self.Run = CH['Run']
		self.Measure = CH['Measure']
		self.std_PI = CH['std_PI']
		self.std_PH = CH['std_PH']
		self.SE_std_PI =CH['SE_std_PI']
		self.SE_std_PH =CH['SE_std_PH']
		self.angle_degree = CH['angle']/(1e3* np.pi/180)
		self.mu_PH = CH['mu_PH']
		self.SE_mu_PH = CH['SE_mu_PH']
		self.mu_PI = CH['mu_PI']
		self.SE_mu_PI = CH['SE_mu_PI']
		self.angle = CH['angle']
		self.Count = CH['Count']
		self.Ercount = CH['Ercount']
		self.CountEllip = CH['CountEllip']
		self.ErcountEllip = CH['ErcountEllip']
		#rho = CH['rho']
		#covariance = CH['covariance']
		self.Ellip_total_ratio = CH['Ellip_total_ratio']
		#Ellip_to_totalcount_ratio = CountEllip/Count
		del CH.f
		CH.close()


	def make(self):
		"""Extract 3 sigma region specifications from npz file"""
		self.Run = np.array([])
		self.Measure = np.array([])
		self.std_PI = np.array([])
		self.std_PH = np.array([])
		self.SE_std_PI = np.array([])
		self.SE_std_PH = np.array([])
		self.angle_degree = np.array([])
		self.mu_PH = np.array([])
		self.SE_mu_PH = np.array([])
		self.mu_PI = np.array([])
		self.SE_mu_PI = np.array([])
		self.angle = np.array([])
		self.Count = np.array([])
		self.Ercount = np.array([])
		self.CountEllip = np.array([])
		self.ErcountEllip = np.array([])
		#rho = np.array([])
		#covariance = np.array([])
		self.Ellip_total_ratio = np.array([])
		#Ellip_to_totalcount_ratio = CountEllip/Count



