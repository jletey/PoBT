#!/usr/bin/env python3
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# title      Read GFF File Script                                                  +
# project    A-Study-of-Transcription-and-Its-Affects                              +
# repository https://github.com/johnletey/A-Study-of-Transcription-and-Its-Affects +
# author     John Letey                                                            +
# email      john.letey@colorado.edu                                               +
# copyright  Copyright (C) 2018                                                    +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Imports
from Bio import SeqIO
## Implementation of read_gff
def read_gff(gff_filename):
    with open(gff_filename) as gff_file:
        seq = []
        for seq_record in SeqIO.parse(gff_file, 'gff'):
            seq.append(str(seq_record.seq))
    return seq
