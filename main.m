% main implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

% Load the data from the fasta file
run('loadData.m');
% Load the PSSM from the tamo file
run('loadPSSM.m');
% Get the name of the chromosome from input.txt
input = textread('input.txt', '%s', 'delimiter', '\n');
chrName = input{2, 1};
% Get the threshold values from input.txt
input = textread('input.txt', '%s', 'delimiter', '\n');
weakThresh = input{5, 1};
strongThresh = input{6, 1};
% Get the chromosome
chrNumber = chrName(4);
chrNumber = str2num(chrNumber);
chr = data{2, chrNumber};
% Break up the chromosome into equal segments of length lenOfPSSM
chr = cellstr(reshape(chr, lenOfPSSM, [])');
% Get how many chunks of the chromosome there are
[ amount, ~ ] = size(chr);
