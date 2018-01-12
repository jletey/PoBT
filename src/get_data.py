#!/usr/bin/env python3
## Imports
import Bio
from Bio import SeqIO
import pandas as pd
## Implementation of getCHRs
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
## Implementation of getPSSMs
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
