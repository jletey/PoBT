% loadPSSM implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

% Get the filename and TF from input.txt
input = textread('input.txt', '%s', 'delimiter', '\n');
filename = input{3, 1};
TF = input{4, 1};
% Get the file extension
[ ~, ~, ext ] = fileparts(filename);
% Check to see if the file is a tamo file
if strcmp(ext, '.tamo') == 1
    % Load in the tamo file
    input = textread(filename, '%s', 'delimiter', '\n');
    % Check all of the possible source lines for the TF
    for i = 0:123
        % Get line 19 + 42*i
        line = input{19 + 42*i, 1};
        % Create the line your looking for
        correctLine = ['Source:  ', TF];
        % Compare
        if strcmp(line, correctLine) == 1
            position = i;
        end
    end
    % Set the start and end line for the PSSM
    startLine = 2 + 42*position;
    % Get the startLine's length to figure out the length of the PSSM
    firstLine = input{startLine, 1};
    % Figure out how long the PSSM is going to be
    [ ~, len ] = size(firstLine);
    lenOfPSSM = (len - 3)/10;
    % Create a cell array that will contain the PSSM
    PSSM = {};
    newCollumn = {0; 0; 0; 0};
    for i = 1:lenOfPSSM
        PSSM = horzcat(PSSM, newCollumn);
    end
    % Get the all the lines of the PSSM
    firstLine = input{startLine + 1, 1};
    secondLine = input{startLine + 2, 1};
    thirdLine = input{startLine + 3, 1};
    fourthLine = input{startLine + 4, 1};
    % Get the values and insert them into a cell array
    for i = 1:lenOfPSSM
        value = firstLine(((i - 1)*10 + 7):((i - 1)*10 + 12));
        value = str2num(value);
        PSSM(1, i) = {value};
        value = secondLine(((i - 1)*10 + 7):((i - 1)*10 + 12));
        value = str2num(value);
        PSSM(2, i) = {value};
        value = thirdLine(((i - 1)*10 + 7):((i - 1)*10 + 12));
        value = str2num(value);
        PSSM(3, i) = {value};
        value = fourthLine(((i - 1)*10 + 7):((i - 1)*10 + 12));
        value = str2num(value);
        PSSM(4, i) = {value};
    end
else
    % Display the error to the user
    disp('You did not enter in the name of a tamo file into input.txt');
end

% Note that this script doesn't return anything, but the variable PSSM 
% that holds the corresponding PSSM to the given TF will be accessible 
% outside of this script