import pandas as pd
import matplotlib
# Ensure matplotlib does not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_bar_and_line( city, column1, column2):  # Renamed function
    # Read the CSV file into a pandas DataFrame
    data_file = 'resources/data_interpolated.csv'
    df = pd.read_csv(data_file)
    df = df[df['CityName'] == city]

    rates = df[['Year', 'MORTGAGE30US']].dropna().drop_duplicates().set_index('Year')
    sales = df['SalesTotal'].groupby(df['Year']).sum()

    # Plot the data
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.bar(rates.index, sales.values, color='blue', alpha=0.5)
    ax2.plot(rates.index, rates.values.flatten, color='red')

    # Set labels and title
    ax1.set_xlabel('Time')
    ax1.set_ylabel(column1)
    ax2.set_ylabel(column2)
    plt.title(f'{column1} and {column2} over Time')

    plt.savefig('static/bar_and_line_plot.png')
    plt.close(fig)

if __name__ == '__main__':
    # Example usage
    city = 'United States'
    column1 = 'SalesTotal'
    column2 = 'MORTGAGE30US'
    plot_bar_and_line(city, column1, column2)