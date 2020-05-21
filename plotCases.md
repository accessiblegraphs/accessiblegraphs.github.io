---
layout: default
title: 'Global Evolution of Covid-19 Cases'
dataset: 'GlobalTimeSeries'
lastUpdated: 'May 3, 2020'
---

The number of new confirmed Covid-19 cases and total number of confirmed Covid-19 cases are in graphs below. The data is updated daily with the [Johns Hopkins CSSE database](https://github.com/CSSEGISandData/COVID-19).

The first bar graph shows the number of new daily confirmed Covid-19 cases for the US, China, Italy.

The second arithmetic graph shows how the number of confirmed Covid-19 cases (y-axis) evolve over time (x-axis) for Italy, the US, and China. People are generally much more familiar with arithmetic graphs, where the x-axis and y-axis values are linearly (and equally) spaced apart. Arithmetic graphs are often used to visualize absolute changes over time. While scrolling through dates on the x-axis, the absolute number of cases on a day corresponds to the height of the corresponding curve on the y-axis. A straight line trending upwards indicates a constant growth of confirmed cases over time, whereas an upwards curving line indicates an accelerating growth of confirmed cases over time. 

The third semi-logarithmic graph also shows how the number of confirmed Covid-19 cases (y-axis) evolve over time (x-axis) for Italy, the US, and China. Semi-logarithmic graphs are often used to visualize relative changes or percent changes over time. Equal distances in height correspond to equal ratios of confirmed cases in the semi-logarithmic graph. If the number of confirmed doubled each day, the graph would show a straight increasing line, and if the number of confirmed cases tripled each day, the graph would show an even steeper straight increasing line. In other words, the slope of the curve (change in confirmed cases over the change in time) is related to how quickly the confirmed cases multiply. 

## How to Explore This Graph With SAS
Use keyboard shortcut G to cycle between countries (US, China, Italy). Set the Speech setting (Keyboard Shortcut C) to Terse. Use Keyboard Shortcut V to cycle between Scan and Explore mode. Use the right/left arrow keys to sweep left and right along the x-axis of the graph. Use keyboard shortcut S to cycle between chord and melody. 

{% include graphInstructions.html %}

{% include plotNewCases.html %}

{% include plotCasesLinear.html %}

{% include plotCasesLog.html %}

{% include questionform.html %}

{% include tableData.html %}

## Articles in the Media

* [What's a logarithmic graph and how does it help explain the spread of COVID-19?](https://www.weforum.org/agenda/2020/04/covid-19-spread-logarithmic-graph/). World Economic Forum. Sean Flemming. (2020 April 03).







