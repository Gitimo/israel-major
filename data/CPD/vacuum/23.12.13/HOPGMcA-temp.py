import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

def readCPD(fname, convert_time='True', time_format='', skiplines=46):
	tmp=np.genfromtxt(fname,skip_header=skiplines)
	if convert_time == 'True':
		t0=tmp[0,1]
		if time_format == 's':
			tmp[:,1] = (tmp[:,1]-t0)
		elif time_format == 'h':
			tmp[:,1] = (tmp[:,1]-t0)/(60*60)
		else:
			tmp[:,1] = (tmp[:,1]-t0)/60
	plt.plot(tmp[:,0],tmp[:,2])
	plt.show()
	out=tmp[:,2]
	return out
	
def wfprobe(value,error):
	out=[]
	out.append(4.65+value)
	out.append(error)
	return out

def wfsample(probe,value,error):
	out=[]
	out.append(probe[0]-value)
	out.append(np.sqrt(np.power(probe[1],2)+np.power(error,2)))
	return out

#rc('text',usetex=True)
#rc('font',**{'family':'serif','serif':['Computer Modern']})
#one = readCPD('hopg1.CPD')
#two = readCPD('hopg2.CPD')
#three = readCPD('hopg3.CPD')
#four = readCPD('hopgnewspotTup.CPD')

#pKone = [	[63,1000,299],[196,0.11,299],[197,0.093,299],[217,0.089,299],
			#[218,0.062,299],[218,0.062,299],[363,0.052,299],[551,0.043,299],
			#]


#fig,ax1 = plt.subplots()
#ax2=ax1.twinx()
#def mylines():
	##CPD
	#ax1.plot(vacHOPG1[0:360,0],vacHOPG1[0:360,1],color='r',label='Ambient')
	#ax1.hold(True)
	#ax1.plot(vacHOPG1[359:366,0],vacHOPG1[359:366,1],'0.7')
	#ax1.plot(vacHOPG1[361:1313,0],vacHOPG1[361:1313,1],color='b',label='Weak pump')
	#ax1.plot(vacHOPG1[1312:1316,0],vacHOPG1[1312:1316,1],'0.7')
	#ax1.plot(vacHOPG1[1315:5514,0],vacHOPG1[1315:5514,1],color='k',label='Turbo pump')
	#ax1.plot(vacHOPG1[5516:5590,0],vacHOPG1[5516:5590,1],color='b',label='Weak pump')
	##Pressure
	#t=list()
	#ind = (0,359,361,410,480,580,980,1300,1313,1315,1380,1410,1450,1480,1560,1600,1700,
		#1755,1770,1810,1830,1935,2075,2170,2200,2300,2390,2569,5300,5580)
	#p = (0.1,0.1,0.1,0.08,0.075,0.067,0.046,0.035,0.0019,0.0017,0.0016,0.0016,0.0014,0.0013,
		#0.0012,0.0011,0.001,0.00097,0.00095,0.00092,0.0009,0.00083,
		#0.00075,0.00071,0.00069,0.00065,0.00062,0.00058,0.00038,0.1)
	#for i in ind:
		#t.append(vacHOPG1[i,0])
	#ax2.plot(t,p,'om')
	#ax2.set_yscale('log')
	#ax2.set_ylabel('Pressure',color='m')
#mylines()
#def myannotations():
	#plt.annotate(
			#'Taken on a different date',
			#xy=(125, 128), arrowprops=dict(arrowstyle='->'), xytext=(132, 110))
        
	##Labels
	#ax1.set_xlabel('Time [min]')
	#ax1.set_ylabel('CPD [mV] (Proble - Sample)')
	#ax1.set_title('CPD of HOPG with the McAllister')
	#ax1.grid(True)
	##Plot the legend
	#p1 = plt.Rectangle((0, 0), 1, 1, fc="r")
	#p2 = plt.Rectangle((0, 0), 1, 1, fc="b")
	#p3 = plt.Rectangle((0, 0), 1, 1, fc="k")
	#p4 = plt.Rectangle((0, 0), 1, 1, fc="m")
	#ax2.set_ylim(0.0001,1)
	##ax1.legend((p1, p2, p3, p4), ('Ambient','Weak Pump','Turbo Pump', 'Pressure'))
#myannotations()
#plt.savefig('hopgvacwithpressure.pdf',bbox_inches=0)
#plt.show()
