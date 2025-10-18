---
title: 'Supporting Non-Visual Data Sensemaking for Blind and Low Vision Users Using Touch and Sound'
layout: default
---

<div align="center">

<b>Danyang Fan</b> <br>
Department of Mechanical Engineering

<br><br>
 
<b>Advisor:</b> Sean Follmer <br>
<b>Committee:</b> Sile O'Modhrain, Allison Okamura, Hari Subramonyam, Chris Chafe

<br><br>

</div>

<img src="{{site.baseurl}}/images/defenseTeaser.png" class="img-responsive" alt="Multi-panel figure of project images. Top left is a tactile bar graph. Bottom left is a tilted physical platform supporting tokens that form a distribution. Top middle is a line graph of pitch over time. Bottom middle is a 3D stacked bar graph of physical tokens. Top right is a motorized fader that slides a user's finger. Bottom right is a servo motor that tilts a platform beneath a user's finger."> 

**Date:** November 3, 2025 @ 1:30pm PT    
**Location:** [Stanford Building 520, Room 121](https://maps.app.goo.gl/oH7s7iofPD3kKcrN8)  
**[Join Via Zoom](https://stanford.zoom.us/j/99615217690?pwd=jUZjz3NdLfevYH8Qh6GGFfKOjO8glV.1)**  **Passcode:** 921110  
<a href="/Invites/Dan's Thesis Defense .ics" target="_target"> **Add to Calendar** </a>  
**Download Slides:** (will be added the morning of)

Visualizations such as graphs and charts have become an essential way to communicate and reason about complex data. Yet their benefits often exclude people who are blind or have low vision (BLV). This talk explores how sound and touch can make data more accessible and meaningful for BLV individuals. I begin by examining current practices and lived experiences in accessing visualizations non-visually, highlighting both the promises and the challenges of existing approaches. I then present two new data exploration systems that leverage the unique strengths of auditory and haptic perception to enable richer and more accurate interpretations of data. Finally, through an extended co-design of interactive and multimodal data learning tools and activities, I reflect on how close collaboration with critical stakeholders can lead to systems that are not only functional but also empowering in their real-world contexts. Collectively, this work reimagines how people can experience and learn from data beyond sight to broaden participation in how we understand and communicate with data.


<!-- 
<img src="{{site.baseurl}}/images/banner.png" class="img-responsive" alt="Three examples of data visualizations to inform the public about the COVID-19 pandemic. The first is titled flatten the curve, and shows two bell-shaped distributions. One distribution is tall and narrow, indicating a large peak in cases above a dashed line that represents the healthcare capacity level. The other distribution is short and wide, indicating a small drawn-out peak in cases that stays below the healthcare capacity line. The second graph shows the reproduction rate of the virus, on the y-axis, by state, on the x-axis. The third shows the number of tests conducted by the CDC and US Public labs over time."> 

Visualizations have become an increasingly vital tool for effective communication in our data-driven era. The COVID-19 pandemic, with its case trackers and emphasis on [*flattening the curve*](https://www.pathstoliteracy.org/resource/flatten-curve-graphic-accessible-format/) has underscored the significant role visualizations play in informing critical decisions made by policymakers, businesses, and the public. However, accessible data representations have lagged behind for people who are blind or have low vision. Many of these individuals rely on [screen readers](https://www.afb.org/blindness-and-low-vision/using-technology/assistive-technology-products/screen-readers) to read and interact with information on digital devices such as computers and phones. 

# How accessible are visualizations on the web?

In our [study on the accessibility of COVID-19 visualizations on the web](https://dl.acm.org/doi/10.1145/3557899), we found the following: 

Of 76 visualizations audited from top-ranked Google Search websites on the COVID-19 pandemic:

* only **16%** were rated by expert auditors as very or extremely **accessible**, whereas 71% were rated as slightly or not at all accessible for screen readers users.
* only **15%** supported screen reader access to specific **data points**.
* only **5%** conveyed any form of **trends or patterns** to screen readers.
* only **43%** provided **accessible tabular** representations.
* only **35%** exposed supported **interactive features**, such as sorting, panning, filtering to screen readers.

Of 127 screen reader users surveyed:

* 65% reported encountering data-driven media at lease once a week.
* only **27%** of screen reader users describe that the **media they typically encounter is accessible**.
* **94%** of respondents indicate **they have concerns** accessing accurate COVID-19 data.

# What can we do to make data more accessible?

## As practitioners: 

* Consider accessibility from the beginning and use libraries that support direct screen-reader access to the data. [HighCharts](https://www.highcharts.com/docs/accessibility/accessibility-module), [SAS Graphics Accelerator](https://support.sas.com/software/products/graphics-accelerator/), [Apple Audio Graphs](https://developer.apple.com/documentation/accessibility/audio_graphs), [VoxLens](https://github.com/athersharif/voxlens), and [Chart Reader](https://github.com/microsoft/chart-reader) are several. Study participants felt less confident interpreting the information accurately when depending solely on text summaries that are others' interpretations of data.
* Review the [Chartability](https://chartability.fizz.studio/) heuristics when designing your data experience. Assess the accessibility of your data experience.
* Consider providing multiple different methods of access to support users of different screen reader configurations, experiences, and preferences. Many users in our study combined insights from multiple representations (e.g. table and alternative text) to complement information gaps and inform exploration. Providing downloadable data files allows users to explore the data through the familiarity of their own tools. 
* Screen readers present materials sequentially. Having to retain multiple quantities of information while navigating using screen readers can be mentally taxing to users. Consider screen reader experiences as stories. Provide context with specific data points and details. 
* Implement visualization experiences that are complete. Additional information, such as the source of the data, the data update time, options to download, and alternative representations should be easily accessible through each visualization experience (e.g. place these details in the same header as the visualization).
* People's prior experience and domain knowledge greatly affects their takeaways from visualizations. Consider a diverse audience with different backgrounds when introducing new visualization features. Provide instructions for how to interpret visualization content.

## As researchers: 

* Investigate methods for embracing interactive features and alternative modalities in web infrastructure that support flexible navigation, gestalt understandings, interactive feedback, expressive communication, and multiple levels of data abstraction. Many users in our study made use of their own interactive features such as find, linked lists, and multiple tabs to reduce the effort of navigation.
* Investigate ways to make connections between multiple complementary accessible representations more explicit to provide more tightly coordinated views.
* Research methods and interactions to build data literacy as screen reader users consume data visualizations on the web. For example, progressively uncovering details can can provide scaffolding for helping people better digest and understand information.
-->
<!-- ## As advocates:

* Ensure the accessibility of essential data-driven information, particularly during times of crisis.
* Advocate for people with disabilities at the start of any project and especially during times of crisis. -->

<!-- You can learn more about our study through our paper titled: The Accessibility of Data Visualizations on the Web for Screen Reader Users: Practices and Experiences During COVID-19, which can be downloaded <a href="/Papers/TheAccessibilityOfDataVisualizationsOnTheWebForScreenReaderUsers.pdf" target="_target"> here </a> or accessed [on the web](https://dl.acm.org/doi/10.1145/3557899).

## Additional Reading and Resources:

* [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/): Guidelines for web accessibility.
* [Chartability](https://chartability.fizz.studio/): Heuristics for making data experiences more accessible. 
* [Sharif et al.](https://dl.acm.org/doi/10.1145/3441852.3471202) and [Holloway et al.](https://dl.acm.org/doi/abs/10.1145/3373625.3418015?casa_token=JovnPzIEOQMAAAAA:WNb05igso9m0DXhZszIoYI6ROStfyXlGTzF9huG47QU9AtMNge8AhPN3Fc8Xfyz3jIDoQDGCaxuf5Q): Research understanding screen readers' experience with online data visualizations.
* [HighCharts](https://www.highcharts.com/blog/accessibility/), [SAS Graphics Accelerator](https://support.sas.com/software/products/graphics-accelerator/), [Apple Audio Graphs](https://developer.apple.com/documentation/accessibility/audio_graphs), [VoxLens](https://www.google.com/search?q=voxlens&oq=voxlens&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDwyBggCEEUYPNIBCDYwMzdqMWo0qAIAsAIA&sourceid=chrome&ie=UTF-8), and [Chart Reader](https://www.microsoft.com/en-us/research/publication/chart-reader-accessible-visualization-experiences-designed-with-screen-reader-users/): Products that provide more accessible screen reader experiences.

The Accessible Graphics project is a collaboration between researchers at Stanford University and the University of Michigan to better understand the state of data accessibility on the web for screen reader users during the COVID-19 pandemic.  --> 


<!--
The Accessible Graphics project is a collaboration between reseachers at Stanford University and the Uniersity of Michigan to investigate the state of data accessibility on the web for screen reader users during the COVID-19 pandemic. 

The project consists of three parts:
* A survey of 127 screen reader users regarding their experiences and preferences accessing data on the web.
* In-depth interviews and observations of 12 screen readers interacting with online data visualizations.
* An accessibility audit of 87 data visualizations from top-ranked Google searches, conducted by web accessibility specialists.

# Study Results

Below is a summary of the results included from our paper titled: <a href="/Papers/siu2021dataCovid.pdf" target="_target"> COVID-19 Highlights the Issues Facing Blind and Visually Impaired People in Accessing Data on the Web. </a>

## Survey

### Accessing data-driven information

* 94% of respondents indicate they have concerns accessing accurate COVID-19 data.
* 17% of respondents agree that data-driven media they encounter is typically accessible with their use of technology.
* Respondents ranked trends as most commonly inaccessible, followed by information about pandemic severity, day-to-day advice, and health and safety guidelines.
* Popular types of tasks respondents would like access to data-driven information for are: orientation and mobility, data-related media, education related, work related, personal tasks, and art and expression.


### Ways of accessing information

* Respondents highlight the importance of good summary descriptions, tables for drawing their own conclusions, alternative audio and tactile methods of consumption, and improved screen reader compatability.
* Respondents looked for accessibility branded COVID-19 websites (28%), learned to interpret data using sonification techniques (25%), listened to more podcasts where trends are "better described" (21%), relied on visual interpration services or relatives (15%), or looked for download access to raw tabular data (10%). 
* 92% of respondents believe that tactile methods are helpful for exploring data graphics, while 55% indicated that they were at least compentant in using tactile graphics for data tasks. 
* 87% of respondents believe that audio-methods are helpful for exploring data graphics, while 23% indicated that they were at least compentant in using audio-methods for data tasks.

## Interview and Observations

* For accessibility-driven data websites, prior experience and domain expertise greatly affected participants' takeaways.
* Participants combined insights from multiple representations (e.g. table and alternative text) to complement information gaps and inform exploration.
* When making data comparisons, having to retain multiple quantities of information while sequentially navigating through screen readers can impose high cognitive load.
* Participants made use of interactive features such as find, linked lists, and multiple tabs to reduce the navigation effort.
* Relying on other people's interpretations of data in alternative text descriptions, discrepancies in how data is presented, and unfamiliar tools can reduce users' confidence in interpreting data.

## Data Accessibility Audit

The results of this study are currently under peer review, and will be uploaded once accepted.

--!>

<!--
The Accessible Graphics project was launched to provide important up-to-date multimodal graphics. We are continuously updating the site and expanding on the library of graphics available currently related to the COVID-19 health crisis. The project currently uses [SAS Graphics Accelerator](https://support.sas.com/software/products/graphics-accelerator/index.html) which is only supported in [Google Chrome](https://www.google.com/chrome/). We have provided instruction on [how to use SAS Graphics Accelerator]({% link usingSAS.md %}).

## List of data graphics available:
* [Flatten the Curve]({% link flattenTheCurve.md %})
* [Global Evolution of Covid-19 Cases]({% link plotCases.md %})
* [Rt: Effective Reproduction Rate]({% link rtlive.md %})
* [Deaths by Race]({% link deathsByRace.md %})
* [Civilian Unemployment Rate]({% link unemployment.md %})

Have a plot you want to see but is not here? [Send us a suggestion]({% link contact.md %}). 

<br>

## Project Data Collection
We are also interested in understanding the strengths and limitations of existing technologies in providing effective alternative representations. We are gathering feedback to improve how we present the graphics and to support the design of multimodal visualization libraries. Each visualization has an option to submit questions you may have about the graphic or data. Human volunteers will be answering questions. You may opt to receive an email alert when someone has posted an answer. Last, we are also collecting more general information on multimodal data literacy and the state of media accessibility. [Visit our survey]({% link survey.md %}) to learn more or participate.

<br>

## Datasets In Use
* [Johns Hopkins CSSE database](https://github.com/CSSEGISandData/COVID-19)
* [CDC Coronavirus Cases, Data & Surveillance](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/testing-in-us.html)
* [Rt.Live](https://rt.live/)
* [U.S. Bureau of Labor Statistics](https://www.bls.gov/charts/employment-situation/civilian-unemployment-rate.htm)

-->
