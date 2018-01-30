#!/usr/bin/env python3
## Imports
from time import time
# from pyfaidx import Fasta
from get_pssm import get_pssm
from output_of_pssm import output_of_pssm
## Implementation of calculate_hits
def calculate_hits(chrData, PSSMFilename, TF, OutFilename):
    # Get the time at the begining of the function
    t_beg = time()
    # Get the PSSM for the corresponding transcription factor
    PSSM, lenOfPSSM = get_pssm(PSSMFilename, TF)
    # Get the strong and weak thresholds
    weakThreshold = 0.35
    strongThreshold = 0.7
    # Open the output file
    fileID = open(OutFilename, 'w')
    # Find the maximum possible probability
    maximum = 1
    for i in range(lenOfPSSM):
        maxForCollumn = 0
        for j in range(4):
            if PSSM[j][i] > maxForCollumn:
                maxForCollumn = PSSM[j][i]
        maximum = maximum + maxForCollumn
    # Evaluate the chromosome with the PSSM and count how many strong and weak sites there are for the forwards direction
    for i in chrData.keys():
        data = str(chrData[i])
        for j in range(len(data)):
            if (j + lenOfPSSM) > len(data):
                output = output_of_pssm(PSSM, data[j:] + str([' ' for k in range(j + lenOfPSSM - 1 - len(data))]), maximum, lenOfPSSM)
                end = len(data)
            else:
                output = output_of_pssm(PSSM, data[j:(j + lenOfPSSM)], maximum, lenOfPSSM)
                end = j + lenOfPSSM
            if output >= weakThreshold:
                if output < strongThreshold:
                    fileID.write(str(i) + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output) + '\t' + '+' + '\t' + '.' + '\t' + 'weak' + '\n')
                else:
                    fileID.write(str(i) + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output) + '\t' + '+' + '\t' + '.' + '\t' + 'strong' + '\n')
    # Evaluate the chromosome with the PSSM and count how many strong and weak sites there are for the reverse compliment direction
    for i in chrData.keys():
        data = chrData[i][:].complement
        data = str(data[:].reverse)
        for j in range(len(data)):
            if (j + lenOfPSSM) > len(data):
                output = output_of_pssm(PSSM, data[j:] + str([' ' for k in range(j + lenOfPSSM - 1 - len(data))]), maximum, lenOfPSSM)
                end = len(data)
            else:
                output = output_of_pssm(PSSM, data[j:(j + lenOfPSSM)], maximum, lenOfPSSM)
                end = j + lenOfPSSM
            if output >= weakThreshold:
                if output < strongThreshold:
                    fileID.write(str(i) + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output) + '\t' + '+' + '\t' + '.' + '\t' + 'weak' + '\n')
                else:
                    fileID.write(str(i) + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output) + '\t' + '+' + '\t' + '.' + '\t' + 'strong' + '\n')
    # Close the output file
    fileID.close()
    # Get the time at the end of the function
    t_end = time()
    # Return the amount of seconds it took the function to run (in seconds)
    return t_end - t_beg