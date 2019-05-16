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

datos3=np.loadtxt("datos3.dat", delimiter="	" )
datos_t3= datos3[:,0]
datos_y3= datos3[:,1]


datos4=np.loadtxt("datos4.dat", delimiter="	" )
datos_t4= datos4[:,0]
datos_y4= datos4[:,1]

angu5=(datos3[:,1]-datos4[:,1])
angu6=np.abs(angu5)
log6=np.log(angu6)

plt.figure()
plt.plot(log)
plt.savefig("terceraimagen.pdf")

#La tercera grafica queda igual a la segunda aun cuando usamos los valores mencionados en el 06-oscPoincareBifur.
