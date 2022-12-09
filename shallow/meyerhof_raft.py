# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:58:58 2022

@author: albert pamonag (albertp16)
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


##given data 
data = {
        "B" : 20, ##ft
        "Df" : 6.2, ##ft
        "Cu" : 2000, ##lb/ft2
        "FOS" : 2.5, 
        "phi" : 0
        }

meyerhof_bearing_capacity_factors = {
    "angle" : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
    "nc" : [5.14,5.38,5.63,5.90,6.19,6.49,6.81,7.16,7.53,7.92,8.35,8.80,9.28,9.81,10.37,10.98,11.63,12.34,13.10,13.93,14.83,15.82,16.88,18.05,19.32,20.72,22.25,23.94,25.80,27.86,30.14,32.67,35.49,38.64,42.16,46.12,50.59,55.63,61.35,67.87,75.31,83.86,93.71,105.11,118.37,133.88,152.10,173.64,199.26,229.93,266.89],
    "nq" : [1.00,1.09,1.20,1.31,1.43,1.57,1.72,1.88,2.06,2.25,2.47,2.71,2.97,3.26,3.59,3.94,4.34,4.77,5.26,5.80,6.40,7.07,7.82,8.66,9.60,10.66,11.85,13.20,14.72,16.44,18.40,20.63,23.18,26.09,29.44,33.30,37.75,42.92,48.93,55.96,64.20,73.90,85.38,99.02,115.31,134.88,158.51,187.21,222.32,265.51,319.07],
    "ny" : [0.00,0.07,0.15,0.24,0.34,0.45,0.57,0.71,0.86,1.03,1.22,1.44,1.69,1.97,2.29,2.65,3.06,3.53,4.07,4.68,5.39,6.20,7.13,8.20,9.44,10.88,12.54,14.47,16.72,19.34,22.40,25.99,30.22,35.19,41.06,48.03,56.31,66.19,78.03,92.25,109.41,130.22,155.55,186.54,224.64,271.76,330.35,403.67,496.01,613.16,762.89]
}

meyerhof_pd = {
    'nc': meyerhof_bearing_capacity_factors['nc'],
    'nq': meyerhof_bearing_capacity_factors['nq'],
    'ny': meyerhof_bearing_capacity_factors['ny'],
    }

angle = 0
nc = meyerhof_bearing_capacity_factors["nc"][0]
nq = meyerhof_bearing_capacity_factors["nq"][0]
ny = meyerhof_bearing_capacity_factors["ny"][0]

meyerhof_table = pd.DataFrame(data = meyerhof_bearing_capacity_factors)

def meyerhofShapeFactor(b,l,nq,nc,angle):
    fcs = 1 + (b/l)*(nq/nc)
    fqs = 1 + (b/l)*(nq/nc)*math.tan(math.radians(angle)) ##TODO
    fys = 1 - (0.4*(b/l))
        
    return {
        "fcs" : fcs, 
        "fqs" : fqs,
        "fys" : fys
            
    }

shape_factor = meyerhofShapeFactor(data["B"],data["B"],nq,nc,angle)
print(shape_factor)
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

# plotTerzaghi(nc,nq,ny,angle,"Terzaghi")