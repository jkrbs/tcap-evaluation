#!/usr/bin/env python3

import sys
from scipy.stats import ttest_ind, variation, describe, mode
from numpy import mean, percentile
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
    times[int(r[0])].append(int(r[2])/(1000**2))
    # convert to seconds
    if int(r[1]) not in cats:
        cats.append(int(r[1]))
# print([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]][0])

print([v for _,v in enumerate(times)])
alltimes = sum([times[v] for _,v in enumerate(times)], [])
print(describe(alltimes))

with open(sys.argv[2], 'w') as f:
    f.write("star, chain\n")
    for i, c in enumerate(times):
        f.write(f"{mean(times[c])}, {percentile(times[c], 10)}, {percentile(times[c], 90)}\n")

