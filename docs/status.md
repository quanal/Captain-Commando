Project summery: Our project is using Natural Languale Processing to command the AI agent what to do. We use Deterministic Finite State machine to classify the command out of any other statement or questions that the user put to the AI agent. The goal of our project is the AI agent be able to execute the command from simple to complex such as: go to the tree, go and cut the tree, or find the house, go behind the nearest tree... 

Approach: 
  Our algorithm is to classify the user input first and make sure it is a command. Next we will break the command into a list of work and classify which one is the action and the object. Furthermore, the command may or may not contain the transition word such as (to, the, until ...) or adjective that describe the object such as (corlor adjective: green, red, blue or position adjective: nearest, next to something, behind). At first, we use text classifier NaiveBayesClassifier from textblob.classifiers library to classify which input is command which is not. Then use nlkt.pos_tag() to classify which word in the input is action, or object base on the tag of the word. Using that result, we can identify which one is a action word and which one is the target word, then we have extracion function to retrieve action and object base on the tag of each word. One problem of this approach is the pos_tag() function sometime does not give us the good result. For example, if the input is "move left" then the pos_tag() function will consider move is a noun and left is a verb. 

<img src="https://github.com/quanal/Captain-Commando/blob/master/docs/move_left.png">

Anothe problem of this approach is even if we switch the order of our cammand it still execute it eventhough the sentence seem non-sense. For example, command is "go to the red block" then the agent will take go as an action and red block as an object, but if we switch the order of this command such as "go block red to the" the agent still execute the command. Because our extraction function only take action and obj base on the tag and ignore the order of the command, it will always give the agent an action and an object.
  
  Therefore we decided to switch to another approach to classify command out of the user_input. We use DFA (Deterministic Finite State Machine) to take the input. The state machine will accept if the user input follow the certain structure. Below is the picture of our simple DFA to accept or reject the user_input. 

<img src="http://farm5.staticflickr.com/4221/34799352621_6e541fdafe_b.jpg">

For example: if the user input is "go to the house", the command will be split into list of word and each word will be pass into the state machine to see if after run the whole list, it will be in the accpet state or reject state. The example above will go:
(State 0 , "go") = State 1, 

(State 1, "to") = State 3,

(State 3, "the") = State 4,

(State 4,"house") = State 6

State 6 is in accpeting state so the input is accepted. After that we will use extraction function to take the action and object to pass to our AI agent. 
Another example: "to the house go", the command will be split in to ["to","the","house","go"]:
(State 0, "to" ) = state None, 
Then it will reject the input and return 0 meaning the input above is not valid command.
The disadvantage of this approach is our state machine is quiet simple to identify the more complex command such as "go to the red house", "go to the nearest red house", "go and find the red stone". They're all valid command but the state machine is not recognized any adjective go before the object just yet. We will have this in our final Project.

Next approach is to have the agent execute command base on action and object. We use the function to randomly put item into the field such as (coal, carrot...) then we achieve the position of that item (x,y,z) coordinate and then we use dijkstra's algorithm for shortest path to find the way for our AI agent to get to the item. The problem of this is the position of each item is in (x,y,z) coordinate and our dijkstra's algorithm take input as the index of the block of our agent and index of the block where the item is. Therefore we use the formular below to get to the index of the block.

<img src="http://farm5.staticflickr.com/4243/34767366632_9efc3504f8_b.jpg">

The way the x,y,z and index of each block works is if you go north then your index will decrease by 21 and your z will decrease by 1. South: index increase 21 and z increase by 1. West: index and x will decrease by 1. Ease: both index and x will increase by 1. There for if we have the current position of agent (both index and x,y,z) and the current x,y,z of the item we can figure out the current index of the item by:

horizontal = item_x - agent_x

vertical = 21 * (item_z - agent_z)

item_index = agent_index + vertical + horizontal

