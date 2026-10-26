=== INFORMATION ===

- Python script that does gene expression analysis on count matrices.
- Calculates base Mean, log2 Fold Change, lfcSE, p-value and padj.
- Generates a differential expression matrix.
- Warning! It might not work on files with certain kinds of tabulation.
- More features will come in future releases...



=== USAGE ===

1) Download the count matrix you want to analyze (as a .csv file) from the NCBI GEO database.
2) Move the file into the program's directory and rename it as "m.csv".
3) Execute "GenExpAn.sh" in a terminal.
If everything goes well, you should be able to see the general statistics in the "results.csv", and the differential expression values in the "differential_expression_values.csv" files produced in the same directory.



=== CONTENT ===

.git                                 git directory (for git integration, not necessary)
venv                                 virtual environment directory (holds the required python libraries)
diff_matrix_script.py                the script that generates a matrix of differential expression values between single values and average
diff_stats_script.py                 the script that calculates the general differential expression between condition and control
GenExpAn.sh                          the main executable script
m.csv                                example count matrix included to test the program (not necessary)
preparing_script.py                  the script that "cleans" the count matrix so it can be processed by the other script
README.txt                           informations about this program (not necessary)



=== NOTES ===

- This program works in a virtual environment that includes the following Python libraries:
  - pandas
  - pydeseq2

- After the analysis, the "cleanmatrix.csv", "metadata.csv", "results.csv" and "differential_expression_values.csv" files will be generated; remember to remove them once you're done
