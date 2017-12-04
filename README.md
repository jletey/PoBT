![JupyterNotebook](https://img.shields.io/badge/jupyter%20notebook-5.2.1-orange.svg) 
![Python3.6](https://img.shields.io/badge/python-3.6-blue.svg)
![BuildStatus](https://img.shields.io/badge/build-passing-brightgreen.svg)
<!-- ![BuildStatus](https://img.shields.io/badge/build-failing-red.svg) -->

# A Study of Transcription and Its Affects

**Contributors:** John Letey (John.Letey@colorado.edu) and David Knox (David.Knox@colorado.edu)

**Notes:** To get to my GitHub repository, go to this [website](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects). For instructions on how to use my repository, go [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/current/instructions.md). For more information on the builds of this project, go [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/current/build.md).

**Dependencies:** My Jupyter Notebook uses the [biopython](https://github.com/biopython/biopython) package, which you can easily download using the built in interface in the Anaconda Navigator. Look at my instructions [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/current/instructions.md) on how to download biopython. I also have the dependency of having the package [pandas](https://github.com/pandas-dev/pandas), which should come pre-installed when you download Anaconda.

Here is the pipeline I followed in this project:

![pipeline](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/current/Pictures/pipeline.png?raw=true)

I have broken this project into to two major portions. The first portion calculates the hits (weak and strong transcription factor binding sights) for a specified chromosome (or all of the chromosomes) and transcription factor. The second portion analyses these hits. <!--Before we talk about these two parts more in depth, I'm going to give you a brief introduction on why I'm doing this.-->

<!--## Introduction-->

<!--The fundamental component of life, whether we're talking about animals or humans or anything, is the cell. The cell is the most complex and unique part of any living being. As humans, some of us wonder what goes on inside such a fundamental component of us. That when I started wondering, is there a pattern? In all cells, the DNA goes through a process called transcription which converts it into RNA (which then the cell uses to make proteins, and then the process repeats). While doing this, there are transcription factors, which the whole point of there existence is to bind to the DNA. Each transcription factor has a unique target string which it is looking for in the DNA sequence.-->

<!--## Part 1: Finding the Hits-->

<!--We're given both the chromosomes (in fasta format) and transcription factors and there corresponding pssm (in tamo format). How to we get strong and weak sites out of this? The way I implemented the part, was:-->

<!--## Part 2 : Analyzing the Hits-->

