import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request, send_from_directory
from sqlalchemy import create_engine
import pandas as pd
import os
import uuid  # for generating unique filenames

app = Flask(__name__)

# Define the static folder where images will be saved
STATIC_FOLDER = "static"
app.config["STATIC_FOLDER"] = STATIC_FOLDER


# Load the data and perform cleaning
def load_and_clean_data():
    # Create engine to access PostgreSQL DB
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/data_sql")

    # Load data from DB
    data = pd.read_sql_query('SELECT * FROM "Data"', engine)

    # Clean the data
    # Drop rows with NaN values
    data.dropna(inplace=True)

    # Drop columns with duplicate values
    data = data.drop(columns=["Date", "CityName", "StateName"])

    # Convert relevant columns to numeric data type & round to whole number
    numeric_columns = [
        "Year",
        "Median Income",
        "MORTGAGE30US",
        "MedianSalePrice",
        "MedianListPrice",
        "SalesTotal",
        "Unemployment Rate",
        "Total Population",
    ]
    data[numeric_columns] = (
        data[numeric_columns].apply(pd.to_numeric, errors="coerce").round().astype(int)
    )

    # Rename columns
    data.rename(
        columns={
            "MORTGAGE30US": "Mortgage Interest Rate",
            "MedianSalePrice": "Median Sale Price",
            "MedianListPrice": "Median List Price",
            "SalesTotal": "Sales Total",
        },
        inplace=True,
    )

    # Filter by years 2009 to 2022
    data = data[(data["Year"] >= 2018) & (data["Year"] <= 2022)]

    # Drop duplicate rows
    data = data.drop_duplicates()

    return data


# Load and clean the data
data = load_and_clean_data()


# Build function to change secondary x axis displayed
def plot_with_secondary_axis(y_variable):
    # Group the filtered data by 'Year' and calculate the mean of 'SalesTotal' and the specified y_variable
    us_data = (
        data.groupby("Year")
        .agg({"Sales Total": "sum", y_variable: "mean"})
        .reset_index()
    )

    # Building sns barplot
    plt.figure(figsize=(12, 8))
    sns.barplot(
        data=us_data,
        x=us_data.index,
        y=us_data["Sales Total"],
        color="blue",
        saturation=0.75,
        fill=True,
    )
    sns.set_style("white")
    sns.color_palette("husl", 9)

    # Create a secondary y-axis
    ax2 = plt.gca().twinx()

    # Your Seaborn line plot
    sns.lineplot(x=us_data.index, y=y_variable, data=us_data, color="red", ax=ax2)

    # Set x-axis ticks and labels
    plt.xticks(ticks=us_data.index, labels=us_data["Year"])

    # Set labels and title
    plt.xlabel("Year")
    plt.ylabel("Total Home Sales in US")
    ax2.set_ylabel(y_variable)
    plt.title(f"Total Home Sales and {y_variable} in the US from 2018 to 2022")

    # Dynamically generate a unique filename
    filename = str(uuid.uuid4()) + ".png"
    filepath = os.path.join(app.config["STATIC_FOLDER"], filename)

    # Save the plot to the static folder
    plt.savefig(filepath, facecolor="white", bbox_inches="tight")

    # Return the filepath
    return filepath


# Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        y_variable = request.form["y_variable"]
        plot_path = plot_with_secondary_axis(y_variable)
        return render_template("index.html", plot_path=plot_path)
    else:
        return render_template("index.html")


# Route to serve the static image file
@app.route("/plot/<path:filename>")
def serve_plot(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)