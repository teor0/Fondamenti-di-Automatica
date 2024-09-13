#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:04:34 2024

@author: dfamul
"""

# modello dei due serbatoi (monte e valle)

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt

# parametri numerici del modello

alpha12=0.5
alpha20=0.2
beta11=1

# Matrici A, B, C e D
A=[[-alpha12,0.0],\
   [alpha12,-alpha20]]
    
B=[[beta11],[0]]

C=[[0,alpha20]]

D=[[0]]

# Orizzonte temporale

t0=0.0
tf=30.0


N=300

t=np.linspace(t0,tf,N)

# Condizioni iniziali

x0=[0.0,0.0]


# Profilo temporale ingresso

u=np.ones((len(t),1))

# Sistema dinamico immagazzinato dentro python

tanks=signal.lti(A,B,C,D)

# Simulazione numerica del sistema

t1, y1, x1 = signal.lsim(tanks,u,t,x0)

# Rappresento il risultato

fig, axs=plt.subplots(2)
axs[0].plot(t1,x1[:,0],t1,x1[:,1],'b-',linewidth=1.5)
axs[0].legend(['Vol 1','Vol 2'])
axs[0].grid(True)
axs[1].plot(t1, y1,'k-',linewidth=1.5)
axs[1].grid(True)

