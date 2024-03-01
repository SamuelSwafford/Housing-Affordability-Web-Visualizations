import pandas as pd
import seaborn as sns
import matplotlib
# Ensure matplotlib does not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def plot_bar_and_line(city, column1, column2):
    """
    Function to plot given data for a specific city with one column represented as a bar plot and the other as a line plot.
    
    Parameters:
    - city: Name of the city to filter the data.
    - column1: Column name for the bar plot.
    - column2: Column name for the line plot.
    """
    # Load the data
    file_path = 'resources/data_interpolated.csv'
    data = pd.read_csv(file_path)
    # Filter data for the specified city
    city_data = data[data['CityName'].str.lower() == city.lower()].groupby('Year').agg({column1: 'sum', column2: 'mean'}).dropna()

    # Set the Seaborn style
    sns.set(style="whitegrid")

    # Create the figure and a single subplot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar plot for the first specified column
    sns.barplot(x=city_data.index, y=city_data[column1], color='b', alpha=0.6, ax=ax1, label=column1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel(column1, color='b')
    ax1.tick_params(axis='y', colors='b')

    # Adjust y-axis to avoid exponential notation
    ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # Create a secondary y-axis for the second specified column
    ax2 = ax1.twinx()

    # Line plot for the second specified column
    ax2.plot(city_data.index, city_data[column2], color='r', label=column2)
    ax2.set_ylabel(column2, color='r')
    ax2.tick_params('y', colors='r')

    # Title and legend
    fig.suptitle(f'{column1} and {column2} in {city.title()} Over Years')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.savefig('static/bar_and_line_plot.png')  # Save the plot to the static directory
    plt.close()





if __name__ == '__main__':
    # Example usage of the function
    plot_bar_and_line("United States", "SalesTotal", "MORTGAGE30US")