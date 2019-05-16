import numpy as np
import matplotlib.pylab as plt
import math

datos=np.loadtxt("datos.dat", delimiter="	" )
datos_t= datos[:,0]
datos_y= datos[:,1]


datos2=np.loadtxt("datos2.dat", delimiter="	" )
datos_t2= datos2[:,0]
datos_y2= datos2[:,1]

plt.figure()
plt.plot(datos_t,datos_y)
plt.savefig("primeraimagen.pdf")

plt.figure()
plt.plot(datos_t2,datos_y2)
plt.savefig("primeraimagen2.pdf")

angu1=(datos[:,1]-datos2[:,1])
angu=np.abs(angu1)
log=np.log(angu)
#print (angu)



plt.figure()
plt.plot(log)
plt.savefig("segundaimagen.pdf")
