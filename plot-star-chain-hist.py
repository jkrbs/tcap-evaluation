#!/usr/bin/env python3
import numpy as np
import math
import sys
from scipy.stats import ttest_ind, variation, describe, mode


def cdf_from_histogram(histogram):
    """
    Calculate the cumulative distribution function (CDF) from histogram data.
    """
    values = np.array(histogram.index)
    frequencies = np.array(histogram)
    cdf_values = np.cumsum(frequencies) / np.sum(frequencies)
    return values, cdf_values


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

    times[int(r[0])][int(r[2])].append(int(r[3]))
    # convert to seconds
    if int(r[2]) not in cats:
        cats.append(int(r[2]))
star = sum([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]], [])
chain = sum([list(map(lambda x:x/k, v))  for v,k in [(times[1][k], k) for k in times[1].keys()]], [])
nobins = math.ceil(math.sqrt(len(star)))
star_hist, star_bins = np.histogram(star, nobins)
nobins = math.ceil(math.sqrt(len(chain)))
chain_hist, chain_bins = np.histogram(chain, nobins)

with open(f"cdf-star-{sys.argv[2]}", 'w') as f:
    data_sorted = np.sort(star)
    # calculate the proportional values of samples
    p = 1. * np.arange(len(star)) / (len(star) - 1)
    for i in range(0,len(p)):
        f.write(f"{data_sorted[i]}, {p[i]}\n")

with open(f"cdf-chain-{sys.argv[2]}", 'w') as f:
    data_sorted = np.sort(chain)
    # calculate the proportional values of samples
    p = 1. * np.arange(len(chain)) / (len(chain) - 1)
    for i in range(0,len(p)):
        f.write(f"{data_sorted[i]}, {p[i]}\n")


with open(f"chain-{sys.argv[2]}", 'w') as f:
    f.write("bin, chain\n")
    for i,v in enumerate(chain_hist):
        f.write(f"{chain_bins[i]}, {chain_hist[i]}\n")

with open(f"star-{sys.argv[2]}", 'w') as f:
    f.write("bin, star\n")
    for i,v in enumerate(star_hist):
        f.write(f"{star_bins[i]}, {star_hist[i]}\n")

