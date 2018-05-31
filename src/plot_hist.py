#!/usr/bin/env python
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# title      Plot Histogram Script                                                 +
# project    A-Study-of-Transcription-and-Its-Affects                              +
# repository https://github.com/johnletey/A-Study-of-Transcription-and-Its-Affects +
# author     John Letey                                                            +
# email      john.letey@colorado.edu                                               +
# copyright  Copyright (C) 2018                                                    +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Imports
from time import time
from read_gff import read_gff
import matplotlib.pyplot as plt
plt.style.use('bmh')
import numpy as np
## Implementation of plot_hist
def plot_hist(HitsInFilename, PicFile):
    # Get the time at the beginning of the function
    t_beg = time()
    # Get the data from the GFF file
    data = read_gff(HitsInFilename)
    # Sort the data into sets of weak sites and strong sites
    weakSites, strongSites = [], []
    for i in range(len(data)):
        if data[i][len(data[i])-1] == 'weak':
            weakSites.append(int(data[i][3]))
        else:
            strongSites.append(int(data[i][3]))
    weakSites = np.array(weakSites)
    strongSites = np.array(strongSites)
    # Set the number of plus or minus range of what we're going to be analyzing and the size of the buckets
    r = 150
    s = 3
    # Analyze the hits
    categories = [0 for i in range(r//s)]
    for i in range(strongSites.shape[0]):
        for j in range(weakSites.shape[0]):
            mat = [0 for i in range(r//s)]
            value = abs(strongSites[i] - weakSites[j])
            if value > r:
                break
            for k in range(r//s):
                if value <= s*k and value > s*(k-1):
                    mat[k] = value
            for i in range(len(mat)):
                categories[i] += mat[i]
    print(categories)
    """
    for i in range(len(strongSites)):
        for j in range(len(weakSites)):
            value = abs(strongSites[i] - weakSites[j])
            for k in range(r//s):
                if (value <= (s*k) and (value >= s*(k-1))):
                    categories[k] += 1
    """
    """
    for i in range(len(strongSites)):
        position1 = 0
        position2 = 0
        for j in range(len(weakSites)):
            if weakSites[j] <= strongSites[i]-r:
                position1 = j
            if weakSites[j] <= strongSites[i]+r:
                position2 = j
        for j in range(position1, position2):
            value = abs(strongSites[i] - weakSites[j])
            for k in range(r//s):
                if (value <= (s*k) and (value > s*(k-1))):
                   categories[k] += 1
    """
    # Plot the histogram
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,5))
    ax.bar(range(len(categories)), categories, color='black', label='histogram')
    plt.plot(range(len(categories)), [np.mean(categories) for i in range(len(categories))], color='#a76c6e', label='mean')
    plt.plot(range(len(categories)), [2*np.std(categories)+np.mean(categories) for i in range(len(categories))], color='steelblue', label='Standard Deviation (+2)')
    plt.plot(range(len(categories)), [np.std(categories)+np.mean(categories) for i in range(len(categories))], color='gray', label='Standard Deviation (+1)')
    if np.mean(categories)-np.std(categories) >= 0:
        plt.plot(range(len(categories)), [np.mean(categories)-np.std(categories) for i in range(len(categories))], color='gray', label='Standard Deviation (-1)')
    if np.mean(categories)-2*np.std(categories) >= 0:
        plt.plot(range(len(categories)), [np.mean(categories)-2*np.std(categories) for i in range(len(categories))], color='steelblue', label='Standard Deviation (-2)')
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left", fontsize=12)
    fig.savefig(PicFile)
    # Print where the peak value occurs
    peakIndex = np.argmax(categories)
    peak = peakIndex*s + 0.5*s
    print("The peak at {:.3f}".format(peak))
    # Get the time at the end of the function
    t_end = time()
    # Return the amount of seconds it took the function to run (in seconds) and also where the peak value occurs
    return (t_end - t_beg, peak)
