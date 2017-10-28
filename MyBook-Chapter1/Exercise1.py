# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:56:28 2017

@author: ndoannguyen
"""

import numpy as np
import matplotlib.pyplot as plt


#value of a polynomial
def P(coeffs, x):
    """
        Find the value of a polynomial at x
        coeffs is the coefficients a_0, ..., a_N of the polynomial
    """
    value = 0;
    for degree in range(len(coeffs)):
        value += coeffs[degree] * x**degree
    return value

def plot_in_range(begin, end, A):
    """
    """
    x_range = np.arange(begin, end, 0.1)
    y_range = original_function(x_range)
    P_range = P(A, x_range)
    plt.plot(x_range, y_range, label = "y = sin x")

    P_label = "y = "

    for degree in range(len(A)):
        P_label += " + " + str(np.round(A[degree], 2)) + "x**" + str(degree)
    
    plt.plot(x_range, P_range, label = P_label)

def original_function(x):
    return np.sin(x)           #Question a
    #return np.sin(5*x)          #Question b

def exercise1(X):
    """
        Chapter 1, exercise 1.2
        Find a polynomial P of degree 5 statisfying P(x) = sin x, x = -2, -1, 0, 1, 2
    """
    N = len(X)
    Y = np.array([original_function(x) for x in X])

    #P(x) = a_0 + a_1*x + ... + a_4*x^^4

    entries = np.zeros((N, N))
    for n in range(N):
        for i in range(N):
            entries[i][n] = X[i]**n

    A = np.dot(np.linalg.inv(entries), Y)
    plot_in_range(-5, 5, A)

X = range(-2, 3)
exercise1(X)
