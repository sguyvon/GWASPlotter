# GWASPlotter
A simple web-based tool for visualising Genome-Wide Association Studies (GWAS) summary statistics using Manhattan and QQ plots. This tool allows users to upload GWAS data and generate visualisations to explore significant genetic variants in their dataset.

**Overview** \
Genome-Wide Association Studies (GWAS) calculate p-values to assess the statistical significance of associations between genetic variants and disease phenotypes, using logistic regression to compare allele frequencies between case (affected) and control (unaffected) groups. To visualise these p-values, and therefore determine genomics areas of interest, Manhattan plots are used. This tool creates Manhattan plots and QQ plots from GWAS summary statistics for users to analyse and decide on further steps.

## Features

- Upload GWAS summary statistics (CSV,TSV or txt format).
- Generate Manhattan and QQ plots.
- Filters SNPs with p-values above 1e-2 to optimize performance.
- Save plots as PNG files for further use.

## Requirements
This tool is written in Python. To run this tool locally, you will need to install the following dependencies.

### Required Packages
Python 3.x \
Streamlit: For creating the web-based interface. \
Pandas: For data handling and manipulation. \
Matplotlib: For generating Manhattan and QQ plots.
