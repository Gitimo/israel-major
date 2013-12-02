#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
from  pylab import *
import matplotlib.pyplot as plt

ind1 = (0.9, 1.65, 2.15, 2.9)
ind2 = (1.1, 1.85, 2.35, 3.1)

bar_width=0.2

HOPG = ( -0.481, -1.112, -1.041, 0)
HOPGstdev = (0.007, 0.008, 0.024, 0)
PROBE = ( -0.481+4.65-0.071, -1.112+4.65-0.071, -1.041+4.65, 0)
PROBEstdev = (0.007,0.008,0.024, 0)


SE, ax1 = plt.subplots()
ax2 = ax1.twinx()
PL1 = ax1.bar(ind1, HOPG, bar_width, 
				alpha=0.4, color='blue', 
				yerr=HOPGstdev, error_kw={'ecolor': '0.3'})
				
PL2 = ax2.bar(ind2, PROBE, bar_width,
				alpha=0.4, color='red',
				yerr=PROBEstdev, error_kw={'ecolor': '0.3'})

ax1.set_ylabel('CPD (mV)', color ='b')
ax2.set_ylabel('$\phi$ (mV)', color ='r')
ax1.set_title('CPD of HOPG & work-function of the probe')
ax1.set_xticklabels( (	'Air', 'N$_2$ out', 'N$_2$ in', 'Vacuum'), 
						rotation=90 )
ax2.set_xticklabels( (	'Air', 'N$_2$ out', 'N$_2$ in', 'Vacuum'), 
						rotation=90 )
ax2.figure.canvas.draw()
ax1.legend( (PL1[0], PL2[0]), 
			('CPD (V)', '$\phi_{Probe}$ (eV)'), 'lower right' ,numpoints=1)
plt.subplots_adjust(bottom=0.2)
plt.show()

