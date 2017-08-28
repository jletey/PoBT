% loadData implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

% Ask the user to enter in the name of the fasta file
filename = input('Please enter in the name of your fasta file : ', 's');
% Get the file extension
[ ~, ~, ext ] = fileparts(filename);
% Check to see if the file is a fasta file
if strcmp(ext, '.fasta') == 1
    % Load in the fasta file
    data = fastaread(filename, 'ignoregaps', true);
    % The function fastaread returns a structure, but it's way easier to 
    % work with cell array, so let's convert data into a cell array
    data = struct2cell(data);
    % Tell the user that the file has been loaded
    disp('Your fasta file has been loaded succesfully');
else
    % Display the error to the user
    disp('You did not enter a .fasta file');
end

% Note that this script doesn't return anything, but the variable data
% that holds all of the data from the fasta file will be accessible 
% outside of this script