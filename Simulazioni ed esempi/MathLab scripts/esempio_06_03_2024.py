#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:49:43 2024

@author: dfamul
"""

# Modello aziendale per verificare il Principio di Peter

import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt

# Pesi numerici modello

# Ingresso

beta11=0.6
beta12=0.4

# Stato

alpha12=0.1
alpha13=0.05
alpha23=0.15
alpha24=0.1
alpha34=0.1
alpha35=0.05
alpha45=0.2
alpha46=0.15
alpha56=0.1
alpha50=0.05
alpha60=0.45

# Matrici A, B, C, D

A=[[-(alpha12+alpha13),0,0,0,0,0],\
   [alpha12,-(alpha23+alpha24),0,0,0,0],\
   [alpha13,alpha23,-(alpha34+alpha35),0,0,0],\
   [0,alpha24,alpha34,-(alpha45+alpha46),0,0],\
   [0,0,alpha35,alpha45,-(alpha56+alpha50),0],\
   [0,0,0,alpha46,alpha56,-alpha60]]
    
B=[[beta11],[beta12],[0],[0],[0],[0]] 


C=np.identity((6))  # misuro tutto l'organigramma

D=np.zeros((6,1))   # non monitoro le candidature esterne

# Orizzonte temporale (in trimestri, ricoridamolo)

t0=0.0

tf=40.0

N=200  # Numero di passi

t=np.linspace(t0,tf,N)

# Numero di dipendenti iniziali

x0=[300,100,150,50,90,30]

# Andamento delle candidature esterne

u=10*np.ones((len(t),1))


# Variabile Sistema Dinamico dentro python

azienda=signal.lti(A,B,C,D)

# Simulazione numerica del modello

t1, y1, x1=signal.lsim(azienda,u,t,x0)

# Frazione di incompetenti per ciascun livello stipendiale

fr1=x1[:,0]/(x1[:,0]+x1[:,1])

fr2=x1[:,2]/(x1[:,2]+x1[:,3])

fr3=x1[:,4]/(x1[:,4]+x1[:,5])

# Grafico Frazione Incompetenti

plt.plot(t1,fr1,t1,fr2,t1,fr3)
plt.legend(['I liv','II liv','III liv'])
plt.grid(True)



   





