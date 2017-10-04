% distances implementation
% Copyright (2017) University of Colorado
% All Rights Reserved
% Author: John Letey

% Read in hits.txt
input = textread('hits.txt', '%s', 'delimiter', '\n');
% Parse hits.txt
positionOfWeak = {};
positionOfStrong = {};
for i = 9:(size(input, 1) - 5)
    line = input{i, 1};
    j = 1;
    while line(j) ~= ' '
        j = j + 1;
    end
    position = line(1:(j - 1));
    j = size(line, 2) - 1;
    while line(j) ~= ' '
        j = j - 1;
    end
    type = line((j + 1):(size(line, 2) - 1));
    if strcmp(type, 'weak') == 1
        positionOfWeak = horzcat(positionOfWeak, str2num(position));
    end
    if strcmp(type, 'strong') == 1
        positionOfStrong = horzcat(positionOfStrong, str2num(position));
    end
end
% Read in input.txt
input = textread('input.txt', '%s', 'delimiter', '\n');
% Get the threshold values from input.txt
weakThresh = str2num(input{5, 1});
strongThresh = str2num(input{6, 1});
% Open output.csv and write to it
% T = cell2table(PSSM, 'RowNames', {'A', 'C', 'G', 'T'});
% writetable(T, 'output.csv', 'WriteRowNames', true);
% fileID = fopen('output, 'w');
% csvwrite('output.csv', [''], 1, 1);
% fprintf(fileID2, '%s %s \n', 'searching', chrName);
% fprintf(fileID2, '%s %s \n', 'for transcription factor', TF);
% fprintf(fileID2, '%s %s \n', 'weak threshold:', num2str(weakThresh));
% fprintf(fileID2, '%s %s \n', 'strong threshold:', num2str(strongThresh));
% fprintf(fileID2, '%s %s %s \n', 'The PSSM for transcription factor', TF, 'is');
% variableNames = mat2cell(1:lenOfPSSM, 1);
% Compare the weak and strong sites
categories = [];
for i = 1:size(positionOfStrong, 2)
    for j = 1:size(positionOfWeak, 2)
        mat = zeros(1, str2num(input{8, 1})/str2num(input{7, 1}));
        value = abs(positionOfStrong{1, i} - positionOfWeak{1, j});
        for k = 1:str2num(input{8, 1})/str2num(input{7, 1})
            if (value <= (str2num(input{7, 1})*k)) && (value > (str2num(input{7, 1})*(k-1)))
                mat(k) = value;
            end
        end
        if sum(mat ~= zeros(1, str2num(input{8, 1})/str2num(input{7, 1}))) >= 1
            categories = vertcat(categories, mat);
        end
    end
end
% Plot the histogram
histogram(categories, str2num(input{8, 1})/str2num(input{7, 1}))
title('Histogram of Distances between Strong and Weak Sites');
xlabel('Distance from Strong to Weak Site');
ylabel('Amount of Sites');
% Save the histogram to histogram.png
print('-dpng', 'histogram.png', '-r100');
% Close output.csv
%fclose(fileID2);