import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Prevents using any GUI backend
import matplotlib.pyplot as plt

def plot_affordability_vs_time(*cities):
    data_file = 'resources/data_interpolated.csv'
    # Load the data
    data = pd.read_csv(data_file)

    # Filter the data for the specified cities and for non-null HAI (Housing Affordability Index) values
    filtered_data = data[data['CityName'].isin(cities) & data['HAI'].notnull()]

    # Convert Date to datetime for plotting
    filtered_data.loc[:, 'Date'] = pd.to_datetime(filtered_data['Date'])

    # Plotting with different colors for better differentiation
    colors = ['blue', 'green', 'red', 'purple', 'orange']

    plt.figure(figsize=(15, 8))

    for city, color in zip(cities, colors):
        city_data = filtered_data[filtered_data['CityName'] == city]
        plt.plot(city_data['Date'], city_data['HAI'], label=city, color=color)

    plt.title('Housing Affordability Index Over Time for Top 5 Cities by Population')
    plt.xlabel('Year')
    plt.ylabel('Housing Affordability Index (HAI)')
    plt.legend()
    plt.grid(True)
    # Add a horizontal line at 100 to indicate the threshold for affordability
    plt.axhline(y=100, color='black', linestyle='--')
    plt.savefig('static/five_city_line_plot.png')
    plt.close()

if __name__ == '__main__':
    # Example usage, adjust as necessary
    cities = ['New York', 'Los Angeles', 'Chicago', 'Dallas', 'Houston']  # Update with real city names for testing
    plot_affordability_vs_time(*cities)