# A Study of Transcription and Its Affects

**Notes:** Here is a [PDF](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/raw/master/README.pdf) version of this README file.

**Warning:** `main.m` takes 1522.384501 seconds, which is approximately 25 minutes, to run.

To run the this repository locally, you will first want to download (or cloan) this repository and then run `main.m` with the command

```matlab
run('main.m');
```

The script `main.m` is broken up into two major parts. Please note that hits are strong and weak binding sites.

## Part 1 : Finding the Hits
The script that finds the hits, which is called from `main.m`, is called `hits.m`. `hits.m` goes through the chromosome and calculates the output using the PSSM. From there, it goes through all of the outputs, and compares then to our strong and weak thresholds. Every output that is bigger than the weak threshold and less than the strong threshold is classified as a weak site. Every output that is bigger than the strong threshold is classified as a strong site.

## Part 2 : Analyzing the Hits
The script that analyses the hits, which is called from `main.m`, is called `distances.m`. `distances.m` calculates the distances between every strong and weak site. After `distances.m` calculates the distances between every strong and weak site, it plots a histogram of how many sites are in certain ranges of distances from each other. Here is what the histogram looks like:

![settings window](https://github.com/JohnLetey/A-Study-of-Transcription-and-Its-Affects/blob/master/histogram.png?raw=true)

Using this, we can analyse and look at ranges have the highest amount of sites and why.