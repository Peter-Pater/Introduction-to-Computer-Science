# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:46:39 2016

@author: Mebius, Weichen
"""
import math


class Data:
    def __init__(self, points):
        self.x_list = [p[0] for p in points]
        self.y_list = [p[1] for p in points]
    def xmean(self):
        #comment out the following line when you start
        return sum(self.x_list)/len(self.x_list)
        # TODO: implement this function to return the mean of all the x coordinates
    def ymean(self):
        #comment out the following line when you start
        return sum(self.y_list)/len(self.y_list)
        # TODO: implement this function to return the mean of all the y coordinates
    def xsd(self):
        d = 0
        for x in self.x_list:
            d = d + (x - self.xmean())**2
        d = d/len(self.x_list)
        d = d ** 0.5
        return d
        # TODO: implement this function to return the standard deviation of all the x coordinates
    def ysd(self):
        d = 0
        for y in self.y_list:
            d = d + (y - self.ymean())**2
        d = d/len(self.y_list)
        d = d ** 0.5
        return d

        # TODO: implement this function to return the standard deviation of all the y coordinates

    def correlation(self):
        #comment out the following line when you start
        return
        mul_list = [(self.x_list[i]*self.y_list[i]) for i in range(len(self.x_list))]
        x_sq = [(self.x_list[i])**2 for i in range(len(self.x_list))]
        y_sq = [(self.y_list[i])**2 for i in range(len(self.y_list))]
        r = sum(mul_list)/(math.sqrt(sum(x_sq)*sum(y_sq)))
        return r

    def slope(self):
        #comment out the following line when you start
        return
        r = self.correlation()
        s_x = self.xsd()
        s_y = self.ysd()
        b = r*(s_y/s_x)
        return b

    def intercept(self):
        #comment out the following line when you start
        return
        A = self.ymean() - self.slope()*self.xmean()
        return A

    def reg_error(self, a, b):
        pass
        # TODO: implement this function to return the summed square errors

if __name__ == "__main__":
    points = [(3.723, 14.517), (5.634, 6.672), (4.123, 7.426)]
    our_data = Data(points)

    x_mean = our_data.xmean()
    y_mean = our_data.ymean()
    x_sd = our_data.xsd()
    y_sd = our_data.ysd()

    r = our_data.correlation()

    slope = our_data.slope()
    A = our_data.intercept()
    print("The formula is: Y=", slope, "*X + ", A )

    error = our_data.reg_error(slope, A)
    print("The error is ", error)




