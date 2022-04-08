# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np #importing numpy
#import math
import matplotlib.pyplot as plt

# k = shape factor
# v = mean wind speed from global wind atlas, HKN measurements
# a =v/0.886; scale factor formula from introduction to wind turbines
num = 10000 #number of steps in which the probability distribution is divided into
u = np.linspace(0,25,num)
#Weibull curve
# The below function gives us the plots of probability distribution curve (weibull curve). We need 
# to provide values of k (shape factor), v (mean wind speed), a (scale factor) and num.
# The function also returns the    
def weibull_curve(k,v,a,num,col):
    f = (k/a)*((u/a)**(k-1))* (np.exp(-((u/a)**k))) #formula to calculate probability 
    # distribution for different values of k,a,u 
    z = int(num/25) # This step is to keep f = 1
    f = f/z # This step is to keep f = 1
    #print(sum(f)) #should always be equal to one
    plt.subplot(1, 2, 1)
    plt.xlim(0,25)
    plt.ylim(0,0.1)
    plt.plot(u, f*z, marker='', linestyle='-', color=col,label='Square') 
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Weibull PDF') 
    plt.title('Weibull Curve')
    return f

freq1 = np.array(weibull_curve(2.2, 9.37, 9.37/0.886, num,"r")) #Frequency wind atlas
freq2 = np.array(weibull_curve(2.3, 9.69, 10.95, num, "g")) #Frequency HKN experiment data
# Omnidirectional wind speed data at a height of 120m

# Lidar measurements at  HKN at 120m

#Power curve
#The power curve is simply modelled by using simple formula between 0 and cut out speed.
#Beyond cut out speed until 25m/s it is operated at rated power. Above 25m/s P=0. 


pi = np.pi
r = 120 #radius of rotor
rho =0.53#density
Cp = 16/27
eta = 0.9 # efficiency of drive train
#A = np.pi(r**2) #Area swept by rotor
P = []
for u1 in u:
    if u1>0 and u1<=12: #range is 0 to 12 to make curve much more smoother
        P.append(0.5*Cp*rho*(u1**3)*(pi*(r**2)*eta))
    elif u1>12 and u1<= 25:
        P.append(11000000.)  
    else:
        P.append(0.)
p = [item/1000000 for item in P] #converting power to MW
power_curve = np.array(p) # converting to array
plt.subplot(1, 2, 2)
plt.xlim(0,25)
plt.ylim(0,12)
plt.plot(u,p, marker='', linestyle='-', color='b',label='Square') 
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Power (MW)') 
plt.title('Power Curve')
plt.savefig('Weibull_Powercurve.pdf')

#Power yield & capacity factor
#Power is calculated by multiplying the pdf with the power curve
def power_yield(freq): 
    Py = 0.95*sum(freq*power_curve) #Power Yield in MW, 5% wake losses 
    CF = Py/11 #Capacity factor
    print(CF)
    
power_yield(freq1) #Frequency wind atlas
power_yield(freq2) #Frequency HKN experiment data