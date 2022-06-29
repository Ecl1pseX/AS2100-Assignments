#!/usr/bin/env/python3.9
# Pranit Zope
# AE20B046
# Task 05 : Integrals using Quadrature
# File containing the fucntions used for regression (directly taken from Task02)

import numpy as np
from matplotlib import pyplot as plt



def determinant(m):
    det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return det

def inverse(m):
    inv=np.zeros((2,2))
    inv[0][0]=m[1][1]/determinant(m)
    inv[0][1]=-1*(m[0][1]/determinant(m))
    inv[1][0]=-1*(m[1][0]/determinant(m))
    inv[1][1]=(m[0][0]/determinant(m))
    return inv

def transpose(m,size):
    temp=np.ones((2,size))
    for i in range(0,size):
        temp[1][i]=m[i][1]
    return temp


def prod(AT,a,b,A,c,d):
    if(b==c):
        temp=np.zeros((a,d))
        for i in range(a):
            for j in range(d):
                sum=0
                for k in range(b):
                    sum=sum+AT[i][k]*A[k][j]
                temp[i][j]=sum
        return temp

def curve(A1,B1):             
    size=len(A1)
    A=np.ones((size,2))
    for i in range(0,size):
        A[i][1]=np.log10(A1[i])
    
    B=np.zeros((size,2))
    for i in range(size):
        B[i][0]=np.log10(B1[i])
    

    AT=transpose(A,size)
    AT_A=prod(AT,2,size,A,size,2)
    AT_A_inv=inverse(AT_A)
    AT_B=prod(AT,2,size,B,size,1)
    sol=prod(AT_A_inv,2,2,AT_B,2,1)
   
    return sol


def bfline(A1,B1):
    size=len(A1)
    A=np.ones((size,2))
    for i in range(0,size):
        A[i][1]=A1[i]
    B=np.zeros((size,2))
    for i in range(size):
        B[i][0]=B1[i]
    AT=transpose(A,size)
    AT_A=prod(AT,2,size,A,size,2)
    AT_A_inv=inverse(AT_A)
    AT_B=prod(AT,2,size,B,size,1)
    sol=prod(AT_A_inv,2,2,AT_B,2,1)

    return sol