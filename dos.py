#!/usr/bin/env python3

import sys
from scipy.stats import ttest_ind, variation, describe, mode
from numpy import mean, percentile
def plot_exec_time(path, l,c):

    return times

op = sys.argv[1]
data = open(op, 'r').read()
cutoff = 0
send_times = []
for pair in data.split('\n'):
    r = pair.split(',')
    if len(r) != 2:
        continue
    send_times.append(int(r[1]))

data = open(sys.argv[2], 'r').read()
cutoff = 0
recv_times = []
for pair in data.split('\n'):
    r = pair.split(',')
    if len(r) != 2:
        continue
    recv_times.append(int(r[1]))
# print([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]][0])

with open(sys.argv[3], 'w') as f:
    f.write("time ms, send, recv\n")
    for i, c in enumerate(recv_times):
        s = 0
        if i < len(send_times):
            s = send_times[i]
        f.write(f"{i}, {c}, {s}\n")

