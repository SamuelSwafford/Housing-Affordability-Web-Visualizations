import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data_file, column1, column2):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(data_file)

    # Convert the 'time' column to datetime format
    df['time'] = pd.to_datetime(df['time'])

    # Set the 'time' column as the index
    df.set_index('time', inplace=True)

    # Plot the data
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.bar(df.index, df[column1], color='blue', alpha=0.5)
    ax2.plot(df.index, df[column2], color='red')

    # Set labels and title
    ax1.set_xlabel('Time')
    ax1.set_ylabel(column1)
    ax2.set_ylabel(column2)
    plt.title(f'{column1} and {column2} over Time')

    # Show the plot
    plt.show()

# Example usage
data_file = 'data_interpolated.csv'
column1 = 'column1_name'
column2 = 'column2_name'
plot_data(data_file, column1, column2)