# A Study of Transcription and Its Affects

To run the this repository locally, you will first want to download (or cloan) this repository and then run `main.m` with the following command

```
run('main.m');
```

You can also type the above line of code into any of your MatLab scripts or functions to use its outputs. `main.m` takes input from the file `input.txt`, which is formated as follows (where numbers are the line numbers)

1. Name of fasta file
2. Name of chromosome
3. Name of tamo file
4. Name of TF (**T**ranscription **F**actor)
5. Weak threshold value
6. Strong threshold value
7. The maximum allowed distance between weak and strong sites

`main.m` outputs the file `output.txt`, which contains a little about what the program is doing and important numbers the program outputs.
