## A Study of Transcription and Its Affects

**Warning:** `main.m` takes 1522.384501 seconds, which is approximately 25 minutes, to run.

To run the this repository locally, you will first want to download (or cloan) this repository and then run `main.m` with the command

```
run('main.m');
```

The script `main.m` is broken up into two major parts. The first part is a script called `hits.m`, which takes the given input from `input.txt` and outputs all of the strong and weak binding sites. The second part is a script called `distances.m`, which takes the hits calculated by `hits.m` and finds all of the sites that are up to a certain distance away from each other. `hits.m` takes input from the file `input.txt`, which is formated as follows (please note that numbers are line numbers)

1. Name of fasta file
2. Name of chromosome
3. Name of tamo file
4. Name of the TF (**T**ranscription **F**actor) you want to use
5. Weak threshold value
6. Strong threshold value
7. Size of each category of distances between sites
8. Maximum allowed plus/minus distance between a strong and weak site

`main.m` outputs the file `output.txt`, which contains a little about what the program is doing and important numbers the program outputs. `main.m` also outputs the file `output.csv`, which contains a little more data than `output.txt`, since a *csv* file can easily hold more data than a *txt* file, but the files are both roughly the same.