import math as M
import pandas as PS
import matplotlib.pyplot as MP

gstats=PS.read_csv("general_statistics.csv", index_col=0)   # Import matrix
nldp=[-M.log(i,10) for i in gstats["pvalue"]]   # changes all padj values to their negative log10

colormap=['grey' if y < 1.3 else 'red' if x > 0 else 'blue' for x,y in zip(gstats["log2FoldChange"],nldp)]   # set personalized colormap

print("creating visualization: STARTED...")
MP.figure(figsize=(10,8))   # Set up the figure
graph=MP.scatter(gstats["log2FoldChange"],nldp,c=colormap,s=2)   # Defines a scatter plot
MP.title("Volcano Plot")   # Add a title
MP.xlabel("up/down-regolation level (log2 Fold Change)")   # Add a label for the x-axis
MP.ylabel("statistical signifiance (-log10 p-value)")   # Add a label for the y-axis
MP.tight_layout()
print("creating visualization: FINISHED!")
MP.savefig("volcanoplot.png",dpi=300)   # Save result to png file
print("SUCCESS! Results have been saved in 'volcanoplot.png'.")
MP.show()   # Show everything
