import pandas as pd
import matplotlib
# Ensure matplotlib does not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_affordability_vs_time(city1, city2, city3, city4, city5):
    # Load your data
    df = pd.read_csv('Resources/data_interpolated.csv')

    # Filter data for the selected cities
    df_filtered = df[df['City'].isin([city1, city2, city3, city4, city5])]

    # Plot data
    for city in [city1, city2, city3, city4, city5]:
        city_data = df_filtered[df_filtered['City'] == city]
        plt.plot(city_data['Year'], city_data['Affordability'], label=city)

    plt.xlabel('Year')
    plt.ylabel('Affordability')
    plt.title('Affordability vs Time')
    plt.legend()
    plt.savefig('static/five_city_line_plot.png')
    plt.close(fig)

if __name__ == '__main__':
    plot_affordability_vs_time('City1', 'City2', 'City3', 'City4', 'City5')