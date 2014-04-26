import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

vacHOPG1 = np.genfromtxt("vacHOPG1.txt")
t1 = vacHOPG1[0,0]
vacHOPG1[:,0] = (vacHOPG1[:,0]-t1)/60
vacHOPG1[:,1] = vacHOPG1[:,1]*1000
vacHOPG2 = np.genfromtxt("vacHOPG2.txt")
t2 = vacHOPG2[0,0]
vacHOPG2[:,0] = (vacHOPG2[:,0]-t2)/60
vacHOPG2[:,1] = vacHOPG2[:,1]*1000
vacHOPG3 = np.genfromtxt("vacHOPG3.txt")
t3 = vacHOPG3[0,0]
vacHOPG3[:,0] = (vacHOPG3[:,0]-t3)/60
vacHOPG3[:,1] = vacHOPG3[:,1]*1000


fig,ax1 = plt.subplots()
#Plot the lines
def mylines():
	ax1.plot(vacHOPG1[0:360,0],vacHOPG1[0:360,1],color='r',label='Ambient')
	ax1.hold(True)
	ax1.plot(vacHOPG1[359:366,0],vacHOPG1[359:366,1],'0.7')
	ax1.plot(vacHOPG1[365:1310,0],vacHOPG1[365:1310,1],color='b',label='Weak pump')
	ax1.plot(vacHOPG1[1310:1316,0],vacHOPG1[1310:1316,1],'0.7')
	ax1.plot(vacHOPG1[1315:-20,0],vacHOPG1[1315:-20,1],color='k',label='Turbo pump')

	ax1.plot(vacHOPG2[60:3450,0],vacHOPG2[60:3450,1],color='r',label='Ambient')
	ax1.plot(vacHOPG2[3449:3456,0],vacHOPG2[3449:3456,1],'0.7')
	ax1.plot(vacHOPG2[3455:5370,0],vacHOPG2[3455:5370,1],color='b',label='Weak pump')
	ax1.plot(vacHOPG2[5370:5376,0],vacHOPG2[5370:5376,1],'0.7')
	ax1.plot(vacHOPG2[5375:6410,0],vacHOPG2[5375:6410,1],color='k',label='Turbo pump')
	ax1.plot(vacHOPG2[6410:6421,0],vacHOPG2[6410:6421,1],'0.7')
	ax1.plot(vacHOPG2[6420:-20,0],vacHOPG2[6420:-20,1],'b')

	ax1.plot(vacHOPG3[0:1317,0],vacHOPG3[0:1317,1],color='b',label='Weak pump')
	ax1.plot(vacHOPG3[1316:1320,0],vacHOPG3[1316:1320,1],'0.7')
	ax1.plot(vacHOPG3[1319:2348,0],vacHOPG3[1319:2348,1],color='k',label='Turbo pump')
	ax1.plot(vacHOPG3[2348:2349,0],vacHOPG3[2348:2349,1],'0.7')
	ax1.plot(vacHOPG3[2350:-60,0],vacHOPG3[2350:-60,1],color='b',label='Weak pump')
mylines()
#Plot the annotations
def myannotations():
	plt.annotate(
			'Taken on a different date',
			xy=(125, 128), arrowprops=dict(arrowstyle='->'), xytext=(132, 110))
        
	#Labels
	ax1.set_xlabel('Time [min]')
	ax1.set_ylabel('CPD [mV] (Proble - Sample)')
	ax1.set_title('CPD of HOPG with the McAllister')
	ax1.grid(True,which='both')
	#Plot the legend
	p1 = plt.Rectangle((0, 0), 1, 1, fc="r")
	p2 = plt.Rectangle((0, 0), 1, 1, fc="b")
	p3 = plt.Rectangle((0, 0), 1, 1, fc="k")
	ax1.legend((p1, p2, p3), ('Ambient','Weak Pump','Turbo Pump',))


myannotations()


plt.savefig('HOPG-McAllister.pdf', bbox_inches=0)

plt.show()
