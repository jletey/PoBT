% main implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

% Load the data from the fasta file
run('loadData.m');
% Load the PSSM from the tamo file
run('loadPSSM.m');
% Get the name of the chromosome
input = textread('input.txt', '%s', 'delimiter', '\n');
chr = input{2, 1};
% Break up chr into segments the same length as the PSSM

% Evaluate the PSSMs
