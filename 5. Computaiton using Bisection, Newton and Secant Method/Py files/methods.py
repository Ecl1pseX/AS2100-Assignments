#!/usr/bin/env/python3.9
# Pranit Zope
# AE20B046
# Task 05 : Integrals using Quadrature
# File containing the fucntions of various methods used

import numpy as np

def leftep(n):
    dx=(np.pi/2)/n
    area=0
    x=0
    for i in range(n):
        area=area+np.sin(x)*dx
        x=x+dx
    return area

def rightep(n):
    dx=(np.pi/2)/n
    area=0
    x=dx
    for i in range(n):
        area=area+np.sin(x)*dx
        x=x+dx
    return area

def midpt(n):
    dx=(np.pi/2)/n
    area=0
    x=dx/2
    for i in range(n):
        area=area+np.sin(x)*dx
        x=x+dx
    return area

def trapezoid(n):
    dx=(np.pi/2)/n
    area=0
    x=0
    for i in range(n):
        temp=((np.sin(x)+np.sin(x+dx))/2)*dx
        area=area+temp
        x=x+dx
    return area
