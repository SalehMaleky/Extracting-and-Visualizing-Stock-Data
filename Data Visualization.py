!pip install yfinance==0.1.67
!mamba install bs4==4.10.0 -y
!pip install nbformat==4.2.0
#apt-get install python-lxml
#easy_install lxml
#pip install lxml
!pip install lxml
!pip install parser-libraries
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
tsla = yf.Ticker("TSLA")
tesla_data = tsla.history(period = "max")
tesla_data.reset_index(inplace = True)
tesla_data.head()
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
# Step 4 Use a BeautifulSoup method for extracting data
# Step 4 Use a BeautifulSoup method for extracting data
beautiful_soup = BeautifulSoup(html_data, )
for row in beautiful_soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    data = {'Date': date, 'Revenue': revenue}
    tesla_revenue = tesla_revenue.append({"Date":data, "Revenue":revenue}, ignore_index = True)
    print(tesla_revenue)
#tesla_soup = BeautifulSoup(html_data, "html5lib")
tesla_soup = BeautifulSoup(html_data, "html.parser")
tesla_revenue = pd.DataFrame(columns=["Data", "Revenue"])
print(tesla_revenue)
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.tail()
#print(tesla_revenue.tail(5))
import pandas as pd

# Assuming the current DataFrame is df
df = pd.DataFrame({
    'Date': ['2013', '2012', '2011', '2010', '2009'],
    'Revenue': ['$2,013', '$413', '$204', '$117', '$112'],
    'ExtraColumn': [2013, 413, 204, 117, 112]  # This represents your current extra column
})

# Create a new DataFrame with just 'Date' and 'Revenue' columns
new_df = df[['Date', 'Revenue']]

# Print the new DataFrame
print(new_df)
gme=yf.Ticker("GME")
gme_data=gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
#print(html_data)
beautiful_soup = BeautifulSoup(html_data,)
gem_revenue = pd.DataFrame(columns = ["Data", "Revenue"])
for row in beautiful_soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    data = {'Date': date, 'Revenue': revenue}
    gem_revenue = gem_revenue.append({"Date":data, "Revenue":revenue}, ignore_index = True)
print(gem_revenue)
gem_revenue ["Revenue"] = gem_revenue ['Revenue'].str.replace(',|\$',"")
gem_revenue.dropna(inplace=True)
gem_revenue = gem_revenue[tesla_revenue['Revenue'] != ""]
gem_revenue.tail(6)
# Assuming df is your DataFrame
df = pd.DataFrame({
    'Date': [
        {'Date': '2013', 'Revenue': '$2,013'},
        {'Date': '2012', 'Revenue': '$413'},
        {'Date': '2011', 'Revenue': '$204'},
        {'Date': '2010', 'Revenue': '$117'},
        {'Date': '2009', 'Revenue': '$112'}
    ],
    'Revenue': [2013, 413, 204, 117, 112]
})

# Convert the 'Date' dictionaries into a DataFrame
date_revenue_df = df['Date'].apply(pd.Series)

# Display the first 5 rows
print(date_revenue_df.head(5))
!pip install pandas plotly
def make_graph(tesla_data, tesla_revenue, company_name):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=0.3)
    stock_data_specific = tesla_data[tesla_data.Date <= '2021-06-14']
    revenue_data_specific = tesla_revenue[revenue_data.Date <= '2021-06-14']
    
    fig.add_trace(
        go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), 
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), 
        row=2, col=1
    )
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False, height=900, title=company_name, xaxis_rangeslider_visible=True)
    fig.show()
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(tesla_data, tesla_revenue, company_name):
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, 
        subplot_titles=("Historical Share Price", "Historical Revenue"), 
        vertical_spacing=0.3
    )
    
    stock_data_specific = tesla_data[tesla_data['Date'] <= '2021-06-14']
    revenue_data_specific = tesla_revenue[tesla_revenue['Date'] <= '2021-06-14']
    
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data_specific['Date'], infer_datetime_format=True), 
            y=stock_data_specific['Close'].astype("float"), 
            name="Share Price"
        ), 
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(revenue_data_specific['Date'], infer_datetime_format=True), 
            y=revenue_data_specific['Revenue'].astype("float"), 
            name="Revenue"
        ), 
        row=2, col=1
    )
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(
        showlegend=False, 
        height=900, 
        title=company_name, 
        xaxis_rangeslider_visible=True
    )
    
    fig.show()

# Example data, replace this with your actual data
tesla_data = pd.DataFrame({
    'Date': ['2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13', '2021-06-14'],
    'Close': [600, 610, 620, 630, 640]
})

tesla_revenue = pd.DataFrame({
    'Date': ['2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13', '2021-06-14'],
    'Revenue': [10, 12, 14, 16, 18]
})

make_graph(tesla_data, tesla_revenue, 'Tesla')
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define the make_graph function
def make_graph(stock_data, revenue_data, company_name):
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, 
        subplot_titles=("Historical Share Price", "Historical Revenue"), 
        vertical_spacing=0.3
    )
    
    fig.add_trace(
        go.Scatter(
            x=stock_data['Date'], 
            y=stock_data['Close'].astype("float"), 
            name="Share Price"
        ), 
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=revenue_data['Date'], 
            y=revenue_data['Revenue'].astype("float"), 
            name="Revenue"
        ), 
        row=2, col=1
    )
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(
        showlegend=False, 
        height=900, 
        title=company_name, 
        xaxis_rangeslider_visible=True
    )
    
    fig.show()

# Example GameStop stock data
gme_data = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', periods=6, freq='M'),
    'Close': [17.25, 18.84, 21.34, 25.15, 27.89, 24.58]
})

# Example GameStop revenue data
gme_revenue = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', periods=6, freq='Q'),
    'Revenue': [150, 200, 250, 300, 350, 400]
})

# Convert Date columns to datetime
gme_data['Date'] = pd.to_datetime(gme_data['Date'])
gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])

# Filter data up to '2021-06-14'
end_date = '2021-06-14'
stock_data_specific = gme_data[gme_data['Date'] <= end_date]
revenue_data_specific = gme_revenue[gme_revenue['Date'] <= end_date]

# Use the make_graph function to plot the GameStop data
make_graph(stock_data_specific, revenue_data_specific, 'GameStop')