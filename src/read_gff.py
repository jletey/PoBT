#!/usr/bin/env python
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# title      Read GFF File Script                                                  +
# project    A-Study-of-Transcription-and-Its-Affects                              +
# repository https://github.com/johnletey/A-Study-of-Transcription-and-Its-Affects +
# author     John Letey                                                            +
# email      john.letey@colorado.edu                                               +
# copyright  Copyright (C) 2018                                                    +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Imports
# from Bio import SeqIO
## Implementation of read_gff
def read_gff(gff_filename):
    seq = []
    fileID = open(gff_filename, 'r')
    line = fileID.readline().split('\n')[0]
    while line:
        seq.append(line.split('\t'))
        line = fileID.readline().split('\n')[0]
    return seq
