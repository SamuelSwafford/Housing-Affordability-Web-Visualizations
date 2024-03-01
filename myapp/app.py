import pandas as pd
from flask import Flask, render_template, request, send_from_directory
from myapp.heatmap import plot_housing_affordability
from myapp.five_city_line_plot import plot_affordability_vs_time
from myapp.bar_and_line_plot import plot_bar_and_line

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    # Read the CSV file
    df = pd.read_csv('resources/data_interpolated.csv')

    # Extract the unique city-state combinations
    cities = df[['CityName', 'StateName']].drop_duplicates()
    cities['CityState'] = cities['CityName'] + ', ' + cities['StateName']
    city_options = cities['CityName'].tolist()

    year = None
    plot_url = None
    line_plot_url = None
    city = None
    bar_and_line_plot_url = None
    if request.method == 'POST':
        year = request.form.get('year')
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        city3 = request.form.get('city3')
        city4 = request.form.get('city4')
        city5 = request.form.get('city5')
        city = request.form.get('city')
        plot_url = f'/plot/{year}'
        line_plot_url = f'/line_plot/{city1}/{city2}/{city3}/{city4}/{city5}'
        bar_and_line_plot_url = f'/bar_and_line_plot/{city}'
    return render_template('index.html', year=year, plot_url=plot_url, line_plot_url=line_plot_url, city=city, bar_and_line_plot_url=bar_and_line_plot_url, city_options=city_options)

@app.route('/plot/<int:year>')
def heatmap_plot(year):
    plot_housing_affordability(year)
    return send_from_directory('static', 'heatmap.png')

@app.route('/line_plot/<city1>/<city2>/<city3>/<city4>/<city5>')
def line_plot(city1, city2, city3, city4, city5):
    plot_affordability_vs_time(city1, city2, city3, city4, city5)
    return send_from_directory('static', 'five_city_line_plot.png')

@app.route('/bar_and_line_plot/<city>')
def bar_and_line_plot(city):
    # Using 'MedianSalePrice' and 'MedianListPrice' as the columns to plot
    plot_bar_and_line('resources/data_interpolated.csv', 'MedianSalePrice', 'MedianListPrice')
    return send_from_directory('static', 'bar_and_line_plot.png')

if __name__ == '__main__':
    app.run(debug=True)
