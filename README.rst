.. image:: https://img.shields.io/travis/JohnLetey/A-Study-of-Transcription-and-Its-Affects/master.svg
   :alt: Testing with TravisCI
   :target: https://travis-ci.org/JohnLetey/A-Study-of-Transcription-and-Its-Affects
.. image:: https://img.shields.io/github/issues/JohnLetey/A-Study-of-Transcription-and-Its-Affects.svg
   :alt: Issues
   :target: https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/issues

A Study of Transcription and Its Affects
========================================

**Contributors:** John Letey (John.Letey@colorado.edu) and David Knox (David.Knox@colorado.edu)

**Warnings:** My Python code takes a long time to run. I'd suggest looking at the output of my program and not running my code to get the output.

**Notes:** To get to my GitHub repository, go to this [website](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects). For instructions on how to use my repository, go [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/instructions.md). For more information on the builds of this project, go [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/build.md). For an overview on this repository, go [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/overview.md).

**Dependencies:** My Jupyter Notebook uses the [biopython](https://github.com/biopython/biopython) package, which you can easily download using the built in interface in the Anaconda Navigator. Look at my instructions [here](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/instructions.md) on how to download biopython. I also have the dependency of having the package [pandas](https://github.com/pandas-dev/pandas), which should come pre-installed when you download Anaconda.

The below figure is the pipeline which I implemented in this project:

![pipeline](https://github.cm/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/Pictures/pipeline.png?raw=true)

I have broken this project into to two major portions. The first portion calculates the hits (weak and strong transcription factor binding sights) for a specified chromosome (or all of the chromosomes) and transcription factor. The second portion analyses these hits. Let's jump right in.
