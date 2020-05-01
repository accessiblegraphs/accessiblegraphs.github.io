---
layout: default
title: 'Rt: Effective Reproduction Rates'
plot: 'plotRt'
dataset: 'rt'
---

State-by-state effective reproduction rates for Covid-19 is provided by the bar graph below. The data is updated daily from [Rt.Live](https://rt.live/). The model for calculating Rt was made and is updated by Kevin Systrom and Thomas Vledeck.

The effective reproduction rate (Rt) is a metric used by epidemiologists to measure the transmission potential of a disease. The metric indicates the average number of people infected by an infectious person, also known as the average number of secondary transmissions. While the proper terms may sound complex, the theory is pretty simple: an Rt value greater than one indicates that each person on average transmits to more than one other person, and the virus will spread quickly. An Rt value less than one, on the other hand, indicates that each person on average transmits to less than one other person, meaning the virus will stop spreading.

{% include graphInstructions.html %}

{% include plotRt.html %}

{% include form.html %}

{% include tableData.html %}
