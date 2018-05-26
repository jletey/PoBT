#!/usr/bin/env python
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# title      Main Script                                                           +
# project    A-Study-of-Transcription-and-Its-Affects                              +
# repository https://github.com/johnletey/A-Study-of-Transcription-and-Its-Affects +
# author     John Letey                                                            +
# email      john.letey@colorado.edu                                               +
# copyright  Copyright (C) 2018                                                    +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Imports
import sys
from time import time
from pyfaidx import Fasta
from calculate_hits import calculate_hits
from plot_hist import plot_hist
from multiprocessing import Pool
## Get the parameters when the user called to function
args = list(sys.argv[1:])
data_path = args[0]
n = int(args[1])
show_fasta_data = args[2]
output_path = args[3]
## Print out to the user and tell then what options they selected
print('>>>>>>>>>>>>>>>>>>')
print('data files =', '[' + data_path + '/' + 'yeast.tamo' + ']', 'and', '[' + data_path + '/' + 'SGDv3.fasta' + ']')
print('# of chromosomes unused =', n)
print('>>>>>>>>>>>>>>>>>>')
## Get the fasta data
# Get the data from the fasta file that I'm working with
genes = Fasta(data_path + '/SGDv3.fasta', as_raw=True)
# Get the chromosomes
chrs = list(genes.keys())
# Get the amount of chromosomes
numOfCHR = len(chrs)
# Show the fasta data
if show_fasta_data == 'y':
    for chrom in chrs[:len(chrs)-n]:
        print('The first 5 letters in', chrom, 'are -', genes[chrom][0:5])
## Calculate the hits and the hists
# Get all of the possible transcription factors
tamoData = []
fileID = open(data_path + '/yeast.tamo', 'r')
line = fileID.readline()
while line:
    tamoData.append(line[:len(line)-1])
    line = fileID.readline()
tfList = []
for i in range(124):
    line = tamoData[19 + 42*i - 1]
    tfList.append(line[9:])
# Define functions for multiprocessing
def hits_func():
    print('It took', calculate_hits(genes, chrs[:len(chrs)-n], data_path + '/yeast.tamo', tf, output_path + '/hits/Hits'+tf+'.gff')/60, 'minutes to calculate the hits for transcription factor', tf)
def hist_func():
    time_took, peak = plot_hist(output_path + '/hits/Hits'+tf+'.gff', output_path + '/hists/Hist'+tf+'.png')
    print('It took', time_took/60, 'minutes to compute the histogram analysis for transcription factor', tf)
    return peak
# Go through each transcription factor and calculate all the hits for that specific one
"""
for tf in tfList[:30]:
    with Pool(4) as p:
        r = p.apply_async(hits_func)
        result = r.get()
"""
# Go through each transcription factor and plot a histogram for that specific one
peaks = []
for tf in tfList[:30]:
    with Pool(4) as p:
        r = p.apply_async(hist_func)
        peaks.append(r.get())
fileID = open(output_path + '/peaks.txt', 'w')
for peak, tf in zip(peaks, tfList[:30]):
    fileID.write(tf + '\t' + str(peak) + '\n')
fileID.close()