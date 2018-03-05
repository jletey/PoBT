#!/usr/bin/env python3
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# title      Output of PSSM Script                                                 +
# project    A-Study-of-Transcription-and-Its-Affects                              +
# repository https://github.com/johnletey/A-Study-of-Transcription-and-Its-Affects +
# author     John Letey                                                            +
# email      john.letey@colorado.edu                                               +
# copyright  Copyright (C) 2018                                                    +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Implementation of output_of_pssm
def output_of_pssm(PSSM, sequence, maximum, lenOfPSSM):
    # Go through the PSSM and calculate the output for the given sequence
    output = 1.0
    for i in range(lenOfPSSM):
        if sequence[i] == 'A':
            output += PSSM[0][i]
        if sequence[i] == 'C':
            output += PSSM[1][i]
        if sequence[i] == 'T':
            output += PSSM[2][i]
        if sequence[i] == 'G':
            output += PSSM[3][i]
    output /= maximum
    # Return output
    return output