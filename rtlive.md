---
layout: default
title: 'Webpage Status Update'
plot: 'plotRt'
dataset: 'rt'
lastUpdated: 'August 15, 2020'
---


The webpage is no longer being supported and the data is not longer up to date. [CVStats](https://cvstats.net/) provides updated information about the current state of the pandemic.

## Reproduction Rate

State-by-state effective reproduction rates for Covid-19 is provided by the bar graph below. The data is updated daily from [Rt.Live](https://rt.live/). The model for calculating Rt was made and is updated by Kevin Systrom and Thomas Vledeck.

The effective reproduction rate (Rt) is a metric used by epidemiologists to measure the transmission potential of a disease. The metric indicates the average number of people infected by an infectious person, also known as the average number of secondary transmissions. While the proper terms may sound complex, the theory is pretty simple: an Rt value greater than one indicates that each person on average transmits to more than one other person, and the virus will spread quickly. An Rt value less than one, on the other hand, indicates that each person on average transmits to less than one other person, meaning the virus will stop spreading.

Confidence intervals are included in visual graphic and data table, but not in the accelerated multimodal graph. Confidence intervals indicate the range of values that have a certain likelihood of containing the true value. For example, the model is 80% sure the true Rt value lies within the 80% confidence interval window. 

## How to Explore This Graph With SAS
Set the Speech setting (Keyboard Shortcut C) to Verbose. Set Navigation (Keyboard Shortcut V) to Explore mode. Use the left/right arrow keys to hear the values for each state ordered in ascending order. Pay close attention to states with a high Rt.

{% include graphInstructions.html %}

{% include plotRt.html %}

{% include questionform.html %}

{% include tableData.html %}

80% confidence interval is indicated by columns titled "lower_80" and "upper_80." 
