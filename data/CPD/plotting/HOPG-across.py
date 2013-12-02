import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

McA = (0.0222,0.0077,0.1689)
McAdate = (17,20,20)
McAav = (0.02,0.01)
N2in = (-1.0573,-1.0557,-1.0165,-1.0142,-1.1060,-1.1773,-1.0637,-1.0781)
N2indate = (x,x,x,13,13)
N2inav = (-1.07,0.05)
N2out = (-1.1065,-1.1243,-1.1088,-1.1076)
N2outdate = () 
N2outav = (-1.1118,0.008)
Air = (-0.479,-0.491,-0.484,-0.473,-0.478,-0.474,-0.560,-0.546,-0.551,-0.571,-0.607,-0.551,-0.319,-0.320,-0.480,-0.329,-0.339,-0.348)
Airdate = (18,18,18,18,18,18,19,19,19,19,19,19,25,25,13,5,3,3)
Av18 = (np.average(Air[0:2]),np.average(Air[3:5]))
Av19 = (np.average(Air[6:8]),np.average(Air[9:11]))
Av25 = (np.average(Air[12:13]))
Av3 = (np.average(Air[-2:-1]))

Std18 = (np.std(Air[0:2]),np.std(Air[3:5]))
Std19 = (np.std(Air[6:8]),np.std(Air[9:11]))
Std25 = (np.std(Air[12:13]))
Std3 = (np.std(Air[-2:-1]))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.errorbar((3,18,18,19,19,25),(Av3,Av18[0],Av18[1],Av19[0],Av19[1],Av25),
				yerr=(Std3,Std18[0],Std18[1],Std19[0],Std19[1],Std25),
				fmt='bo')
ax.hold(True)
ax.plot(Airdate, Air, 'kx')
ax.set_xlabel('Date, X th of November')
ax.set_ylabel('CPD [mV] (Sample - Probe)')
ax.set_title('HOPG on different days')
ax.set_xlim((0,27))

plt.show()

#hopglong = genfromtxt('airHOPGlong.txt')
#hopglong[:,0] = (hopglong[:,0] - hopglong[0,0]) / 60
#longplot = plt.figure(hopglong[:,0],hopglong[:,1])
#longplot.set_xlabel('Time [min]')
#longplot.set_ylabel('CPD [mV] (Sample - Probe)')
#longplot.set_title('CPD of HOPG, 618')

#plt.savefig('longplot.pdf',bbox_inches=0)
