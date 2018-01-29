#!/usr/bin/env python3
## Imports
from time import time
from pyfaidx import Fasta
from get_pssm import get_pssm
from output_of_pssm import output_of_pssm
## Implementation of calculate_hits
def calculate_hits(chrFilename, CHR, PSSMFilename, TF, OutFilename):
    # Get the time at the begining of the function
    t_beg = time()
    # Get the chromosome
    chrData = Fasta(chrFilename)[CHR]
    # Get the PSSM for the corresponding transcription factor
    PSSM, lenOfPSSM = get_pssm(PSSMFilename, TF)
    # Get the strong and weak thresholds
    weakThreshold = 0.35
    strongThreshold = 0.7
    # Open the output file
    fileID = open(OutFilename, 'w')
    # Write to the output file
    # fileID.write('# searching ' + CHR + '\n')
    # fileID.write('# for transcription factor ' + TF + '\n')
    # fileID.write('# weak threshold: ' + str(weakThreshold) + '\n')
    # fileID.write('# strong threshold: ' + str(strongThreshold) + '\n')
    # fileID.write('\n')
    # fileID.write('# The following is the outputs of the program in the forwards direction. \n')
    # fileID.write('# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
    # fileID.write('# \n')
    # fileID.write('# position  strength  type       \n')
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
        data = chrData[i]
        for j in range(len(data)):
            if (j + lenOfPSSM) > len(chrData):
                output = outputOfPSSM(PSSM, data[j:] + str([' ' for k in range(j + lenOfPSSM - 1 - len(chrData))]), maximum, lenOfPSSM)
                end = len(chrData)
            else:
                output = outputOfPSSM(PSSM, data[j:(j + lenOfPSSM)], maximum, lenOfPSSM)
                end = j + lenOfPSSM
            # out.append(output)
            if output >= weakThreshold:
                if output < strongThreshold:
                    fileID.write(CHR + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output1) + '\t' + '+' + '\t' + '.' + '\t' + 'weak' + '\n')
                    # fileID.write('  ' + str(j) + '     ' + str(output) + '     ' + ' ' + 'weak  ' + '\n')
                    # weakAmount += 1
                    # positionOfWeak.append(j)
                else:
                    fileID.write(CHR + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output1) + '\t' + '+' + '\t' + '.' + '\t' + 'strong' + '\n')
                    # fileID.write('  ' + str(j) + '     ' + str(output) + '     ' + ' ' + 'strong  ' + '\n')
                    # strongAmount += 1
                    # positionOfStrong.append(j)
    # Output to the output file the amount of weak and strong sites for the forwards direction
    # fileID.write('# \n')
    # fileID.write('# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
    # fileID.write('# \n')
    # fileID.write('# The number of weak sites for the forwards direction is ' + str(weakAmount) + '\n')
    # fileID.write('# The number of strong sites for the forwards direction is ' + str(strongAmount) + '\n')
    # Write to the output file
    # fileID.write('\n')
    # fileID.write('\n')
    # fileID.write('# The following is the outputs of the program in the reverse compliment direction. \n')
    # fileID.write('# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
    # fileID.write('# \n')
    # fileID.write('# position  strength  type       \n')
    # Take the reverse compliment of the PSSM
    for i in range(4):
        PSSM[i] = PSSM[i][::-1]
    temp = PSSM[0]
    PSSM[0] = PSSM[3]
    PSSM[3] = temp
    temp = PSSM[1]
    PSSM[1] = PSSM[2]
    PSSM[2] = temp
    # Find the maximum possible probability
    maximum = 1
    for i in range(lenOfPSSM):
        maxForCollumn = 0
        for j in range(4):
            if PSSM[j][i] > maxForCollumn:
                maxForCollumn = PSSM[j][i]
        maximum = maximum + maxForCollumn
    # Evaluate the chromosome with the PSSM and count how many strong and weak sites there are for the reverse compliment direction
    for i in chrData.keys():
        data = chrData[i]
        for j in range(len(data)):
            if (j + lenOfPSSM) > len(chrData):
                output = outputOfPSSM(PSSM, data[j:] + str([' ' for k in range(j + lenOfPSSM - 1 - len(chrData))]), maximum, lenOfPSSM)
                end = len(chrData)
            else:
                output = outputOfPSSM(PSSM, data[j:(j + lenOfPSSM)], maximum, lenOfPSSM)
                end = j + lenOfPSSM
            # out.append(output)
            if output >= weakThreshold:
                if output < strongThreshold:
                    fileID.write(CHR + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output1) + '\t' + '+' + '\t' + '.' + '\t' + 'weak' + '\n')
                    # fileID.write('  ' + str(j) + '     ' + str(output) + '     ' + ' ' + 'weak  ' + '\n')
                    # weakAmount += 1
                    # positionOfWeak.append(j)
                else:
                    fileID.write(CHR + '\t' + TF + '\t' + 'hit' + '\t' + str(j) + '\t' + str(end) + '\t' + str(output1) + '\t' + '+' + '\t' + '.' + '\t' + 'strong' + '\n')
                    # fileID.write('  ' + str(j) + '     ' + str(output) + '     ' + ' ' + 'strong  ' + '\n')
                    # strongAmount += 1
                    # positionOfStrong.append(j)
    # Output to the output file the amount of weak and strong sites for the reverse compliment direction
    # fileID.write('# \n')
    # fileID.write('# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
    # fileID.write('# \n')
    # fileID.write('# The number of weak sites for the reverse compliment direction is ' + str(weakAmount) + '\n')
    # fileID.write('# The number of strong sites for the reverse compliment direction is ' + str(strongAmount) + '\n')
    # Close the output file
    fileID.close()
    # Get the time at the end of the function
    t_end = time()
    # Return the amount of seconds it took the function to run (in seconds)
    return t_end - t_beg