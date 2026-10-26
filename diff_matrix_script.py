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

# === STATISTICS ANALYSIS === #
print("estimation of normalization & dispersion factors: STARTED...")
dataset.deseq2()   # Estimates normalization & dispersion factors
print("estimation of normalization & dispersion factors: FINISHED!")

print("differential expression statistics calculation: STARTED...")
stats = DeseqStats(dataset, contrast=["condition", "treated", "control"])   # Produces statistics by comparing the data with "condition"="treated" to those with "condition"="control"
stats.summary()
print("differential expression statistics calculation: FINISHED!")

# === OBTAIN DATA FOR HEATMAP === #
print("variance stabilizing transformation: STARTED...")
dataset.vst()   # Runs "Variance Stabilizing Transformation" on dataset.
vstprematrix = PS.DataFrame(   # Makes new table with the resulting data.
    dataset.layers["vst_counts"], index=dataset.obs_names, columns=dataset.var_names   # dataset.layers["vst_counts"] = Normalized expression values per sample.
)
vstmatrix = vstprematrix.T   # Returns to standard layout
print("variance stabilizing transformation: FINISHED!")

# === SELECT MOST SIGNIFICANT GENES (NOT USED YET...) === #
print("selecting top 50 results: STARTED...")
statres = stats.results_df
sortstatres = statres.dropna(subset=["padj"]).sort_values("padj")   # Orders statres by padj values.
top50 = sortstatres.head(50).index.tolist()   # Selects the top 50 values.
topmatrix = vstmatrix.loc[top50]   # Subset (top 50) of the vstmatrix.
print("selecting top 50 results: FINISHED!")

# === CENTERING AND SAVING DATA === #
diffmatrix = vstmatrix.sub(vstmatrix.mean(axis=1), axis=0)   # Centers data around 0
diffmatrix.to_csv("differential_expression_values.csv")
print("SUCCESS! Results have been saved in 'differential_expression_values.csv'.")
