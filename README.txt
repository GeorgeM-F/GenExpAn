=== INFORMATION ===

- Python script that does gene expression analysis on count matrices.
- Calculates base Mean, log2 Fold Change, lfcSE, p-value and padj, then uses those values to make a Volcano Plot.
- Generates a differential expression matrix, then uses those value to make a Heatmap.
- Warning! It might not work on files with certain kinds of tabulation.
- More features will come in future releases...



=== HOW TO USE ===

1) Download the count matrix you want to analyze (as a .csv file) from the NCBI GEO database.
2) Move the file into the program's directory and rename it as "m.csv".
3) Execute "GenExpAn.sh" in a terminal.
If everything goes well, you should be able to see:
- the general statistics in "results.csv"
- the differential expression values in "differential_expression_values.csv"
- the Volcano Plot in "volcanoplot.png"
- the Heatmap in "heatmap.png"
(all these files are created in the same directory)



=== CONTENT ===

.git                                git directory (for git integration, not necessary)
venv                                virtual environment directory (holds the required python libraries)
diff_matrix_script.py               the script that generates a matrix of differential expression values between single values and average; it takes "cleanmatrix.csv" and "metadata.csv", and generates "general_statistics.csv"
diff_stats_script.py                the script that calculates the general differential expression between condition and control; it takes "cleanmatrix.csv" and "metadata.csv", and generates "differential_expression_values.csv"
example (heatmap).png               an example of a resulting heatmap (not necessary)
example (volcano plot).png          an example of a resulting volcano plot (not necessary)
GenExpAn.sh                         the main executable script; it works by concatenating the scripts: "preparing_script.py", "diff_stats_script.py", "diff_matrix_script.py", "volcanoplot_visualization_script.py" and "heatmap_visualization_script.py" in this order
heatmap_visualization_script.py     the script that generates the Heatmap; it takes "differential_expression_values.csv" and generates "heatmap.png"
m.csv                               example count matrix included to test the program (not necessary)
preparing_script.py                 the script that "cleans" the count matrix so it can be processed by the other script; it takes "m.csv" and generates "cleanmatrix.csv" and "metadata.csv"
README.txt                          informations about this program (not necessary)
volcanoplot_visualization_script.py the script that generates the Volcano Plot; it takes "general_statistics.csv" and generates "volcanoplot.png"



=== NOTES ===

- This program works in a virtual environment that includes the following Python libraries:
  - pandas
  - pydeseq2

- After the analysis, the following files are created:
  - "cleanmatrix.csv"
  - "metadata.csv"
  - "results.csv"
  - "general_statistics.csv"
  - "differential_expression_values.csv"
  - "volcanoplot.png"
  - "heatmap.png"
  remember to remove them once you're done
