import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

vacHOPG1 = np.genfromtxt("vacHOPG1.txt")
t1 = vacHOPG1[0,0]
vacHOPG1[:,0] = (vacHOPG1[:,0]-t1)/60

vacHOPG2 = np.genfromtxt("vacHOPG2.txt")
t2 = vacHOPG2[0,0]
vacHOPG2[:,0] = (vacHOPG2[:,0]-t2)/60
vacHOPG3 = np.genfromtxt("vacHOPG3.txt")
t3 = vacHOPG3[0,0]
vacHOPG3[:,0] = (vacHOPG3[:,0]-t3)/60

f,(ax,ax2) = plt.subplots(2,1,sharex=True)

#Plot the lines
ax.plot(vacHOPG1[0:360,0],vacHOPG1[0:360,1],color='r',label='Ambient')
ax.plot(vacHOPG1[359:366,0],vacHOPG1[359:366,1],'0.7')
ax.plot(vacHOPG1[365:1310,0],vacHOPG1[365:1310,1],color='b',label='Weak pump')
ax.plot(vacHOPG1[1310:1316,0],vacHOPG1[1310:1316,1],'0.7')
ax.plot(vacHOPG1[1315:-20,0],vacHOPG1[1315:-20,1],color='k',label='Turbo pump')

ax.plot(vacHOPG2[60:3450,0],vacHOPG2[60:3450,1],color='r',label='Ambient')
ax.plot(vacHOPG2[3449:3456,0],vacHOPG2[3449:3456,1],'0.7')
ax.plot(vacHOPG2[3455:5370,0],vacHOPG2[3455:5370,1],color='b',label='Weak pump')
ax.plot(vacHOPG2[5370:5376,0],vacHOPG2[5370:5376,1],'0.7')
ax.plot(vacHOPG2[5375:6410,0],vacHOPG2[5375:6410,1],color='k',label='Turbo pump')
ax.plot(vacHOPG2[6410:6421,0],vacHOPG2[6410:6421,1],'0.7')
ax.plot(vacHOPG2[6420:-20,0],vacHOPG2[6420:-20,1],'b')

ax.plot(vacHOPG3[0:1318,0],vacHOPG3[0:1318,1],color='b',label='Weak pump')
ax.plot(vacHOPG3[1317:1320,0],vacHOPG3[1317:1320,1],'0.7')
ax.plot(vacHOPG3[1320:2420,0],vacHOPG3[1320:2420,1],color='k',label='Turbo pump')
ax.plot(vacHOPG3[2420:2480,0],vacHOPG3[2420:2480,1],'0.7')
ax.plot(vacHOPG3[2480:-60,0],vacHOPG3[2480:-60,1],color='b',label='Weak pump')

#Second plot for outlier

ax2.plot(vacHOPG1[0:360,0],vacHOPG1[0:360,1],color='r',label='Ambient')
ax2.plot(vacHOPG1[359:366,0],vacHOPG1[359:366,1],'0.7')
ax2.plot(vacHOPG1[365:1310,0],vacHOPG1[365:1310,1],color='b',label='Weak pump')
ax2.plot(vacHOPG1[1310:1316,0],vacHOPG1[1310:1316,1],'0.7')
ax2.plot(vacHOPG1[1315:-20,0],vacHOPG1[1315:-20,1],color='k',label='Turbo pump')

ax2.plot(vacHOPG2[60:3450,0],vacHOPG2[60:3450,1],color='r',label='Ambient')
ax2.plot(vacHOPG2[3449:3456,0],vacHOPG2[3449:3456,1],'0.7')
ax2.plot(vacHOPG2[3455:5370,0],vacHOPG2[3455:5370,1],color='b',label='Weak pump')
ax2.plot(vacHOPG2[5370:5376,0],vacHOPG2[5370:5376,1],'0.7')
ax2.plot(vacHOPG2[5375:6410,0],vacHOPG2[5375:6410,1],color='k',label='Turbo pump')
ax2.plot(vacHOPG2[6410:6421,0],vacHOPG2[6410:6421,1],'0.7')
ax2.plot(vacHOPG2[6420:-20,0],vacHOPG2[6420:-20,1],'b')

ax2.plot(vacHOPG3[0:1318,0],vacHOPG3[0:1318,1],color='b',label='Weak pump')
ax2.plot(vacHOPG3[1317:1320,0],vacHOPG3[1317:1320,1],'0.7')
ax2.plot(vacHOPG3[1320:2420,0],vacHOPG3[1320:2420,1],color='k',label='Turbo pump')
ax2.plot(vacHOPG3[2420:2480,0],vacHOPG3[2420:2480,1],'0.7')
ax2.plot(vacHOPG3[2480:-60,0],vacHOPG3[2480:-60,1],color='b',label='Weak pump')


#Zooming an cutting
ax.set_ylim(.12,.2) # outliers only
ax2.set_ylim(-0.05,.055) # most of the data
#Hiding stuff
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off') # don't put tick labels at the top
ax2.xaxis.tick_bottom()


#Plot the legend
#p1 = plt.Rectangle((0, 0), 1, 1, fc="r")
#p2 = plt.Rectangle((0, 0), 1, 1, fc="b")
#p3 = plt.Rectangle((0, 0), 1, 1, fc="k")
#ax.legend((p1, p2, p3), ('Ambient','Weak Pump','Turbo Pump'))

plt.show()
