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
weakThresh = str2num(input{5, 1});
strongThresh = str2num(input{6, 1});
% Get the chromosome
chrNumber = chrName(4);
chrNumber = str2num(chrNumber);
chr = data{2, chrNumber};
% Break up the chromosome into equal segments of length lenOfPSSM
chr = cellstr(reshape(chr, lenOfPSSM, [])');
% Get how many chunks of the chromosome there are
[ amount, ~ ] = size(chr);
% Open output.txt and write to it
fileID = fopen('output.txt', 'w');
fprintf(fileID, '%s %s \n', '# searching', chrName);
fprintf(fileID, '%s %s \n', '# for transcription factor', TF);
fprintf(fileID, '%s %s \n', '# weak threshold:', num2str(weakThresh));
fprintf(fileID, '%s %s \n', '# strong threshold:', num2str(strongThresh));
fprintf(fileID, '# \n');
fprintf(fileID, '# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n');
fprintf(fileID, '# \n');
fprintf(fileID, '# %10s %10s %10s \n', 'position', 'strength', 'type');
% Find the maximum possible probability
max = 1;
for i = 1:lenOfPSSM
    maxForCollumn = 0;
    for j = 1:4
        if PSSM{j, i} > maxForCollumn
            maxForCollumn = PSSM{j, i};
        end
    end
    max = max*maxForCollumn;
end
% Evaluate all the chunks of the chromosome with the PSSM and count how
% many strong and weak sites there are
out = {};
weakAmount = 0;
strongAmount = 0;
for i = 1:amount
    output = outputOfPSSM(PSSM, chr{i, 1}, max);
    out = horzcat(out, output);
    if (output >= weakThresh)
        if (output < strongThresh)
            fprintf(fileID, '  %10d   %10s %6s \n', i, num2str(output), 'weak');
            weakAmount = weakAmount + 1;
        else
            fprintf(fileID, '  %10d   %10s %8s \n', i, num2str(output), 'strong');
            strongAmount = strongAmount + 1;
        end
    end
end
% Close output.txt
fclose(fileID);
