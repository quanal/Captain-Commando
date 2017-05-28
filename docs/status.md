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

Our first classifier focuses in distinguishing a text input (sentence). During the implementation process we notice that sometimes when we would write any type of sentence into the command line it will be difficult for or agent to identify the what a command really is. For instance, what if the user writes a question or a statement instead of a command, how would our agent execute an action when given a question? Or How would our agent extract a verb or a noun from a sentence that doesn’t include a verb/noun at all? Our first observation was that in Natural language a command does include verb and nouns Knowing this we decided that the first step is to use Naive Bayes Classifier in order for our agent to be able to filter out sentences that are questions or statements, where statements are compliments, or insults etc.

<img src="http://farm5.staticflickr.com/4270/34891425106_0323cecf89_b.jpg">


Problem with Naive Bayes Classifier is that it bases its prediction on the occurrence of words. For instance, if you observe the training data for our classifier (Look at the figure below), you can see that a lot of the data that start with "what", "where", "why" will be classify as a question because those words occur constantly in the in the training data. This causes an issue because it doesn't focus in the order of the sentence, so a sentence like "that What is?" will still be classified as a question. This presents a problem because that is not the proper sentence structure for the English language. Now The solution to this is explained later in this evaluation part of the report. The reason why we used Naive Bayes classifier was because we wanted to categories the general aspect of a sentence. In other words, we wanted to filter out sentences that weren't a command.
<br><br>
<h4>Training Data</h4>
<img src="http://farm5.staticflickr.com/4228/34800541851_e7e6e4cba9_b.jpg">
<br><br>
<h4>Test Data</h4>
<img src="http://farm5.staticflickr.com/4223/34122301603_0b22425f0c_b.jpg">


Another issue that was presented was that our classifier was performing poorly (look at the figure below). We can see that the accuracy of our learner based on our data does poorly in distinguishing between a statement a question or a command. One way in which we fixed this was through feeding it more relevant data to our project. For instance, putting commands that will only work in Malmo such as "move to the tree" and avoid irrelevant commands such as "Make a backflip". By doing this we narrow down the amount of important data we feed to our classifier. Also, if you look at the Feature for our classifier we notice that a lot of these features are relevant to commands in Malmo. If Malmo was more complex to the point where we can perform any sort of action like a backflip or make the agent laugh then it would be important to create a huge training data structure.

<img src="http://farm5.staticflickr.com/4244/34800409321_00b86d568c_b.jpg">
<br>
<h4>Features</h4>
<img src="http://farm5.staticflickr.com/4267/34891960246_9a7b450c5c_b.jpg">

As we improved our sentence_data(Training data) and as we train our classifier to have more relevance to possible Malmo commands we notice that the accuracy of our Naive Bayes classifier increased. The reason for this is because when we run the classifier with the test data, it is accurate when distingishing a command from any other type of sentence.(Look at the figure below).

<img src="http://farm5.staticflickr.com/4195/34891619076_aaa70f8c6b_b.jpg">
<img src="http://farm5.staticflickr.com/4198/34891641866_b69ca92d0c_b.jpg">
<br>

<h4><b>Challenge and Remaining Goal</b></h4>

    The function of getting current AI agent is not consistence. Sometime it return the true position (xyz), but other time, the z values is different by +/-1.
    
    <img src = "http://farm5.staticflickr.com/4267/34567568080_a5d692c45c_b.jpg">
    
     How to manipulate the environment so that there is various type of objects for us to test what our Agent can do. Right now, we only dropping objects such as (coal, carrot, egg, ..) onto the maze the field ant random positions. In future we want to have a house, or a tree to see if our Agent can recognize which one is the house or tree and perform certain action to the object.</li>
  
     Our first remaining goal is to make our DFA more powerful to be able to recognize more complex command. As I mentioned above, our DFA only allow command in simple structure (verb + go + to + noun). We want our DFA can recognize more complex command such as if the user input adjective to describe the object like position or color of that object
  Secondly, our AI agent only limited to perform movement action such as go left, go right, go to one object. We want our agent can perform various type of actions for example: attack, find a certain object, cut the tree, etc ...

