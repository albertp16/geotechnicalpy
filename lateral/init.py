# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:16:47 2021

@author: Albert Pamonag
Lateral Piles Capacity Computations

"""
import math 
import matplotlib.pyplot as plt

##Transerve reinforcement 
db = 10 ##minimum per NSCP 2015
s = 60 ##mm
fc = 34.47 ##Mpa Concrete Strength
fyh = 276 ##Mpa Spiral Reinforcement 
hc = 300 #mm2
ag = 400*400 #mm2
ach = 300*300 #mm2
P = 350*1000 #N (Maximum Axial Capacity) Note: 0.65 factor

ash_arr = []
ash2_arr = []
ash_govern = []  
axial_arr = []
i = 0
max_axial = 1165 ##KN
while i <= max_axial: 
    P = i*1000
    ash = 0.3*s*hc*(fc/fyh)*((ag/ach)-1)*(0.5 - 1.4*(P/(fc*ag)))
    ash2 = 0.12*s*hc*(fc/fyh)*(0.5 + ((1.4*P)/(fc*ag)))
    govern = max(ash,ash2)
    ash_arr.append(ash)
    ash2_arr.append(ash2)
    ash_govern.append(govern)
    axial_arr.append(i)
    i = i + 1

mini_x = [157,157]
mini_y = [0,1200]    

fig, ax = plt.subplots()
ax.plot(ash_arr, axial_arr, label = "Eq. 308.5.5")
ax.plot(ash2_arr, axial_arr, label = "Eq. 308.5.6")
ax.plot(ash_govern, axial_arr, label = "Ash govern", color = "red")
ax.plot(mini_x, mini_y, label = "Value of dia. 10 @ 60mm spacing")
ax.set(xlabel='Ash (mm2)', ylabel='P (kN)',
       title='P versus Ash')
ax.grid()
plt.legend()
plt.show()

area = (math.pi/4)*math.pow(db,2)*2
print('Actual area = ' + str(area))

##Transerve reinforcement 
db = 12 ##minimum per NSCP 2015
s = 72 ##mm
fc = 34.47 ##Mpa Concrete Strength
fyh = 276 ##Mpa Spiral Reinforcement 
hc = 300 #mm2
ag = 400*400 #mm2
ach = 300*300 #mm2
P = 1165*1000 #N (Maximum Axial Capacity) Note: 0.65 factor


ash = 0.3*s*hc*(fc/fyh)*((ag/ach)-1)*(0.5 - 1.4*(P/(fc*ag)))
ash2 = 0.12*s*hc*(fc/fyh)*(0.5 + ((1.4*P)/(fc*ag)))
print('From Eq. 308.5.5 = ' + str(ash))
print('From Eq. 308.5.6 = ' + str(ash2))


area = (math.pi/4)*math.pow(db,2)*2
print('Actual area = ' + str(area))

