#!/usr/bin/env python3
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
## Get the parameters when the user called to function
args = list(sys.argv[1:])
data_path = args[0]
n = args[1]
show_fasta_data = args[2]
hits_path = args[3]
## Print out to the user and tell then what options they selected
print('>>>>>>>>>>>>>>>>>>')
print('data files =', '[' + data_path + '/' + 'yeast.tamo' + ']', 'and', '[' + data_path + '/' + 'SGDv3.fasta' + ']')
print('# chromosomes unused =', n)
print('>>>>>>>>>>>>>>>>>>')
## Get the fasta data
# Get the data from the fasta file that I'm working with
genes = Fasta(data_path + '/SGDv3.fasta')
# Get the chromosomes
chrs = genes.keys()
# Get the amount of chromosomes
numOfCHR = len(chrs)
# Show the fasta data
if show_fasta_data == 'y':
    for chrom in chrs[:len(chrs)-n]:
        print('The first 25 letters in', chrom, 'are -', genes[chrom][0:24])
## Calculate the hits
print(calculate_hits(genes, data_path + '/yeast.tamo', 'HSF1', 'src/hits/HitsHSF1.gff'))
