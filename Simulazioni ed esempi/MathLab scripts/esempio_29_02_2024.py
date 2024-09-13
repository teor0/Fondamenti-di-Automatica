# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Scrivo le "matrici" A, B, C, D del modello

# importo le librerie necessarie per "simulare" sistema

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt


# inizio dai parametri "fisici" (si fa per dire)

alpha10=4.0
beta11=2.0

A=[-alpha10]
B=[beta11]
C=[1.0]
D=[0.0]

# immagazzino la quaterna A, B, C, D nella struttura
# modello di flusso che python mette a disposizione

serbatoio=signal.StateSpace(A,B,C,D)


# l'asse dei tempi e' l'intervallo [0, 5] (secondi)

t=np.arange(0,5,0.01)

# 500 passi

# Il serbatoio e' vuoto (condizione iniziale)

x0=0.0

# Costruisco l'ingresso


u=np.zeros((len(t),1))

for i in range(len(t)):
    if (t[i]>0.25) and (t[i]<1.5):
        u[i]=1.0
    else:
        u[i]=0.0

# Parte finale (simulazione)

t1, y1, x1 = signal.lsim(serbatoio,u,t,x0)

# Rappresento graficamente il risultato

plt.plot(t1,y1,'b-',linewidth=1.5)

plt.grid(True)



