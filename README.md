<p align="center">
  <h1 align="center">Patterns of Binding Targets</h1>

  <p align="center">
    <a href="https://johnletey.github.io/PoBT/">Main Website</a>
    ·
    <a href="https://github.com/johnletey/PoBT/">GitHub Repository</a>
    ·
    <a href="https://github.com/johnletey/PoBT/raw/master/paper/main.pdf">Download Paper</a>
  </p>
</p>

## Table of Contents

- [Overview](#abstract)
- [Quick Start](#quick-start)

## Abstract

Research project investigating if weak affinity binding sites aid in unwrapping the nucleosome so that strong affinity sites can occur, and if there's a certain pattern between the different binding sites if this occurs. Using Python computer programs to simulate the binding process. We inputted pre-mapped yeast chromosomes and yeast transcription factors into our model.

## Quick Start

Please see the [notes and warnings](#notes-and-warnings) section before proceeding! Note that, if you want to do all of the following by hand, go for it... but if you're lazy, just simply run `bash run.sh`.

**Installing Dependencies**

1. Install Python 3

2. Install requirements:

```sh
pip install -r requirements.txt
```

**Running code on my data**

To easily run code on my data, simply run this command:

```sh
python src/main.py src/data 2 n src/hits/ src/hists/
```

**Running on your own data**

To run my code on your own data, please note that my program takes in two files, namely, on FASTA formatted and the other one TAMO formatted. After that, it's pretty simple, but just make sure to follow the below instructions:

Start off with the command `python src/main.py`

1. Then, the first argument to pass in is the data directory (in my case it was `src/data`)
2. Then, pass in the number of chromosomes that you don't want to use (in my case it was 2)
3. Then, if you want to see a basic output of the chromosome, pass in `y`, otherwise pass in `n`
4. Then, pass in the folder where you want to hold all of the hits files (the folder has to exist)
5. And finally, pass in the folder where you want to hold all of the histogram files (the folder has to exist)

After that, you should be good to go!
