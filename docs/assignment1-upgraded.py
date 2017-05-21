# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #7: The Maze Decorator

import MalmoPython
import os
import sys
import time
import json
import math
import random
from priority_dict import priorityDictionary as PQ

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  #  flush print output immediately

command = [('pick','carrot'), ('go', 'planks')]



#This is sets of testing items, will update once code is finalized
#items= ["red_flower white_tulip", "coal", "planks spruce", "planks birch", "planks dark_oak", "rabbit", "carrot", "potato", "brown_mushroom"]
item2 = ["red_flower white_tulip", "coal", "planks spruce", "planks birch", "planks dark_oak", "rabbit", "carrot", "potato", "brown_mushroom"]
item1 = ["planks dark_oak", "rabbit", "carrot", "potato", "brown_mushroom"]
items= item1 + item2

def buildPositionList(items):
    positions=[]
    for item in items:
        positions.append((random.randint(0,18), random.randint(0,18)))
    print("prosition = {}".format(positions))
    return positions



def getItemDrawing(positions):
    d = {}
    drawing=""
    index=0

    for p in positions:
        item = items[index].split()
        
        drawing += '<DrawItem x="' + str(p[0]) + '" y="80" z="' + str(p[1]) + '" type="' + item[0]
        d[item[0]] = (p[0], 80, p[1])
        
       
        if len(item) > 1:
            drawing += '" variant="' + item[1]
            d[item[1]] = (p[0], 80, p[1])
        drawing += '" />'
        
        index += 1

    return drawing

def getSubgoalPositions(positions):
    goals=""
    for p in positions:
        goals += '<Point x="' + str(p[0]) + '" y="80" z="' + str(p[1]) + '" tolerance="1" description="ingredient" />'
    return goals


def GetMissionXML(seed, gp, size=80):
    positions = buildPositionList(items)
    
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

              <About>
                <Summary>Hello world!</Summary>
              </About>

            <ServerSection>
              <ServerInitialConditions>
                <Time>
                    <StartTime>1000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
              </ServerInitialConditions>


              <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"/>
    
    

                  <DrawingDecorator>
                    <DrawSphere x="-27" y="70" z="0" radius="30" type="air"/>
              
                    ''' + getItemDrawing(positions) + '''
                  </DrawingDecorator>

                  <MazeDecorator>
                    <Seed>'''+str(seed)+'''</Seed>
                    <SizeAndPosition width="''' + str(size) + '''" length="''' + str(size) + '''" height="10" xOrigin="-32" yOrigin="69" zOrigin="-5"/>
                  
                   <StartBlock type="emerald_block" fixedToEdge="true"/>
                    <EndBlock type="redstone_block" fixedToEdge="true"/>
                    <PathBlock type="diamond_block"/>
                    <FloorBlock type="stone"/>
                    <GapBlock type="air"/>
                    <GapProbability>'''+str(gp)+'''</GapProbability>
                    
                    <AllowDiagonalMovement>false</AllowDiagonalMovement>
                  </MazeDecorator>
                  
                  <ServerQuitFromTimeUp timeLimitMs="10000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>

              <AgentSection mode="Survival">
                <Name>CS175AwesomeMazeBot</Name>

                <AgentStart>
                     <Placement x="20" y="79" z="0.5"/>
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
                <ObservationFromSubgoalPositionList>''' + getSubgoalPositions(positions) + '''
                </ObservationFromSubgoalPositionList>
                <ObservationFromFullInventory/>

      <AgentQuitFromCollectingItem>
                    <Item type="rabbit_stew" description="Supper's Up!!"/>
                </AgentQuitFromCollectingItem>

                    <DiscreteMovementCommands/>
                    <AgentQuitFromTouchingBlockType>
                        <Block type="redstone_block"/>
                    </AgentQuitFromTouchingBlockType>
                    <ObservationFromGrid>
                      <Grid name="floorAll">
                        <min x="-40" y="-1" z="-40"/>
                        <max x="40" y="-1" z="40"/>
                      </Grid>
                  </ObservationFromGrid>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''



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

def find_start_end(grid):
    """
    Finds the source and destination block indexes from the list.

    Args
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)

    Returns
        start: <int>   source block index in the list
        end:   <int>   destination block index in the list
    """
    #------------------------------------
    #
    #   Fill and submit this code
    #
    start = 0
    end  = 0
    for i in range(len(grid)):
        if grid[i] == "emerald_block":
            start = i
        elif grid[i] == "redstone_block":
            end = i
    return (start, end)
    #-------------------------------------

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


def dijkstra_shortest_path(grid_obs, source, dest):
    """
    Finds the shortest path from source to destination on the map. It used the grid observation as the graph.
    See example on the Tutorial.pdf file for knowing which index should be north, south, west and east.

    Args
        grid_obs:   <list>  list of block types string representing the blocks on the map.
        source:     <int>   source block index.
        dest:       <int>   destination block index.

    Returns
        path_list:  <list>  block indexes representing a path from source (first element) to destination (last)
    """
    #------------------------------------
    #
    #   Fill and submit this code
    #
    predecessors = {source: float('inf')}
    visited_blocks = {source: 0}
    queue = PQ()
    queue.__setitem__(source, 0)
    goodIndices = []

    print len(grid_obs)

    for index in range(len(grid_obs)):
        if grid_obs[index] != "air":
            goodIndices.append(index)

    for index in goodIndices:
        if index != source:
            visited_blocks[index] = float('inf')

    while queue:
        blocks_to_go = []
        current_position = queue.smallest()
        del queue[current_position]

        for difference in [-81, -1, 1, 81]:
            if (current_position + difference) in goodIndices:
                blocks_to_go.append(current_position + difference)

        for block_Index in blocks_to_go:
            gap = visited_blocks[current_position] + 1
            if gap < visited_blocks[block_Index]:
                visited_blocks[block_Index] = gap
                predecessors[block_Index] = current_position
                queue.__setitem__(block_Index, gap)

    shortest_paths = []
    while dest != source:
        shortest_paths.append(dest)
        dest = predecessors[dest]
    shortest_paths.append(source)
    shortest_paths.reverse()

    return shortest_paths
    #-------------------------------------


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
    num_repeats = 10

for i in range(num_repeats):
    size =  int(36 + .5*i)
    print "Size of maze:", size
    my_mission = MalmoPython.MissionSpec(GetMissionXML("10", .2 + float(i/20.0), size), True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission.requestVideo(1280, 800)
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

    # Loop until mission starts:
    print "Waiting for the mission", (i+1), "to start ",
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        #sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text

    print


    #print "Mission", (i+1), "running."

    grid = load_grid(world_state)
    print(find_start_end(grid))
    start, end = find_start_end(grid) # implement this
    path = dijkstra_shortest_path(grid, start, end)  # implement this
    print "Shortest path: ", path
    action_list = extract_action_list_from_path(path)
    #print "Output (start,end)", (i+1), ":", (start,end)
    #print "Output (path length)", (i+1), ":", len(path)
    #print "Output (actions)", (i+1), ":", action_list

    # Loop until mission ends:
    action_index = 0
    print "Collecting ingredients..."
    while world_state.is_mission_running:

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            ob = json.loads(msg)
            #print msg
            #print ob
            #printInventory(ob)

            '''
            if u'yawDelta' in ob:
                current_yaw_delta = ob.get(u'yawDelta', 0)
                agent_host.sendCommand( "turn " + str(current_yaw_delta) )
                agent_host.sendCommand( "move " + str(1.0 - abs(current_yaw_delta)) )

            else:
                agent_host.sendCommand("move 0")
                agent_host.sendCommand("turn 0")

            
                if checkInventoryForItem(ob, "rabbit"):
                    print "Cooking the rabbit..."
                    checkFuelPosition(ob, agent_host)
                    agent_host.sendCommand("craft cooked_rabbit")
                    time.sleep(1)
                elif checkInventoryForItem(ob, "potato"):
                    print "Cooking the potato..."
                    checkFuelPosition(ob, agent_host)
                    agent_host.sendCommand("craft baked_potato")
                    time.sleep(1)
                elif checkInventoryForBowlIngredients(ob):
                    print "Crafting a bowl..."
                    agent_host.sendCommand("craft bowl")
                    time.sleep(1)
                elif checkInventoryForStewIngredients(ob):
                    print "Crafting a stew..."
                    agent_host.sendCommand("craft rabbit_stew")
                    time.sleep(1)
                

        if world_state.number_of_rewards_since_last_state > 0:
            reward = world_state.rewards[-1].getValue()
            print "Reward: " + str(reward)
            total_reward += reward
        world_state = agent_host.getWorldState()

        '''
        #sys.stdout.write(".")
        time.sleep(0.1)

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



