% hits implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

% Load the data from the fasta file
run('loadData.m');
% Load the PSSM from the tamo file
run('loadPSSM.m');
% Read in input.txt
input = textread('input.txt', '%s', 'delimiter', '\n');
% Get the name of the chromosome from input.txt
chrName = input{2, 1};
% Get the threshold values from input.txt
weakThresh = str2num(input{5, 1});
strongThresh = str2num(input{6, 1});
% Get the chromosome
chrNumber = chrName(4);
chrNumber = str2num(chrNumber);
chr = data{2, chrNumber};
% Get the length of the chromosome
[ ~, len ] = size(chr);
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
% Evaluate the chromosome with the PSSM and count how many strong and weak sites there are
out = {};
positionOfWeak = {};
positionOfStrong = {};
weakAmount = 0;
strongAmount = 0;
for i = 1:len
    if (i + lenOfPSSM - 1) > len
        output = outputOfPSSM(PSSM, horzcat(chr(i:end), blanks(i + lenOfPSSM - 1 - len)), max);
    else
        output = outputOfPSSM(PSSM, chr(i:(i + lenOfPSSM - 1)), max);
    end
    out = horzcat(out, output);
    if (output >= weakThresh)
        if (output < strongThresh)
            fprintf(fileID, '  %10d   %10s %6s \n', i, num2str(output), 'weak');
            weakAmount = weakAmount + 1;
            positionOfWeak = horzcat(positionOfWeak, i);
        else
            fprintf(fileID, '  %10d   %10s %8s \n', i, num2str(output), 'strong');
            strongAmount = strongAmount + 1;
            positionOfStrong = horzcat(positionOfStrong, i);
        end
    end
end
% Fix the PSSM so that it isn't in log-odds notation
for i = 1:lenOfPSSM
    for j = 1:4
        PSSM{j, i} = PSSM{j, i}/max;
    end
end
% Output to output.txt the amount of weak and strong sites
fprintf(fileID, '# \n');
fprintf(fileID, '# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n');
fprintf(fileID, '# \n');
fprintf(fileID, '# The number of weak sites is %d \n', weakAmount);
fprintf(fileID, '# The number of strong sites is %d \n', strongAmount);
% Close output.txt
fclose(fileID);