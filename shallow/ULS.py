# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:58:58 2022

@author: albert pamonag (albertp16)
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

terzaghi_bearing_capacity_factors = {
    "angle" : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
    "nc" : [5.70,6.00,6.30,6.62,6.97,7.34,7.73,8.15,8.60,9.09,9.61,10.16,10.76,11.41,12.11,12.86,13.68,14.60,15.12,16.56,17.69,18.92,20.27,21.75,23.36,25.13,27.09,29.24,31.61,34.24,37.16,40.41,44.04,48.09,52.64,57.75,63.53,70.01,77.50,85.97,95.66,106.81,119.67,134.58,151.95,172.28,196.22,224.55,258.28,298.71,347.50],
    "nq" : [1.00,1.10,1.22,1.35,1.49,1.64,1.81,2,2.21,2.44,2.69,2.98,3.29,3.63,4.02,4.45,4.92,5.45,6.04,6.70,7.44,8.26,9.19,10.23,11.40,12.72,14.21,15.90,17.81,19.98,22.46,25.28,28.52,32.23,36.50,41.44,47.16,53.80,61.55,70.61,81.27,93.85,108.75,126.50,147.74,173.28,204.19,241.80,287.85,344.64,415.14],
    "ny" : [0.00,0.01,0.04,0.06,0.10,0.14,0.20,0.27,0.35,0.44,0.56,0.69,0.85,1.04,1.26,1.52,1.82,2.18,2.59,3.07,3.64,4.31,5.09,6,7.08,8.34,9.84,11.60,13.70,16.18,19.13,22.65,26.87,31.94,38.04,45.41,54.36,65.27,78.61,95.03,115.31,140.51,171.99,211.56,261.60,325.34,407.11,512.84,650.67,831.99,1072.80]
}

meyerhof_bearing_capacity_factors = {
    "angle" : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
    "nc" : [5.14,5.38,5.63,5.90,6.19,6.49,6.81,7.16,7.53,7.92,8.35,8.80,9.28,9.81,10.37,10.98,11.63,12.34,13.10,13.93,14.83,15.82,16.88,18.05,19.32,20.72,22.25,23.94,25.80,27.86,30.14,32.67,35.49,38.64,42.16,46.12,50.59,55.63,61.35,67.87,75.31,83.86,93.71,105.11,118.37,133.88,152.10,173.64,199.26,229.93,266.89],
    "nq" : [1.00,1.09,1.20,1.31,1.43,1.57,1.72,1.88,2.06,2.25,2.47,2.71,2.97,3.26,3.59,3.94,4.34,4.77,5.26,5.80,6.40,7.07,7.82,8.66,9.60,10.66,11.85,13.20,14.72,16.44,18.40,20.63,23.18,26.09,29.44,33.30,37.75,42.92,48.93,55.96,64.20,73.90,85.38,99.02,115.31,134.88,158.51,187.21,222.32,265.51,319.07],
    "ny" : [0.00,0.07,0.15,0.24,0.34,0.45,0.57,0.71,0.86,1.03,1.22,1.44,1.69,1.97,2.29,2.65,3.06,3.53,4.07,4.68,5.39,6.20,7.13,8.20,9.44,10.88,12.54,14.47,16.72,19.34,22.40,25.99,30.22,35.19,41.06,48.03,56.31,66.19,78.03,92.25,109.41,130.22,155.55,186.54,224.64,271.76,330.35,403.67,496.01,613.16,762.89]
}

terzaphi_pd = {
    'nc': terzaghi_bearing_capacity_factors['nc'],
    'nq': terzaghi_bearing_capacity_factors['nq'],
    'ny': terzaghi_bearing_capacity_factors['ny'],
    }

terzagi_table = pd.DataFrame(data = terzaphi_pd)

def plotTerzaghi(nc,nq,ny,angle,author,plotx,ploty):
    
    ##defeault size
    if plotx == 'undefined' : plotx = 15
    if ploty == 'undefined' : ploty = 10
    
    fig, ax = plt.subplots(figsize=(plotx,ploty))
    ax.plot(nc, angle, label = "nc")
    ax.plot(nq, angle, label = "nq")
    ax.plot(ny, angle, label = "ny")
    
    if(author == 't'):
        name = 'Terzaghi'
    elif(author == 'm'):
        name = 'Meyerhof'
    
    ax.set(xlabel="Bearing Capacity Factor, Nc, Nq, Ny", ylabel="Angle of Shear resistance,Φ'(deg)",
            title= name + "Bearing Capacity Factor")
    ax.grid()
    fig.savefig(name + "_plot.png")
    plt.xscale('log')
    plt.legend()
    plt.show()

    plot_x = nc
    plot_x2 = nq
    plot_x3 = ny
    plot_y = angle
    
    fig, ax = plt.subplots(figsize=(15,10))
    
    ax.plot(plot_x, plot_y, label = "nc")
    ax.plot(plot_x2, plot_y, label = "nq")
    ax.plot(plot_x3, plot_y, label = "ny")
    
    
    ax.set(xlabel="Bearing Capacity Factor, Nc, Nq, Ny", ylabel="Angle of Shear resistance,Φ'(deg)",
            title="Meyerhof Bearing Capacity Factor")
    ax.grid()
    fig.savefig("Meyerhof_plot.png")
    plt.xscale('log')
    plt.legend()
    plt.show()

def bearingTerzaghi(c,nc,q,nq,y,b,nr,ftg_type):
    """
    Terzaghi (1943) Bearing Capacity Equation

    Parameters
    ----------
    c : TYPE float
        DESCRIPTION. Cohesion\n
    nc : TYPE float
        DESCRIPTION. Terzaghi Capacity Factors\n
    q : TYPE float
        DESCRIPTION. Surcharge\n
    nq : TYPE float
        DESCRIPTION. Terzaghi Capacity Factors\n
    y : TYPE float
        DESCRIPTION. Unit Weight of Soil\n
    b : TYPE float
        DESCRIPTION. Width of Foundation\n
    nr : TYPE float
        DESCRIPTION.Terzaghi Capacity Factors\n
    ftg_type : TYPE string
        DESCRIPTION. sc & sr factor from type of foundation ["strip","square","circular"]\n

    Returns
    -------
    ubc : TYPE float
        DESCRIPTION. Ultimate Bearing Capacity

    """
    if ftg_type == 'strip':
        sc = 1
        sr = 1
    elif ftg_type == 'square': 
        sc = 1.3 
        sr = 0.8
    elif ftg_type == 'circular': 
        sc = 1.3
        sr = 0.6 
    
    cohesion_term = c*nc*sc
    surcharge_term = q*nq 
    soil_weight_term = 0.5*y*b*nr*sr
    
    ubc = cohesion_term + surcharge_term + soil_weight_term
    return ubc


"-----------------------------------------------"
"------------------Meyerhof---------------------"
"-----------------------------------------------"

def meyerhofShapeFactor(b,l,nq,nc,angle):
    fcs = 1 + (b/l)*(nq/nc)
    fqs = 1 + (b/l)*(nq/nc)*math.tan(math.radians(angle)) ##TODO
    fys = 1 - (0.4*(b/l))
        
    return {
        "fcs" : fcs, 
        "fqs" : fqs,
        "fys" : fys
            
    }

def meyerhofInclinationFactor(angle,beta):
    '''
    Inclination Factors<br>
    reference: Meyerhof (1963); Hanna and Meyerhof (1981)
    Parameters
    ----------
    angle : TYPE float<br>
        DESCRIPTION.Angle of friction<br>
    beta : TYPE float<br>
        DESCRIPTION.Inclination of the load on the foundation with respect to the vertical<br>

    Returns
    -------
    dict <br>
        DESCRIPTION. Meyerhof Inclination Factors

    '''
    fci = math.pow((1 - (beta/90)),2)
    fqi = fci
    fyi = 1 - (beta/angle)

    return {
        "fci" : fci,
        "fqi" : fqi,
        "fyi" : fyi
    }

def meyerhofDepthFactor(df,b,angle,nc):

    dfoverB = df/b
    rad_angle = math.radians(angle)
    if dfoverB <= 1:
        if angle == 0 :
            fcd = 1 + (0.4*(dfoverB))
            fqd = 1
            fyd = 1
        else:
            fqd =  1 + ((2*math.tan(rad_angle))*math.pow(1 - math.sin(rad_angle),2)*dfoverB)
            fcd = fqd - ((1 - fqd)/(nc*math.tan(rad_angle)))
            fyd  = 1
    else :
        if angle == 0:
            fqd_init = 0.4*math.atan(dfoverB) ##radians
            fqd =  1 + (0.4*fqd_init)
            fyd  = 1
            fcd = 1 
         
        else:
            fqd_init = math.atan(dfoverB) ##radians
            fqd =  1 + 2*math.atan(rad_angle)*math.pow(1 - math.sin(rad_angle),2)*fqd_init
            fcd = 1 + (0.4*(dfoverB))
            fyd  = 1
     
    return {
        "fcd" : fcd,
        "fqd" : fqd,
        "fyd" : fyd,               
    }

def bearingMeyerhof(c,nc,fcs,fcd,fci,q,nq,fqs,fqd,fqi,y,b,nr,fys,fyd,fyi):
    cohension = c*nc*fcs*fcd*fci
    surcharge = q*nq*fqs*fqd*fqi
    soil = 0.5*y*b*nr*fys*fyd*fyi
    qu = cohension + surcharge + soil
    return qu
