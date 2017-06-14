---
layout: default
title:  Final Report
---

## Video

[![Description of the Video](https://img.youtube.com/vi/FI3aW0RabBg/0.jpg)](https://www.youtube.com/watch?v=FI3aW0RabBg)

## Project Summary

## Approaches
<h4>Environment</h4>

Environent plays an important role in our project since out agent relies heavily on the objects' names and their coordinates to defien where to go on the maze based on the shortest paths algorithms.  Understand all neccessary items in the xml and apply them to our actual project took quite a bit time for us.  When building the environment for the agent to interact, there are 2 states:

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
Qualitative:
Part of Speech Tagger vs. Deterministic Finite Automaton Machine 
Issue: Captain commando is an AI project that relies on the extraction of components in a sentence. For instance, to execute a command that is given as text by the user, our Agent has to be able to know the action that it will be performing. Maybe the action is to attack a sheep, or to find the nearest tree. To accomplish this, our agent must be able to split the sentence into words and correctly identify the verb, the adjective and the noun inside that sentence. What if the given text is not a command? As we explained in our status report our agent can distinguish between a command, question or a statement. Knowing this our agent would disregard any other forms sentences that are not commands.  Now, let’s analyze the two approaches that we have implemented for our agent to extract these three components in a sentence (Verb, Adjective, Noun).

Part of Speech Tagger
Part of speech tagger is a NLTK tool function that accepts a list of words as an input and returns a list of tuples. 
Here is an example of an execution 
<br><img src="http://farm5.staticflickr.com/4234/35168377281_6f27073853_b.jpg">

Now, POS tagger was the tool that we initially used for our agent to get the verbs, adjectives and nouns. However, we started noticing that it wasn’t very accurate when detecting the three components. 
Here is an example of an incorrect output of POS tagger,
<br><img src="http://farm5.staticflickr.com/4284/34454444504_83521a11ef_b.jpg"> 

Notice how the command is very similar to the previous example, in fact the only thing that is different is the color of the car. However, the output indicates that there is no adjective and the POS tagger classified ‘pink’ as a noun and not an adjective.

<br>
Deterministic Finite Automaton Machine
The finite state machine was used to help the agent filter out the sentences that were classified as commands but did not have the proper English sentence structure (if you are interested in reading about this, go to the status report under evaluation). We made use of this Non-Deterministic Finite Automaton Machine to perform the same task as a POS tagger, but in a more efficient way. 
Here, is the finite machine that we built. It is different from the one that we presented in our status report. (in the approach explain more inn detail the new update.)

<br>
<img src="blob:https://www.flickr.com/60475818-b694-4718-82e2-b752857c4b4b">

As you can see from the finite state machine, the only accept states are {5,6,7,9,11,13}, meaning that out machine only accepts commands with the following patterns.
Here are a few examples,
•	Please “Verb” to the “Noun”
•	“Verb” to the “Noun”
•	“Verb” to the “Adjective” “Noun”
•	“Verb” a/an/the “Noun”
•	“Verb” a/an/the “Adjective” “Noun”
The reason why we structured it that way was because most of the Malmo commands start with the verb and they are followed by the adjective and lastly, the noun. Again, this was to avoid commands like, “red car go to the”, which are an improper structure of an English sentence. 
Let’s look at a look at the output of our state machine, 

<br>
<img src="http://farm5.staticflickr.com/4233/34454470054_9824325e1f_b.jpg">

Notice that the input is the same as the POS tagger example, in this case pink was detected as the adjective and the finite machine also outputs the accepting state in which it terminated.

Test 
Let’s compare how both methods compare to each other to see which one is more efficient in extracting the verb, adjective and the noun for a set of 100 sentences. 
First, the test data is structures as follows,

<br>
<img src="http://farm5.staticflickr.com/4241/35131867982_518e028f2c_b.jpg">

The key of the dictionary represents the input that will be passed to the POS tagger and the DFA. The value is the expected result for each method. 

Quantitative 
Performance 

<br>
<img src="http://farm5.staticflickr.com/4274/35298271455_d395458f38_b.jpg">



## References

Minecraft Wiki: 
http://minecraft.gamepedia.com/Coordinates

Xml schema for MineCraft's items:
https://github.com/Microsoft/malmo/blob/master/Schemas/Types.xsd

Minecraft XML Schema Documentation:
http://microsoft.github.io/malmo/0.16.0/Schemas/MissionHandlers.html#element_ObservationFromRay



