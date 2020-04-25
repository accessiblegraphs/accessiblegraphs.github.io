# Scrapes and updates relevant web-data into accessiblegraphs website
# Requires chromdriver installed in usr/local/bin: https://chromedriver.chromium.org/downloads
# Dan F and Alexa S
# April 23, 2020

# Installs need-to-be installed packages
#import PackageSetup
#PackageSetup.main()

# Import relevant libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

# Module variables
CDCTestData = []

# configure webdriver
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def main():
    
    scrapeCDC()
    plotCDC()
    
    
def scrapeCDC():
    
    # open up CDC website
    driver.get("https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/testing-in-us.html")
    
    # get page source
    pageSource = driver.page_source
    
    # make instance of Beautiful soup class
    soup = BeautifulSoup(pageSource, 'html.parser')
    
    # find table in site
    table = soup.find(class_= 'table table-header-light nein-scroll')
    table = table.find('tbody')
    
    # list all td tages in table
    td_list = table.find_all('td')
    
    # scrape all values in td tags in table
    values = [pt.get_text() for pt in td_list]
    
    # store all values in CDCTestData Array
    global CDCTestData 
    CDCTestData = [values[i:i+3] for i in range(0, len(values), 3)]

    driver.quit()

def plotCDC():
    
    # Find first index of ‡ symbol
    indices_pp = min([i for i, elem in enumerate(CDCTestData) if any('‡' in sublist for sublist in elem)])
    
    # Find first index of § symbol
    indices_squig = min([i for i, elem in enumerate(CDCTestData) if any('§' in sublist for sublist in elem)])

    # Obtian array of relevant plot series
    dates = [element[0] for element in CDCTestData]
    CDCLabTests = [int(element[1].split('‡')[0]) for element in CDCTestData]
    PublicLabTests = [int(element[2].split('§')[0]) for element in CDCTestData]
    
    # Plot CDC graph
    fig = go.Figure()
    fig.add_trace(go.Bar(x=dates,y=CDCLabTests, name='CDC Labs', marker_color='rgb(220, 50, 32)'))
    fig.add_trace(go.Bar(x=dates,y=PublicLabTests, name='US Public Labs', marker_color='rgb(0, 90, 181)'))

    # Plot layout settings
    fig.update_layout(
            title='Number of Specimans Tested for SARS CoV-2 by <br>CDC labs and US Public Labs',
            title_x=0.5,
            xaxis_title = 'Date',
            yaxis_title = 'Specimans Tested',
            font = dict(size = 16),
            height=600,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend_orientation="h",
            legend=dict(x=-.1, y=-0.2),
            bargap=0.01, # gap between bars of adjacent location coordinates.
            bargroupgap=0 # gap between bars of the same location coordinate.
            )
            
    # Add shaded uncertainty region
    fig.update_layout(
        shapes=[
            # 1st highlight during Feb 4 - Feb 6
            dict(
                type="rect",
                # x-reference is assigned to the x-values
                xref="x",
                # y-reference is assigned to the plot paper [0,1]
                yref="paper",
                x0=dates[indices_squig],
                y0=0,
                x1=dates[len(dates)-1],
                y1=1,
                fillcolor="lightgray",
                opacity=0.5,
                layer="below",
                line_width=0,
        )])
    fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor='black', tickformat = "digit",)
        
    fig.write_html("../_includes/CDCTestingPlotly.html",
        include_plotlyjs = 'cdn',
        full_html = False,
        default_width = '110%',
        default_height = '100%',
        )
    
    

if __name__ == '__main__':
    main()