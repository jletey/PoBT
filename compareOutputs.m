% compareOutputs function definition and implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

function [ out ] = compareOutputs( outputs, strongThresh, weakThresh )
% This function compares all of the outputs to the strong and weak
% thresholds

% Get the length of the outputs cell array
[ ~, len ] = size(outputs);
% Declare out to the empty cell array
out = cell(1, len);
% Go through outputs and compare each individual output to the strong and
% weak thresholds to see if it is a strong, weak, or unclassified binding
% site
for i = 1:len
    if outputs{1, i} <= weakThresh
        out{1, i} = 'W'; % "W" means weak
    elseif outputs{1, i} >= strongThresh
        out{1, i} = 'S'; % "S" means strong
    else
        out{1, i} = 'U'; % "U" means unclassified
    end
end
% Open a blank figure
figure;
% Graph the outputs with the thresholds
plot(1:len, cell2mat(outputs), '--o', ...
     1:len, weakThresh * ones(1, len), ...
     1:len, strongThresh * ones(1, len));
% Make the plot look nice
title('Graph of the Outputs from the PSSMs with Thresholds');
lgd = legend({'Outputs' 'Weak Threshold' 'Strong Threshold'}, ...
             'Location', 'NorthEast');
title(lgd, 'Legend');
end