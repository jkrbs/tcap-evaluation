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
times = {}
cats = []
for pair in data.split('\n'):
    r = pair.split(',')
    if len(r) != 3:
        continue
    if int(r[0]) not in times.keys():
        times[int(r[0])] = []
    times[int(r[0])].append(int(r[2])/1000)
    # convert to seconds
    if int(r[0]) not in cats:
        cats.append(int(r[0]))
# print([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]][0])

print([v for _,v in enumerate(times)])
alltimes = sum([times[v] for _,v in enumerate(times)], [])
print(describe(random.sample(alltimes, 200)))

with open(sys.argv[2], 'w') as f:
    f.write("num_caps, avg, 10percentile, 90percentile\n")
    for i, c in enumerate(cats):
        f.write(f"{c}, {mean(times[c])}, {percentile(times[c], 10)}, {percentile(times[c], 90)}\n")

with open(f"cdf-{sys.argv[2]}", 'w') as f:
    data_sorted = np.sort(times[1000])
    # calculate the proportional values of samples
    p = 1. * np.arange(len(times[1000])) / (len(times[1000]) - 1)
 
    f.write("x,y\n")
    for i in range(0,len(p)):
        f.write(f"{data_sorted[i]}, {p[i]}\n")

