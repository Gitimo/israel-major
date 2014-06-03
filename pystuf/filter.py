import numpy as np
import matplotlib.pyplot as plt
import pylab as pyl
from matplotlib import rc, rcParams
from matplotlib.ticker import MultipleLocator

axis = ('Upstairs','Downstairs both','Downstairs outer')

ISX = ('56','66','69','71','74','74','100','100')
xpos=np.arange(len(ISX))

up = (535.2,540.4,533.9,543.1,540.4,541.73,543.5,0)
uperr = (.5,.4,.4,.3,.12,.09,.6,0)

downB = (473,0,462,0,473,0,480.8,479)
downBerr = (1.1,0,1.8,0,1.4,0,.9,1.8)

downO = (473,469.7,472,478.4,481,476,489,0)
downOerr = (.6,.5,3,.5,1.3,6,2,0)

majorLocator   = MultipleLocator(0.1)
minorLocator   = MultipleLocator(0.05)

width=0.15

fig, ax = plt.subplots()
plt.bar(xpos-width,	up,width=width,yerr=uperr,align='center',alpha=0.8,color='0.5',ecolor='k')
plt.bar(xpos,	downB,width=width,yerr=downBerr,align='center',alpha=0.8,color='g',ecolor='k')
plt.bar(xpos+width,	downO,width=width,yerr=downOerr,align='center',alpha=0.8,color='r',ecolor='k')


plt.grid(True,axis='y',which='minor',color='0.4',linestyle='-')
plt.grid(True,axis='y',which='major',color='0.8',linestyle='-')

plt.ylim(425,550)
ax.set_ylabel('SPV (mV)')
ax.set_xlabel('Transmission percentage of filter')
ax.set_title('Surface Photo-Voltage compared')
#ax.set_xticks(xpos)
#ax.set_xticklabels( ISX )
plt.xticks(xpos,ISX)

p1 = plt.Rectangle((0, 0), 1, 1, fc="0.5")
p2 = plt.Rectangle((0, 0), 1, 1, fc="g")
p3 = plt.Rectangle((0, 0), 1, 1, fc="r")
plt.legend((p1, p2,p3), ('Upstairs','Downstairs both','Downstairs outer'),loc=4)

#ax.yaxis.set_major_locator(majorLocator)
#ax.yaxis.set_minor_locator(minorLocator)
ax.set_axisbelow(True)

#plt.show()
plt.savefig('SaturationFilterSeries.pdf', bbox_inches=0)

