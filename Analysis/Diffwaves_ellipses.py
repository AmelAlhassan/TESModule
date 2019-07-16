# Diffwaves_Ellipses.py
# Author: Amel Alhassan 
# Date: Jan.2016

#describtion
# PH and PI are arrays of mean values of error ellipses for laser regions of different wavelengthes. These ellipses are descriped using the functios ellipse# bellow. The ellipses are drown and a linear fitting of their mean values are made.


import numpy as np

import matplotlib.pylab as plt

from matplotlib.patches import Ellipse

fig = plt.figure()

ax = plt.gca()

PH = np.array([-108.0,-60.7,-74.1,-47.2,-28.3])

PI = np.array([212.2,110.0,138.8,82.0,46.35])

m0,b0 = np.polyfit(PH[1:4],PI[1:4],1)#linear fitting of 3 center points

m,b = np.polyfit(PH[0:4],PI[0:4],1)#linear fitting of 4 center points

m1,b1 = np.polyfit(PH,PI,1)#linear fitting of 5 center points ( 4 lasers + background)

plt.xlabel('PH(mV)')

plt.ylabel('PI(mV.us)')

#ellipse1 = Ellipse((-108,212.2),9.28*2.,74.68*2.,.033*180/3.14,edgecolor='purple',facecolor = 'none',linewidth = 1, label ='405 nm')

#ellipse2 = Ellipse((-60.7,110.),9.18*2.,52.72*2.,.044*180/3.14,edgecolor='maroon',facecolor = 'none',linewidth = 1,label='804 nm')

#ellipse3 = Ellipse((-74.1,138.8),9.11*2.,37.47*2.,.064*180/3.14,edgecolor='orangered',facecolor = 'none',linewidth = 1, label='635 nm')

#ellipse4 = Ellipse((-47.2,82.0),10.75*2.,41.61*2.,.085*180/3.14,edgecolor='k',facecolor = 'none',linewidth = 1, label = '1064 nm')


ellipse1 = Ellipse((-108,209.9),9.18*2.,40.49*2.,.061*180/3.14,edgecolor='purple',facecolor = 'none',linewidth = 1, label ='405 nm')

ellipse2 = Ellipse((-74.1,136.8),9.45*2.,39.02*2.,.066*180/3.14,edgecolor='orangered',facecolor = 'none',linewidth = 1, label='635 nm')

ellipse3 = Ellipse((-60.7,108.3),9.27*2.,39.78*2.,.058*180/3.14,edgecolor='maroon',facecolor = 'none',linewidth = 1,label='804 nm')

ellipse4 = Ellipse((-47.2,82.5),10.63*2.,40.72*2.,.079*180/3.14,edgecolor='k',facecolor = 'none',linewidth = 1, label = '1064 nm')

#ellipse5 = Ellipse((-28.3,46.35),10.86*2.,39.17*2.,.122*180/3.14,edgecolor='r',facecolor = 'none',linewidth = 1, label = 'BG')

ax.set_ylim(0,300)

ax.set_xlim(-160,-20)

ax.plot(PH,PI,'.')

ax.plot(PH,m0*PH +b0,'-')

ax.add_patch(ellipse1)

ax.add_patch(ellipse2)

ax.add_patch(ellipse3)

ax.add_patch(ellipse4)

#ax.add_patch(ellipse5)

plt.legend(loc='best')

fig.savefig('Diffwaves_Ellipses')

print 'fit on 3: m0', m0, ',b0',b0

print 'fit on 4: m', m, ',b',b

print 'fit on 5: m1', m1, ',b1',b1
