
import nltk
from nltk.corpus import brown
from textblob.classifiers import NaiveBayesClassifier
import classify


EXACT_MATCH = ["please","forward","backward","and"]
class DFA:
    current_state = None;
    def __init__(self, states, transition_function, start_state, accept_states):
        self.states = states;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;
    
    def in_accept_state(self):
        return self.current_state in self.accept_states;
    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;

    def run_with_input_list(self, input_list, verb_list):
        nouna = None
        verba = None
        adja = None
        #print(len(input_list))
        counter = 0 
        self.go_to_initial_state();
        
        for inp in input_list:
            #print(nltk.pos_tag([inp]))
            counter += 1
           # print counter
           # print inp
            if inp in EXACT_MATCH:
                self.transition_to_state_with_input(inp)
                nouna = inp
            elif inp in verb_list:
                verba = inp
               # print(verba)
                self.transition_to_state_with_input("verb")
            else:
                tag = nltk.pos_tag([inp])
                #print(tag)
                if tag[0][1] == 'NN' or tag[0][1] == 'NNS':
                    #print("why")
                    if counter == len(input_list):
                        self.transition_to_state_with_input("noun")
                        nouna = tag[0][0]
                    elif counter != len(input_list):
                        self.transition_to_state_with_input("adj")
                        adja = tag[0][0]                        
                elif tag[0][1] == 'JJ' or tag[0][1] == 'JJS':
                    self.transition_to_state_with_input("adj")
                    adja = tag[0][0]
                else:
                    self.transition_to_state_with_input(inp)

            continue;
        if self.in_accept_state():
            return self.current_state, verba, nouna, adja
        else:
            return 0, None, None, None 
    pass;

#############################################################################################
def get_all_the_verb(file_name):
    #The function will take a txt file of all the verb and
    #put all the verb into a set
    verb_set = set()
    try:
        data = open(file_name,'r')
        for line in data:
            verb_set.add(line.split()[1])
        return verb_set
    except:
        print("file not found")

def extract_command_input(command, accept_state):
    #This function base on what acceptance state of DFA
    #to determine the input command
    action_dict = {"go":"go","move":"go","get":"go","destroy":"atk","cut":"atk"}
    command_word_list = command.split()
    return [action_dict[command_word_list[0]],command_word_list[-1]]

def create_transition_function():
    tf = {}
    tf[(0,"please")] = 2
    tf[(0,"verb")] = 1
    tf[(2,"verb")] = 1
    tf[(1,"to")] = 3  
    tf[(1,"the")] = 8 
    tf[(1,"a")] = 8
    tf[(1,"an")] = 8
    tf[(8,"noun")] = 9 
    tf[(1,"forward")] = 7
    tf[(1,"backward")] = 7
    tf[(1,"noun")] = 6
    tf[(3,"the")] = 4
    tf[(4,"adj")] = 10
    tf[(8,"adj")] = 12
    tf[(12,"noun")] = 13
    tf[(10,"noun")] = 11
    tf[(4,"noun")] = 6
    tf[(4,"left")] = 5
    tf[(4,"right")] = 5

    return tf
    

test_data=dict()
test_data["go to the park"] = ['go',None,'park']
test_data["go to the red car"] = ['go','red','car']
test_data["go to the pink pig"] = ['go','pink','pig']
test_data["move to the left"] = ['move',None,'left']
test_data["make a beautiful sword"] = ['make','beautiful','sword']
test_data["attack the fat pig"] = ['attack','fat','pig']
test_data["destroy the red stone"] = ['destroy','red','stone']
test_data["move forward"] = ['move',None,'forward']
test_data["please craft an amazing plane"] = ['craft','amazing','plane']
test_data["go to the blue water"] = ['go','blue','water']

test_data["jump to the block"] = ['jump',None,'block']
test_data["please look at the green text"] = ['look','green','text']
test_data["find the best thing"] = ['find','best','thing']
test_data["destroy the strongest animal"] = ['destroy','strongest','animal']
test_data["fight the ugliest monster"] = ['fight','ugliest','monster']
test_data["attack the horse"] = ['attack',None,'horse']
test_data["create a golden stone"] = ['create','golden','stone']
test_data["move backward"] = ['move',None,'backward']
test_data["please run to the door"] = ['run',None,'door']
test_data["draw a long path"] = ['draw','long','path']

test_data["find the closest person"] = ['find','closest','person']
test_data["remove the pretty bird"] = ['remove','pretty','bird']
test_data["please avoid the lava"] = ['avoid',None,'lava']
test_data["go to the farthest block"] = ['go','farthest','block']
test_data["make a left"] = ['make',None,'left']
test_data["battle the strongest beast"] = ['battle','strongest','beast']
test_data["bounce forward"] = ['bounce',None,'forward']
test_data["call the person"] = ['call',None,'person']
test_data["move to the edge"] = ['move',None,'edge']
test_data["please cure the blue bird"] = ['cure','blue','bird']

test_data["build the tallest house"] = ['build','tallest','house']
test_data["clean the whole house"] = ['clean','whole','house']
test_data["carry the fullest box"] = ['carry','fullest','box']
test_data["choose the best path"] = ['choose','best','path']
test_data["hit the cat"] = ['hit',None,'cat']
test_data["kick the skinny dog"] = ['kick','skinny','dog']
test_data["follow the horse"] = ['follow',None,'horse']
test_data["come to the green stone"] = ['come','green','stone']
test_data["buy the cheapest car"] = ['buy','cheapest','car']
test_data["grab the golden sword"] = ['grab','golden','sword']

test_data["shower in the water"] = ['shower',None,'water']
test_data["go to the next mission"] = ['go','next','mission']
test_data["break the wall"] = ['break',None,'wall']
test_data["move to the best position"] = ['move','best','position']
test_data["carry the person"] = ['carry',None,'person']
test_data["jump forward"] = ['jump',None,'forward']
test_data["hop backward"] = ['hop',None,'backward']
test_data["navigate to the hot lava"] = ['navigate','hot','lava']
test_data["please come to the nearest wall"] = ['come','nearest','wall']
test_data["turn to the right"] = ['turn',None,'right']

test_data["turn to the left"] = ['turn',None,'left']
test_data["use the golden sword"] = ['use','golden','sword']
test_data["use the best weapon"] = ['use','best','weapon']
test_data["ignore the lava"] = ['ignore',None,'lava']
test_data["please use the best car"] = ['use','best','car']
test_data["make a stop"] = ['make',None,'stop']
test_data["skate to the park"] = ['skate',None,'park']
test_data["move to the truck"] = ['move',None,'truck']
test_data["please kill the cat"] = ['kill',None,'cat']
test_data["please grab the shinny object"] = ['grab','shinny','object']

test_data["turn the block"] = ['turn',None,'block']
test_data["craft the biggest wall"] = ['craft','biggest','wall']
test_data["go to the future"] = ['go',None,'future']
test_data["destroy the computer"] = ['destroy',None,'computer']
test_data["attack the wall"] = ['attack',None,'wall']
test_data["crouch to the botttom floor"] = ['crouch','botttom','floor']
test_data["use the shield"] = ['use',None,'shield']
test_data["turn forward"] = ['turn',None,'forward']
test_data["turn backward"] = ['turn',None,'backward']
test_data["make a nice dog"] = ['make','nice','dog']

test_data["please attack the house"] = ['attack',None,'house']
test_data["please destroy the house"] = ['destroy',None,'house']
test_data["wear the best hat"] = ['wear','best','hat']
test_data["put the yellow shorts"] = ['put','yellow','shorts']
test_data["wear the gray helmet"] = ['wear','gray','helmet']
test_data["make a turn"] = ['make',None,'turn']
test_data["make the biggest jump"] = ['make','biggest','jump']
test_data["go to the fastest car"] = ['go','fastest','car']
test_data["please make the hardest test"] = ['make','hardest','test']
test_data["please find the cat"] = ['find',None,'cat']

test_data["go to the start"] = ['go',None,'start']
test_data["use the cute shield"] = ['use','cute','shield']
test_data["grab the fat pig"] = ['grab','fat','pig']
test_data["please use the new block"] = ['use','new','block']
test_data["please punch the hardest rock"] = ['punch','hardest','rock']
test_data["punch the tree"] = ['punch',None,'tree']
test_data["destroy the tallest building"] = ['destroy','tallest','building']
test_data["cut the tall tree"] = ['cut','tall','tree']
test_data["fight the snowman"] = ['fight',None,'snowman']
test_data["run to the nearest toy"] = ['run','nearest','toy']

test_data["craft the best sword"] = ['craft','best','park']
test_data["break the tree"] = ['break',None,'tree']
test_data["separate the red blocks"] = ['separate','red','blocks']
test_data["smash the golden block"] = ['smash','golden','block']
test_data["make a beautiful sword"] = ['make','beautiful','sword']
test_data["run to the house"] = ['run',None,'house']
test_data["stop the pig"] = ['stop',None,'pig']
test_data["smash the tree"] = ['smash',None,'tree']
test_data["race to the finish line"] = ['race','finish','line']
test_data["please go to the class"] = ['go',None,'class']




def main():
    verb_set = get_all_the_verb("verb.txt")
    states = {0,1,2,3,4,5,6,7,8,9,10,11,12,13}
    
    tf = {}
    tf[(0,"please")] = 2
    tf[(0,"verb")] = 1
    tf[(2,"verb")] = 1
    tf[(1,"to")] = 3
    tf[(1,"forward")] = 7
    tf[(1,"backward")] = 7
    tf[(1,"noun")] = 6
    tf[(3,"the")] = 4
    tf[(4,"noun")] = 6
    tf[(4,"left")] = 5
    tf[(4,"right")] = 5
    tf[(1,"the")] = 8
    tf[(1,"a")] = 8###
    tf[(1,"an")] = 8 ###i made these new states
    tf[(8,"noun")] = 9###
    tf[(4,"adj")] = 10
    tf[(10,"noun")] = 11
    tf[(8,"adj")] = 12
    tf[(12,"noun")] = 13
    start_state = 0
    accept_states = {5,6,7,1,9,11,13}
    
    dfa = DFA(states,tf,0,{1,5,6,7,9,11,13})

    
    pos_value = [None,None,None]
    dfa_value = [None,None,None]
    POS_score = 0
    DFA_score = 0
    for sentence, expected_value in test_data.iteritems():
        #print (sentence)
        list_of_tags = classify.tagger(sentence)
        #print(list_of_tags)
        
        action = classify.get_action(list_of_tags)
        #print("Action: {}".format(action))
        pos_value[0] = action
        
        adj = classify.get_adjective(list_of_tags)
        #print("Adjective: {}".format(adj))
        pos_value[1] = adj
        
        obj = classify.get_object(list_of_tags)
        #print ("Object: {}".format(obj))
        pos_value[2] = obj
        
        #print("POS RESULT: {}".format(pos_value))

        num, verba, nouna, adja= dfa.run_with_input_list(sentence.split(),verb_set)
        #print ("State: {}    Verb: {}     Noun: {}      Adjective: {}".format(num, verba, nouna, adja))

        dfa_value[0] = verba
        dfa_value[1] = adja
        dfa_value[2] = nouna
        
        
        if pos_value == expected_value:
            #print(True)
            POS_score += 1
                
        if dfa_value == expected_value:
            #print(True)
            DFA_score += 1
    
    float(78)/100
    print("POS Tagger Average Score: {}".format(float(POS_score)/100.0))
    print("DFA Average Score: {}".format(float(DFA_score)/100.0))

    


if __name__=='__main__':
    main()
