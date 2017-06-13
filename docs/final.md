---
layout: default
title:  Final Report
---

## Video

[![Description of the Video](https://img.youtube.com/vi/FI3aW0RabBg/0.jpg)](https://www.youtube.com/watch?v=FI3aW0RabBg)

## Project Summary

## Approaches
<h4>Environment</h4>

Environent plays an important role in our project since out agent relies heavily on the objects' names and their coordinates to defien where to go on the maze based on the shortest paths algorithms.  When building the environment for the agent to interact, there are 2 states that we have come across.

Status report state:
- As we showed that in in the status report state, we can only have the maze (with biggger size added).

Final state: 
In the final state, we took some office hours with Professor to figure out how to add more items on the maze so that the agent can try its actions/movements:

<ul><b>These materials have been used in this project to create the environment and all items, blocks, and entities:</b>
  <li>Tutorial 5</li>
  <li>craft_work.py</li>
  <li>Homework assignments: 1 and 2</li>
  <li>Malmo xml schemas via this link https://github.com/Microsoft/malmo/blob/master/Schemas/Types.xsd</li>
</ul>

As a initial plan, we need an environemnt with maze with air as gaps (to apply the finding shortest paths), and all other items added onto that same maze.  On the move to the final state, we did the following steps:

Build up the environment with various types of objects:

Built up a maze with size of 80x80, with gap, walls surrounded
Code:
<img src="http://farm5.staticflickr.com/4262/35079539232_e6a313a361_b.jpg">
<br>
<img src="http://farm5.staticflickr.com/4238/35205019196_d29a17defe_b.jpg">


<br>Added more bock types, such as stone, brown mushroon block, water block
<img src="http://farm5.staticflickr.com/4244/35115539441_db38d744a6_b.jpg">
<br>
<img src="http://farm5.staticflickr.com/4227/35205250156_2b1254454c_b.jpg">

<br>Since house is not a typical block, item, or entity in the MineCraft game, we have to manually draw it on the maze.  There are 2 parts of the house that we built separately: roof and walls.  The final house that we added on the maze shown as below:

<br><img src="http://farm5.staticflickr.com/4247/35157519921_fcd372813f_b.jpg">
<br>
<img src="http://farm5.staticflickr.com/4275/35121143702_7d4d37fa24_b.jpg">

We also added many other types of items and entities onto the maze:
<img src="http://farm5.staticflickr.com/4277/34900234660_eea9cdcee3_b.jpg">





## Evaluation


## References

Minecraft Wiki: 
http://minecraft.gamepedia.com/Coordinates

Xml schema for MineCraft's items:
https://github.com/Microsoft/malmo/blob/master/Schemas/Types.xsd

Minecraft XML Schema Documentation:
http://microsoft.github.io/malmo/0.16.0/Schemas/MissionHandlers.html#element_ObservationFromRay



