import pandas as pd
from flask import Flask, render_template, request
import time
from myapp.heatmap import plot_housing_affordability
from myapp.five_city_line_plot import plot_affordability_vs_time
from myapp.bar_and_line_plot import plot_bar_and_line

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    df = pd.read_csv('resources/data_interpolated.csv')
    cities = df[['CityName', 'StateName']].drop_duplicates()
    cities['CityState'] = cities['CityName'] + ', ' + cities['StateName']
    city_options = cities['CityName'].tolist()
    
    # Determine allowed columns for 'col' variable
    allowed_columns = df.select_dtypes(include='number').columns.tolist()
    allowed_columns.remove('Year')
    allowed_columns.remove('SalesTotal')
    col_options = allowed_columns  # This will be passed to the template

    # Initialize variables to None; they may be updated based on form input
    year = None
    city1, city2, city3, city4, city5, city, col = (None,)*7

    if request.method == 'POST':
        year = request.form.get('year')
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        city3 = request.form.get('city3')
        city4 = request.form.get('city4')
        city5 = request.form.get('city5')
        city = request.form.get('city')
        col = request.form.get('col')  # Retrieve the selected column for the bar and line plot

        plot_housing_affordability(year)
        plot_affordability_vs_time(city1, city2, city3, city4, city5)
        plot_bar_and_line(city, col)  # Pass both city and col to the plotting function

    cache_buster = time.time()
    return render_template('index.html', cache_buster=cache_buster, city_options=city_options, col_options=col_options)

if __name__ == '__main__':
    app.run(debug=True)
