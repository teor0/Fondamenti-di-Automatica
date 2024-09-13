#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:52:58 2024

@author: dfamul
"""

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt

# Modello del tempo atmosferico

# Matrice di transizione della catena di Markov

A=np.array([[0.2,0.1,0.05],\
            [0.3,0.2,0.15],\
            [0.5,0.7,0.8]])
    
# Condizione iniziale random

x0=np.random.rand(3,1)

# Questo non e' un vettore stocastico perche', in linea
# di prinicipio la somma degli elementi non "vale" 1

x0=x0/np.sum(x0)

# Divido per la somma e genero il vettore stocastico 

npassi=100

# Numero di passi rispetto al quale voglio valutare
# stato della catena di Markov

for i in range(npassi):
    x0=A@x0
    
print('Stato dopo 100 passi :', x0)
   