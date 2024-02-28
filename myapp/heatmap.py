import pandas as pd
import geopandas as gpd
import matplotlib
# Ensure matplotlib does not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_housing_affordability(year):
    # Load the data from the uploaded CSV file
    file_path = 'Resources/data_interpolated.csv'
    data = pd.read_csv(file_path)

    # Filter and Aggregate the Data for the specified year
    data_year = data[data['Year'] == year]
    average_hai_per_state = data_year.groupby('StateName')['HAI'].mean().reset_index()

    # Load the shapefile
    shapefile_path = "us_states_shapefile/cb_2021_us_state_20m.shp"
    us_states_map = gpd.read_file(shapefile_path)

    # Rename columns to match the housing affordability data
    us_states_map = us_states_map.rename(columns={'STUSPS': 'StateName'})

    # Merge the Data with the Map
    merged_map_data = us_states_map.merge(average_hai_per_state, on='StateName', how='left')

    # Plot the Map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged_map_data.plot(column='HAI', ax=ax, legend=True, cmap='OrRd', edgecolor='black', linewidth=0.3)
    ax.set_title(f'Average Housing Affordability by State in {year}', fontsize=15)
    plt.axis('off')

    # Save the plot directly to the static directory
    plt.savefig('static/heatmap.png')
    plt.close(fig)

# This ensures that the script can be imported and called from elsewhere without immediately executing.
if __name__ == '__main__':
    # Example usage
    plot_housing_affordability(2020)
