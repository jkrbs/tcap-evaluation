#!/usr/bin/env python3

import sys
from scipy.stats import ttest_ind, variation, describe, mode
from numpy import mean, percentile


def load(path):
    data = open(path, 'r').read()
    times = {}
    for pair in data.split('\n'):
        r = pair.split(',')
        if len(r) != 2:
            continue
        if int(r[0]) not in times.keys():
            times[int(r[0])] = []
        times[int(r[0])].append(int(r[0])*8*100/(int(r[1]))/10**5)

    # print([list(map(lambda x:x/k, v))  for v,k in [(times[0][k], k) for k in times[0].keys()]][0])
    return times
    print([v for _,v in enumerate(times)])
#    alltimes = sum([a/v for a in times[v] for v in times.keys()], [])
#    print(f"====\n{path}\n{describe(alltimes)}\n====\n\n")

times = {}
times["512B"] = load(sys.argv[2])
times["1KiB"] = load(sys.argv[3])
times["2KiB"] = load(sys.argv[4])
times["4KiB"] = load(sys.argv[5])

with open(sys.argv[1], 'w') as f:
    f.write("transfer size, 512B Avg, 512B 10percentile, 512B 90 percentile, 1KiB Avg, 1KiB 10percentile, 1KiB 90 percentile, 2KiB Avg, 2KiB 10percentile, 2KiB 90 percentile, 4KiB Avg, 4KiB 10percentile, 4KiB 90 percentile\n")
    for size in sorted(times["1KiB"].keys()):
        st = f"{mean(times['512B'][size])}, {percentile(times['512B'][size], 10)}, {percentile(times['512B'][size], 90)}, "
        st += f"{mean(times['1KiB'][size])}, {percentile(times['1KiB'][size], 10)}, {percentile(times['1KiB'][size], 90)}, " 
        st += f"{mean(times['2KiB'][size])}, {percentile(times['2KiB'][size], 10)}, {percentile(times['2KiB'][size], 90)}, "
        st += f"{mean(times['4KiB'][size])}, {percentile(times['4KiB'][size], 10)}, {percentile(times['4KiB'][size], 90)},\n"
       
        f.write(f"{size}, {st}")

