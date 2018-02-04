#!/usr/bin/env python3
## Imports
from read_gff import read_gff
## Implementation of plot_hist
def plot_hist(InFilename, HitsInFilename, PicFile):
    # Get the time at the begining of the function
    t_beg = time()
    # Open the input file that holds the hits
    fileID = open(HitsInFilename, 'r')
    # Initialize the list that will hold the input
    data = []
    # Read in the input file
    line = fileID.readline()
    while line:
        data.append(line[:len(line)-1])
        line = fileID.readline()
    # Parse the input
    weakSites = []
    strongSites = []
    for i in range(len(data)):
        line = data[i]
        if len(line) != 0:
            if line[0] != '#':
                # Get the position of the hit
                position = line[2:8]
                position = int(position)
                # Get the type of the hit
                typeOfHit = line[len(line)-8:len(line)-2]
                # Input the position into the correct list
                if typeOfHit == 'strong':
                    strongSites.append(position)
                if typeOfHit == '  weak':
                    weakSites.append(position)
    # Sort the lists holding the hits
    weakSites = list(set(weakSites))
    weakSites.sort()
    strongSites = list(set(strongSites))
    strongSites.sort()
    # Close the input file that holds the hits
    fileID.close()
    # Read in the input file
    Input = readInInput(InFilename)
    # Get the number of plus or minus range of what we're going to be anaylsing and the size of the buckets
    r = Input[5]
    s = Input[4]
    # Analyse the hits
    categories = [0 for i in range(r)]
    #for i in range(len(strongSites)):
    #    for j in range(len(weakSites)):
    #        value = abs(strongSites[i] - weakSites[j])
    #        for k in range(r//s):
    #            if (value <= (s*k) and (value > s*(k-1))):
    #                categories[k] += 1
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
    # Plot the histogram
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,5))
    ax.bar(range(len(categories)), categories, color='black', label='Histogram')
    plt.plot(range(len(categories)), [mean(categories) for i in range(len(categories))], color='red', label='Mean')
    plt.plot(range(len(categories)), [2*std(categories)+mean(categories) for i in range(len(categories))], color='steelblue', label='Standard Deviation (+2)')
    plt.plot(range(len(categories)), [std(categories)+mean(categories) for i in range(len(categories))], color='cyan', label='Standard Deviation (+1)')
    if mean(categories)-std(categories) >= 0:
        plt.plot(range(len(categories)), [mean(categories)-std(categories) for i in range(len(categories))], color='cyan', label='Standard Deviation (-1)')
    if mean(categories)-2*std(categories) >= 0:
        plt.plot(range(len(categories)), [mean(categories)-2*std(categories) for i in range(len(categories))], color='steelblue', label='Standard Deviation (-2)')
    ax.legend()
    fig.savefig(PicFile)
    plt.show()
    # Get the time at the end of the function
    t_end = time()
    # Return the amount of seconds it took the function to run (in seconds)
    return t_end - t_beg
