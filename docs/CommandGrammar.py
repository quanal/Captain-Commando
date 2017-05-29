import nltk

#Move and Cut is treated as NN in pos_tag

EXACT_MATCH = ["please","forward","backward","left","right","and"]
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
        self.go_to_initial_state();
        for inp in input_list:
            if inp in EXACT_MATCH:
                self.transition_to_state_with_input(inp)
            elif inp in verb_list:
                self.transition_to_state_with_input("verb")
            else:
                tag = nltk.pos_tag([inp])
                if tag[0][1] == 'NN' or tag[0][1] == 'NNS':
                    self.transition_to_state_with_input("noun")
                else:
                    self.transition_to_state_with_input(inp)
            continue;
        if self.in_accept_state():
            return self.current_state
        else:
            return 0
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
    tf[(1,"the")] = 4
    tf[(1,"forward")] = 7
    tf[(1,"backward")] = 7
    tf[(1,"noun")] = 6
    tf[(3,"the")] = 4
    tf[(4,"noun")] = 6
    tf[(4,"left")] = 5
    tf[(4,"right")] = 5

    return tf
    
##############################################################################################
if __name__ == '__main__':
    verb_set = get_all_the_verb("verb.txt")
    states = {0,1,2,3,4,5,6,7}
    
    tf = {}
    tf[(0,"please")] = 2
    tf[(0,"verb")] = 1
    tf[(2,"verb")] = 1
    tf[(1,"to")] = 3
    tf[(1,"the")] = 4
    tf[(1,"forward")] = 7
    tf[(1,"backward")] = 7
    tf[(1,"noun")] = 6
    tf[(3,"the")] = 4
    tf[(4,"noun")] = 6
    tf[(4,"left")] = 5
    tf[(4,"right")] = 5
    start_state = 0
    accept_states = {5,6,7}
    
    dfa = DFA(states,tf,0,{5,6,7})

    user_input = raw_input("Please enter command: ")
    while user_input != 'quit':
        print dfa.run_with_input_list(user_input.split(),verb_set)
        user_input = raw_input("Please enter command: ")

        
