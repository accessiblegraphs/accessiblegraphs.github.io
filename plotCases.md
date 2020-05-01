---
layout: default
title: 'Global Evolution of Covid-19 Cases'
dataset: 'GlobalTimeSeries'
---

The evolution of Covid-19 cases is shown for select countries in arithmetic and logarithmic graphs below. The data is updated daily with the [Johns Hopkins CSSE database](https://github.com/CSSEGISandData/COVID-19).

Arithmetic and semi-logarithmic graphs are often used to display the evolution of Covid-19 cases over time. Both graphs display the exact same data in different ways to highlight different aspects of the data. 

People are generally much more familiar with arithmetic graphs, where the x-axis and y-axis values are linearly (and equally) spaced apart. Arithmetic graphs are often used to visualize absolute changes over time. The first arithmetic graph shows how the number of confirmed Covid-19 cases (y-axis) evolve over time (x-axis) for Italy, US, and China. While scrolling through dates on the x-axis, the absolute number of cases on a day corresponds to the height of the corresponding curve on the y-axis. A straight line trending upwards indicates a constant growth of confirmed cases over time, whereas an upwards trending curve indicates an accelerating growth of confirmed cases over time. 

Semi-logarithmic graphs, instead, show y-axis values to be logarithmically spaced and are often used to visualize relative or percent changes over time. Equal distances in height correspond to equal ratios of confirmed cases in the semi-logarithmic graph. If the number of confirmed doubled each day, the graph would show a straight increasing line, and if the number of confirmed cases tripled each day, the graph would show an even steeper increasing line. In other words, the slope of the curve (change in confirmed cases over the change in time) is related to how quickly the confirmed cases multiply. 

{% include graphInstructions.html %}

{% include plotCasesLinear.html %}

{% include plotCasesLog.html %}

{% include form.html %}

{% include tableData.html %}

## Articles in the Media

* [What's a logarithmic graph and how does it help explain the spread of COVID-19?](https://www.weforum.org/agenda/2020/04/covid-19-spread-logarithmic-graph/). World Economic Forum. Sean Flemming. (2020 April 03).







