---
layout: default
title:  Final Report
---

## Video

[![Description of the Video](https://img.youtube.com/vi/FI3aW0RabBg/0.jpg)](https://www.youtube.com/watch?v=rQd7vvLrs8o&t=3s)


## Project Summary
  Our goal of this project remains the same: using natural language processing to control the A.I agent to do thing that we want. In specific we want to our A.I agent be able to execute from simple command such as “go, jump, go left, go right …” to more complex command such as “go to a specific location, break something…” To do this we use the Deterministic Finite Automata machine to take input from use and check if the input is valid. 
  
## Approaches
<h4><b>Environment: </b></h4>

Environent plays an important role in our project since out agent relies heavily on the objects' names and their coordinates to defien where to go on the maze based on the shortest paths algorithms.  Understand all neccessary items in the xml and apply them to our actual project took quite a bit time for us.  When building the environment for the agent to interact, there are 2 states:

<h5>Status report state:</h5>
- As we showed that in in the status report state, we can only have the maze (with biggger size added).

<h5>Final state:</h5>
In the final state, we took some office hours with Professor to figure out how to add more items on the maze so that the agent can try its actions/movements:

<ul><b>These materials have been used in this project to create the environment and all items, blocks, and entities:</b>
  <li>Tutorial 5</li>
  <li>craft_work.py</li>
  <li>Homework assignments: 1 and 2</li>
  <li>Malmo xml schemas via this link https://github.com/Microsoft/malmo/blob/master/Schemas/Types.xsd</li>
</ul>

As a initial plan, we need an environemnt with maze with air as gaps (to apply the finding shortest paths), and all other items added onto that same maze.  On the move to the final state, we did the following steps:

Build up the environment with various types of objects.
Built up a maze with size of 80x80, with gap, walls surrounded.

<br>
''' + self.drawWalls() + '''	

<br>
<img src="http://farm5.staticflickr.com/4283/35168828711_d1099543b6_b.jpg">


<br>Added more bock types, such as stone, brown mushroon block, water block

<br>
<img src="http://farm5.staticflickr.com/4259/35258329776_7bc2528e60_b.jpg">

<br>
<img src="http://farm5.staticflickr.com/4235/35298581875_11a00077c5_b.jpg">

<br>Since house is not a typical block, item, or entity in the MineCraft game, we have to manually draw it on the maze.  There are 2 parts of the house that we built separately: roof and walls.  The final house that we added on the maze shown as below:

<br>
<img src="http://farm5.staticflickr.com/4240/35258280566_a90816ceb8_b.jpg">

<br>
<img src="http://farm5.staticflickr.com/4200/35132287322_995375d58a_b.jpg">

We also added many other types of items and entities onto the maze:
<br>
<img src="http://farm5.staticflickr.com/4240/35132504122_9eb6391447_b.jpg">

<br>
<img src="http://farm5.staticflickr.com/4207/35258667256_67020a0276_b.jpg">

<h4><b>Algorithm: </b></h4>

Our baseline for this project is to classify user input into command and non-command. For command, we want our Agent to perform simple command such as “go, go left, go right, go forward, go backward”. To classy find Command from user input, we’ve used two technique for this. The first Technique we use is text classifier NaiveBayesClassifier from textblob.classifiers library. To do this, we have to manually create a lot of data (picture of data). Such data as short sentence of “Command sentence” and “Non-Command sentence”. Pseudo code for this is :
 
<br><img src="http://farm5.staticflickr.com/4239/34465306934_aeb524a955_b.jpg">

The execute function will take verb and use movement dictionary to classify what type of verb. For example, “move, go to, reach” will be classified as “go”, “break, destroy, kill” will be classified as “attack”. 

Our second technique is to use Deterministic Finite Machine to classify command. Below is the picture of our first DFA.

<br><img src="http://farm5.staticflickr.com/4203/35309387515_78a08c1d5e_b.jpg">

Our first DFA is simple. It only allow one action and one object without any adjectives support. The structure of our DFA is: (please) verb (go to) object, or (please) verb (forward/backward).

To classify the meaning of word, we first use NaiveBayesClassifier from textblob.classifiers library. Just as the command, we manually create data for the classifier to learn and test it using different words that have similar meaning. 

PICTURE OF DATA OF TEXTBLOB and output
<br><img src="http://farm5.staticflickr.com/4279/34921459270_8e2922b31e_b.jpg">

<br><img src="http://farm5.staticflickr.com/4264/35179250131_b11b18e9a6_b.jpg">


Next stage, to improve performance of our A.I Agent, we upgrade our DFA so that it allow the command to be more complex. We add state 9 and state 8 to the DFA to allow our DFA accept command with multiple verb and multiple adjective. Also we connect state 5 to state 6 so we can allow command with ‘position object’. 

<br><img src="http://farm5.staticflickr.com/4256/35269053556_fec63529dc_b.jpg">

In our DFA, there are 4 acceptance state : 1,5,6,7. 

State 1 is for basic action such as "attack, go, jump...".

State 5 and 7 is for moving in specific direction such as "forward, backward, left, right"

State 6 is the most complex and powerful. It allow command to have multiple verb, multiple adjective described object. For example if the command is "Please go and find the left red stone". The command will be go into state 0 -> 1 -> 9 -> 1 -> 4 -> 8 -> 8 -> 6 then will be accepted.

At first, to recognize action, we use textblob library to train our data, but the problem is we have to generate data manually and it take so much time. 

<br><img src="http://farm5.staticflickr.com/4260/34465398374_9c6af1267c_b.jpg">

Therefore we switch to use gensim library, library allow us to find the similar between words. For example with two command "Go to the green stone" and "Break the wall". First we find the most similar basic action with the one in command then we find the most similar object that on the map with the object that in the command.

<br><img src="http://farm5.staticflickr.com/4230/35269606286_266f0dec07_b.jpg">

<br><img src="http://farm5.staticflickr.com/4240/35143138872_4c84df26ec_b.jpg">



To execute command, we do the following general algorithm. 
<br><img src="http://farm5.staticflickr.com/4279/35179412411_a53521c75e_b.jpg">

In our dfa class, we extract information on the command as follow:.
<br><img src="http://farm5.staticflickr.com/4205/35179412521_beb7050c49_b.jpg">

## Evaluation
<h3><b>Qualitative:</b></h3>
<h4><b>Part of Speech Tagger vs. Deterministic Finite Automaton Machine:</b></h4>
Issue: Captain commando is an AI project that relies on the extraction of components in a sentence. For instance, to execute a command that is given as text by the user, our Agent has to be able to know the action that it will be performing. Maybe the action is to attack a sheep, or to find the nearest tree. To accomplish this, our agent must be able to split the sentence into words and correctly identify the verb, the adjective and the noun inside that sentence. What if the given text is not a command? As we explained in our status report our agent can distinguish between a command, question or a statement. Knowing this our agent would disregard any other forms sentences that are not commands.  Now, let’s analyze the two approaches that we have implemented for our agent to extract these three components in a sentence (Verb, Adjective, Noun).

<h4><b>Part of Speech Tagger</b></h4>
Part of speech tagger is a NLTK tool function that accepts a list of words as an input and returns a list of tuples. 
Here is an example of an execution 
<br><img src="http://farm5.staticflickr.com/4234/35168377281_6f27073853_b.jpg">

Now, POS tagger was the tool that we initially used for our agent to get the verbs, adjectives and nouns. However, we started noticing that it wasn’t very accurate when detecting the three components. 
Here is an example of an incorrect output of POS tagger,
<br><img src="http://farm5.staticflickr.com/4284/34454444504_83521a11ef_b.jpg"> 

Notice how the command is very similar to the previous example, in fact the only thing that is different is the color of the car. However, the output indicates that there is no adjective and the POS tagger classified ‘pink’ as a noun and not an adjective.

<br>
<h4><b>Deterministic Finite Automaton Machine</b></h4>
The finite state machine was used to help the agent filter out the sentences that were classified as commands but did not have the proper English sentence structure (if you are interested in reading about this, go to the status report under evaluation). We made use of this Non-Deterministic Finite Automaton Machine to perform the same task as a POS tagger, but in a more efficient way. 
Here, is the finite machine that we built. It is different from the one that we presented in our status report. (in the approach explain more inn detail the new update.)

<br>
<img src="http://farm5.staticflickr.com/4256/35269053556_fec63529dc_b.jpg">

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
 
<h4><b>Test</b></h4>
Let’s compare how both methods compare to each other to see which one is more efficient in extracting the verb, adjective and the noun for a set of 100 sentences. 
First, the test data is structures as follows,

<br>
<img src="http://farm5.staticflickr.com/4241/35131867982_518e028f2c_b.jpg">

The key of the dictionary represents the input that will be passed to the POS tagger and the DFA. The value is the expected result for each method. 

<h3><b>Quantitative:</b></h3>
<h4><b>Performance:</b></h4>

<br>
<img src="http://farm5.staticflickr.com/4274/35298271455_d395458f38_b.jpg">

<br>
<img src="https://www.flickr.com/9f2bf1e1-2fe0-4cb9-9dea-7b723951932d">

Using the 100 manually generated test data sentences we see that the finite machine gets 78% correct while POS tagger only gets 34% correct. Keep in mind that the reason for this outcome is because most of the test data is constructed so that our state machine could accept the command. If we were to change the data in a way that our state machine won’t be able to accept it, then we would have a different outcome. However, since we are focusing on commands that would work on Malmo, we restrict the amount of sentence structure in order to get a better performance with our extractor. Another approach could be to update the finite machine to accept more complex commands.

<h3><b>Qualitative:</b></h3>
<h4><b>Gemsin Word2Vec (Automated) vs Textblob Classifier (Manual)</b></h4>
Issue: Captain Commando relies on the classification of objects and actions. It is important for our learner to understand that “moving” is different from “jumping” and that a “block” is not the same as a “pig”, but also that ‘hoping’ means the same as ‘jump’.  In order for our agent to learn these difference and similarities, we used the Textblob classifier which allowed us to create a learner and feed it training data that was manually generated as a list of verbs and objects. (If you are interested in more information about this method, please go to the status report under evaluation). The issue with the use of Naïve Bayes Classifier was that it wasn’t as accurate and precise in classifying objects. For instance, let’s say we were to train our learner to classify objects such as an Emerald_block, then green block would work, however green horse would work too even though horse is not similar to a block. The issue with Naïve Bayes classifier is that it classifies depending on how often the word appears on the training data. Another issue is that we need to manually generate the training data, which becomes a problem when there are a lot of items in the environment.  

<h3><b>Textblob Classifier (Manual)</b></h3>
Let’s take a close look at this issue, suppose that our training data is composed of the following,

<br>
<img src="http://farm5.staticflickr.com/4247/34488379663_343a713357_b.jpg">

Notice, that the list of tuples has some of the different types of names that can be considered an “emerald_block” or a “redstone_block”. Let’s feed this training data to out learner using Naïve Bayes classifier as showed as follows,

<br>
<img src="http://farm5.staticflickr.com/4207/35168499671_fdfc72071c_b.jpg">

If we were to run some test data on our learner, to see if it knows the difference between a red stone and an emerald stone it will get it correct because those are the two items that were classified in our training data. For example,

<br>
<img src="http://farm5.staticflickr.com/4254/34488459083_eebce01c7a_b.jpg">

However, the issue is when we want to predict if something very unrelated to a block is classified as one of those two items in the training data, for instance,

<br>
<img src="http://farm5.staticflickr.com/4255/34454642324_40fac44449_b.jpg">

We can see that a green shark is classified as an emerald block which creates an issue because a shark is not the same as a block. This issue arises because our data only defines what those two objects are however it does not train the learner of things that are NOT considered a red stone or an emerald block. For this we have to generate more data that will define what is not an emerald block or a Redstone. 

<h3><b>Solution: Gemsin Word2Vec (Automated)</b></h3>
Gemsin Word2Vec is a tool that uses the GoogleNews-vectors-negative300.bin.gz file that generates a score of similarity between words. 
Let’s take a look at a run, 

<br>
<img src="http://farm5.staticflickr.com/4282/35298428015_897b2fff02_b.jpg">

The input is “go to the river” and using the finite state machine mentioned earlier in this report, it extracts the verb and the noun of the input command. Then, using the ‘similarity’ function from gensim.models.word2vec,

<br>
<img src="http://farm5.staticflickr.com/4285/35168600181_5562ab884a_b.jpg">

It compares the extracted verb to all the actions in Malmo and the extracted noun to all the objects in the Malmo environment. We make use of these results to obtain the item with the highest similarity score. Now, how does this help solve the issue that was previously stated? As you can see from the results, for the verb ‘go’, the Malmo action that had the highest similarity score was “move”. As for the object “river”, the highest similarity score was from the item “water”. This is very important for our agent because an object such as a green horse won’t have a high similarity score for the Malmo object “block”.


## References
Minecraft Wiki: http://minecraft.gamepedia.com/Coordinates<br>
Xml schema for MineCraft's items: https://github.com/Microsoft/malmo/blob/master/Schemas/Types.xsd<br>
Minecraft XML Schema Documentation: http://microsoft.github.io/malmo/0.16.0/Schemas/MissionHandlers.html#element_ObservationFromRay<br>



