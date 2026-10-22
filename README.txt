=== INFORMATION ===

- Python script that does gene expression analysis on count matrices.
- It calculates: base Mean, log2 Fold Change, lfcSE, p-value and padj.
- Better usability and more features will come in future releases...



=== USAGE ===

1) Download the count matrix you want to analyze (as a text file) from the NCBI GEO database
2) Move the file into the program's directory
3) In "cleanscript.py", replace the example file name (on both lines 11 and 15) with the name of the downloaded file
4) Enter the directory and execute "source venv/bin/activate"
5) In the same session execute "python3 cleanscript.py" (this will process and clean up the input file, converting into a form that can be used by the actual analysis script)
6) If everything goes well, in the same session execute "python3 script.py" (this will run the actual analysis)
7) If everything goes well, you can see the final results in the "results.csv" file produced in the same directory.



=== CONTENT ===

.git                                       git directory (for git integration, not necessary)
cleanscript.py                             the script that "cleans" the count matrix
venv virtual                               environment directory (holds the required python libraries)
example screenshot.png                     example screenshot of the program in use (not necessary)
GSE330228_Mtb_H37Rv_mutants_raw_counts.csv example count matrix included to test the program (not necessary)
README.txt                                 informations about this program (not necessary)
script.py                                  the script that does the differential analysis



=== NOTES ===

- This program works in a virtual environment that includes the following Python libraries:
  - pandas
  - pydeseq2

- After the analysis, the "cleanmatrix.csv", "metadata.csv" and "results.csv" files will be generated; remember to remove them once you're done
