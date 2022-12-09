# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:56:41 2022

@author: albert pamonag
"""
import pandas as pd
data = {
    "1" : {
        "length" : 20,
        "ysat" : 118,
        "cu" : 700,
        "PI" : 15
    },
    "2" : {
        "length" : 40,
        "ysat" : 122.4,
        "cu" : 1500,
        "PI" : 20
    },    
}

# //Ultimate Skin Friction Resistance 

# //using alpha method
Pa = 2000 ## 100

alpha = {
    "0.1" : 1,
    "0.2" : 0.92,
    "0.3" : 0.82,
    "0.4" : 0.74,
    "0.6" : 0.62,
    "0.8" : 0.54,
    "1.0" : 0.48,
    "1.2" : 0.42,
    "1.4" : 0.40,
    "1.6" : 0.38,
    "1.8" : 0.36,
    "2.0" : 0.35,
    "2.4" : 0.34,
    "2.8" : 0.34,
}
print(alpha)

def usr(alpha,cu,perimeter,length):
    value = alpha*cu*perimeter*length 
    return value

def topBottomSearch(value,data):

    for i in data:
        index_one = float(i)
        if(index_one > value):
            bottom = index_one
            bottom_index = i
            break

    for i in data:
        index_one = float(i)
        if(index_one < value):
            top = index_one
            top_index = i
    results = {
        'top' : top,
        'bottom' : bottom
        }
    return results

def interpolate(Y1,Y2,X1,X2,X):
    Y = Y1 + (Y2 - Y1)/(X2 - X1) * (X * X1)
    return Y


perimeter = (16*4)/12 ##ft 
pd_label = []
pd_length = []
pd_cu = []
pd_alpha = []
pd_skin = []
total_length = 0
total_skin = 0
for i in data:
    pd_label.append('Layer ' + str(i))
    cu = data[i]["cu"]
    length = data[i]["length"]
    ratio = cu/Pa
    pd_length.append(length)
    pd_cu.append(cu)
    total_length += length
    results = topBottomSearch(ratio,alpha)
    # print(results['top'])
    top_value = alpha[str(results['top'])]
    bot_value = alpha[str(results['bottom'])]
    print(top_value)
    print(bot_value)
    print(results['top'])
    alpha_value = interpolate(top_value,bot_value,results['top'],results['bottom'],ratio)
    
    pd_alpha.append(alpha_value)
    
    # ##console.log(alpha_value)
    friction = usr(alpha_value,cu,perimeter,length)
    pd_skin.append(friction/1000)
    total_skin += friction/1000
    # print(friction/1000)
pd_label.append('Total')
pd_length.append(total_length)
pd_cu.append('')
pd_alpha.append('')
pd_skin.append(total_skin)

df = pd.DataFrame({
      'Desciption': pd_label,
      'Length (ft)': pd_length,
      'Cu': pd_cu,
      'Alpha': pd_alpha,
      'Ultimate Skin Friction (kips)': pd_skin,     
      })
# //-=--=-=-