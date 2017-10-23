![JupyterNotebook](https://img.shields.io/badge/jupyter-notebook-orange.svg)
![Python3.6](https://img.shields.io/badge/python-3.6-blue.svg)

# A Study of Transcription and Its Affects

**Contributors:** John M. Letey (John.Letey@colorado.edu), David A. Knox (David.Knox@colorado.edu)

**Notes:** To get to my GitHub repository, go to this [website](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects). For instructions on how to use my repository, go [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/instructions.md).

I have broken this project into to major portions. The first portion calculates the hits (weak and strong transcription factor binding sights) for a specified chromosome and transcription factor. The second portion analyses these hits. Let's talk about these two portions more in depth.

## Part 1: Finding the Hits

To calculate the hits, I read in from a file called `input.txt` which is formatted as follows:

|  Line Number  | Description |
|:---:|:---:|
| 1 | Name of fasta file |
| 2 | Name of tamo file |
| 3 | Weak threshold value |
| 4 | Strong threshold value |
| 5 | Size of each category of distances between sites |
| 6 | Maximum allowed plus/minus distance between a strong and weak site |

I had originally sought out to do this project in MatLab, but with the fact that we're running our code with super big data (and for the sake of your and my sanity), I have decided to use Python, with Jupyter Notebook, for this project. I read in the chromosomes from a fasta file called `SGDv3.fasta` and the associated PSSM to the transcription factor from the tamo file called `yeast.tamo`. Before we continue, let's first read in `input.txt`.

## Part 2 : Analyzing the Hits
[settings window](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/instructions.md?raw=false)