#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:10:07 2024

@author: dfamul
"""

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt


# Definisco i parametri del modello di Leslie

# Sopravvivenza alla nascita e aging

s0=1.0
s1=0.3
s2=0.5

# Fertilita'

f1=0.0
f2=1.0
f3=5.0

# Matrice di Leslie


A=[[s0*f1,s0*f2,s0*f3],\
   [s1,0,0],\
   [0,s2,0]]
    
B=np.zeros((3,1))

C=np.identity((3))

D=np.zeros((3,1)) 

# Popolazione iniziale

x0=[1,0,0]

# Modello di decisione

popolazione=signal.dlti(A,B,C,D)

# Orizzonte temporale di simulazione

k=np.arange(0, 30, 1, dtype=int)

# Ingresso nullo (ci deve stare comunque)

u=np.zeros((len(k),1)) 

# Simulo il modello di decisione

_, y, x=signal.dlsim(popolazione,u,k,x0)

plt.stem(k,x[:,0],'k')
plt.stem(k,x[:,1],'b')
plt.stem(k,x[:,2],'r')
plt.grid(True)
plt.legend(['I classe','II classe','III classe'])
plt.show()

  
