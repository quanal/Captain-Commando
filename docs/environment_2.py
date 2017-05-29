
from textblob.classifiers import NaiveBayesClassifier
import classify
import MalmoPython
import os
import sys
import time
import json
import random

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  


###############################################################################
#########################LEARNERS FOR COMMANDS AND OBJECTS##################### 
###############################################################################
corpus = [
('What is this', 'Question'),
('Please go to the Tree', 'Command'),
('Cut the tree', 'Command'),
('Move to the house', 'Command'),
('What is the view', 'Question'),
('I want you to go to the table', 'Command'),
('Where do i find the tree', 'Question'),
("Move forward to the next block ", 'Command'),
('Can you move three steps', 'Question'),
('Jump into the pool', 'Command'),
('What is that you are looking', 'Question'),
('Please move to the right', 'Command'),
('Create some flowers', 'Command'),
('Check the floor', 'Command'),
('How is the movie', 'Question'),
('I want you to go to the table', 'Command'),
('how are you not moving', 'Question'),
("Move forward to the next block", 'Command'),
('why are you sad?', 'Question'),
('Run into the pool', 'Command'),
('The beer was good.', 'Statement'),
('I do not enjoy my job', 'Statement'),
("I ain't feeling bad today.", 'Statement'),
("I feel amazing!", 'Statement'),
('Gary is a friend of mine.', 'Statement'),
("I can't believe I'm doing this.", 'Statement'),
('Make a cool toy', 'Command'),
('Make a left', 'Command'),
('Make a right', 'Command'),
('WHat is love', 'Question'),
("Move forward to the next block", 'Command'),
('why are you sad?', 'Question'),
('Make a cool toy', 'Command'),
('my professor is the best.', 'Statement'),
('Im a bad person', 'Statement'),
("You look are amazing", 'Statement'),
("Do you thing you are cool", 'Question'),
('Why do you like me', 'Question'),
("can you help me with this", 'Question'),
("Walk three steps",'Command'),
("Make three Jumps",'Command'),
("You have nice eyes",'Statement'),
("You are beautiful",'Statement'),
("She is very pretty", 'Statement')
]
learner = NaiveBayesClassifier(corpus)

#this is for items in the enviroment
object_data = [
('emerald', 'emerald_block'),
('green block', 'emerald_block'),
('green square', 'emerald_block'),
('green thing', 'emerald_block'),
('green stuff', 'emerald_block'),
('green box', 'emerald_block'),
('light green thing', 'emerald_block'), 
('green block', 'emerald_block'),
('red block', 'redstone_block'),
('red square', 'redstone_block'),
('red stone', 'redstone_block'),
('red thing', 'redstone_block'),
('red stuff', 'redstone_block'),
('dark red thing', 'redstone_block'), 
('dark red block', 'redstone_block'),
('red box', 'redstone_block')

]
object_learner = NaiveBayesClassifier(object_data)

movementDict = {""}
##############################################################################
######################### ENVIROMENT #########################################
##############################################################################

mazeSize = 10 
agentLocationList= [(0,0)]
list_of_items= [ "coal", "planks", "rabbit", "carrot", "potato"]
itemsLocationsList = [(9,18), (11,17), (9,18), (10,18), (15,10)]
#itemsLocationsList = [(5,8), (11,14), (12,5), (11,8), (15,10)]
itemInfo = {}


def getAgentLocations(agent_location_x, agent_location_y):
    agentLocationList.append(agent_location_x, agent_loaction_y)
    return agentLocationList


def itemInformation(list_of_items, itemsLocationsList):
    global itemInfo
    for itemName in list_of_items:
        random_index = random.randrange(0,len(itemsLocationsList))
        itemInfo[itemName] =  (itemsLocationsList[random_index][0], itemsLocationsList[random_index][1])
    return itemInfo



def getItemDrawing(itemInfoDict):
    drawing= ''
    for itemName, item_coordinate in itemInfoDict.items():
        drawing += '<DrawItem x="' + str(item_coordinate[0]) + '" y="57" z="' + str(item_coordinate[1]) + '" type="' + itemName  + '" />'
    return drawing


def getSubgoalPositions(itemInfoDict):
    goals=""
    for itemName, item_coordinate in itemInfoDict.items():
        goals += '<Point x="' + str(item_coordinate[0]) + '" y="57" z="' + str(item_coordinate[1]) + '" tolerance="1" description="ingredient" />'
    return goals
    

def GetMissionXML(seed, gp, size=40):
    global list_of_items
    global itemsLocationsList
    itemInfoString = itemInformation(list_of_items, itemsLocationsList)
    for k,v in itemInfoString.items():
      	print(' {} : {},{}'.format(k,v[0],v[1]))
    	return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

              <About>
                <Summary>Hello world!</Summary>
              </About>

            <ServerSection>
              <ServerInitialConditions>
                <Time>
                    <StartTime>23999</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
              </ServerInitialConditions>


              <ServerHandlers>
                    <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"/>
    
    

                  <DrawingDecorator>
                    <DrawSphere x="-27" y="70" z="0" radius="30" type="air"/>
              
                    ''' + getItemDrawing(itemInfoString) + '''
                  </DrawingDecorator>
                  <MazeDecorator>
                    <Seed>'''+str(seed)+'''</Seed>
                    <SizeAndPosition width="''' + str(size) + '''" length="''' + str(size) + '''" height="10"/>
                  
                   <StartBlock type="emerald_block" fixedToEdge="true"/>
                    <EndBlock type="redstone_block" fixedToEdge="true"/>
                    <PathBlock type="diamond_block"/>
                    <FloorBlock type="diamond_block"/>
                    <GapBlock type="air"/>
                    <GapProbability>'''+str(gp)+'''</GapProbability>
                    
                    <AllowDiagonalMovement>false</AllowDiagonalMovement>
                  </MazeDecorator>
                  
                  <ServerQuitFromTimeUp timeLimitMs="1000000000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>

              <AgentSection mode="Survival">
                <Name>CS175AwesomeMazeBot</Name>

                <AgentStart>
                     <Placement x="0" y="57" z="0"/>
                    <Inventory></Inventory>
                </AgentStart>

                <AgentHandlers>

                <RewardForCollectingItem>
                    <Item reward="10" type="planks" variant="spruce dark_oak" />
                    <Item reward="100" type="cooked_rabbit carrot baked_potato brown_mushroom"/>
                    <Item reward="500" type="bowl"/>
                    <Item reward="1000" type="rabbit_stew"/>
                </RewardForCollectingItem>

          <RewardForDiscardingItem>
                    <Item reward="-2" type="planks"/>
                    <Item reward="-6" type="cooked_rabbit carrot baked_potato brown_mushroom"/>
                </RewardForDiscardingItem>


<ContinuousMovementCommands turnSpeedDegs="40"/>
                <SimpleCraftCommands/>
                <InventoryCommands/>
                <ObservationFromSubgoalPositionList>''' + getSubgoalPositions(itemInfoString) + '''
                </ObservationFromSubgoalPositionList>

                              <ObservationFromNearbyEntities>
                    <Range name="entities" xrange="40" yrange="40" zrange="40"/>
                </ObservationFromNearbyEntities>


                <ObservationFromFullInventory/>

      <AgentQuitFromCollectingItem>
                    <Item type="rabbit_stew" description="Supper's Up!!"/>
                </AgentQuitFromCollectingItem>

                    <DiscreteMovementCommands/>
                    <ObservationFromGrid>
                      <Grid name="floorAll">
                        <min x="-40" y="-1" z="-40"/>
                        <max x="40" y="-1" z="40"/>
                      </Grid>
                  </ObservationFromGrid>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

################################################################################
###### FUNCTIONS TO GET THE GRID AND RUN SHOREST PATH ALGORITHM ################
################################################################################
def load_grid(world_state):
    """
    Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

    Args
        world_state:    <object>    current agent world state

    Returns
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
    """
    while world_state.is_mission_running:
        #sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            grid = observations.get(u'floorAll', 0)
            break
    return grid


def find_start_end(grid,):
  
    """
    Finds the source and destination block indexes from the list.

    Args
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)

    Returns
        start: <int>   source block index in the list
        end:   <int>   destination block index in the list
    """
    counter = 0
    eb_index = None
    rb_index = None
    for i in grid:

        if i == 'emerald_block':
            eb_index = counter
           
        if i == 'redstone_block':
            rb_index = counter

            
        counter+=1

    return (eb_index, rb_index)


def extract_action_list_from_path(path_list):
    """
    Converts a block idx path to action list.

    Args
        path_list:  <list>  list of block idx from source block to dest block.

    Returns
        action_list: <list> list of string discrete action commands (e.g. ['movesouth 1', 'movewest 1', ...]
    """

    action_trans = {-81: 'movenorth 1', 81: 'movesouth 1', -1: 'movewest 1', 1: 'moveeast 1'}
    alist = []
    for i in range(len(path_list) - 1):
        curr_block, next_block = path_list[i:(i + 2)]
        alist.append(action_trans[next_block - curr_block])

    return alist


def findMin(pQ):
    result = None
    if(len(pQ) > 0):
        m = 5000
        for i in pQ:
            if pQ[i] < m:
                m = pQ[i]
                result = i
    else:
        return None
    return result

def findValidMove(grid):
    validSpace = []
    for i in range(len(grid)):
        if grid[i] != "air":
            validSpace.append(i)
    return validSpace



def remove_air(grid):
    d = dict()
    legal_moves = []
    counter = 0 
    for i in grid:
        if i == 'diamond_block' or i == 'redstone_block'or i == 'emerald_block':
            d[i] = counter
            legal_moves.append(counter)
        counter +=1
    return d, legal_moves

    
def dijkstra_shortest_path(grid,source,end):
    possPath = findValidMove(grid)
    #print(possPath)
    print(source,end)
    parent = {source:None}
    currDisDict = {source:0}
    for i in range(len(possPath)):
        if possPath[i] != source:
            parent[possPath[i]] = None
            currDisDict[possPath[i]] = 10000
    movement = [1,-1,81,-81]
    pQ = {source:0}
    count = 0
    while len(pQ) != 0:
        #print(count)
        currPoss = findMin(pQ)
        del pQ[currPoss]
        possList = []
        for i in movement:
            if (currPoss + i) in possPath:
                possList.append(currPoss+i)
        for i in possList:
            newDis = currDisDict[currPoss] + 1
            if newDis < currDisDict[i]:
                currDisDict[i] = newDis
                parent[i] = currPoss
                pQ[i] = newDis
        count += 1
    myShortestPath = []
    result = []
    dest = end
    #print(parent)
    while dest != source:
        myShortestPath.append(dest)
        dest = parent[dest]
    myShortestPath.append(source)
    for i in reversed(myShortestPath):
        result.append(i)
    source = end
    
    return result, source     

##################################
# FIND THE AGENT LOCATION
##################################
def get_obj_locations(agent_host):
    print("inside get_obj_location")
    nearyby_obs = {}
    while True:
        world_state = agent_host.getWorldState()
        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            ob = json.loads(msg)
            for ent in  ob['entities']:
                print ent
                name = ent['name']
                # if name != 'Chester':
                nearyby_obs[name] = (ent['x'], ent['yaw']+57, ent['z'])

            return nearyby_obs

###############################################################################
################ STARTS THE AGENT AND RUNS THE MISSION ########################
###############################################################################

# Create default Malmo objects:
agent_host = MalmoPython.AgentHost()

try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

if agent_host.receivedArgument("test"):
    num_repeats = 1
else:
    num_repeats = 2 #REMMBER THIS IS THE LEVELS




for i in range(num_repeats):
    size = int(20 + .5*i)
    print "Size of maze:", size
    my_mission = MalmoPython.MissionSpec(GetMissionXML("20", .2 +float(i/20.0), size), True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission.requestVideo(800, 500)
    my_mission.setViewpoint(1)
    # Attempt to start a mission:
    max_retries = 3
    my_clients = MalmoPython.ClientPool()
    my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000)) # add Minecraft machines here as available

    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_clients, my_mission_record, 0, "%s-%d" % ('Moshe', i) )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print "Error starting mission", (i+1), ":",e
                exit(1)
            else:
                time.sleep(2)
    
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text


##########################Getting the environment##################
    
#This is where we will implement our mission. The General idea is to make our
#perfom simple task like go to the green block and redblock an so on and so on.
#What we currently have is a classifier that determines whether the user_input
#is a Command/Question/Statement. 
    grid = load_grid(world_state)
    objects_pos, legal_pos = remove_air(grid) #object pos 
    print('object position: {}'.format(objects_pos))
    print('legal_pos position: {}'.format(legal_pos))
###############################################################################
    user_input = None
    #####Initial source =====>
    source = 3280
    single_commands = ['jump','Jump',]

    runCount =0


    while(user_input != "Quit"):
        runCount +=1
        print('runCount = {}'.format(runCount))
        agentLocation = get_obj_locations(agent_host)


        for k, v in agentLocation.items():
            print 'start round {}: ({}, {}, {})'.format(runCount, v[0], v[1], v[2])
       

        #THIS IS NOT THE SAME ANYMORE
        user_input = raw_input("Please enter a command: ")
        list_of_tags = classify.tagger(user_input)
        action = classify.get_action(list_of_tags)
        print("_________________________________________________")
        print("ACTION: {}".format(action))
        obj = classify.get_object(list_of_tags)
        print("OBJECT: {}".format(obj))
        adj = classify.get_adjective(list_of_tags)
        print("Discription: {}".format(adj))
        result = learner.classify(user_input)
        print("TYPE OF SENTENCE: {}".format(result))
        print("_________________________________________________")
        
###############################################################################
############## SIMPLE ACTIONS LIKE JUMP/MOVE LEFT/MOVE RIGHT ##################
###############################################################################
    


#####Quantity of something can be added by extracting the tag CD
                
        if result == 'Command':
            if user_input == "Jump" or user_input == "jump":
                agent_host.sendCommand("jump 1")
                world_state = agent_host.getWorldState()
                

            
            if obj == "right" or obj == "Right":
                temp_source = source - 1
                #CHECKS IF YOU DONT FALL
                if temp_source in legal_pos:
                    agent_host.sendCommand("movewest 1")
                    world_state = agent_host.getWorldState()
                    source = source - 1
                else:
                    print("If i make another right I will Fall to my death")
                
            if obj == "left" or obj == "Left":
                temp_source = source + 1
                #CHECKS IF YOU DONT FALL
                if temp_source in legal_pos:
                    agent_host.sendCommand("moveeast 1")
                    world_state = agent_host.getWorldState()
                    source = source + 1
                else:
                    print("If I make another left I will fall to my death")

            
            #THIS HAPPENS IF USER KNOWS THE EXACT NAME OF THE OBJECT
            if obj in objects_pos.keys():
                print("GOOOOOOD")
                dest = objects_pos[obj]
                print("Start: ", source)
                print("End: ", dest)
                print("Shortest Path: ")
                path, source = dijkstra_shortest_path(grid, source, dest)  # implement this
                action_list = extract_action_list_from_path(path)
                action_index = 0
                print("New Start: ", source)
                while (action_index != len(action_list)):
                    time.sleep(0.1)
                    agent_host.sendCommand(action_list[action_index])
                    action_index += 1
                    world_state = agent_host.getWorldState()
                print(action_list)
                agentLocation = get_obj_locations(agent_host)
                print("After finish dijtra's")
                print(agentLocation)
            #Formal descriptions    
            else:
                if adj != None:
                    #agent will try to understand the description
                    adj_obj = adj + " " +obj
                    #determines if the adjective + the noun refers to an object
                    #in the enviroment
                    exact_obj = object_learner.classify(adj_obj)
                    print(exact_obj)
                    if exact_obj in objects_pos.keys():
                        dest = objects_pos[exact_obj]
                        print("Start: ", source)
                        print("End: ", dest)
                        print("Shortest Path: ")
                        path, source = dijkstra_shortest_path(grid, source, dest)  # implement this
                        action_list = extract_action_list_from_path(path)
                        action_index = 0
                        print("New Start: ", source)
                        while (action_index != len(action_list)):
                            time.sleep(0.1)
                            agent_host.sendCommand(action_list[action_index])
                            action_index += 1
                            world_state = agent_host.getWorldState()
                        print(action_list)
##                        agentLocation = get_obj_locations(agent_host)
##                        print(agentLocation)
                else:
                    pass
                    #print("I cant find that item: Sorry!!")
                ##id object not in the enviroment
        if result == 'Question':
            print("Good Question!! I dont know the answer to that. But give me a command")
        if result == 'Statement':
            print("Good Statement!! But give me a command")


    while world_state.is_mission_running:
        #sys.stdout.write(".")
        time.sleep(0.1)
        #command = raw_input("PLease enter a command: ")
        # Sending the next commend from the action list -- found using the Dijkstra algo.
        if action_index >= len(action_list):
            print "Error:", "out of actions, but mission has not ended!"
            time.sleep(2)
        else:
            agent_host.sendCommand(action_list[action_index])
        action_index += 1
        if len(action_list) == action_index:
            # Need to wait few seconds to let the world state realise I'm in end block.
            # Another option could be just to add no move actions -- I thought sleep is more elegant.
            time.sleep(2)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text

    print
    print "Mission", (i+1), "ended"
    # Mission has ended.
