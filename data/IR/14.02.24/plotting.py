import numpy as np
import matplotlib.pyplot as plt
import pylab as pyl
from matplotlib import rc, rcParams


rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

def readCSV (fname, skiplines=0):
	tmp=np.genfromtxt(fname, skip_header=skiplines, delimiter=',', dtype=None)
	return tmp

ann = readCSV('ann.CSV')
five = readCSV('FirstPole5.CSV')
six = readCSV('FirstPole6.CSV')
seven = readCSV('FirstPole7.CSV') 
cyc = readCSV('cyclohexanone1.CSV')


fig,ax1 = plt.subplots()
ax1.plot(ann[0:,0],ann[0:,1],color='black',label='Ann')
ax1.hold(True)
#ax1.plot(five[0:,0],five[0:,1],color='r',label='Slowly cooled')
#ax1.plot(six[0:,0],six[0:,1],color='b',label='Quenched at RT')
ax1.plot(seven[0:,0],seven[0:,1],color='r',label='Quenched on ice')
ax1.plot(cyc[0:,0],cyc[0:,1],color='b',label='Cyclohexanone')
ax1.plot([840,840],[-0.3,0.2],linestyle='--',color='black')
ax1.plot([1280,1280],[-0.3,0.2],linestyle='--',color='black')
ax1.plot([1234,1234],[-0.3,0.2],linestyle='--',color='c')
ax1.axis([800,1400,-0.3,0.2])
plt.xlabel('Wavenumbers (cm$^{-1}$)')
plt.ylabel('Absorbance (a.u.)')
ax1.legend()
plt.show()

plt.savefig('newIRplot.pdf', bbox_inches=0)
