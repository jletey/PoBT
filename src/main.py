#!/usr/bin/env python3
## Imports
import sys
from pyfaidx import Fasta
## Get the parameters when the user called to function
args = list(sys.argv[1:])
## Tell the user that all data will be grabbed from the data section
print('All data used will be grabbed from the data section (titled data)')
if len(args) > 0:
    choice = args[0]
    print('Are you okay with this? [y/n]', choice)
else:
    choice = str(input('Are you okay with this? [y/n] '))
isDifferentDataPath = False
if choice == 'n':
    if len(args) > 0:
        path = args[1]
        isDifferentDataPath = True
        print('What is you data path called?', path)
    else:
        path = str(input('What is your data path called? '))
    if path[len(path)-1] == '/':
    	path = path[:len(path)-1]
else:
    path = 'data'
## Get the fasta data
# Ask the user how much data they want to throw away
if len(args) > 0:
    if isDifferentDataPath:
        n = int(args[2])
    else:
        n = int(args[1])
    print('How many chromosomes do you want to throw away?', n)
else:
    n = int(input('How many chromosomes do you want to throw away? '))
# Get the data from the fasta file that I'm working with and take away two of those
genes = Fasta(path + '/SGDv3.fasta')
print(genes.keys())
print(type(genes))
print(genes[0])
# Get the amount of chromosomes
# countCHR = fastaDF.count()
# numOfCHR = countCHR['chromosome']
# Show the fasta data
if len(args) > 0:
    if isDifferentDataPath:
        choice = args[3]
    else:
        choice = args[2]
    print('Show the fasta data? [y/n]', choice)
else:
    choice = str(input('Show the fasta data? [y/n] '))
if choice == 'y':
    for key in genes.keys():
        print(genes[key][0:25])