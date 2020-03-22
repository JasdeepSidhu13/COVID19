import numpy as np
import matplotlib.pyplot as plt

### German data
xg=np.linspace(0,100,10)
print("No. of days="+str(xg))
yg=.0217*xg**4-1.5927*xg**3+38.058*xg**2-319.61*xg+660.22
print("Number of confirmed case predicted="+str(yg))

plt.plot(xg,yg)
plt.ylabel('Prediction of No. of people infected in Germany')
plt.show()

### Italian data
xi=np.linspace(0,100,10)
print("No. of days="+str(xi))
yi=0.04*xi**4-2.445*xi**3+50.775*xi**2-384.52*xi+727.53
plt.plot(xi,yi)
plt.ylabel('Prediction of No. of people infected in Italy')
plt.show()

### Washington state data
xw=np.linspace(0,60,11)
yw=3.924*xw**3-42.763*xw**2+216.84*xw+83.714
plt.plot(xw,abs(yw))
plt.ylabel('Prediction of No. of people infected in Washington state')
plt.show()

### California state data
xc=np.linspace(0,60,11)
yc=9.3869*xc**2-7.6845*xc+150.84
plt.plot(xc,abs(yc))
plt.ylabel('Prediction of No. of people infected in California')
plt.show()

### Florida state data
xf=np.linspace(0,60,11)
yf=0.3384*xf**3-0.2825*xf**2+6.3315*xf+10.143
plt.plot(xf,abs(yf))
plt.ylabel('Prediction of No. of people infected in Florida')
plt.show()
