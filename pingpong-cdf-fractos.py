#!/usr/bin/env python3
import numpy as np
import sys
from scipy.stats import ttest_ind, variation, describe, mode
from numpy import mean, percentile
import random
def plot_exec_time(path, l,c):

    return times

op = sys.argv[1]
data = open(op, 'r').read()
cutoff = 0
times = []
for pair in data.split('\n'):
    if pair != '':
        times.append(float(pair)*(1000**2))
    # print([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]][0])

print(describe(random.sample(times, 200)))

with open(f"cdf-{sys.argv[2]}", 'w') as f:
    data_sorted = np.sort(random.sample(times, 100))
    # calculate the proportional values of samples
    p = 1. * np.arange(100) / (100 - 1)
 
    f.write("x,y\n")
    for i in range(0,len(p)):
        f.write(f"{data_sorted[i]}, {p[i]}\n")

