=== INFORMATION ===

- Python script intended to do gene expression analysis on count matrices.
- In its current state, it can only show the first ten rows and columns of the count matrix; more functionalities will be added in the future.



=== USAGE ===

1) Download the count matrix you want to analyze (as a text file) from the NCBI GEO database
2) Move the file into the program's directory
3) In "script.py", replace the example file name with the name of the downloaded file
4) Enter the directory and execute "source venv/bin/activate", then execute the "script.py" file with python3



=== CONTENT ===

.git                       git directory (for git integration, not necessary)
venv virtual               environment directory (holds the required python libraries)
example screenshot.png     example screenshot of the program in use (not necessary)
GSE33064_series_matrix.txt example count matrix included to test the program (not necessary)
README.txt                 informations about this program (not necessary)
script.py                  the actual executable



=== NOTES ===

- This program works in a virtual environment that includes the following Python libraries:
  - pandas
