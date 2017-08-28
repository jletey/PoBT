% evaluatePSSMs function definition and implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

function [ out ] = evaluatePSSMs( PSSMs, sequences )
% This function evaluates all PSSMs given a list of DNA sequences

% Declare out to the empty cell array
out = {};
% Calculate the size of the PSSMs
[ ~, lenPSSM ] = size(PSSMs);
% Calculate the size of the sequences
[ ~, lenSeq ] = size(sequences);
% Get to see if the amount of PSSMs is the same as the amount as sequences
if lenPSSM == lenSeq
    % Declare the variables PSSM and sequence that will hold 
    for i = 1:lenSeq
        % Calculate the output of PSSM number i
        output = outputOfPSSM(PSSMs{i}, sequences{i});
        % Add output to out
        out = horzcat(out, {output});
    end
    % Open a blank figure
    figure;
    % Plot all the outputs in out
    plot(1:lenSeq, cell2mat(out));
    % Make the plot look nice
    title('Graph of the Outputs from the PSSMs');
else
    % Display the error
    disp('The number of the sequences of DNA is not the same length as the number of PSSMs');
    % Since out is a cell array, I've chosen the empty cell array to be the
    % error output of my function
    out = {};
end
end