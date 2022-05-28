import nltk
import string

needs = "The application to teach and find new places that I can travel to"
goals = "I can find out about the new places I am traveling to"
tokensNeeds = nltk.word_tokenize(needs)
postagNeeds = nltk.pos_tag(tokensNeeds)
#print(postagNeeds)
postagNeeds2 = [list(i) for i in zip(*postagNeeds)]
tokensGoals = nltk.word_tokenize(goals)
postagGoals = nltk.pos_tag(tokensGoals)
#print(postagGoals)
postagGoals2 = [list(i) for i in zip(*postagGoals)]
      
def adjNoun(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "JJ" and "NN" in token2:
                    indeks = token2.index("JJ")
                    while(indeks<len(token2)):
                        print(token[indeks],end=' ')
                        indeks = indeks+1
                    return("")
    except ValueError:
        return ("")
    
def verbNoun(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "VBP" and "NN" in token2:
                    indeks = token2.index("VBP")
                    while(indeks<len(token2)):
                        print(token[indeks],end=' ')
                        indeks = indeks+1
                    return("")
    except ValueError:
        print("")

def Noun(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "NN" in token2:
                    indeks = token2.index("NN")
                    while(indeks<len(token2)):
                        print(token[indeks],end=' ')
                        indeks = indeks+1
                    return("")
    except ValueError:
        print("")
            
def Verb(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "VB" in token2:
                    indeks = token2.index("VB")
                    while(indeks<len(token2)):
                        print(token[indeks],end=' ')
                        indeks = indeks+1
                    return("")
    except ValueError:
        print("Tidak ada verb")

import string

def is_header(line):
    return line.startswith(string.punctuation)

print("AS A USER,".center(60,"─"))

# if(adjNoun(postagNeeds2)!=None or Noun(postagNeeds2)!=None):
print("I WANT A...".center(60,"─"))
adjNoun(postagNeeds2),print("")
Noun(postagNeeds2),print("")
# if(verbNoun(postagNeeds2)!=None or Verb(postagNeeds2)!=None):
print("I WANT TO...".center(60,"─"))
verbNoun(postagNeeds2),print("")
Verb(postagNeeds2),print("")
print("SO THAT I CAN...".center(60,"─"))
adjNoun(postagGoals2)
verbNoun(postagGoals2)
Noun(postagGoals2)
Verb(postagGoals2)



"""
CC coordinating conjunction 
CD cardinal digit 
DT determiner 
EX existential there (like: “there is” … think of it like “there exists”) 
FW foreign word 
IN preposition/subordinating conjunction 
JJ adjective – ‘big’ 
JJR adjective, comparative – ‘bigger’ 
JJS adjective, superlative – ‘biggest’ 
LS list marker 1) 
MD modal – could, will 
NN noun, singular ‘- desk’ 
NNS noun plural – ‘desks’ 
NNP proper noun, singular – ‘Harrison’ 
NNPS proper noun, plural – ‘Americans’ 
PDT predeterminer – ‘all the kids’ 
POS possessive ending parent’s 
PRP personal pronoun –  I, he, she 
PRP$ possessive pronoun – my, his, hers 
RB adverb – very, silently, 
RBR adverb, comparative – better 
RBS adverb, superlative – best 
RP particle – give up 
TO – to go ‘to’ the store. 
UH interjection – errrrrrrrm 
VB verb, base form – take 
VBD verb, past tense – took 
VBG verb, gerund/present participle – taking 
VBN verb, past participle – taken 
VBP verb, sing. present, non-3d – take 
VBZ verb, 3rd person sing. present – takes 
WDT wh-determiner – which 
WP wh-pronoun – who, what 
WP$ possessive wh-pronoun, eg- whose 
WRB wh-adverb, eg- where, when
"""