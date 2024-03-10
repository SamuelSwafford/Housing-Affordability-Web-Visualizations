import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Prevents using any GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

def plot_affordability_vs_time(*city_states):
    with plt.style.context('fivethirtyeight'):
        data_file = 'resources/data_interpolated.csv'
        # Load the data
        data = pd.read_csv(data_file)

        # Split city and state for filtering
        cities = [city_state.split(',')[0] for city_state in city_states] # Extract city names
        
        # Filter the data for the specified cities and for non-null HAI (Housing Affordability Index) values
        filtered_data = data[data['CityName'].isin(cities) & data['HAI'].notnull()]

        # Convert Date to datetime for plotting
        filtered_data.loc[:, 'Date'] = pd.to_datetime(filtered_data['Date'])

        # Plotting with different colors for better differentiation
        colors = ['blue', 'green', 'red', 'purple', 'orange']

        plt.figure(figsize=(15, 8))
        # Use city-state labels in the plot
        for city_state, color in zip(city_states, colors):
            city = city_state.split(',')[0]  # Extract city name for filtering
            city_data = filtered_data[filtered_data['CityName'] == city]
            sns.lineplot(x='Date', y='HAI', data=city_data, label=city_state, color=color, ci=None)

        plt.title('Housing Affordability Index Over Time for ' + ', '.join(city_states))
        plt.xlabel('Year')
        plt.ylabel('Housing Affordability Index (HAI)')
        plt.legend()
        plt.grid(True)
        # Add a horizontal line at 100 to indicate the threshold for affordability
        plt.axhline(y=100, color='black', linestyle='--')
        plt.savefig('static/five_city_line_plot.svg')
        plt.close()

if __name__ == '__main__':
    # Example usage, adjust as necessary with city-state combinations for testing
    city_states = ['New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Dallas, TX', 'Houston, TX']
    plot_affordability_vs_time(*city_states)
