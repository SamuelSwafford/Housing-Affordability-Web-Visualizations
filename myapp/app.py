from flask import Flask, render_template, request, send_from_directory
from myapp.heatmap import plot_housing_affordability
from myapp.five_city_line_plot import plot_affordability_vs_time

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Renders the home page of the web application.

    If the request method is POST, retrieves the selected year and cities from the form data.
    Constructs the URLs for the plot and line plot based on the selected year and cities.
    Passes the year, plot URL, and line plot URL as variables to the index.html template.
    """
    year = None
    plot_url = None
    line_plot_url = None
    if request.method == 'POST':
        year = request.form.get('year')
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        city3 = request.form.get('city3')
        city4 = request.form.get('city4')
        city5 = request.form.get('city5')
        plot_url = f'/plot/{year}'
        line_plot_url = f'/line_plot/{city1}/{city2}/{city3}/{city4}/{city5}'
    return render_template('index.html', year=year, plot_url=plot_url, line_plot_url=line_plot_url)

@app.route('/plot/<int:year>')
def plot(year):
    plot_housing_affordability(year)
    return send_from_directory('static', 'heatmap.png')

@app.route('/line_plot/<city1>/<city2>/<city3>/<city4>/<city5>')
def line_plot(city1, city2, city3, city4, city5):
    plot_affordability_vs_time(city1, city2, city3, city4, city5)
    return send_from_directory('static', 'five_city_line_plot.png')

if __name__ == '__main__':
    app.run(debug=True)