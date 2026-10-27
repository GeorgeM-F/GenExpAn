import pandas as PS
import matplotlib.pyplot as MP

hmatrix=PS.read_csv("differential_expression_values.csv", index_col=0)   # Import matrix

print("creating visualization: STARTED...")
MP.figure(figsize=(10,8))   # Set up the figure
graph=MP.imshow(hmatrix.values,cmap="coolwarm",aspect="auto")
MP.colorbar(graph,label="Up/down-regulation level")   # Add colorbar
MP.xticks(ticks=range(len(hmatrix.columns)),labels=hmatrix.columns,rotation=90)   # Add column labels
MP.yticks(ticks=range(len(hmatrix.index)),labels=hmatrix.index)   # Add row labels
MP.title("Heatmap")   # Add a title
MP.xlabel("Samples")   # Add a label for the x-axis
MP.ylabel("Genes")   # Add a label for the y-axis
MP.tight_layout()
print("creating visualization: FINISHED!")
MP.savefig("heatmap.png",dpi=300)   # Save result to png file
print("SUCCESS! Results have been saved in 'heatmap.png'.")
MP.show()   # Show everything
