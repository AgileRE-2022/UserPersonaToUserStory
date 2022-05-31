import nltk

"""
RULES:
1) System will detect [NEEDS] with either ADJ+NOUN or NOUN (both nouns are singular)
2) Please refrain using VERB and PLURAL NOUN in NEEDS - system will most likely create incorrect result
3) You must include VERB in [GOALS] but DO NOT use it at THE VERY START OF THE SENTENCE
4) In short, the supported format is:
   [NEEDS] ADJ+NOUN/NOUN (singular noun)
   [GOALS] Subject+modal (can, may, etc.)+VERB
"""

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
                    hasil = []
                    if token2.index("JJ")<token2.index("NN"):
                        while(indeks<len(token2)):
                            b = token[indeks]
                            hasil.append(b)
                            indeks = indeks+1
                        return(" ".join([str(item) for item in hasil]))
                    else:
                        return Noun(teks)
    except ValueError:
        return("[ERROR DETECTED: Format not supported]")

def Verb(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "VB" in token2:
                    indeks = token2.index("VB")
                    hasil = []
                    while(indeks<len(token2)):
                        b = token[indeks]
                        hasil.append(b)
                        indeks = indeks+1
                    return(" ".join([str(item) for item in hasil]))
    except ValueError:
        return("[ERROR DETECTED: Format not supported]")

def Noun(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "NN" in token2:
                    indeks = token2.index("NN")
                    hasil = []
                    while(indeks<len(token2)):
                        b = token[indeks]
                        hasil.append(b)
                        indeks = indeks+1
                    return(" ".join([str(item) for item in hasil]))
    except ValueError:
        return("[ERROR DETECTED: Format not supported]")
            

print("AS A USER,".center(60,"─"))

#if(adjNoun(postagNeeds2)!=None or Noun(postagNeeds2)!=None or Verb(postagNeeds2)!=None):
if(Noun(postagNeeds2)!=None):
    print("I WANT...".center(60,"─"))
    if(adjNoun(postagNeeds2)!="[ERROR DETECTED: Format not supported]"):
        resNeeds = ["I want a",adjNoun(postagNeeds2)]
        print(adjNoun(postagNeeds2)),print("")
    else:
        resNeeds = ["I want a",Noun(postagNeeds2)] #INI PRIORITAS VERB DI BAWAH
        print(Noun(postagNeeds2)),print("")
    # elif(Verb(postagNeeds2)!=None):
    #     #print("I WANT TO...".center(60,"─"))
    #     resNeeds = ["I want to",Verb(postagNeeds2)]
    #     print("I want to",Verb(postagNeeds2)),print("")
    # ^^^^ IF ELSE GAK JALAN JADI NANGKAP ERROR AJA --> WAJIB ADJ+NOUN
else:
    resNeeds = ["[ERROR DETECTED: Format not supported]"]       
print("SO THAT I CAN...".center(60,"─"))
# print(adjNoun(postagGoals2))
# print(verbNoun(postagGoals2))
# print(Noun(postagGoals2))
if(Verb(postagGoals2)!=None):
    resGoals = ["so that I can",Verb(postagGoals2)] #entah kenapa kalau error, errornya gak ketangkep
    print(Verb(postagGoals2))
# elif(verbNoun(postagGoals2)!=None): #ternyata kalau "Order a lot", order kehitung CC/konjungsi di nltk
#     #DONT USE VERB AT THE START OF THE SENTENCE
#     resGoals = ["so that I can",verbNoun(postagGoals2)] #entah kenapa kalau error, errornya gak ketangkep
#     print("so that I can",verbNoun(postagGoals2))
else:
    resGoals = ["[ERROR DETECTED: Format not supported]"]
print("HASIL".center(60,"─"))
hasil = ["As a user,"]+resNeeds+resGoals
if "[ERROR DETECTED: Format not supported]" not in hasil:
    print(" ".join([str(item) for item in hasil])) #apa perlu .upper()?
else:
    print("No user story generated. Please use the supported format!")



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