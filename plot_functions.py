import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def manhattan_plot(df):
    df['-log10(p-value)'] = -np.log10(df['p-value'])
    
    plt.figure(figsize=(10, 6))
    # Use alternating colors for chromosomes
    df['color'] = np.where(df['chromosome'] % 2 == 0, 'skyblue', 'navy')
    
    plt.scatter(df['position'], df['-log10(p-value)'], c=df['color'], s=10)
    plt.xlabel('Genomic Position')
    plt.ylabel('-log10(p-value)')
    plt.title('Manhattan Plot')
    plt.grid(True)
    
    st.pyplot(plt)

def qq_plot(df):
    sorted_pvals = np.sort(df['p-value'])
    expected = np.arange(1, len(sorted_pvals) + 1) / (len(sorted_pvals) + 1)
    plt.figure(figsize=(6, 6))
    
    plt.scatter(-np.log10(expected), -np.log10(sorted_pvals), c='navy', s=10)
    plt.plot([0, 1], [0, 1], transform=plt.gca().transAxes, color='red', ls='--')
    plt.xlabel('Expected -log10(p-value)')
    plt.ylabel('Observed -log10(p-value)')
    plt.title('QQ Plot')
    plt.grid(True)
    
    st.pyplot(plt)
