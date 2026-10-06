import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    draw = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
        # -> chạy thuật toán bình phương tối thiểu (Ordinary Least Squares) 
        # để tìm ra một đường thẳng duy nhất y = ax + b khớp nhất
    intercept = res.intercept
    slope = res.slope
    years = pd.Series(range(df['Year'].min(), 2051)) 
        #-> viết cho các năm thành hết dạng toán học, dùng được phép nhân vector trực tiếp
    y = slope * years + intercept

    plt.plot(years, y, 'r')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    rct_res = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    rct_intercept = rct_res.intercept
    rct_slope = rct_res.slope
    rct_years = pd.Series(range(2000, 2051))

    y2 = rct_slope * rct_years + rct_intercept
    plt.plot(rct_years, y2, 'b')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()