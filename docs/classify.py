import nltk
from nltk.corpus import brown
from textblob.classifiers import NaiveBayesClassifier

##TODO: tagger - classify each word meaning in a sentence

"""Function Uses taggers to identify the type of word (Part of Speech)"""
def main():
    while(1):
        command = raw_input("Please Enter a Command: ")
        list_of_tags = tagger(command)
        print (list_of_tags)
        action = get_action(list_of_tags)
        print(action)
        obj = get_object(list_of_tags)
        print (obj)
        adj = get_adjective(list_of_tags)
        print(adj)



"""Input: a String that represents the command
Ouput: a list of each word and its tag"""
def tagger(command):
    text = nltk.word_tokenize(command)
    Tags = nltk.pos_tag(text)
    return Tags


""""Get the action from the sentence"""
def get_action(list_of_tags):
    for tup in list_of_tags:
        if tup[1] == 'VBP' or tup[1] == 'VB' or tup[1] == 'VBD' :
            return tup[0]

"""Gets the object from the sentence"""
def get_object(list_of_tags):
    list_of_nouns = []
    for tup in list_of_tags:
        if tup[1] == 'NN' or tup[1]=='NNS':
            list_of_nouns.append(tup[0])
    if len(list_of_nouns) == 0:
        return "There is no noun"
    else:
        return list_of_nouns[-1]

def get_adjective(list_of_tags):
    for tup in list_of_tags:
        if tup[1] == 'JJ':
            return tup[0]
    
if __name__ == '__main__':
    main()
