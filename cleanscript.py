import pandas as PS

# === MAKE PANDAS TABLE BASED ON TABULATION === #
try:   # if there are no separators:
    matrix = PS.read_csv("m.csv", sep=None, engine="python", index_col=0)
except Exception as e:   # if there are multiple spaces as separators:
    matrix = PS.read_csv("m.csv", sep=r"\s+", index_col=0)

# === IF NEEDED, TRANSPOSE MATRIX === #
# makes a new table "matrixi" based on the original "matrix"
# Warning! This assumes that there should normally be more columns that rows!
if matrix.shape[0] > matrix.shape[1]:   # if matrix rows > matrix columns
    matrixi = matrix.T
    print("note: matrix has been transposed")
else:
    matrixi = matrix.copy()

# === CONVERT ALL VALUES TO INTEGER NUMBERS === #
matrixi = matrixi.round().astype(int)
print("note: all values have been converted to integers")

# === REMOVE NOT SIGNIFICANT ENOUGH DATA === #
# Assumes that all genes should have a total expression count of at least 10
matrixi = matrixi.loc[:, matrixi.sum(axis=0) >= 10]
print("note: genes with too low expression values have been removed from the count matrix")

# === CREATE METADATA FILE === #
# Warning! This considers everything that's not "ctrl" or "control" as: "treated"
metadata = PS.DataFrame(index=matrixi.index)
metadata["condition"] = [
    "control" if ("ctrl" in sample.lower() or "control" in sample.lower() or i < len(matrixi.index) // 2)   # ??? Assigns a condition based on the sample name or dividing them by half.
    else "treated"
    for i, sample in enumerate(matrixi.index)
]
print("note: metadata have been generated")

# === CONVERT ALL VALUES TO INTEGER NUMBERS === #
matrixi = matrixi.apply(PS.to_numeric, errors='coerce').fillna(0).astype(int)
print("note: all values have been converted to integers")

# === SAVE EVERYTHING TO FILE === #
matrixi.to_csv("cleanmatrix.csv")
print("SUCCESS!: processed count matrix has been saved as 'cleanmatrix.csv'")
metadata.to_csv("metadata.csv")
print("SUCCESS!: metadata have been saved as 'metadata.csv'")
