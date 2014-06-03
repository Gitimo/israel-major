import numpy as np
import matplotlib.pyplot as plt
import pylab as pyl
from matplotlib import rc, rcParams
from matplotlib.ticker import MultipleLocator

axis = ('Downstairs','Upstairs')

ISX = ('0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0')
xpos=np.arange(len(ISX))
upISI = (512.1,525.5,534,536.7,540,542,543,543.8,544.2,543.5)
upISIerr = (.02,.11,4,.3,1.4,3,1.6,0.9,0.9,0.6)

downISI = (433.1,454,464.1,466,475,476.9,480.1,483,487.7,486)
downISIerr = (.7,3,.4,6,2,.8,.9,1.7,0.4,2)

majorLocator   = MultipleLocator(0.1)
minorLocator   = MultipleLocator(0.05)

width=0.15

fig, ax = plt.subplots()
plt.bar(xpos-width,	upISI,width=width,yerr=upISIerr,align='center',alpha=0.8,color='0.5',ecolor='k')
plt.bar(xpos+width,	downISI,width=width,yerr=downISIerr,align='center',alpha=0.8,color='r',ecolor='k')


plt.grid(True,axis='y',which='minor',color='0.4',linestyle='-')
plt.grid(True,axis='y',which='major',color='0.8',linestyle='-')

plt.ylim(425,550)
ax.set_ylabel('SPV (mV)')
ax.set_xlabel('Current through Diode (A)')
ax.set_title('Surface Photo-Voltage compared')
#ax.set_xticks(xpos)
#ax.set_xticklabels( ISX )
plt.xticks(xpos,ISX)

p1 = plt.Rectangle((0, 0), 1, 1, fc="0.5")
p2 = plt.Rectangle((0, 0), 1, 1, fc="r")
plt.legend((p1, p2), ('Upstairs','Downstairs'),loc=4)

#ax.yaxis.set_major_locator(majorLocator)
#ax.yaxis.set_minor_locator(minorLocator)
ax.set_axisbelow(True)

#plt.show()
plt.savefig('SaturationCurrentSeries.pdf', bbox_inches=0)
