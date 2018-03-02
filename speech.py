import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = input("provide sentence: ") #for the prototype a sentence is given, but can be changed to given sentence
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
store = list();
verbs = {
        'VB': 1,
        'VBD': 1,
        'VBG' : 1,
        'VBN' : 1,
        'VBP' : 1,
        'VBZ' : 1
    }
for i in range(0,len(tagged)):
    if (verbs.get(tagged[i][1],'0') == 1) :  
        store.append(tagged[i][0])
print (store)
print(tagged)
