# Analyzing The Relationship Between The Housing Market, Housing Affordability, and Economic Factors
# Project Overview
A lot of US Citizens either lease or own their current home. A common myth of leasing goes as “why would I pay someone else’s mortgage by leasing while I could be paying my own mortgage.” As this is a big debate, there are a lot of economic factors (income, employment, unemployment, interest rates, credit score) that contribute to the decision of purchasing a home. In addition to the Economic Factors that a lot of individuals consider, the housing market: listing and selling price, interest rate, and affordability lead to potential buyers asking themselves a lot of Real Estate questions.

Common Real Estate Questions:
“Is this the perfect time to buy my home?"
"Will I get a low interest rate?"
"Will my purchase price be the lowest it will be in this economy?"

Therefore, in this project, we focus primarily through visualizations of the US Housing Market from datasets from 2009 to 2022 to prove housing affordability changes throughout the country and over time due to economic factors. All the information comes from datasets that are online from Zillow and National Associaltion of Realtors. 

A US Heat Map is color coded depending on Housing Affordability. If the HAI for a state is high, it’s color coded in a darker color. On the other hand, if a state is more affordable, it’s color coded in a lighter color. It can be concluded that the bigger cities are more expensive. Meaning, HAI is higher. 

Bar Chart demonstrates the relationship between interest rate and volume of sales over time.
It can be concluded that as interest rate is high, Selling Price is lower and so are sales low.
When the interest rate is low, Selling price is high and sales are high.

The Housing Affordability Calculator:
You put in information of the median income, median price, down payment, and maximum monthly payment percent from income. Once all that information is submitted, it lets the user know if they would be able to afford a house or not. 


# Industry Relevance
The housing market is closely linked to the economy as it has contributed roughly 12% of the GDP for the last five years. This makes it the current largest contributor to the economy, almost tied with manufacturing at 11%. As such, analysis of the housing market affects people at all levels from the homeowners to policy makers and real estate professionals. Housing affordability and the size of the difference between the listing price and final sales price can both illustrate the volatility of the housing market. A more stable housing market is a factor in overall economic growth as it encourages more people to become homeowners. Of course, there are more variables that influence a person’s ability to make such a large investment, such as levels of income, unemployment, and interest rates. Breaking down some of these factors for individual analysis may help understand and even predict the market

# Data Collection and Cleaning
Data for the median income and unemployment levels was sourced from the US Census API while information regarding housing was pulled from the Zillow API. A challenge that presented itself early on was choosing what metrics would represent the economy most efficiently. Cleaning the data and merging it into one dataset also proved to be difficult. The dataset contains many variables represented throughout time on a yearly basis, but many metropolitan areas did not have information for all variables at all times. Names or ways of identifying the same variable were inconsistent across data sources. For example, the names of the cities in the US Census API are written differently from how they are represented with Zillow. Those names were changed in order to create a column to merge data. A linear interpolation to the data was used to account for missing values in median sale price and median list price data sets. Number of homes sold and median income were not adjusted as they were the most complete. The mortgage rates used in this project are calculated monthly by the Federal Home Loan Mortgage Corporation, or Freddie Mac.

# Project Approach
The analysis involves statistical methods and data visualization techniques to present trends and relationships. Python libraries like Pandas, NumPy, and Matplotlib/Seaborn were employed for data manipulation and visualization. Regression analysis was used to model the relationship between housing metrics and economic factors.


# Data and Analysis
## Affordability
The first area to be explored is the state of affordable housing today across the US. The Housing Affordability Index (HAI) arose as shorthand for how likely a typical family would be able to afford the average mortgage in their area. HAI is calculated by dividing the Mean Family Income (MFI) by the Qualifying Income (QI) and multiplying that by 100. The QI is a tool used to evaluate mortgage loan applications and estimates how much income is required to afford a standard mortgage. If the QI and the MFI are equal, that suggests the typical family can afford to pay one complete mortgage (an HAI index of 100). As the MFI decreases relative to the QI, a family would only be able to afford to partially pay the mortgage. The lower this number is, the less affordable a market is considered (an HAI of < 100). Conversely, an MFI greater than QI suggests that a single family could afford to pay for their mortgage and then some, implying a healthy economy (an HAI > 100). The chart below is a graphic representation of the HAI in the US in 2022.

![Average Housing Affordability by State in 2022](https://github.com/Ishicka/The-Seven/assets/102836930/b4ddc915-ba6a-4799-8065-84c3004a6cea)

The following chart shows the HAI in New York, Los Angeles, Houston, Chicago, and Dallas from 2011 through 2022. The graph shows there was a general downwards trend in HAI throughout the country.  A spike in affordability is seen in 2012 through 2014, around the same time the government rolled out post-recession relief programs. Similarly, when the interest rate decreased due to the COVID-19 pandemic, HAI increased. This graph also illustrates that the HAI of New York and Los Angeles remains low and relatively consistent while Chicago, Dallas, and Houston tend to be relatively high, indicating that a high demand for housing may inversely correlate with the HAI.

![Housing Affordability Index Over Time for Top 5 Cities by Population](https://github.com/Ishicka/The-Seven/assets/102836930/dcf310ca-ba92-46d6-8988-2d5b1488c882)

The next visualization shows a linear regression of the number of homes sold and HAI across all cities and times in the data set. There appears to be a slight inverse relationship between population and HAI, but the correlation is weak (R^2 value is .06). From this it is assumed that there is a weak relationship between HAI and the number of homes sold, which represents the overall state of the market. Therefore, HAI is not an accurate predictor of market activity.

![Linear Regression of Housing Affordability Index vs Total Sales](https://github.com/Ishicka/The-Seven/assets/102836930/0c905f88-1542-428a-8f77-f0c1a7f0bcc0)

## Median List Price and Median Sales Price
When a house is put on the market, the price it is initially listed as and its final selling price are often different. These are referred to as the Median List Price (MLP) and Median Sales Price (MSP) when discussing the housing market of a particular area. When there is a trend of homes selling below asking price, it can be assumed that they are in a “Buyer’s Market,” meaning the supply of homes outweighs the demand. A “Seller’s Market” is the reverse, where there are not enough homes to meet demand and buyers must compete over the same properties.
Analyzing the Housing  market using median list price and median sale price involves exploring various aspects of the data. Using the classic supply-and-demand model, demand refers to the MSP, as it signifies the willingness of buyers to pay for housing. Supply corresponds to the MLP as it reflects the availability of housing stock in the U.S. market. In a seller's market with high demand and limited supply, sellers may list properties at a lower price to attract multiple offers, leading to a higher sale price. In a buyer's market with ample supply and low demand, sellers may initially list properties at higher prices, but due to the competitive nature of the market, they may have to reduce prices to close a deal.

For the MLP in our dataset, the average price was $278,590.74 and the standard deviation was $174,552.93. The standard deviation measures the amount of variation or dispersion in a set of values. In this context, it indicates how spread out the Median List Prices are around the mean. For the MSP, the average price was $236,321.50 and the standard deviation of the dataset was $141,586.75. The standard deviation is lower in both variables, which suggests less variability in the data and more values similar to the mean. Furthermore, the interquartile range (IQR) method was employed to detect outliers in the dataset. For each feature in the dataset, the IQR was calculated separately, thus allowing the lower and upper bounds of the outliers for each feature to be determined. Based on the determination the outliers were kept in the dataset because it provides valuable insights.

![Boxplot Outliers_plot](https://github.com/Ishicka/The-Seven/assets/148410176/5383b42c-c602-4d23-adb3-305ac12d3d80)

Box plots visually represent the distribution of data and identify outliers. Outliers are the points that fall beyond the "whiskers" of the box plot. Based on the context of our study, the nature of the data, and the goals of your analysis keeping the outliers is beneficial as they essential for understanding the phenomena being studied. A sample of the outlier was reviewed and it was concluded that while some regions have higher prices (e.g. California) that appear as outliers compared to the national data, they are consistent within their region. Therefore, they still add value to the analysis and were concluded in the dataset.

The overlaid plot (see below) shows the distributions of the median sale price (in blue) and the median list price (in orange) within the same graph. This visualization allows for a direct comparison between the two distributions, highlighting similarities and differences in their frequency and range.

<img width="418" alt="Screenshot 2023-12-18 213036" src="https://github.com/Ishicka/The-Seven/assets/52751074/b1e3ffa4-f45c-443a-baa0-b4ce1ab8f6a2">

The next image shows a linear regression of MLP and MSP. Visually, it is clear there is a strong positive correlation and this is confirmed by the R^2 value of 0.79. This indicates that when the median list price of homes increases, the median sale price also tends to increase, and vice versa. When sellers perceive that the market is strong and property values are high, they may list their homes at higher prices. If buyers are willing to pay those prices, it results in higher median sale prices. Conversely, in a weaker market, sellers may be more inclined to lower their list prices, leading to lower median sale prices.

![Scatter Plot of MLP vs MSP_plot](https://github.com/Ishicka/The-Seven/assets/148410176/f7d15490-e17e-4d92-be31-4a0e1f419cfb)

The plot reviews the Median list price versus the Median sale price for California ,Texas and Kansas.  There is an upward trend in both the sales and listing price for each state being reviewed. Specifically in California the plot reflects that buyers are paying less than the Median list price hence, the time period being analyzed draws the conclusion that they are in the buyers market.Buyer's market means that the demand for houses are less than the actual supply which creates negotiation power. Kansas on the other hand shows a multiple overlaps in 2021 and 2022 reflecting a possible shift in the market from buyers to sellers’ market.
 
![Median Sales Prices_plot](https://github.com/Ishicka/The-Seven/assets/148410176/a4377d01-bbd4-46b4-b00c-723d08328f1f)

## Economic Factors
The initial analysis suggests a limited correlation between HAI and the housing market trends. Further, we will examine the correlation with home sales volume. Housing prices, as we know, are influenced by a plethora of economic indicators, including inflation, employment rates, GDP growth, consumer confidence, and notably, interest rates. The below graphic displays the total home sales in the U.S. juxtaposed with national mortgage interest rates over time. This graph suggests an inverse relationship between these two factors. The impact of interest rates on housing prices is particularly nuanced. While initially lower interest rates may stimulate demand and increase prices, excessively low rates can lead to economic instability, subsequently affecting housing prices in unexpected ways. An investigation into government policies and economic trends, beginning with the 2008 Housing Bubble, can illustrate this.

![image](https://github.com/Ishicka/The-Seven/assets/148410176/bce3d5d4-8935-48ef-b77e-52f651b2bd84)

During this period, high home prices, speculative buying, and risky lending practices led to a dramatic market downturn and a significant drop in property values. Following the crisis, the 2009-2012 Post-Recession Recovery phase witnessed efforts by the federal government to stabilize the market. Initiatives like the Home Affordable Modification Program (HAMP) and the First-Time Homebuyer Credit were introduced. The subsequent Recovery and Growth phase (2013-2019) saw the housing market benefit from lower interest rates, job market improvements, and growing consumer confidence, especially in metropolitan areas.
The COVID-19 pandemic initially brought uncertainty to the housing market, with some areas experiencing a slowdown. However, the shift towards remote work and record-low mortgage rates eventually led to increased demand for suburban and rural properties, driving up home buying activity. Currently, the market is experiencing a significant downturn in home sales, a trend not seen in the past decade, attributed to high interest rates and factors like inflation and economic conditions.

The next chart presents a scatter plot comparing average MSP with mortgage rates, revealing a slight positive correlation (R^2 value of 0.01). This finding reinforces the notion that while these factors are interrelated, they do not reliably predict each other. It underscores the complexity of the housing market, influenced by a multitude of variables, including those broader economic indicators mentioned earlier.

![Linear Regression of Average Median Sale Price vs Mortgage Interest Rate](https://github.com/Ishicka/The-Seven/assets/102836930/14c91ec4-7beb-4c6c-a9c8-f1cc717594d3)


# Issues & Findings
In summary, the housing market is unique due to its cyclical nature, local variations, sensitivity to interest rates, and long-term investment characteristics. While it is influenced by economic factors, its behavior can be somewhat insulated, and the market may lag behind or follow its own trajectory compared to other sectors of the economy. The interconnectedness of economic indicators and demographic trends makes predicting the housing market's movements a complex task.  From this, it is concluded that the overall relationship between the housing market, the HAI, and the economy likely has a nonlinear correlation.
Nonlinearity implies that the relationship between housing prices and economic indicators is not proportional or straightforward. Changes in economic indicators may not result in linear changes in housing prices. Instead, the connection may be characterized by curves, thresholds, or other non-linear patterns. Interest rates, for example, can have a nonlinear impact on housing prices. Initially, lower interest rates may stimulate demand and increase prices, but excessively low rates may lead to economic instability, affecting housing prices in unexpected ways. Behavioral economics also plays a role. Buyer sentiment, perceptions of the market, and speculative behavior can introduce nonlinearities into the housing price dynamics.
