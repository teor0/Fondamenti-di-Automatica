#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:06:52 2024

@author: dfamul
"""

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt


# Modello assicurazioni, matrice di transizione A

A=np.zeros((14,14))

# Probabilita' di avere un sinistro da un anno al
# successivo

p=0.2

A[0,0]=(1-p)
A[0,1]=(1-p)

A[13,12]=p
A[13,13]=p

for i in range(1,13,1):
    A[i,i-1]=p
    A[i,i+1]=1-p

# Condizione iniziale random

x0=np.random.rand(14,1)

# Questo non e' un vettore stocastico perche', in linea
# di prinicipio la somma degli elementi non "vale" 1

x0=x0/np.sum(x0)

# Vedo cosa succede dopo, ad es., 30 anni

npassi=30

for i in range(npassi):
    x0=A@x0
    
print('Stato dopo 30 passi :', x0)


