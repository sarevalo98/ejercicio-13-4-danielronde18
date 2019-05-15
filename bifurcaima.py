import numpy as np
import matplotlib.pylab as plt
import math

datos=np.loadtxt("datosbifur.dat", delimiter="	" )
datos_t= datos[:,0]
datos_y= datos[:,1]

plt.figure()
plt.plot(datos_t,datos_y)
plt.savefig("primeraimagen.pdf")
