import pandas as PS   # imports the "pandas" module, renamed as "PS"
try:   # tries doing this:
    matrix = PS.read_csv(   # defines "matrix" as...
        "GSE33064_series_matrix.txt",   # target file to analyze; replace with the file you want to analyze
        sep='\t',
        index_col=0,
        comment='!',   # ignores all lines starting with "!", which are not useful
        low_memory=False
    )
    print("\nFirst ten rows and cols of the count matrix:")
    print(matrix.iloc[:10, :10])   # shows the first 10 rows and columns of matrix
except Exception as e:   # in case of failure, does this instead:
    print(f"Loading error: {e}")
    print("Warning! Loading error. Please make sure your file is a valid format.")
