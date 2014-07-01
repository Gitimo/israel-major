import numpy as np
import matplotlib.pyplot as plt
import pylab as pyl
from matplotlib import rc, rcParams
from matplotlib.ticker import MultipleLocator

axis = ('Downstairs - old','Downstairs - new','Upstairs')

xpos= (11,22,34,43,58,64,70,75,80,84,87,91,94,96,98,100)
upISI = (512.1,525.5,534,536.7,540,542,543,543.8,544.2,543.5,-100,-111,-111,-111,-111,-111)
upISIerr = (.02,.11,4,.3,1.4,3,1.6,0.9,0.9,0.6,0,0,0,0,0,0)

downoldISI = (433.1,454,464.1,466,475,476.9,480.1,483,487.7,486,-100,-111,-111,-111,-111,-111)
downoldISIerr = (.7,3,.4,6,2,.8,.9,1.7,0.4,2,0,0,0,0,0,0)

downnewISI = (405,441,430,460,484,470,480,475,478,480,-111,481,-111,482,-111,480)
downnewISIerr = (5,1,20,12,15,20,10,8,2,11,0,1,0,3,0,3)

majorLocator   = MultipleLocator(0.1)
minorLocator   = MultipleLocator(0.05)

width=0.2

fig, ax = plt.subplots()
plt.errorbar(xpos,	upISI,		yerr=upISIerr,xerr=0.5,			fmt='o',alpha=0.8,color='0.5',ecolor='k')
plt.errorbar(xpos,	downnewISI,	yerr=downnewISIerr,xerr=0.5,	fmt='o',alpha=0.8,color='b',ecolor='k')
plt.errorbar(xpos,	downoldISI,	yerr=downoldISIerr,xerr=0.5,	fmt='o',alpha=0.8,color='r',ecolor='k')


plt.grid(True,axis='y',which='minor',color='0.4',linestyle='-')
plt.grid(True,axis='y',which='major',color='0.8',linestyle='-')
plt.xlim(0,110)
plt.ylim(400,550)
ax.set_ylabel('SPV (mV)')
ax.set_xlabel('Percentage of maximum intensity')
ax.set_title('Surface Photo-Voltage compared')
#ax.set_xticks(xpos)
#ax.set_xticklabels( ISX )
#plt.xticks(xpos,ISX)

p1 = plt.Rectangle((0, 0), 1, 1, fc="0.5")
p2 = plt.Rectangle((0, 0), 1, 1, fc="r")
p3 = plt.Rectangle((0, 0), 1, 1, fc="b")
plt.legend((p1, p2,p3), ('Upstairs','Downstairs - old','Downstairs - new'),loc=4)

#ax.yaxis.set_major_locator(majorLocator)
#ax.yaxis.set_minor_locator(minorLocator)
ax.set_axisbelow(True)

#plt.show()
plt.savefig('SaturationIntensitySeries.pdf', bbox_inches=0)