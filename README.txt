=== INFORMATION ===

- Python script that does gene expression analysis on count matrices.
- It calculates: base Mean, log2 Fold Change, lfcSE, p-value and padj.
- Warning! It might not work on files with certain kinds of tabulation.
- More features will come in future releases...



=== USAGE ===

1) Download the count matrix you want to analyze (as a .csv file) from the NCBI GEO database.
2) Move the file into the program's directory and rename it as "m.csv".
3) Execute "GenExpAn.sh" in a terminal.
If everything goes well, you should be able to see the final results in the "results.csv" file produced in the same directory.



=== CONTENT ===

.git                                 git directory (for git integration, not necessary)
cleanscript.py                       the script that "cleans" the count matrix
venv virtual                         environment directory (holds the required python libraries)
example screenshot (GenExpAn.sh).png example screenshot of the program in execution (not necessary)
example screenshot (results.csv).png example screenshot of the final results (not necessary)
GenExpAn.sh                          the main executable script
m.csv                                example count matrix included to test the program (not necessary)
README.txt                           informations about this program (not necessary)
script.py                            the script that does the differential analysis



=== NOTES ===

- This program works in a virtual environment that includes the following Python libraries:
  - pandas
  - pydeseq2

- After the analysis, the "cleanmatrix.csv", "metadata.csv" and "results.csv" files will be generated; remember to remove them once you're done
