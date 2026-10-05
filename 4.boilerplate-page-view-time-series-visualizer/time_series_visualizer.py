import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'],index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    
    fig, ax = plt.subplots(figsize=(16, 5))
        # fig (hình ảnh để lưu) và ax (trục toạ độ để vẽ)

    ax.plot(df.index,df['value'], color = 'red', linewidth = 1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    months_order = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]   # ghi để có thể chú thích đúng theo thứ tự các tháng thay vì để kí tự theo thứ tự bản chữ cái
    
    df_bar['month'] = pd.Categorical(df_bar['month'], categories = months_order,ordered=True)
    
    df_bar = df_bar.groupby(['year','month'])['value'].mean().unstack()

    # Draw bar plot
    ax2 = df_bar.plot(kind = 'bar', figsize=(10,8))
    fig = ax2.figure
        # nếu nhờ thẳng pandas vẽ thì phải khai báo 2 bươc để lưu vào figure được

    ax2.set_ylabel ('Average Page Views')
    ax2.set_xlabel('Years')
    ax2.legend(title = 'Months')
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(20, 8))

    sns.boxplot(x='year', y='value', data = df_box, ax = ax3)
    ax3.set_title('Year-wise Box Plot (Trend)')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Page Views')

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data = df_box, order = month_order, ax = ax4)
    ax4.set_title('Month-wise Box Plot (Seasonality)')
    ax4.set_xlabel('Month')
    ax4.set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
