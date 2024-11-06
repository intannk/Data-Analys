import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    years = data['Year']
    sea_levels = data['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(years, sea_levels, color='blue', label='Original Data')

    # Create first line of best fit for all data
    slope1, intercept1, _, _, _ = linregress(years, sea_levels)
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = slope1 * x_pred1 + intercept1
    plt.plot(x_pred1, y_pred1, color='red', label='Best Fit Line (1880-2050)')

    # Create second line of best fit from year 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = slope2 * x_pred2 + intercept2
    plt.plot(x_pred2, y_pred2, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
