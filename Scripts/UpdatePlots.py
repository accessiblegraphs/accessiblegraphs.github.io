# Scrapes and updates relevant web-data into accessiblegraphs website
# Requires chromdriver installed in usr/local/bin: https://chromedriver.chromium.org/downloads
# Dan F and Alexa S
# April 23, 2020

# Installs need-to-be installed packages

# Import relevant libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import re
import pandas as pd
import time

# Module variables
CDCTestData = []
RtData = []
JHGlobal = []

def main():
    
    scrapeCDC()
    plotCDC()
    modifyCDC()

    scrapeRt()
    plotRt()
    modifyRt()
    
    scrapeJHGlobal()
    plotJHGlobal() 
    modifyJHGlobal()
    
   

def scrapeJHGlobal():
        
    # scrapeJHGlobal()
    plotData = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    
    # filter by China, US, Italy   
    plotData = plotData[plotData['Country/Region'].isin(['US', 'Italy', 'China'])]

    # sum values of same country
    plotData = plotData.groupby('Country/Region').sum()

    # filter latitude and longitude columns
    plotData = plotData.drop(['Lat', 'Long'], axis=1)

    global JHGlobal

    # transpose data to categorize by country
    JHGlobal = plotData.transpose()
    
    # calculate logarithmic data
    JHGlobal['log10US'] = np.log10(JHGlobal['US'])
    JHGlobal['log10China'] = np.log10(JHGlobal['China'])
    JHGlobal['log10Italy'] = np.log10(JHGlobal['Italy'])  
    
    # calculate delta
    JHGlobal['New Daily US Cases'] = JHGlobal['US'] - JHGlobal['US'].shift(1)
    JHGlobal['New Daily China Cases'] = JHGlobal['China'] - JHGlobal['China'].shift(1)
    JHGlobal['New Daily Italy Cases'] = JHGlobal['Italy'] - JHGlobal['Italy'].shift(1)
    
    # make copy of dataframe with most recent date first
    JHGlobal_Rev = JHGlobal.sort_index(ascending=False)
    
    # update csv output columns
    JHGlobal_Rev['Total Confirmed Cases US'] = JHGlobal_Rev['US']
    JHGlobal_Rev['Total Confirmed Cases China'] = JHGlobal_Rev['China']
    JHGlobal_Rev['Total Confirmed Cases Italy'] = JHGlobal_Rev['Italy']
    
    # update csv
    headers = ['Total Confirmed Cases US', 'Total Confirmed Cases China', 'Total Confirmed Cases Italy',
            'New Daily US Cases', 'New Daily China Cases', 'New Daily Italy Cases']
    JHGlobal_Rev.to_csv('../Dataset/GlobalTimeSeries.csv' ,index=True, columns = headers, float_format='%.0f')
    
    # replace inf with 0
    JHGlobal = JHGlobal.replace(-np.inf,0)
    
def plotJHGlobal():

    ######################## Plot New Cases ############################

    # Plot New Cases (Bar Graph)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=JHGlobal.index,y=JHGlobal['New Daily US Cases'], name='US', 
                         marker_color='blue'))
    fig.add_trace(go.Bar(x=JHGlobal.index,y=JHGlobal['New Daily China Cases'], name='China', 
                         marker_color='red'))
    fig.add_trace(go.Bar(x=JHGlobal.index,y=JHGlobal['New Daily Italy Cases'], name='Italy', 
                         marker_color='green'))

    # Plot layout settings
    fig.update_layout(
            title='New Daily Confirmed COVID-19 Cases',
            title_x=0.5,
            xaxis_title = 'Date',
            yaxis_title = 'New Daily Confirmed COVID-19 Cases',
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
    
    # gridlines on, number format to digits
    fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor='black', tickformat = "digit")
        
    fig.write_image("../Images_Plotly/NewDailyCases.png",width=1200, height=1000, scale=2)
    
    ######################## Plot Linear Cases ############################

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=JHGlobal.index, name='China', y=JHGlobal['China'],
                             line=dict(color='red', width=4, dash='longdash')))
    fig.add_trace(go.Scatter(x=JHGlobal.index, name='Italy', y=JHGlobal['Italy'],
                             line=dict(color='green', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=JHGlobal.index, name='US', y=JHGlobal['US'], 
                             line=dict(color='blue', width=4, dash='solid')))
    
     # Plot layout settings
    fig.update_layout(
            title='Confirmed Covid-19 Cases',
            title_x=0.5,
            xaxis_title = 'Date',
            yaxis_title = 'Confirmed Covid-19 Cases',
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
    
    # grid on, number format to digits
    fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor='gray')
    
    # save to jpg
    fig.write_image("../Images_Plotly/GlobalArith.png",width=1200, height=800, scale=2) 
    
    ######################## Plot Log Cases ############################

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=JHGlobal.index, name='China', y=JHGlobal['China'],
                              line=dict(color='red', width=4, dash='longdash')))
    fig2.add_trace(go.Scatter(x=JHGlobal.index, name='Italy', y=JHGlobal['Italy'],
                              line=dict(color='green', width=4, dash='dashdot')))
    fig2.add_trace(go.Scatter(x=JHGlobal.index, name='US', y=JHGlobal['US'],
                              line=dict(color='blue', width=4, dash='solid')))
    
    # Plot layout settings
    fig2.update_layout(
            yaxis_type="log",
            title='Confirmed Covid-19 Cases',
            title_x=0.5,
            xaxis_title = 'Date',
            yaxis_title = 'Confirmed Covid-19 Cases',
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
    
    # grid on, number format to digits
    fig2.update_yaxes(showgrid = True, gridwidth = 1, gridcolor='lightgray')
    
    # save to jpg
    fig2.write_image("../Images_Plotly/GlobalLog.png",width=1200, height=800, scale=2)
    
def modifyJHGlobal():
    
    
    ######################## Modify New Cases ############################
    
    # make instance of Beautiful soup class
    soup = BeautifulSoup(open("../_includes/plotNewCases.html"), features='html.parser')
    
    # save file in archive in case something goes wrong
    with open(str("../_includes/archive/plotNewCases" + time.strftime("%Y%m%d-%H%M%S") + ".html"), 
              "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))
    
    # Update values in graphics accelerator
    target = soup.find_all(text=re.compile("valuesCount"))
    
    # values to update
    newValuesCount = JHGlobal.index.size* 3
    newNobs = newValuesCount
    newMin = min(JHGlobal['New Daily US Cases'].min(), JHGlobal['New Daily China Cases'].min(), 
                 JHGlobal['New Daily Italy Cases'].min())
    newMax = max(JHGlobal['New Daily US Cases'].max(), JHGlobal['New Daily China Cases'].max(), 
                 JHGlobal['New Daily Italy Cases'].max())
    newData = ''
    dataStartStr = '<ValuesList valuesCount=\"' + str(newValuesCount) + '\" >'
    dataEndStr = '</ValuesList>'
    dataWindow = dataStartStr + '.*?' + dataEndStr
    
    # Data value string
    for i in range(JHGlobal.index.size):
        newData = (newData + '<V>' + 
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['New Daily US Cases'].iloc[i]) + 
                   '</V><V>' + 'US' + '</V><V>' +
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['New Daily China Cases'].iloc[i]) + 
                   '</V><V>' + 'China' + '</V><V>' +
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['New Daily Italy Cases'].iloc[i]) + 
                   '</V><V>' + 'Italy' + '</V>')

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
    
    with open("../_includes/plotNewCases.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 

    ######################## Modify Linear Cases ############################
    
    soup = BeautifulSoup(open("../_includes/plotCasesLinear.html"), features='html.parser')
    
    # save file in archive in case something goes wrong
    with open(str("../_includes/archive/plotCasesLinear" + time.strftime("%Y%m%d-%H%M%S") + ".html"), 
              "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 
    
    # Update values in graphics accelerator
    target = soup.find_all(text=re.compile("valuesCount"))

    # values to update
    newValuesCount = JHGlobal.index.size* 3
    newNobs = newValuesCount
    newMin = min(JHGlobal['China'].min(), JHGlobal['Italy'].min(), JHGlobal['US'].min())
    newMax = max(JHGlobal['China'].max(), JHGlobal['Italy'].max(), JHGlobal['US'].max())
    newData = ''
    dataStartStr = '<ValuesList valuesCount=\"' + str(newValuesCount) + '\" >'
    dataEndStr = '</ValuesList>'
    dataWindow = dataStartStr + '.*?' + dataEndStr
    
    # Data value string
    for i in range(JHGlobal.index.size):
        newData = (newData + '<V>' + 
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['US'].iloc[i]) + 
                   '</V><V>' + 'US' + '</V><V>' +
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['China'].iloc[i]) + 
                   '</V><V>' + 'China' + '</V><V>' +
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['Italy'].iloc[i]) + 
                   '</V><V>' + 'Italy' + '</V>')

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
    
    with open("../_includes/plotCasesLinear.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 
    
    ######################## Modify Log Cases ############################

    soup = BeautifulSoup(open("../_includes/plotCasesLog.html"), features='html.parser')
    
    # save file in archive in case something goes wrong
    with open(str("../_includes/archive/plotCasesLog" + time.strftime("%Y%m%d-%H%M%S") + ".html"), 
              "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 
        
    # Update values in graphics accelerator
    target = soup.find_all(text=re.compile("valuesCount"))

    # values to update
    newValuesCount = JHGlobal.index.size* 3
    newNobs = newValuesCount
    newMin = min(JHGlobal['log10China'].min(), JHGlobal['log10Italy'].min(), JHGlobal['log10US'].min())
    newMax = max(JHGlobal['log10China'].max(), JHGlobal['log10Italy'].max(), JHGlobal['log10US'].max())
    newData = ''
    dataStartStr = '<ValuesList valuesCount=\"' + str(newValuesCount) + '\" >'
    dataEndStr = '</ValuesList>'
    dataWindow = dataStartStr + '.*?' + dataEndStr
    
    # Data value string
    for i in range(JHGlobal.index.size):
        newData = (newData + '<V>' + 
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['log10US'].iloc[i]) + 
                   '</V><V>' + 'log10(US)' + '</V><V>' +
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['log10China'].iloc[i]) + 
                   '</V><V>' + 'log10(China)' + '</V><V>' +
                   str(JHGlobal.index[i]) +  '</V><V>' + str(JHGlobal['log10Italy'].iloc[i]) + 
                   '</V><V>' + 'log10(Italy)' + '</V>')

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
    
    with open("../_includes/plotCasesLog.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 

def scrapeRt():
    
    global RtData
    plotData = pd.read_csv('https://d14wlfuexuxgcm.cloudfront.net/covid/rt.csv')
    
    # obtain most recent date
    mostRecentDate = plotData['date'].max()
    
    # filter by most recent date
    plotData = plotData[plotData['date'] == mostRecentDate]
    
    # update csv
    plotData.to_csv('../Dataset/rt.csv', float_format='%.2f',index=False)
    
    # sort by minimum to maximum rt values
    RtData = plotData.sort_values(by=['median'])
    
def plotRt():
    
    # plot data
    fig = go.Figure(data=go.Scatter(x=RtData['region'], y=RtData['median'], mode='markers', 
        name='50% confidence inteval shown',
            # marker colots                        
            marker=dict(size=15,color=(RtData['median'] < 1).astype('int'), 
                        colorscale=[[0, 'rgb(220, 50, 32)'], [1, 'rgb(0, 90, 181)']]),
            # error bar            
            error_y=dict(type='data', symmetric=False, 
                         array= RtData['upper_50'] - RtData['median'],
                         arrayminus= RtData['median'] -RtData['lower_50'])))
                                    
    
    # Plot layout settings
    fig.update_layout(
            title='COVID-19 Effective Reproduction Rate (R<sub>t</sub>) by State',
            title_x=0.5,
            xaxis_title = 'State',
            yaxis = dict(range = [0,2]),
            yaxis_title = 'Effective Reproduction Rate (R<sub>t</sub>)',
            font = dict(size = 24),
            height=800,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(r=0),
            legend_orientation="h",
            legend=dict(x=-.1, y=-0.2),
            showlegend=True
            )
    
    # Add gridlines
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray', 
                     showline=True, linewidth=2, linecolor='black',)
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black',
                     tickfont=dict(size=16))
    
    # Add horizontal line
    fig.add_shape(
        # Horizontal Line
        go.layout.Shape(
            type="line",
            x0=0,
            y0=1,
            x1=1,
            y1=1,
            xref='paper',
            yref='y',
            line=dict(
                color="Black",
                width=2,
                dash='dash'
            )))

    fig.write_image("../Images_Plotly/RtPlotly.png",width=1200, height=800, scale=2)
    
def modifyRt():
    
    soup = BeautifulSoup(open("../_includes/plotRt.html"), features='html.parser')
    
    # save file in archive in case something goes wrong
    with open(str("../_includes/archive/plotRt" + time.strftime("%Y%m%d-%H%M%S") + ".html"), 
              "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 
    
    # Update values in graphics accelerator
    target = soup.find_all(text=re.compile("valuesCount"))

    # values to update
    newValuesCount = RtData['region'].size
    newNobs = newValuesCount
    newMin = RtData['median'].min()
    newMax = RtData['median'].max()
    newData = ''
    dataStartStr = '<ValuesList valuesCount=\"' + str(newValuesCount) + '\" >'
    dataEndStr = '</ValuesList>'
    dataWindow = dataStartStr + '.*?' + dataEndStr
    
    # Data value string
    for i in range(RtData['region'].size):
        newData = newData + '<V>' + str(RtData['region'].iloc[i]) + '</V><V>' + str(RtData['median'].iloc[i]) + '</V>'    

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
    
    with open("../_includes/plotRt.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 
        
def scrapeCDC():
    
    # configure webdriver
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    
    # open up CDC website
    driver.get("https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/previous-testing-in-us.html")
    
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
    
    # turn array into pandas dataframe
    CDCTestDf = pd.DataFrame(data=CDCTestData, columns=["Date","CDC Lab Tests","Public Lab Tests"])
        
    # sort by most recent date first
    CDCTestDf = CDCTestDf.reindex(index=CDCTestDf.index[::-1])

    # update csv
    CDCTestDf.to_csv('../Dataset/CDC_TestData.csv',index=False)

    driver.quit()

def plotCDC():
    
    # Find first index of ‡ symbol
    #indices_pp = min([i for i, elem in enumerate(CDCTestData) if any('‡' in sublist for sublist in elem)])
    
    # Find first index of § symbol
    #indices_squig = min([i for i, elem in enumerate(CDCTestData) if any('§' in sublist for sublist in elem)])

    # Obtian array of relevant plot series
    dates = [element[0] for element in CDCTestData]
    CDCLabTests = [toInt(element[1].split('‡')[0]) for element in CDCTestData]
    PublicLabTests = [toInt(element[2].split('§')[0]) for element in CDCTestData]
    
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
#    fig.update_layout(
#        shapes=[
#            # 1st highlight during Feb 4 - Feb 6
#            dict(
#                type="rect",
#                # x-reference is assigned to the x-values
#                xref="x",
#                # y-reference is assigned to the plot paper [0,1]
#                yref="paper",
#                x0=dates[indices_squig],
#                y0=0,
#                x1=dates[len(dates)-1],
#                y1=1,
#                fillcolor="lightgray",
#                opacity=0.5,
#                layer="below",
#                line_width=0,
#        )])
    
    # gridlines on, number format to digits
    fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor='black', tickformat = "digit")
        
    fig.write_image("../Images_Plotly/CDCTestingPlotly.png",width=1200, height=1000, scale=2)
    
# For writing html
#    fig.write_html("../_includes/CDCTestingPlotly.html",
#        include_plotlyjs = 'cdn',
#        full_html = False,
#        default_width = '110%',
#        default_height = '100%',
#        )

def modifyCDC():
    
    # make instance of Beautiful soup class
    soup = BeautifulSoup(open("../_includes/plotCDCdata.html"), features='html.parser')
    
    # save file in archive in case something goes wrong
    with open(str("../_includes/archive/plotCDCdata" + time.strftime("%Y%m%d-%H%M%S") + ".html"), 
              "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))
    
    # Update values in graphics accelerator
    target = soup.find_all(text=re.compile("valuesCount"))
    
    # values to update
    newValuesCount = len(CDCTestData) * 2
    newNobs = newValuesCount
    dates = [element[0] for element in CDCTestData]
    CDCLabTests = [toInt(element[1].split('‡')[0]) for element in CDCTestData]
    PublicLabTests = [toInt(element[2].split('§')[0]) for element in CDCTestData]
    newMin = min(min(CDCLabTests), min(PublicLabTests))
    newMax = max(max(CDCLabTests), max(PublicLabTests))
    newData = ''
    dataStartStr = '<ValuesList valuesCount=\"' + str(newValuesCount) + '\" >'
    dataEndStr = '</ValuesList>'
    dataWindow = dataStartStr + '.*?' + dataEndStr
    
    # Data value string
    for i in range(len(CDCLabTests)):
        newData = newData + '<V>' + str(dates[i]) + '</V><V>' + str(PublicLabTests[i]) + '</V><V>US Public Health Labs</V>'
        newData = newData + '<V>' + str(dates[i]) + '</V><V>' + str(CDCLabTests[i]) + '</V><V>CDC Labs</V>'
    

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
    
# to hande if plotted value us empty
def toInt(n):
    try: 
        return int(n)
    except:
        return 0


if __name__ == '__main__':
    main()