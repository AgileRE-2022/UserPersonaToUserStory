import nltk
from nltk.stem import SnowballStemmer
ps = SnowballStemmer(language='english')

"""
RULES:
1) System will detect [NEEDS] with either ADJ+NOUN or NOUN
    Verb 1 sometimes is detected as NOUN, resulting an incorrect user story
2) Please refrain using VERB - system will most likely create an incorrect result
3) You must put VERB in [GOALS] at THE VERY START OF THE SENTENCE
4) In short, the supported format is:
   [NEEDS] SUBJECT+VERB+ADJ+NOUN/NOUN
   [GOALS] VERB
"""
def adjNoun(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "ADJ" and "NOUN" in token2:
                    indeks = token2.index("ADJ")
                    hasil = []
                    if token2.index("ADJ")<token2.index("NOUN"):
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
                if "VERB" in token2:
                    indeks = token2.index("VERB")
                    hasil = [ps.stem(token[indeks])]
                    while(indeks+1<len(token2)):
                        b = token[indeks+1]
                        hasil.append(b)
                        indeks = indeks+1
                    return(" ".join([str(item) for item in hasil]))
    except ValueError:
        return("[ERROR DETECTED: Format not supported]")

def Noun(teks):
    try:
        for token in teks:
            for token2 in teks:
                if "NOUN" in token2:
                    indeks = token2.index("NOUN")
                    hasil = []
                    while(indeks<len(token2)):
                        b = token[indeks]
                        hasil.append(b)
                        indeks = indeks+1
                    return(" ".join([str(item) for item in hasil]))
    except ValueError:
        return("[ERROR DETECTED: Format not supported]")

def postag(needs, goals):
    #needs = "I love a good design"
    #goals = "To understand more about the app"
    tokensNeeds = nltk.word_tokenize(needs)
    postagNeeds = nltk.pos_tag(tokensNeeds, tagset='universal')
    print(postagNeeds)
    postagNeeds2 = [list(i) for i in zip(*postagNeeds)]
    tokensGoals = nltk.word_tokenize(goals)
    postagGoals = nltk.pos_tag(tokensGoals, tagset='universal')
    #print(postagGoals)
    postagGoals2 = [list(i) for i in zip(*postagGoals)]

    retval =""
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
        retval = " ".join([str(item) for item in hasil])
    else:
        retval = "No user story generated. Please use the supported format!"
    
    return retval