# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:12:29 2019

@author: thewo
"""

import math as m
import numpy as np

def BTTP(EV,ISO,AP,SS):

    if SS == 0:
        sISO = np.log(ISO / 100) / np.log(2)
        sAP = -np.log(AP) / np.log(m.sqrt(2))
        sShutter = EV + sISO + sAP
        SS = m.pow(2,-sShutter)
        return(SS);
    elif EV == 0:
        EV = m.log( 100 * m.pow(2,AP) / ( ISO * SS ),2 )
        return EV;
        
        
        
        
    
Calculation = BTTP(0,100,1.4,1)
print(Calculation);
    
    
    
    
    
    
    