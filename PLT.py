#the MATPlotLib Code for my equation
import matplotlib.pyplot as plt
import numpy as np
#US values
US_Ini = 0.43
US_Com = 0.9885
#Uk values
UK_Ini = 0.60
UK_Com = 1.0972
xlist = np.arange(2020,2030)
nlist = np.arange(0,10)
#function for the graph of points
def k(a, b, c):
    c=c**a
    return b*c

ylist = k(nlist, US_Ini , US_Com)
yslist = k(nlist, UK_Ini, UK_Com)
plt.plot(xlist, ylist, 'k', label='US')
plt.plot(xlist, yslist, 'c', label='UK')
plt.xlabel('Year')
plt.ylabel('$')
plt.grid()
plt.legend()
plt.show()
