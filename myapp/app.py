import pandas as pd
from flask import Flask, render_template, request
import time
from myapp.heatmap import plot_housing_affordability
from myapp.five_city_line_plot import plot_affordability_vs_time
from myapp.bar_and_line_plot import plot_bar_and_line

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    # Load the data from CSV
    df = pd.read_csv('resources/data_interpolated.csv')
    cities = df[['CityName', 'StateName']].drop_duplicates()
    cities['CityState'] = cities['CityName'] + ', ' + cities['StateName']
    city_options = cities['CityName'].tolist()

    # Initialize variables to None; they may be updated based on form input
    year = None
    city1, city2, city3, city4, city5, city = (None,)*6

    if request.method == 'POST':
        # Extract form data
        year = request.form.get('year')
        print(year)
        print(type(year))
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        city3 = request.form.get('city3')
        city4 = request.form.get('city4')
        city5 = request.form.get('city5')
        city = request.form.get('city')

        # Call plotting functions to regenerate plots based on the new input
        # These functions overwrite the existing SVG files in the 'static' directory
        plot_housing_affordability(year)  # Make sure this saves to 'heatmap.svg'
        # Assuming plot_affordability_vs_time and plot_bar_and_line are updated to save to their respective .svg files
        plot_affordability_vs_time(city1, city2, city3, city4, city5)
        plot_bar_and_line(city)

    # Pass a cache buster to the template to force browsers to reload the updated images
    cache_buster = time.time()
    return render_template('index.html', cache_buster=cache_buster, city_options=city_options)

if __name__ == '__main__':
    app.run(debug=True)
