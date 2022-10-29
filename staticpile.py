# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:22:58 2022

@author: albert pamonag
"""
import math
import matplotlib.pyplot as plt
import numpy as np

##PILE CAPACITY

def interpolate(X,X1,X2,Y1,Y2):
    value = Y1 + (((X - X1)/(X2 - X1))*(Y2-Y1))
    return value


def topDownSearch(x,data):

    top_index = 0 ##top value

    for i in data["angle"]:

        angle_index = float(i)
            
        if(angle_index < x):
            top_index = angle_index
    
    top = top_index
    bot = top_index + 1
        
    top_value = data["angle"][top]
    down_value = data["angle"][bot]

    value = interpolate(x,top,bot,top_value,down_value)
    return value

meyerhof_pile = {
    "angle" : [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45], 
    "nq" : [12.4,13.8,15.5,17.9,21.4,26,29.5,34,39.7,46.5,56.7,68.2,81,96,115,143,168,194,231,276,346,420,525,650,780,930]
}


##sand

angle = 35 
nq = topDownSearch(angle,meyerhof_pile)

def meyerhofSand(ap,c_prime,q_prime,phi):
    
    qp = ap*q_prime*nq
    pa = 100 ##kPa
    q1 = 0.5*pa*nq*Math.tan(phi)
    qp_limit = ap*q1
    result = Math.min(qp,qp_limit)
    return result

def plotMeyerhofNq():
    plot_x = meyerhof_pile["angle"]
    plot_y = meyerhof_pile["nq"]
    
    fig, ax = plt.subplots(figsize=(8,10))
    ax.plot(plot_x, plot_y)
    ax.set(xlabel="Soil friction Angle,Φ'(deg)", ylabel='Nq*',
            title="Variation of the maximum values Nq* with soil friction angle,Φ'(deg)")
    ax.grid()
    
    fig.savefig("test.png")
    plt.show()

plotMeyerhofNq()

# meyerhofSand()



    