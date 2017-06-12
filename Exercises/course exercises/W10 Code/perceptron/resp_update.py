# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:15:23 2015

@author: zhengzhang
"""
def response(w, x):
    y = x[0] * w[0] + x[1]*w[1]
    if y >= 0:
        return 1
    else:
        return -1

def updateWeights(w, x, lr, iterError):
    """
    todo: implement the delta update rule
    updates the weights status, w at time t+1 is
    w(t+1) = w(t) + learningRate*(d-r)*x
    where d is desired output and r the perceptron response
    iterError is (d-r)
    """
    w[0] += lr * iterError * x[0]
    w[1] += lr * iterError * x[1]
    return 