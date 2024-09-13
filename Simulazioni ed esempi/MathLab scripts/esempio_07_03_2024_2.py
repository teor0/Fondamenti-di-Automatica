#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:56:17 2024

@author: dfamul
"""

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt

# Modello Corso di studi triennale

alpha12=0.7
alpha10=0.2
alpha23=0.8
alpha20=0.15
alpha30=0.99

beta11=1

# Matrici A, B, C e D

A=[[(1-alpha12-alpha10),0,0],\
   [alpha12,(1-alpha23-alpha20),0],\
       [0,alpha23,(1-alpha30)]]
    
B=[[beta11],[0],[0]]

C=[[1.0, 1.0, 1.0],\
   [0,0,alpha30]] 
    
D=np.zeros((2,1))

# Condizione iniziale (corso di nuova istituzione)

x0=[0,0,0]

# Orizzonte temporale (numero anni accademici)

k=np.arange(0,20,1,dtype=int)

# Numero di domande di immatricolazione

u=200*np.ones((len(k),1)) 

# Variabile modello di decisione

cds=signal.dlti(A,B,C,D)

# Simulazione

_, y, x=signal.dlsim(cds,u,k,x0)

plt.subplot(2,1,1)
plt.stem(k,y[:,0])
plt.legend(['Iscritti'])
plt.subplot(2,1,2)
plt.stem(k,y[:,1])
plt.legend(['Laureati'])

   

