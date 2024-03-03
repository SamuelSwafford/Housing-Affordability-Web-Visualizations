import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt

def plot_city_affordability(year):
    # Load the data from the uploaded CSV file
    file_path = 'resources/data_interpolated.csv'
    data = pd.read_csv(file_path)

    # Filter data for the specified year and cities
    cities = ['New York', 'Los Angeles', 'Chicago', 'Dallas', 'Houston']
    year_data = data[(data['Year'] == year) & (data['CityName'].isin(cities))]

    # Create an interactive line plot
    fig = px.line(year_data, x='Date', y='HAI', color='CityName', 
                  title=f'Housing Affordability Index in {year} for Selected Cities')

    # Save the plot directly to the static directory
    plt.savefig('static/cityHAI.png')
    plt.close(fig)