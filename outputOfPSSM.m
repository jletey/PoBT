% outputOfPSSM function definition and implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

function [ out ] = outputOfPSSM( PSSM, sequence )
% This function calculates the output of the PSSM given a DNA sequence

% Calculate the size of the PSSM
[ ~, lenPSSM ] = size(PSSM);
% Calculate the size of the sequence
[ ~, lenSeq ] = size(sequence);
% Check to see if the length of the sequence of DNA is the same length as
% the PSSM
if lenPSSM == lenSeq
    out = 1.0;
    % Go through the PSSM and calculate output
    for i = 1:lenPSSM
        if sequence(i) == 'A'
            out = out * PSSM{1, i};
        end
        if sequence(i) == 'C'
            out = out * PSSM{2, i};
        end
        if sequence(i) == 'T'
            out = out * PSSM{3, i};
        end
        if sequence(i) == 'G'
            out = out * PSSM{4, i};
        end
    end
else
    % Display the error
    disp('The length of the sequence of DNA is not the same length as the PSSM');
    % Since we can never have a probability of 0.0, I've used it as my
    % error output of my function
    out = 0.0;
end
end
