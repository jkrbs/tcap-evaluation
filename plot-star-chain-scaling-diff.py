#!/usr/bin/env python3
import sys
from scipy.stats import ttest_ind, variation, describe, mode
from numpy import mean
def plot_exec_time(path, l,c):

    return times

op = sys.argv[1]
data = open(op, 'r').read()
cutoff = 0
times = {}
cats = []
for pair in data.split('\n'):
    r = pair.split(',')
    if len(r) != 4:
        continue
    if int(r[0]) not in times.keys():
        times[int(r[0])] = {}
    if int(r[2]) not in times[int(r[0])].keys():
        times[int(r[0])][int(r[2])] = []

    times[int(r[0])][int(r[2])].append(int(r[3])/1000)
    # convert to seconds
    if int(r[2]) not in cats:
        cats.append(int(r[2]))
# print([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]][0])
with open(sys.argv[2], 'w') as f:
    diffs = [mean(times[0][k])/mean(times[1][k]) for k in times[0].keys()]
    print(f"overall mean: {mean(diffs[1::])}")
    f.write("num_caps, factor\n")
    for i, c in enumerate(cats):
        f.write(f"{c}, {diffs[i]}\n")
