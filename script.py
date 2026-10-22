import pandas as PS
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
from pydeseq2.default_inference import DefaultInference

# Note: the number of metadata rows must be equal to the number of count matrix columns in order for PyDESeq2 to work!

# === MAKE PANDAS TABLES FROM THE GENERATED FILES === #
matrix = PS.read_csv("cleanmatrix.csv", index_col=0)   # index_col=0 means that the 1st column only includes names
metadata = PS.read_csv("metadata.csv", index_col=0)   # index_col=0 means that the 1st column only includes names

# === SET INFERENCE CPUS === #
inf = DefaultInference(n_cpus=4)   # number of CPU to use for inference

# === MAKE DESEQ DATASET === #
dataset = DeseqDataSet(
    counts=matrix,
    metadata=metadata,
    design_factors="condition",   # Must be equal to the name of the column in the metadata file
    inference=inf
)
print("note: deseq dataset has been created")

# === ACTUAL ANALYSIS === #
print("estimation of normalization & dispersion factors: STARTED...")
dataset.deseq2()   # Estimates normalization & dispersion factors
print("estimation of normalization & dispersion factors: FINISHED!")

print("differential expression statistics calculation: STARTED...")
stats = DeseqStats(dataset, contrast=["condition", "treated", "control"])   # Produces statistics by comparing the data with "condition"="treated" to those with "condition"="control"
print("differential expression statistics calculation: FINISHED!")

# === MAKE SUMMARY === #
stats.summary()   # Makes a summary of produced stats

# === SAVE EVERYTHING TO FILE === #
stats.results_df.to_csv("results.csv")   # Saves stats' results dataframe to file
print("SUCCESS! Results have been saved in 'results.csv'.")

