import pandas as pd

def validate_columns(df, required_columns):
    """Check if all required columns are present in the DataFrame."""
    return all(column in df.columns for column in required_columns)

def filter_snps(df, pvalue_threshold=1e-2):
    """Filter SNPs with p-values <= the specified threshold."""
    return df[df['p-value'] <= pvalue_threshold]


