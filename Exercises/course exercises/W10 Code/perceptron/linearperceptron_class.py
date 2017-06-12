# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 10:59:06 2014
modified from http://glowingpython.blogspot.com/2011/10/perceptron.html
@author: zhengzhang
"""
import random
import pylab
from pylab import rand,plot,show,norm
import resp_update

# generating samples from Gaussian distribution
def genDistribution(xMean, xSD, yMean, ySD, n, label):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append([x, y, label])
    return samples

def plotSamples(samples):
    for s in samples:
        if s[2] == 1:
            plot(s[0],s[1],'ob')
        elif s[2] == -1:
            plot(s[0],s[1],'or')
        else:
            plot(s[0], s[1], 'og')

    pylab.show()

class Perceptron:
    def __init__(self):
        '''
        perceptron initialization
        '''
        self.w = rand(2)*2 -1
        self.learningRate = 0.05
        self.test_steps = 10

    def get_w(self):
        return self.w

    def response(self, x):
        '''
        todo: w and x are both lists with two items
              right now response is always -1
              implement the integrate-and-fire logic:
              return either 1 or -1
        '''
        return resp_update.response(self.w, x)

    def updateWeights(self, x, iterError):
        """
        todo: implement the delta update rule
        updates the weights status, w at time t+1 is
        w(t+1) = w(t) + learningRate * error * x
        where d is desired output and r the perceptron response
        iterError is (d-r)
        """
        resp_update.updateWeights(self.w, x, self.learningRate, iterError)

    def run_test(self, data, data_label):
        # Perceptron test
        num_errs = 0
        for x in data:
            r = self.response(x)
            if r != x[2]: # if the response is not correct
                num_errs += 1
                plot(x[0],x[1],'sg')
            if x[2] == 1:
                plot(x[0],x[1],'ob')
            else:
                plot(x[0],x[1],'or')
        print(data_label, ": ", num_errs, "wrong out of", len(data))
        n = norm(self.w)
        ww = self.w/n
        ww1 = [ww[1],-ww[0]]
        ww2 = [-ww[1],ww[0]]
        print(self.w)
        print(ww1, ww2)
        plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'--k')
        pylab.title(data_label)
        show()

    def train(self, train_data, test_data):
        """
        trains all the vector in data.
        Every vector in data must have three elements,
        the third element (x[2]) must be the label (desired output)
        """
        print("\n------- start training ------\n")
        iteration = 0
        total_iteration = 100
        while iteration < total_iteration:
            train_error = 0.0
            for x in train_data: # for each SAMPLE
                r = self.response(x)
                if x[2] != r: # if we have a wrong response
                    iter_error = x[2] - r # desired response - actual response
                    self.updateWeights(x, iter_error)
                    train_error += abs(iter_error)

            iteration += 1
            # test the model performance on both training and test data
            if iteration % self.test_steps == 0:
                print("\n--------------", iteration, "-----------\n")
                print("total error: ", train_error)
                self.run_test(train_data, 'train')
                self.run_test(test_data, 'test')
                if input("continue: y/n? ") == 'n':
                    break

            if train_error == 0.0:
                print ('converged at iterations ', iteration)
                self.run_test(train_data, 'train')
                self.run_test(test_data, 'test')
                break

# two clusters, each a 2D gaussian
# remove the line below if you want to draw different samples each time
random.seed(0)
c1x_mean = 0.5
c1y_mean = -0.5
c1_std = 0.2
c2x_mean = -0.0
c2y_mean = 0.5
c2_std = 0.2

# generating training set
num_train = 100
trainset_p = genDistribution(c1x_mean, c1_std, c1y_mean, c1_std, num_train, 1)
trainset_n = genDistribution(c2x_mean, c2_std, c2y_mean, c2_std, num_train, -1)
trainset = trainset_n + trainset_p

# generating testing set
num_test = 20
testset_p = genDistribution(c1x_mean, c1_std, c1y_mean, c1_std, num_test, 1)
testset_n = genDistribution(c2x_mean, c2_std, c2y_mean, c2_std, num_test, -1)
testset = testset_p + testset_n

perceptron = Perceptron()   # perceptron instance

perceptron.run_test(trainset, 'train')
perceptron.run_test(testset, 'test')    # let's take a look first

# let's train!
perceptron.train(trainset, testset)  # training
