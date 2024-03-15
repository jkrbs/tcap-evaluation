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
star = sum([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]], [])
chain = sum([list(map(lambda x:x/k, v))  for v,k in [(times[1][k], k) for k in times[1].keys()]], [])
print(f"ttest on per call mean: {ttest_ind(star, chain)}")
print(f"Star: {describe(star)}")
print(f"Chain: {describe(chain)}")

with open(sys.argv[2], 'w') as f:
    star = [mean(times[0][k]) for k in times[0].keys()]
    chain = [mean(times[1][k]) for k in times[0].keys()]
    f.write("num_caps, star, chain\n")
    for i, c in enumerate(cats):
        f.write(f"{c}, {star[i]}, {percentile(times[0][c], 10)}, {percentile(times[0][c], 10)},{chain[i]},  \n")
#    Depth & Arith. Mean & CoV & Min & Max & Arith. Mean & CoV & Min & Max\\
 # star ===== Chain
        s = times[0][c]
        ch = times[1][c]
        print(f"{c} & {round(mean(s),2)} & {round(variation(s),2)} & {round(min(s),2)} & {round(max(s),2)} & {round(mean(ch),2)} & {round(variation(ch),2)} & {round(min(ch),2)} & {round(max(ch), 2)}\\\\")

