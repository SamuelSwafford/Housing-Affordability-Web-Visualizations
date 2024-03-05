#  Housing Affordability Web Visualization 
# Industry Relevance
The housing market is closely linked to the economy as it has contributed roughly 12% of the GDP for the last five years. This makes it the current largest contributor to the economy, almost tied with manufacturing at 11%. As such, analysis of the housing market affects people at all levels from the homeowners to policy makers and real estate professionals. Housing affordability and the size of the difference between the listing price and final sales price can both illustrate the volatility of the housing market. A more stable housing market is a factor in overall economic growth as it encourages more people to become homeowners. Of course, there are more variables that influence a person’s ability to make such a large investment, such as levels of income, unemployment, and interest rates. 

# Home Affordability Index Calculator (HAI)

## Home Affordability Index (HAI):
The Home Affordability Index (HAI) is a measure used to assess whether a typical family has enough income to qualify for a mortgage loan on a typical home. It provides an indication of the affordability of housing for the average household. 

In the context of the NATIONAL ASSOCIATION OF REALTORS®:

A value of 100 means that a family with the median income has exactly enough income to qualify for a mortgage on a median-priced home.

Values above 100 suggest that a family with the median income has more than enough income to qualify for a mortgage on a median-priced home.

Values below 100 indicate that a family with the median income may find it challenging to qualify for a mortgage on a median-priced home.

 http://127.0.0.1:5000/ (link to HAI Calculator)
<img width="449" alt="Screenshot 2024-03-04 163103" src="https://github.com/SamuelSwafford/Housing-Affordability-Web-Visualizations/assets/52751074/4cf5d9c5-eab1-43d6-9a8d-531b429c9bbf">

# How the Calculator Can Be Used:
## Accessing the Calculator:
Users can access the HAI calculator through a web browser by running the Flask application provided in the script.
## Inputting Data:
The calculator presents a form with input fields for essential financial parameters, such as median family income, median home price, mortgage interest rate, down payment percentage, and max monthly payment percentage.
Entering Financial Information:
Users should input their financial information into the respective form fields. These values are crucial for calculating the HAI.
Clicking "Calculate HAI":
After entering the required information, users can click the "Calculate HAI" button.
## HAI Calculation:
The Flask application's calculate_hai function processes the user-inputted data to calculate the Home Affordability Index (HAI) and the qualifying income.
## Result Display:
The calculated HAI and qualifying income are displayed on the web page. 
## Interpreting the Results:
Users can interpret the HAI result to understand whether their income is sufficient to qualify for a mortgage on a median-priced home.
The provided interpretation gives context to the HAI value, helping users assess their housing affordability.
## Charts:
The calculator also includes two bar charts for income comparison and HAI comparison, providing visual representations of the user's financial situation.
## Making Informed Decisions:
Users can use the calculated HAI and interpretation to make informed decisions about their ability to afford a mortgage on a median-priced home.
In summary, the HAI calculator is a tool that empowers users to assess their housing affordability by considering key financial parameters. It provides valuable insights into whether a typical family with the provided income could qualify for a mortgage on a median-priced home, and the interpretation aids users in understanding the implications of the calculated HAI.


# Data and Analysis
## Affordability
The first area to be explored is the state of affordable housing today across the US. The Housing Affordability Index (HAI) arose as shorthand for how likely a typical family would be able to afford the average mortgage in their area. HAI is calculated by dividing the Mean Family Income (MFI) by the Qualifying Income (QI) and multiplying that by 100. The QI is a tool used to evaluate mortgage loan applications and estimates how much income is required to afford a standard mortgage. If the QI and the MFI are equal, that suggests the typical family can afford to pay one complete mortgage (an HAI index of 100). As the MFI decreases relative to the QI, a family would only be able to afford to partially pay the mortgage. The lower this number is, the less affordable a market is considered (an HAI of < 100). Conversely, an MFI greater than QI suggests that a single family could afford to pay for their mortgage and then some, implying a healthy economy (an HAI > 100). The chart below is a graphic representation of the HAI in the US in 2022.
<img width="603" alt="Screenshot 2024-03-04 180147" src="https://github.com/SamuelSwafford/Housing-Affordability-Web-Visualizations/assets/52751074/4292d66d-dee0-4ead-94d8-1779eec3ffdd">

The following chart shows the HAI in New York, Los Angeles, Chicago, Dallas, and Houston from 2011 through 2022. The graph shows there was a general downwards trend in HAI throughout the country.  A spike in affordability is seen in 2012 through 2014, around the same time the government rolled out post-recession relief programs. Similarly, when the interest rate decreased due to the COVID-19 pandemic, HAI increased. This graph also illustrates that the HAI of New York and Los Angeles remains low and relatively consistent while Chicago, Dallas, and Houston tend to be relatively high, indicating that a high demand for housing may inversely correlate with the HAI.
<img width="623" alt="Screenshot 2024-03-04 180125" src="https://github.com/SamuelSwafford/Housing-Affordability-Web-Visualizations/assets/52751074/12cb8da6-174d-4159-80e7-0685cb610148">

## Median List Price and Median Sales Price
When a house is put on the market, the price it is initially listed as and its final selling price are often different. These are referred to as the Median List Price (MLP) and Median Sales Price (MSP) when discussing the housing market of a particular area. When there is a trend of homes selling below asking price, it can be assumed that they are in a “Buyer’s Market,” meaning the supply of homes outweighs the demand. A “Seller’s Market” is the reverse, where there are not enough homes to meet demand and buyers must compete over the same properties.
Analyzing the Housing  market using median list price and median sale price involves exploring various aspects of the data. Using the classic supply-and-demand model, demand refers to the MSP, as it signifies the willingness of buyers to pay for housing. Supply corresponds to the MLP as it reflects the availability of housing stock in the U.S. market. In a seller's market with high demand and limited supply, sellers may list properties at a lower price to attract multiple offers, leading to a higher sale price. In a buyer's market with ample supply and low demand, sellers may initially list properties at higher prices, but due to the competitive nature of the market, they may have to reduce prices to close a deal.

## Economic Factors
The initial analysis suggests a limited correlation between HAI and the housing market trends. Further, we will examine the correlation with home sales volume. Housing prices, as we know, are influenced by a plethora of economic indicators, including inflation, employment rates, GDP growth, consumer confidence, and notably, interest rates. The below graphic displays the total home sales in the U.S. juxtaposed with national mortgage interest rates over time. This graph suggests an inverse relationship between these two factors. The impact of interest rates on housing prices is particularly nuanced. While initially lower interest rates may stimulate demand and increase prices, excessively low rates can lead to economic instability, subsequently affecting housing prices in unexpected ways. An investigation into government policies and economic trends, beginning with the 2008 Housing Bubble, can illustrate this.

<img width="627" alt="Screenshot 2024-03-04 180136" src="https://github.com/SamuelSwafford/Housing-Affordability-Web-Visualizations/assets/52751074/e62bdb7d-21cf-45ab-86fa-552c3d1d2c4f">

During this period, high home prices, speculative buying, and risky lending practices led to a dramatic market downturn and a significant drop in property values. Following the crisis, the 2009-2012 Post-Recession Recovery phase witnessed efforts by the federal government to stabilize the market. Initiatives like the Home Affordable Modification Program (HAMP) and the First-Time Homebuyer Credit were introduced. The subsequent Recovery and Growth phase (2013-2019) saw the housing market benefit from lower interest rates, job market improvements, and growing consumer confidence, especially in metropolitan areas.
The COVID-19 pandemic initially brought uncertainty to the housing market, with some areas experiencing a slowdown. However, the shift towards remote work and record-low mortgage rates eventually led to increased demand for suburban and rural properties, driving up home buying activity. Currently, the market is experiencing a significant downturn in home sales, a trend not seen in the past decade, attributed to high interest rates and factors like inflation and economic conditions.

# Issues & Findings
In summary, the housing market is unique due to its cyclical nature, local variations, sensitivity to interest rates, and long-term investment characteristics. While it is influenced by economic factors, its behavior can be somewhat insulated, and the market may lag behind or follow its own trajectory compared to other sectors of the economy. The interconnectedness of economic indicators and demographic trends makes predicting the housing market's movements a complex task.  From this, it is concluded that the overall relationship between the housing market, the HAI, and the economy likely has a nonlinear correlation.
Nonlinearity implies that the relationship between housing prices and economic indicators is not proportional or straightforward. Changes in economic indicators may not result in linear changes in housing prices. Instead, the connection may be characterized by curves, thresholds, or other non-linear patterns. Interest rates, for example, can have a nonlinear impact on housing prices. Initially, lower interest rates may stimulate demand and increase prices, but excessively low rates may lead to economic instability, affecting housing prices in unexpected ways. Behavioral economics also plays a role. Buyer sentiment, perceptions of the market, and speculative behavior can introduce nonlinearities into the housing price dynamics.

# Ethical Considerations
It's ethically wrong to make profit from data obtain from Zillow. However, we aren't making any profit. We're utilizing the data for educational porpuses and data is also available to the public from the Census. Therefore, this is ethically correct. Another ethical dilema may be telling potential buyers if they may or may not afford to purchase a house because it's rude to tell someone they can't afford a home. However, it isn't wrong because once a buyer makes a loan application, they will be told if they were approved or denied for their loan application. Concluding, this project was created to further develop our skills in developing a website and creating visualualizations for a topic that we're passionate helping others understand housing affordability. 
