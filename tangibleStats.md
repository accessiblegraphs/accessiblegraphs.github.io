---
layout: default
---

<header style="background-color: #2C716F; padding: 0px; color: white; text-align: center;"> 
<h1> Tangible Stats: Embodied and Multimodal Platform for Teaching Data and Statistics to Blind and Low-Vision Students </h1> 
</header>
Danyang Fan (1), Gene SH Kim (1), Olivia Tomassetti( 1), Shloke N Patel (1), Victor R Lee (1), Sile O’Modhrain (2), Sean Follmer (1)

1. Stanford University
2. The University of Michigan

<header style="background-color: #2C716F; padding: 0px; color: white; text-align: center;"> 
<h2> 1 Motivation </h2> 
</header>

**Interactive** data learning tools provide **explorable** ways for students to **build intuition** for **data**, **data representations**, and **statistical measures**. However, these tools are **visually reliant** and are often **not accessible** for blind and low-vision (BLV) students. In this work, we explore methods to better support **non-visual learning** of data and statistics.

<header style="background-color: #2C716F; padding: 0px; color: white; text-align: center;"> 
<h2> 2 Guiding Principles </h2> 
</header>

Our team of blind and sighted students, educators, and researchers chose to emphasize four **guiding principles** to inform the design of a statistics learning platform.

We then ran a focus group with four experienced teachers of visually impaired students to gather **additional insights** about these principles.

* Principle 1: Encourage Active Exploration and Play
    * Focus group insight: BLV students need opportunities to explore and figure things out themselves.

* Principle 2: Emphasize Intuition-Building
    * Focus group insight: Concrete examples and familiar analogies help students learn abstract concepts.
    * Focus group insight: Feedback assists students in internalizing causal relationships.

* Principle 3: Support Customization
    * Focus group insight: Teachers often tailor materials to meet the individual needs of students.
    * Focus group insight: New learning tools often need to be integrated into existing curricula.

* Principle 4: Provide Non-Visual Access
    * Focus group insight: …while also enabling access for sighted students to promote collaborative and inclusive learning.

<header style="background-color: #2C716F; padding: 0px; color: white; text-align: center;"> 
<h2> 3 Learning Platform </h2> 
</header>

<img src="{{site.baseurl}}/images/TangibleStatsPoster.png" class="img-responsive" alt="A labeled diagram highlighting features of the statistical learning platform. The platform comprises white rectangular tokens arranged on a tilting board to form a histogram. A computer monitor behind the platform displays the corresponding data visualization. The diagram highlights five key features: 1) Construct Data Physicalizations:  A hand is depicted adding tokens to the physicalization, illustrating learners' capability to construct and manipulate data representations interactively. 2) Cue into Important Regions through Vibrations: Another hand is shown placed over stacks of tokens with vibration icons, indicating the platform's capacity to deliver vibrotactile feedback to users. 3) Find the mean through touch: A hand is observed adjusting a white slider to the center-of-balance of the board, symbolizing how the platform utilizes this mechanism to help students develop an understanding of statistical mean intuitively. 4) Query Data and Statistical Values: A finger presses on a stack of tokens, demonstrating students' ability to query information about specific segments of the physicalization. 5) Customize Feedback:  The monitor also displays a series of toggles that educators can use to customize and scaffold the feedback provided to learners during their interaction with the platform.
Text labels on the diagram describe these features and are listed as bullet points below the figure."> 

* **Construct Data Physicalizations:** Students construct and manipulate date physicalizations by stacking physical tokens, which are detected by the platform.
* **Highlight Specific Regions through Vibrations:** Educators can customize vibration feedback to draw attention to different regions of the physicalization.
* **Find the Mean Through Touch:** Students locate the mean by sliding an emulated fulcrum to the geometric center of balance, which levels the tilt of the physicalization.
* **Query Data and Statistical Values:** Students retrieve data and statistical information by pressing on specific regions of the representation and listening to the system’s response.
* **Customize Feedback:** Through a web app, educators can toggle different combinations of audio and haptic feedback to accommodate and scaffold a variety of learning activities. 

<header style="background-color: #2C716F; padding: 0px; color: white; text-align: center;"> 
<h2> 4 Exploring Statistics Using Embodied Analogies </h2> 
</header>

We explore the use of embodied analogies, which draw parallels between bodily experiences and abstract concepts, to help promote intuition of statistical measures.

<header style="color: #2C716F; text-align: center;"> 
<h3>4.1 Embodied Mean</h3>
</header>
The platform supports the analogy of center-of-balance to assist learners in developing intuition for statistical mean, illustrated through the following three figures:

<img src="{{site.baseurl}}/images/TStats1.png" width = 500 class="img-responsive" alt="The first image in a sequence of three images showing the use of center-of-balance to help students gain intuition for statistical mean. A set of tokens form a left-skewed distribution on the statistical platform. A white slider is positioned at the center-of-balance which levels the board. A hand is about to add two tokens to the very left of the distribution."> 
Figure 1: The physicalization is level when the emulated fulcrum is positioned at the statistical mean, which is the geometric center of balance.

<img src="{{site.baseurl}}/images/TStats2.png" width = 500 class="img-responsive" alt="The second image in a sequence of three images showing the use of center-of-balance to help students gain intuition for statistical mean. The newly added tokens cause the board and physicalization to tilt left."> 
Figure 2: As students modify the data, they feel the impact of these modifications reflected in the board’s tilt toward the updated mean.

<img src="{{site.baseurl}}/images/TStats3.png" width = 500 class="img-responsive" alt="The third image in a sequence of three images showing the use of center-of-balance to help students gain intuition for statistical mean. A hand moves the white slider to the new center-of-balance, which re-levels the board."> 
Figure 3: The distance students need to adjust the fulcrum to re-balance the mean physically demonstrates the sensitivity of the mean to the modifications.

<header style="color: #2C716F; text-align: center;"> 
<h3>4.2 Embodied Median</h3>
</header>

The platform also supports the interaction of exploring percentiles through feeling symmetry across the median, illustrated through the following figure:

<img src="{{site.baseurl}}/images/TStats4.png" width = 500 class="img-responsive" alt="A set of tokens form a left-skewed distribution on the statistical platform. The stack containing the median value is labeled. When students press on a stack of values on one side of the median, they feel symmetric stacks vibrating on the other side of the median. The figure uses different colors to highlight the correspondence between different stacks of the physicalization, and how they converge to the stack containing the median."> 
Figure 4: Students can press and hold token stacks to hear their percentiles spoken and feel vibrations from symmetric stacks mirrored across the median. Students can narrow in on the median by feeling vibrations converge using an outside-in approach.

You can learn more about our study through our paper titled: Tangible Stats: Embodied and Multimodal Platform for Teaching Data and Statistics to Blind and Low-Vision Students <a href="/Papers/Fan2024TangibleStats.pdf" target="_target"> here.
 <!-- </a> or accessed [on the web](https://dl.acm.org/doi/10.1145/3557899). -->










