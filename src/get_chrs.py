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
