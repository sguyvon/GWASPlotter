import streamlit as st
import pandas as pd
from plot_functions import manhattan_plot, qq_plot
from data_processing import validate_columns, filter_snps

st.title("GWASPlotter: Visualize Your GWAS Data")

# File upload functionality
uploaded_file = st.file_uploader("Upload your GWAS summary file (CSV/TSV)", type=["csv", "tsv"])

if uploaded_file is not None:
    try:
        # Read CSV or TSV file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file, sep='\t')

        st.write("File uploaded successfully!")
        st.write(df.head())

        # Validate required columns
        required_columns = ['rsid', 'chromosome', 'position', 'p-value']
        if validate_columns(df, required_columns):
            st.success("All required columns are present!")
            
            # Filter SNPs with p-values <= 1e-2
            filtered_df = filter_snps(df, pvalue_threshold=1e-2)
            st.write(f"Plotting {len(filtered_df)} SNPs with p-values ≤ 1e-2.")

            # Generate Manhattan Plot
            manhattan_plot(filtered_df)

            # Generate QQ Plot
            qq_plot(filtered_df)
        else:
            st.error(f"File is missing one or more required columns: {', '.join(required_columns)}")
    except Exception as e:
        st.error(f"Error loading file: {e}")
