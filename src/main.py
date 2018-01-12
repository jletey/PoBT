#!/usr/bin/env python3
## Imports
from get_chrs import getCHRs, getPSSMs
import Bio
from Bio import SeqIO
import pandas as pd
from time import time
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
## Get the parameters when the user called to function
args = list(sys.argv[1:])
## Tell the user that all data will be grabbed from the data section
print('All data used will be grabbed from the data section (titled Data)')
if len(args) > 0:
    choice = args[0]
    print('Are you okay with this? [y/n]', choice)
else:
    choice = str(input('Are you okay with this? [y/n] '))
isDifferentDataPath = False
if choice == 'n':
    if len(args) > 0:
        path = args[1]
        isDifferentDataPath = True
        print('What is you data path called?', path)
    else:
        path = str(input('What is your data path called? '))
    if path[len(path)-1] == '/':
    	path = path[:len(path)-1]
else:
    path = 'Data'
## Get the fasta data
# Ask the user how much data they want to throw away
if len(args) > 0:
    if isDifferentDataPath:
        n = int(args[2])
    else:
        n = int(args[1])
    print('How many chromosomes do you want to throw away?', n)
else:
    n = int(input('How many chromosomes do you want to throw away? '))
# Get the data from the fasta file that I'm working with and take away two of those
fastaDF = getCHRs(path + '/SGDv3.fasta', n)
# Get the amount of chromosomes
countCHR = fastaDF.count()
numOfCHR = countCHR['chromosome']
# Show the dataframe
if len(args) > 0:
    if isDifferentDataPath:
        choice = args[3]
    else:
        choice = args[2]
    print('Show the fasta dataframe? [y/n]', choice)
else:
    choice = str(input('Show the fasta dataframe? [y/n] '))
if choice == 'y':
    print(fastaDF)
## Get the tamo data
# Get the data from the tamo file that I'm working with
tamoDF = getPSSMs(path + '/yeast.tamo')
# Get the amount of PSSMs (or TFs, both are the same)
countTF = tamoDF.count()
numOfTF = countTF['TF']
# Show the dataframe
if len(args) > 0:
    if isDifferentDataPath:
        choice = args[4]
    else:
        choice = args[3]
    print('Show the tamo dataframe? Warning, this might be long! [y/n]', choice)
else:
    choice = str(input('Show the tamo dataframe? Warning, this might be long! [y/n] '))
if choice == 'y':
    print(tamoDF)
## Implementation of outputOfPSSM
def outputOfPSSM(PSSM, sequence):
    # Find the length (horizontal length) of the PSSM
    lenOfPSSM = PSSM.count(1) - 1
    lenOfPSSM = lenOfPSSM[0]
    # Find the maximum possible output of the PSSM
    maximumList = list(PSSM.max())
    del maximumList[0]
    maximum = 0
    for i in range(len(maximumList)):
        maximum += maximumList[i]
    # Calculate the output of the PSSM
    output = 0
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            output += PSSM[str(i)][0]
        if sequence[i] == 'C':
            output += PSSM[str(i)][1]
        if sequence[i] == 'T':
            output += PSSM[str(i)][2]
        if sequence[i] == 'G':
            output += PSSM[str(i)][3]
    output /= maximum
    # Return the output of the PSSM
    return output
## Implementation of calculateHits
def calculateHits(fastaDF, tamoDF, numOfTF, numOfCHR, weakThreshold, strongThreshold, Path):
    # Get the time
    t_beg = time()
    # Check to see if the path is made (if not, make it)
    if not os.path.exists(Path):
        os.makedirs(Path)
    # Calculate hits
    for i in range(numOfTF):
        pssm = tamoDF['ForwardsPSSM'][i]
        REVpssm = tamoDF['ReversePSSM'][i]
        TF = tamoDF['TF'][i]
        lenOfPSSM = pssm.count(1) - 1
        lenOfPSSM = lenOfPSSM[0]
        filename = Path + '/Hits' + TF + '.gff'
        fileID = open(filename, 'w')
        for j in range(numOfCHR):
            CHR = fastaDF['sequence'][j]
            print('Calculating the hits for the transcription factor', TF, 'using chromosome', fastaDF['chromosome'][j])
            t_intermediate_beg = time()
            for k in range(len(CHR)):
                if (k + lenOfPSSM) > len(CHR):
                    output1 = outputOfPSSM(pssm, CHR[k:] + str([' ' for l in range(k + lenOfPSSM - 1 - len(CHR))]))
                    output2 = outputOfPSSM(REVpssm, CHR[k:] + str([' ' for l in range(k + lenOfPSSM - 1 - len(CHR))]))
                    end = len(CHR)
                else:
                    output1 = outputOfPSSM(pssm, CHR[k:(k + lenOfPSSM)])
                    output2 = outputOfPSSM(REVpssm, CHR[k:(k + lenOfPSSM)])
                    end = k + lenOfPSSM
                if output1 >= weakThreshold:
                    if output1 < strongThreshold:
                        fileID.write(fastaDF['chromosome'][j] + '\t' + TF + '\t' + 'hit' + '\t' + str(k) + '\t' + str(end) + '\t' + str(output1) + '\t' + '+' + '\t' + '.' + '\t' + 'weak' + '\n')
                    else:
                        fileID.write(fastaDF['chromosome'][j] + '\t' + TF + '\t' + 'hit' + '\t' + str(k) + '\t' + str(end) + '\t' + str(output1) + '\t' + '+' + '\t' + '.' + '\t' + 'strong' + '\n')
                if output2 >= weakThreshold:
                    if output2 < strongThreshold:
                        fileID.write(fastaDF['chromosome'][j] + '\t' + TF + '\t' + 'hit' + '\t' + str(k) + '\t' + str(end) + '\t' + str(output2) + '\t' + '-' + '\t' + '.' + '\t' + 'weak' + '\n')
                    else:
                        fileID.write(fastaDF['chromosome'][j] + '\t' + TF + '\t' + 'hit' + '\t' + str(k) + '\t' + str(end) + '\t' + str(output2) + '\t' + '-' + '\t' + '.' + '\t' + 'strong' + '\n')
            t_intermediate_end = time()
            print('It took', (t_intermediate_end - t_intermediate_beg)/60, 'minutes to calculate the hits for transcription factor', TF, 'using chromosome', fastaDF['chromosome'][j])
        fileID.close()
    # Get the time
    t_end = time()
    # Return the time it took to calculate the hits
    return t_end - t_beg
## Calculate the hits
if len(args) > 0:
    if isDifferentDataPath:
        path = args[5]
    else:
        path = args[4]
else:
    path = 'Hits Files'
time_est = calculateHits(fastaDF, tamoDF, numOfTF, numOfCHR, 0.35, 0.7, path)
print(time_est)
