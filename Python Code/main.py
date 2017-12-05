## Imports
import Bio
from Bio import SeqIO
import pandas as pd
from time import time
import matplotlib.pyplot as plt
import numpy as np
import os
## Tell the user that all data will be grabbed from the data section
print('All data used will be grabbed from the data section')
choice = str(input('Are you okay with this? [y/n] '))
if choice == 'n':
    path = str(input('What is your data path called? '))
else:
    path = 'Data'
##
def getCHRs(filename, numUseless):
    # Tell the user the program is getting the fasta data
    print('Getting the fasta data out of the file:', filename)
    # Get the data from the fasta file
    with open(filename) as fasta_file:
        identifiers = []
        seq = []
        for seq_record in SeqIO.parse(fasta_file, 'fasta'):
            identifiers.append(seq_record.id)
            seq.append(str(seq_record.seq))
    # Put the data into a dataframe
    s1 = pd.Series(identifiers[:len(identifiers)-numUseless], name='chromosome')
    s2 = pd.Series(seq[:len(seq)-numUseless], name='sequence')
    fastaDF = pd.DataFrame(dict(chromosome=s1, sequence=s2))
    # Return the dataframe
    return fastaDF
##
# Get the data from the fasta file that I'm working with and take away two of those
fastaDF = getCHRs(path + '/SGDv3.fasta', 2)
# Get the amount of chromosomes
countCHR = fastaDF.count()
numOfCHR = countCHR['chromosome']
# Show the dataframe
choice = str(input('Show the fasta dataframe? [y/n] '))
if choice == 'y':
	print(fastaDF)
## 
def getPSSMs(filename):
    # Tell the user the program is getting the tamo data
    print('Getting the tamo data out of the file:', filename)
    # Get the PSSMs from the tamo file
    tamo_file = open(filename)
    tamo_data = []
    line = tamo_file.readline()
    while line:
        tamo_data.append(line[:len(line)-1])
        line = tamo_file.readline()
    TF = []
    PSSM = []
    revPSSM = []
    for i in range(len(tamo_data)):
        if tamo_data[i][:6] == 'Source':
            pssm = pd.DataFrame(pd.Series(['A', 'C', 'T', 'G'], name='Letter'))
            REVpssm = pd.DataFrame(pd.Series(['A', 'C', 'T', 'G'], name='Letter'))
            revpssm = []
            lenOfPSSM = int((len(tamo_data[i-16]) - 3)/10) - 1
            firstLine = tamo_data[i-16]
            secondLine = tamo_data[i-15]
            thirdLine = tamo_data[i-14]
            fourthLine = tamo_data[i-13]
            for j in range(lenOfPSSM):
                value1 = float(firstLine[(j*10 + 6):(j*10 + 12)])
                value2 = float(secondLine[(j*10 + 6):(j*10 + 12)])
                value3 = float(thirdLine[(j*10 + 6):(j*10 + 12)])
                value4 = float(fourthLine[(j*10 + 6):(j*10 + 12)])
                revpssm.append([value1, value2, value3, value4])
                pssm.insert(j+1, str(j), pd.Series([value1, value2, value3, value4]))
            temp = revpssm
            revpssm = []
            for j in range(4):
                List = []
                for k in range(len(temp)):
                    List.append(temp[k][j])
                revpssm.append(List)
            for j in range(4):
                revpssm[j] = revpssm[j][::-1]
            temp = revpssm[0]
            revpssm[0] = revpssm[2]
            revpssm[2] = temp
            temp = revpssm[1]
            revpssm[1] = revpssm[3]
            revpssm[3] = temp
            temp = revpssm
            revpssm = []
            for j in range(len(temp[0])):
                List = []
                for k in range(4):
                    List.append(temp[k][j])
                revpssm.append(List)
            for j in range(lenOfPSSM):
                REVpssm.insert(j+1, str(j), pd.Series(revpssm[j]))
            TF.append(tamo_data[i][9:])
            PSSM.append(pssm)
            revPSSM.append(REVpssm)
    # Put the data into a dataframe
    s1 = pd.Series(TF, name='TF')
    s2 = pd.Series(PSSM, name='ForwardsPSSM')
    s3 = pd.Series(revPSSM, name='ReversePSSM')
    pssms = pd.DataFrame(dict(TF=s1, ForwardsPSSM=s2, ReversePSSM=s3))
    # Return the dataframe
    return pssms
##
# Get the data from the tamo file that I'm working with
tamoDF = getPSSMs(path + '/yeast.tamo')
# Get the amount of PSSMs (or TFs, both are the same)
countTF = tamoDF.count()
numOfTF = countTF['TF']
# Show the dataframe
choice = str(input('Show the tamo dataframe? Warning, this might be long! [y/n] '))
if choice == 'y':
        print(tamoDF)
##
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
##
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
##
time_est = calculateHits(fastaDF, tamoDF, numOfTF, numOfCHR, 0.35, 0.7, 'Hits Files')
print(time_est)
