import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.word2vec import Word2Vec
import nltk
from nltk.corpus import brown
from textblob.classifiers import NaiveBayesClassifier
import classify
import nltk



EXACT_MATCH = ["please","forward","backward","and"]
############################################################################################
###### CLASS FINITE AUTOMATA ###############################################################

#Acceptance State:  7: go backward/foward
#                   6: verb + (to + the) +  noun (example: create carrot, go to the house, cut the tree)
#                   5: go left/right

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
            #print counter
            #print inp
            if inp in EXACT_MATCH:
                self.transition_to_state_with_input(inp)
                nouna = inp
            elif inp in verb_list:
                verba = inp
                self.transition_to_state_with_input("verb")
            else:
                tag = nltk.pos_tag([inp])
                #print(tag)
                if tag[0][1] == 'NN' or tag[0][1] == 'NNS':
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


################################################################################


def main():
    """FINITE STATE MACHINE"""
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

    print("Loading data...")
    """Loads the data"""
    model = KeyedVectors.load_word2vec_format('C:\Users\Wicho\Malmo-0.21.0-Windows-64bit\Malmo-0.21.0-Windows-64bit\Python_Examples\GoogleNews-vectors-negative300.bin.gz', binary=True)
    results = model.most_similar(positive=['puppy', 'cat'], negative=['dog'], topn=5)
    print(results)

    sim = model.similarity('woman','man')
    print(sim)
    word = None
    ###we can have a list of items here.

    Malmo_actions = ['move','strafe','pitch','turn','jump','crouch','attack','use']
    Malmo_objects = ['stone','left','right','forward', 'backward','block', 'pig', 'dragon','tree','wood','water', 'car']
    user_input = raw_input("Please enter command: ")
    while user_input != 'quit':
        num, verba, nouna, adja= dfa.run_with_input_list(user_input.split(),verb_set)
        print ("___________________________________________________________")
        print ("State: {}    Verb: {}     Noun: {}      Adjective: {}".format(num, verba, nouna, adja))
        print ("___________________________________________________________")


##        command = raw_input("Please Enter a Command: ")
##        list_of_tags = classify.tagger(command)
##        print (list_of_tags)
##        action = classify.get_action(list_of_tags)
##        print("Action: {}".format(action))
##        obj = classify.get_object(list_of_tags)
##        print ("Object: {}".format(obj))
##        adj = classify.get_adjective(list_of_tags)
##        print("Adjective: {}".format(adj))
        if verba != None:
            print("Action comparison to {}".format(verba))
            for act in Malmo_actions:
                sim = model.similarity(verba,act)
                print("Similarity to {}: {}".format(act,sim))

        if nouna != None:
            print("")
            print("Object comparison to {}".format(nouna))
            for obj in Malmo_objects:
                sim = model.similarity(nouna,obj)
                print("Similarity to {}: {}".format(obj,sim))

        else:
            print("There was no detected verb or noun!!!")

        user_input = raw_input("Please enter command: ")
                
        
 

if __name__=='__main__':

    main()
