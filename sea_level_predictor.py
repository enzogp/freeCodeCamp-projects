import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res_full = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_full = np.arange(df["Year"].min(), 2051)  # de 1880 à 2050
    y_full = res_full.slope * x_full + res_full.intercept
    ax.plot(x_full, y_full)

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_2000 = np.arange(2000, 2051)
    y_2000 = res_2000.slope * x_2000 + res_2000.intercept
    ax.plot(x_2000, y_2000)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()