---
layout: default
title:  Home
---
<img src="http://farm5.staticflickr.com/4200/34066171843_29d7346537_b.jpg">

<h3>About</h3>
Captain Commando is a Natural Language Processing project where an AI agent takes a set of instructions as an input and turns it into actions. This form of interaction focuses in converting text into actual action for the game. To achieve this, the agent needs to learn a what a proper sentence structure really is. Once the agent understands these criteria, it is important for it to break down the sentence and be able to classify the verb, adjective and noun. This classification is important in order for out agent to distinguish the type of action it should take, such as jumping, walking, cutting and etc. Same concept applies for the noun, the agent needs to know the difference between a red cube and a green cube or maybe the difference between a tree and a pig. Furthermore, most of the actions will involve moving from place to place in the destination. To achieve this, the agent will determine the shortest path from its position to the object is trying to reach using Dijkstra’s algorithm.   

<h3>Interactions</h3>

<img src="http://farm5.staticflickr.com/4252/34746200421_e639b83c1a_b.jpg">

The agent is able to classify the item as a redstone_block and it also returns the list of moves for the shorest path. Notice how the agent was able to understand that the red stone was the same as the redstone_block.


<img src="http://farm5.staticflickr.com/4222/34491800670_c3d083db24_b.jpg">

Capable of knowing when he is in danger of falling.


<h3>Implementation</h3>
Language: Python version 2.7

<h4>1. Dijkstra’s algorithm</h4>
The algorithm is used to find the shorest path to items.

<h4>2. Naive Bayes Classifier</h4>
Naive Bayes Classifier is used to classify items in the enviroment and to determine if the text input is a question, statement or command. The learner trains from a list of data that is generated by the programmer.   

<h4>3. Part of Speech Extractor</h4>
This module focuses on extracting the verb, adjective, and the noun from a sentence. 



<h3>Links to tools for Natural Language Processing</h3>




