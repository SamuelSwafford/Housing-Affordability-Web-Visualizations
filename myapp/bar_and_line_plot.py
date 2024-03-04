import pandas as pd
import matplotlib
# Ensure matplotlib does not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_bar_and_line(city='United States', col='MORTGAGE30US'):
    df = pd.read_csv('resources/data_interpolated.csv')
    allowed_columns = df.select_dtypes(include='number').columns.tolist()
    allowed_columns.remove('Year')
    allowed_columns.remove('SalesTotal')
    allowed_columns = set(allowed_columns)
    
    if col not in allowed_columns:
        raise ValueError(f'Invalid column "{col}". Allowed columns are {allowed_columns}')
    
    df = df[df['CityName'] == city]
    df = df[['Date', 'SalesTotal', col]]
    df[col] = df[col].bfill()
    df.dropna(subset=['SalesTotal'], inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    df = df.resample('Y').agg({'SalesTotal': 'sum', col: 'mean'})

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax2.bar(df.index.year, df['SalesTotal'], color='blue', zorder=0, alpha=.5, label='Sales Total')
    ax1.plot(df.index.year, df[col], color='red', zorder=1, label=col)

    ax1.set_xlabel('Time')
    ax1.set_ylabel(col)
    ax2.set_ylabel('Sales Total')
    plt.title(f'{col} and Sales Total Over Time for {city}')

    plt.legend()

    ax1.set_zorder(ax2.get_zorder() + 1)
    ax1.patch.set_visible(False)
    plt.savefig('static/bar_and_line_plot.svg')

    plt.close()

if __name__ == '__main__':
    # Example usage
    city = 'Chicago'
    col = 'MORTGAGE30US'  # Ensure this is a valid column name as per your dataset
    plot_bar_and_line(city, col)
