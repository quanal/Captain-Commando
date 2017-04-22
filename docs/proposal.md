## layout: default
## title: Proposal

Summary of the Project: (30 points)
Our work focuses on the natural language interface.  Most items focus on retrieving user’s commands, analyze iit via AI algorithms, and reflect via agent’s actions in the game.
For the framework, it may be provided by professor, or we’ll built the simple framework just enough for demonstrating the AI algorithms via agent.
For the Minecraft Project we will focus on natural language interface. The main idea of this project is for our agent to execute actions based on commands entered by the user. The input will consist of the text command and the data structure representing the environment of the world in minecraft. Since we are mostly focusing in classifying the text, we will work with a simple Minecraft world. However, as the project progresses then we will add more complexity to the world. One of the main goals is for the agent to be able to distinguish between a verb and a subject when given a command. It is important for our agent to classify these two components within a sentence in order for it to execute the action. Most of the actions will include the agent to move to different places in the environment and to be able to identify the objects in its surroundings. This will require an  algorithm to find the shortest path to the objects. The output will consist of a set of actions that our agent will perform for each command given by the user. 

AI/ML Algorithms (10 points)
Build a dictionary of terms that are used in natural language and that are frequently used in commands and orders. For instance, words such as “Go”, ”Move”,  ”Forward”, ”Cut” and etc will be included in the dictionary. The agent will use this dictionary to determine if the text given by the user is a command or not. This will be performed by a Naive bayes classifier, where the features will be a set of words from the input(The text given by the user). From these features, the algorithm will predict if the sentence input is a command.
After the agent has determined that the sentence is a command, the next step will be to retrieve the verb and the subject from the sentence. For example, if the user inputs, “Cut the tree”, then the algorithm ill retrieve the word “cut” and “tree”. (It could happen that as we progress with this project we can classify other things from sentences such as adjectives. Let’s focus on the “easy” aspects first).
Once the verb and the subject have been obtained, the agent will use the second input which is the data structure that represents the Minecraft World and will look for the object index. Finally, using a shortest path algorithm (dijkstra's algorithm) the agent will move to the object and perform the verb(action). (As I mentioned before, as we progress through the project we can implement other stuff such as adjectives, these adjectives could describe different positions of some objects such as “behind”  the house.One way to implement the this could be by finding the shortest distance to the furthest block the object from the agent. )  

The main idea is to sending command to our agent to perform an action.  Via AI algorithms applied to the coding, the actions in return will be performed differently from the normal actions, such as paths found have to be the shortest paths, when agent builds something, job has to be done quickly, etc …
Due to the limitation in this course, our project is only focus on the AI algorithms in these four mains categories:
Find the paths
Find items and objects  within the environment such as houses and trees
Attack quickly/use tool properly
Built something (Im not sure what you mean by this because building something is )


For example: go to the pig: the agent will go to the pig 
		Cut the tree: the agent will find the tree and cut

Classify Actions and objects
We first will classify which word is in Action category or Object category. 

For example: Go to the dog: “Go” would be classified as the Action and “Dog” would be      classified as the object. 

We will first store our object into a dictionary along with it’s index in environment, then we’ll find the way to reach that position fastest using any shortest path algorithm. 
Shortest path implementation:

Our agent will be asked to perform some task that require it to move from current position to some object. For this kind of actions we will use shortest path algorithms to get to a destination.

	
Tool : we will use natural language tool kit, sklearn… 


In a paragraph or so, mention the main idea behind your project. At the very least, you should have a sentence that clearly explains the input/output semantics of your project, i.e. what information will it take as input, and what will it produce. Mention any applications, if any, for your project.

