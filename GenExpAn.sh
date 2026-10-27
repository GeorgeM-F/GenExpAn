#!/bin/bash
source venv/bin/activate
python3 preparing_script.py
python3 diff_stats_script.py
python3 diff_matrix_script.py
python3 volcanoplot_visualization_script.py
python3 heatmap_visualization_script.py
