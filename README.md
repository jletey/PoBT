# A Study of Transcription and Its Affects

**Warning:** `main.m` takes 1522.384501 seconds, which is approximately 25 minutes, to run.

To run the this repository locally, you will first want to download (or cloan) this repository and then run `main.m` with the command

```matlab
run('main.m');
```

The script `main.m` is broken up into two major parts. Please note that hits are strong and weak binding sites. Please note that before we go into great detail about these two parts, let's first talk about what `input.txt` contains, since both parts use it. `input.txt` is formatted as follows (please note that number are line numbers)

1. Name of fasta file
2. Name of chromosome
3. Name of tamo file
4. Name of the TF (**T**ranscription **F**actor) you want to use
5. Weak threshold value
6. Strong threshold value
7. Size of each category of distances between sites
8. Maximum allowed plus/minus distance between a strong and weak site

## Part 1 : Finding the Hits
The script that finds the hits, which is called from `main.m`, is called `hits.m`. `hits.m` goes through the chromosome and calculates the output using the PSSM. From there, it goes through all of the outputs, and compares then to our strong and weak thresholds. Every output that is bigger than the weak threshold and less than the strong threshold is classified as a weak site. Every output that is bigger than the strong threshold is classified as a strong site. `hits.m` puts all of the values which are either weak or strong intow `hits.txt` for the user to further study.

## Part 2 : Analyzing the Hits
The script that analyses the hits, which is called from `main.m`, is called `distances.m`. `distances.m` calculates the distances between every strong and weak site. After `distances.m` calculates the distances between every strong and weak site, it plots a histogram of how many sites are in certain categories of distances from each other. Here is what the histogram looks like:

![settings window](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/histogram.png?raw=true)

Using this, we can analyse and look at what categories have the highest amount of sites and why.