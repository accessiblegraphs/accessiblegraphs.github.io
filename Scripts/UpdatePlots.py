# Scrapes and updates relevant web-data into accessiblegraphs website
# Requires chromdriver installed in usr/local/bin: https://chromedriver.chromium.org/downloads
# Dan F and Alexa S
# April 23, 2020

# Installs need-to-be installed packages
import PackageSetup
PackageSetup.main()

# Import relevant libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import re

# Module variables
CDCTestData = []

# configure webdriver
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def main():
    
    scrapeCDC()
    plotCDC()
    modifyCDC()

def modifyCDC():
    
    # make instance of Beautiful soup class
    soup = BeautifulSoup(open("../_includes/plotCDCdata_test.html"), features='html.parser')
    
    # Update values in graphics accelerator
    target = soup.find_all(text=re.compile("valuesCount"))
    
    # values to update
    newValuesCount = len(CDCTestData) * 2
    newNobs = newValuesCount
    dates = [element[0] for element in CDCTestData]
    CDCLabTests = [int(element[1].split('‡')[0]) for element in CDCTestData]
    PublicLabTests = [int(element[2].split('§')[0]) for element in CDCTestData]
    newMin = min(min(CDCLabTests), min(PublicLabTests))
    newMax = max(max(CDCLabTests), max(PublicLabTests))
    newData = ''
    dataStartStr = '<ValuesList valuesCount=\"' + str(newValuesCount) + '\" >'
    dataEndStr = '</ValuesList>'
    dataWindow = dataStartStr + '.*?' + dataEndStr
    
    # Data value string
    for i in range(len(CDCLabTests)):
        newData = newData + '<V>' + str(dates[i]) + '</V><V>' + str(CDCLabTests[i]) + '</V><V>CDC Labs</V>'
        newData = newData + '<V>' + str(dates[i]) + '</V><V>' + str(PublicLabTests[i]) + '</V><V>US Public Health Labs</V>'
    

    for v in target:
        #replace valuesCount, nobs, min, max
        target_new = re.sub('valuesCount=.*? ',f'valuesCount=\"{newValuesCount}\" ',v, flags=re.DOTALL)
        target_new = re.sub('nobs=.*? ',f'nobs=\"{newNobs}\" ',target_new, flags=re.DOTALL)
        target_new = re.sub('min=.*? ',f'min=\"{newMin}\" ',target_new, flags=re.DOTALL)
        target_new = re.sub('max=.*? ',f'max=\"{newMax}\" ',target_new, flags=re.DOTALL)
        # replace data values
        target_new = re.sub('<V>.*?</V>','',target_new, flags=re.DOTALL)
        target_new = re.sub(dataWindow,dataStartStr+newData+dataEndStr,target_new, flags=re.DOTALL)
        v.replace_with(target_new)        
    
    with open("../_includes/plotCDCdata.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 
    
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
            xaxis_title = 'Date (data in gray still pending)',
            yaxis_title = 'Specimans Tested',
            font = dict(size = 20),
            height=1000,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend_orientation="h",
            legend=dict(x=-.1, y=-0.2),
            bargap=0.01, # gap between bars of adjacent location coordinates.
            bargroupgap=0, # gap between bars of the same location coordinate.
            margin=dict(r=10)
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
        
    fig.write_image("../Images_Plotly/CDCTestingPlotly.png",width=1200, height=1000, scale=2)
    
# For writing html
#    fig.write_html("../_includes/CDCTestingPlotly.html",
#        include_plotlyjs = 'cdn',
#        full_html = False,
#        default_width = '110%',
#        default_height = '100%',
#        )
    
    

if __name__ == '__main__':
    main()