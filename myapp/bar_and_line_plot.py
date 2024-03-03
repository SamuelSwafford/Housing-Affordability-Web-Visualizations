import pandas as pd
import matplotlib
# Ensure matplotlib does not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_bar_and_line( city = 'United States'):  # Renamed function
    df = pd.read_csv('resources/data_interpolated.csv')
    df = df[df['CityName'] == city]
    df = df[['Date', 'SalesTotal', 'MORTGAGE30US']]
    df['MORTGAGE30US'] = df['MORTGAGE30US'].bfill()
    df.dropna(subset=['SalesTotal'], inplace=True)

    # Convert 'Date' to datetime and set it as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Calculate yearly sum of 'SalesTotal' and yearly average of 'MORTGAGE30US'
    df = df.resample('Y').agg({'SalesTotal': 'sum', 'MORTGAGE30US': 'mean'})

    # Plot the data
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Bar plot
    bar = ax2.bar(df.index.year, df['SalesTotal'], color='blue', zorder=0, alpha=.5)

    # Line plot
    line, = ax1.plot(df.index.year, df['MORTGAGE30US'], color='red', zorder=1)

    # Set labels and title
    ax1.set_xlabel('Time')
    ax1.set_ylabel('MORTGAGE30US')
    ax2.set_ylabel('Sales Total')
    plt.title('Bar and Line Plot')

    # Add legends
    plt.legend([line, bar], ['MORTGAGE30US', 'Sales Total'])

    # Move the line plot to the front
    ax1.set_zorder(ax2.get_zorder() + 1)
    ax1.patch.set_visible(False)
    plt.savefig('static/bar_and_line_plot.png')

    plt.close()
if __name__ == '__main__':
    # Example usage
    city = 'United States'
    # column1 = 'SalesTotal'
    # column2 = 'MORTGAGE30US'
    plot_bar_and_line(city)