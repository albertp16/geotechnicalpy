# -*- coding: utf-8 -*-
"""
Created on Fri May 19 05:53:22 2023

@author: albert pamonag, M.eng
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

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

    # plot_x = nc
    # plot_x2 = nq
    # plot_x3 = ny
    # plot_y = angle
    
    # fig, ax = plt.subplots(figsize=(15,10))
    
    # ax.plot(plot_x, plot_y, label = "nc")
    # ax.plot(plot_x2, plot_y, label = "nq")
    # ax.plot(plot_x3, plot_y, label = "ny")
    
    
    # ax.set(xlabel="Bearing Capacity Factor, Nc, Nq, Ny", ylabel="Angle of Shear resistance,Φ'(deg)",
    #         title="Meyerhof Bearing Capacity Factor")
    # ax.grid()
    # fig.savefig("Meyerhof_plot.png")
    # plt.xscale('log')
    # plt.legend()
    # plt.show()

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

interpolate_nc = interp1d(terzaghi_bearing_capacity_factors["angle"], terzaghi_bearing_capacity_factors["nc"])
interpolate_nq = interp1d(terzaghi_bearing_capacity_factors["angle"], terzaghi_bearing_capacity_factors["nq"])
interpolate_ny = interp1d(terzaghi_bearing_capacity_factors["angle"], terzaghi_bearing_capacity_factors["ny"])


def soilbearing():

#     data = [ ##1.5m depth
# [15.470164,120.958312,21.4344929715,16.57,18],
# [15.499807,121.009187,0,28,19],
# [15.444571,120.944061,32.0350893555,21.33,20],
# [15.509492,120.962494,22.7654515095,17.14,21],
# [15.460807,120.948183,0,30,22],
# [15.459467,120.982864,0,28,23],
# [15.474283,120.94629,0,28,24],
# [15.483289,120.955842,50.013915,5,25],
# [15.490177,120.970732,30.0737593555,20.33,26],
# [15.514434,121.049328,0,31,27],
# [15.482035,120.949791,0,28,28],
# [15.466679,120.93999,30.0737593555,1.5,29],
# [15.492801,120.9288,58.419586981,7.57,30],
# [15.520418,120.955009,26.7581309905,18.86,31],
# [15.461985,121.064609,52.8157729715,5.86,32],
# [15.478631,120.94816,54.2167509905,6.29,33],
# [15.507784,120.9775218,0,34,34],
# [15.485907,121.031805,45.11059,3.5,35],
# [15.465941,120.950737,0,31,36],
# [15.486114,121.032163,0,31,37],
# [15.470905,120.943887,0,32,38],
# [15.515919,120.955992,0,30,39],
# [15.491523,120.96941,0,33,40],
# [15.491792,120.992874,0,31,41],
# [15.488745,121.035599,0,33,42],

#         ]


    data = [
        [15.470164,120.958312,20.1036325,16,18],
        [15.499807,121.009187,30.0737593555,20.33,19],
        [15.444571,120.944061,31.38128,21,20],
        [15.509492,120.962494,29.41995,21,21],
        [15.460807,120.948183,0,30,22],
        [15.459467,120.982864,0,31,23],
        [15.474283,120.94629,0,39,24],
        [15.483289,120.955842,0,28,25],
        [15.490177,120.970732,33.9964193555,22.33,26],
        [15.514434,121.049328,63.939358,8.4,27],
        [15.482035,120.949791,0,31,28],
        [15.466679,120.93999,70.804013,9.07,29],
        [15.492801,120.9288,70.804013,9.07,30],
        [15.520418,120.955009,31.38128,21,31],
        [15.461985,121.064609,61.193496,8.13,32],
        [15.478631,120.94816,61.193496,8.13,33],
        [15.507784,120.9775218,0,37,34],
        [15.485907,121.031805,54.2167509905,6.29,35],
        [15.465941,120.950737,0,30,36],
        [15.486114,121.032163,0,35,37],
        [15.470905,120.943887,0,33,38],
        [15.515919,120.955992,0,28,39],
        [15.491523,120.96941,0,32,40],
        [15.491792,120.992874,52.8157729715,5.86,41],
        [15.488745,121.035599,0,32,42],
            ]

    data_length = len(data)
    i = 0
    while i < data_length:
        angle_index = data[i][3]
        c_index = data[i][2]
        nc_value = interpolate_nc(angle_index)  
        nq_value = interpolate_nq(angle_index)  
        ny_value = interpolate_ny(angle_index)  
        value = bearingTerzaghi(c_index,nc_value,0,nq_value,18,1,ny_value,"square")
        print(value/3)
        i += 1

soilbearing()
# bh_data = [
#     []
#     ]
