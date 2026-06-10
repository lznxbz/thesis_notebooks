from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
from scipy.stats import linregress
import numpy as np

color_l = list(mcolors.BASE_COLORS.keys())
color_index = 0

def plot_with_regression(grid, plot_n, x_vals, y_vals, label, reginleg = False):
    global color_index
    # Linear Regression
    slope, intercept, r, p, se = linregress(x_vals, y_vals)
    y_lr = slope * x_vals + intercept

    if reginleg:
        label = f"{label}  {slope:.2f}  {intercept:.2f}  {r**2:.2f}"
    # Plot
    grid.plot(x_vals, y_lr, "-", color=color_l[plot_n])
    grid.plot(x_vals, y_vals, "o", label=label, color=color_l[plot_n])

    color_index += 1
    return grid, slope, r**2

if __name__ == "__main__":
    print(color_l)
