import numpy as np
import matplotlib.pyplot as plt
import math
theta=np.arange(0,2*np.pi,0.02)
#for i in range (315):
    #print(math.degrees(theta[i]))
x=[math.radians(45),math.radians(46),math.radians(47),math.radians(48),math.radians(49)]
print(x)
y=[1.3,1.4,1.5,1.4,1.6]
plt.subplot(polar=True)
plt.plot(theta,2*np.ones_like(theta),lw=2)
plt.plot(theta,theta/6,'--',lw=2)
plt.plot(0.7853,1.3,lw=2)
plt.plot(0.802,1.4,lw=2)
plt.plot(0.820,1.5,lw=2)
plt.scatter(x,y,s=10)
plt.plot(0.837,1.4,lw=2)
plt.plot(0.855,1.6,lw=2)
plt.plot(theta,np.cos(5*theta),'--',lw=2)
plt.plot(theta,2*np.cos(4*theta),lw=2)
plt.rgrids(np.arange(0.5,2,0.5),angle=45)
plt.thetagrids([0,45,90])
print()
plt.show()