<h4><b>Project summery</b></h4> 
  Our project is using Natural Language Processing to command the AI agent what to do. We use Deterministic Finite State machine to classify the command out of any other statement or questions that the user put to the AI agent. The goal of our project is the AI agent will be able to execute the command from simple to complex such as: go to the tree, go and cut the tree, or find the house, go behind the nearest tree.
<br>
<h4><b>Approach</b></h4> 
  Our algorithm is to classify the user input first and make sure it is a command. Next, we will break the command into a list of words and classify which one is the action and the object. Furthermore, the command may or may not contain the transition word such as (to, the, until ...) or adjective that describe the object such as (color adjective: green, red, blue or position adjective: nearest, next to something, behind). At first, we use text classifier NaiveBayesClassifier from textblob.classifiers library to classify which input is command which is not. Then use nlkt.pos_tag() to classify which word in the input is action, or object base on the tag of the word. Using that result, we can identify which one is a action word and which one is the target word, then we have extracion function to retrieve action and object base on the tag of each word. One problem of this approach is the pos_tag() function sometime does not give us the good result. For example, if the input is "move left" then the pos_tag() function will consider move is a noun and left is a verb. 

<img src="http://farm5.staticflickr.com/4202/34139820603_18238f2c97_b.jpg">

Another problem of this approach is even if we switched the order of our cammand, it still executes it even though the sentence seems non-sense. For example, command is "go to the red block" then the agent will take <i>go</i> as an action and <i>red block</i> as an object, but if we switch the order of this command such as <i>go block red to the</i>, the agent still execute the command. Because our extraction function only takes action and obj based on the tag and ignore the order of the command, it will always gives the agent action and object.
  
  Therefore, we decided to switch to another approach to classify command out of the user_input. We use DFA (Deterministic Finite State Machine) to take the input. The state machine will accept if the user's input follows certain structures. Below is the picture of our simple DFA as to accept or reject the user_input. 

<img src="http://farm5.staticflickr.com/4221/34799352621_6e541fdafe_b.jpg">

For example: if the user input is "go to the house", the command will be splitted into list of words and each word will be passed into the state machine to see if after runs the whole list, it will be in the <i>accept</i> or <i>reject</i> state. The example above will go:

<ul>
<li>(State 0 , "go") = State 1, </li>
<li>(State 1, "to") = State 3,</li>
<li>(State 3, "the") = State 4,</li>
<li>(State 4,"house") = State 6</li>
</ul>

State 6 is in accepting state so the input is accepted. After that we will use extraction function to take the action and object to pass to our AI agent. 
Another example: "to the house go", the command will be split in to ["to","the","house","go"]:
(State 0, "to" ) = state None, 
Then it will reject the input and return 0 meaning the input above is not valid command.
The disadvantage of this approach is our state machine is quiet simple to identify the more complex command such as "go to the red house", "go to the nearest red house", "go and find the red stone". They're all valid command but the state machine is not recognized any adjective go before the object just yet. We will have this in our final Project.

Next approach is to have the agent execute command based on action and object.  We also use the similar ideas as shown in the homework 1, which is using layout of the two-dimensional grid laid out as a one dimentional array,  How ever, the location of the maze, will stays the same in the project. We currently used the random function to locate item onto the maze such as (coal, carrot...) then we achieve the position of that item (x,y,z) coordinate and then we use Dijkstra’s algorithm for shortest path to find the way for our AI agent to get to the item. The problem of this is the position of each item is in (x,y,z) coordinate and our Dijkstra’s algorithm take input as the index of the block of our agent and index of the block where the item is. This is because the grid is represented as a single-dimentional array, this means that we can only get the neighboring block based on the current one's index.  Therefore we use the formula below to get to the index of the blocks:

<img src="http://farm5.staticflickr.com/4243/34767366632_9efc3504f8_b.jpg">

The way the x,y,z and index of each block works is if you go north then your index will decrease by 21 and your z will decrease by 1. South: index increase 21 and z increase by 1. West: index and x will decrease by 1. Ease: both index and x will increase by 1. There for if we have the current position of agent (both index and x,y,z) and the current x,y,z of the item we can figure out the current index of the item by:

<ul>
<li>horizontal = item_x - agent_x </li>
<li>vertical = 21 * (item_z - agent_z)</li>
<li>item_index = agent_index + vertical + horizontal</li>
</ul>
<br>
<h3><b>Evaluation</b></h3>

Our first classifier focuses in distinguishing a text input (sentence). During the implementation process we notice that sometimes when we would write any type of sentence into the command line it will be difficult for or agent to identify the what a command really is. For instance, what if the user writes a question or a statement instead of a command, how would our agent execute an action when given a question? Or How would our agent extract a verb or a noun from a sentence that doesn’t include a verb/noun at all? Our first observation was that in Natural language a command does include verbs and nouns. Knowing this we decided that the first step is to use Naive Bayes Classifier in order for our agent to be able understand what a command is and how is it different from questions or statements, where statements could be compliments and facts or opinions.

<img src="http://farm5.staticflickr.com/4270/34891425106_0323cecf89_b.jpg">


Problem with Naive Bayes Classifier is that it bases its prediction on the occurrence of words. For instance, if you observe the training data for our classifier (Look at the figure below), you can see that a lot of the data that start with "what", "where", "why" will be classify as a question because those words occur constantly in the in the training data and are defined as a question. This causes an issue because it doesn't focus in the order of the sentence, so a sentence like "that What is?" will still be classified as a question. This presents a problem because that is not the proper sentence structure for the English language. Now The solution to this is explained later in this evaluation part of the status report. The reason why we used Naive Bayes classifier was because we wanted to categories the general aspect of a sentence. In other words, we wanted our learner to differentiate a command from the other types of sentences

<br><br>
<h4>Training Data</h4>
<img src="http://farm5.staticflickr.com/4228/34800541851_e7e6e4cba9_b.jpg">

Our training Data was manually genereated and it categorizes three main things. These three things include question, command and statement. 

<br><br>
<h4>Test Data</h4>
<img src="http://farm5.staticflickr.com/4223/34122301603_0b22425f0c_b.jpg">
Like the Training data, we also manually generated the test data necessary to check the accuracy of our classifier/learner. We test the accuracy using the funcion below.

<img src="http://farm5.staticflickr.com/4273/34567791550_eae946be76_b.jpg">

Another issue that was presented was that our classifier was performing poorly (look at the figure below). We can see that the accuracy of our learner, based on the sentence_data does poorly in distinguishing between a statement a question or a command. One way in which we fixed this was through feeding it more relevant data to our learner. For instance, putting commands that will only work in Malmo such as "move to the tree" and avoid irrelevant commands such as "Make a backflip". By doing this we narrow down the amount of important data we feed to our classifier and we focus on increasing the probability for our learner to get commands correctly more specifically commands that are meant for malmo. Then, if we use a test data that has commands related to malmo we can observe that the accuracy will improove. Also, if you look at the most informative Features for our classifier notice that a lot of these features are not relevant to commands in Malmo except for "Move". If we are able to create a sentence_data that generates informative features that relate to Malmo commands, then we can expect our agent to have a higher accuracy when identifying commands.If Malmo was more complex to the point where we can perform any sort of action like a backflip or make the agent laugh then it would be important to create a huge training data structure.

<img src="http://farm5.staticflickr.com/4244/34800409321_00b86d568c_b.jpg">
<br>
<h4>Features</h4>
<img src="http://farm5.staticflickr.com/4267/34891960246_9a7b450c5c_b.jpg">


As we improved our sentence_data(Training data) and as we train our classifier to have more relevance to possible Malmo commands we notice that the accuracy of our Naive Bayes classifier increased. The reason for this is because when we run the classifier with the test data, it is accurate when distingishing a command from any other type of sentence.(Look at the figure below).

<img src="http://farm5.staticflickr.com/4195/34891619076_aaa70f8c6b_b.jpg">
<img src="http://farm5.staticflickr.com/4198/34891641866_b69ca92d0c_b.jpg">

<h4>Finite Machine Implementation</h4>
As we mentioned before, getting our agent to correctly classify a sentence was our first issue. Then, our next step was to get our agent to only accept proper structured English sentences. This implementation is necessary for our agent to avoid incorrect sentence structure like, “Go the please to tree” which the correct way to write this is, “Please go to the tree”. 

The first step to this implementation was to first extract the Part of Speech tagger for each word in the sentence. To do this we used the tagger function from nltk tools that takes in a string as an argument and returns a list of tuples with the word being the first element in the tuple and the tag being the second element in the tuple. Also, for our implementation purposes we focused on extracting the action/verb and the object/noun in order to be able to execute the command. This will be explained in more details later in the evaluation part of the status report. 

<img src="http://farm5.staticflickr.com/4203/34570060170_96d84cdde6_b.jpg">

The reason why we use POS to extract the tags of each word was because we wanted to study the patterns of the correct structure of an English sentence more specifically for a command. Most of the commands we write for Malmo start with a verb, for example, “Go to the red block”, “Destroy the tree”, “Craft a bowl”, etc. Then, we notice that usually there are a few other tags in between the “VB”(Verb) and the “NN”(Noun). Sometimes commands have different structure like the one below. 

<img src="http://farm5.staticflickr.com/4268/34957288315_9849933e90_b.jpg">

In order to be able to accept sentences with correct structure, yet be able to accept different patterns for the tags that are consider to be command sentences. We decided to implement a Finite machine that would allow only those specific patterns to be accepted. Look at the figure below.

<img src="http://farm5.staticflickr.com/4222/34957289055_dc39228d8d_b.jpg">


There are still improvements needed in order for our finite machine to be more efficient. For instance, being able to accept command sentences that have “CD” tags. For instance, “Walk three tiles to the right”. The “CD” for this sentence would be “three”. Lets take a look at how our finite machine works. 
The finite machine is a Deterministic Finite machine and the definition of our DFA is described below. 

(Q, Σ, δ, q0, F)

Q = {0,1,2,3,4,5,6,7}

Σ = {please,verb,to,the,forward,backward,noun,the,left,right}

δ = Q × Σ → Q

q0 = {0}

F = {5,6,7} 


<img src="http://farm5.staticflickr.com/4251/34570065290_57a0577cbc_b.jpg">


This is the implemented transition function. 


<img src="http://farm5.staticflickr.com/4267/34570066340_9ff2f84257_b.jpg">


It return a 5, 6, or 7 if the command structure is approved.


<img src="http://farm5.staticflickr.com/4227/34570067250_4ec302c223_b.jpg">


It returns a “0” if the deterministic finite machine doesn’t accept the structure.


The DFA machine takes a string and a list of verbs that is taken from a file that stores all the possible verbs in the English language. Then, it splits the string and adds the POS tags to each word. This is necessary because the verb is replaced by the actual word, same thing occurs to the noun. The DFA runs the split string and if the objects matches the order of the alphabet then it will return a 5,6,7 meaning it’s the correct structure. Otherwise, it returns a 0.


<h4>Lets take a look at a run.</h4>

Input = Please go to the park.

<h4>Step 1: The sentence is split and the POS Tags are added to each word.</h4>

<img src="http://farm5.staticflickr.com/4226/34571265890_c80281eda1_b.jpg">


<h4>Step 2: Then, we check if the word ‘go’ is in verb.txt.</h4>


<h4>Step 3:  The DFA takes in the user input and splits it, then it runs the input in the finite machine.</h4>


<img src="http://farm5.staticflickr.com/4270/34918158676_887966828a_b.jpg">


<h4>Step 4: returns 6</h4>


<img src="http://farm5.staticflickr.com/4196/34148291393_dfb31f35be_b.jpg">


<h4>Object Classifier</h4>
At this point our agent is able to understand commands and be able to see if the structure of the sentence is correct. The next step Is for our agent to be able to classify an object. Let assume in a Minecraft environment, there is an object such as a red block positioned a few blocks away from our agent, and then the user writes a command : “Go to the red block”. The user is well aware of what a red block is, however for the agent it is difficult to understand the meaning of a red block. Also, the red block might not be called a red block in Malmo but instead its called “redstone_block”.

Similar to how we implemented the classifier for identifying commands, we do the same for all the items inside the selected environment. 
<img src="http://farm5.staticflickr.com/4245/34117134764_f0c2b7ebea_b.jpg">

For our project, As of now we are only using two items in the environment for our final report we intend to add more objects to the environment. These two items are the “redstone_block” and the “emerald_block”. 
<img src="http://farm5.staticflickr.com/4274/34117136754_d21bd239c4_b.jpg">

The reason why we haven’t manually generated more data for the object classifier is because we are trying to change it into an automated way to classify an object. This is because unlike the sentence classifier, where there is only three things to distinguish, for the object classifier we have to accumulate a lot of data in order for it to distinguish all the items in Malmo. 


<h4>Actuator</h4>
For the actuator, we have implemented the Dijkstra’s algorithm to find the shortest path to the objects. Also, we have a grid loader functions that allows us to know the position of all the objects in the environment. We also implemented a function that allows us to update the position of our agent. The implementation is similar to the one in assignment 1. Also, there are times a simple command such as “Make a right” might cause the agent to fall from an edge if there isn’t a block on the right of the agent, but thanks to the grid loader we are able to let the agent know the possible position in which he cant make a move. Furthermore, as we all know once we ended up in the red stone the mission would end, we change the mission to allows to continue to make actions even after we got to the red block. The changes we made to this algorithm was to update our starting position every time we move to a different destination. For the final report we intend to implement the rest of the actions such as “jump”, “Cut”, and etc. 




<br>
<h4><b>Challenge and Remaining Goal</b></h4>
<ul>
    <li>The function of getting current AI agent is not consistence. Sometime it return the true position (xyz), but other time, the z values is different by +/-1. </li>
    
    <li><img src = "http://farm5.staticflickr.com/4267/34567568080_a5d692c45c_b.jpg"></li>
    
     <li> How to manipulate the environment so that there is various type of objects for us to test what our Agent can do. Right now, we only dropping objects such as (coal, carrot, egg, ..) onto the maze the field ant random positions. In future we want to have a house, or a tree to see if our Agent can recognize which one is the house or tree and perform certain action to the object.</li>
    <br>
     <li>Our first remaining goal is to make our DFA more powerful to be able to recognize more complex command. As I mentioned above, our DFA only allow command in simple structure (verb + go + to + noun). We want our DFA can recognize more complex command such as if the user input adjective to describe the object like position or color of that object</li>
  <li>Secondly, our AI agent only limited to perform movement action such as go left, go right, go to one object. We want our agent can perform various type of actions for example: attack, find a certain object, cut the tree, etc ...</li>
  </ul>

<h4>Video</h4>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_DVMI3RfZIY" frameborder="0" allowfullscreen></iframe>

From the video we showed some of the current actions that our agent can take, however there is a lot of room for improvement, such as adding more items and be able to perform more actions. In fact, some of our current failure cases is that our agent is able to classify on object but not is not very accurate. For instance, our agent could go to red block, even if the user tells the agent to move to the “red Horse”. This is some of the few things we have to improve on too make our agent smarter.
