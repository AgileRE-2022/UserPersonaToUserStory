import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
from nltk.stem import SnowballStemmer
ps = SnowballStemmer(language='english')

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

def postag(needsInput, goalsInput):
    #needsInput = "I need a good feature. I want"
    #goalsInput = "I may sleep"
    needs = sent_tokenize(needsInput)
    goals = sent_tokenize(goalsInput)
    listNeeds = needs
    listGoals = goals
    retval = []
    arrNeeds = []
    for needs in listNeeds:
        tokensNeeds = nltk.word_tokenize(needs)
        postagNeeds = nltk.pos_tag(tokensNeeds, tagset='universal')
        #print(postagNeeds)
        postagNeeds2 = [list(i) for i in zip(*postagNeeds)]
        for i in postagNeeds2:
            if "." in i:
                i.remove('.')
            elif "!" in i:
                i.remove('!')
            elif "?" in i:
                i.remove('?')
        arrNeeds.append(postagNeeds2)
        
    #print(arrNeeds)
    finalNeeds = []
    for postagNeeds2 in arrNeeds:
        if(adjNoun(postagNeeds2)!="[ERROR DETECTED: Format not supported]"):
            resNeeds = ["I want a",adjNoun(postagNeeds2)]
            finalNeeds.append(resNeeds)
        else:
            resNeeds = ["I want a",Noun(postagNeeds2)] #INI harusnya array
            finalNeeds.append(resNeeds)
            
    #print(finalNeeds)

    arrGoals = []

    for goals in listGoals:
        tokensGoals = nltk.word_tokenize(goals)
        postagGoals = nltk.pos_tag(tokensGoals, tagset='universal')
        #print(postagGoals)
        postagGoals2 = [list(i) for i in zip(*postagGoals)]
        for i in postagGoals2:
            if "." in i:
                i.remove('.')
            elif "!" in i:
                i.remove('!')
            elif "?" in i:
                i.remove('?')
        arrGoals.append(postagGoals2)
        
    #print(arrGoals)
    finalGoals = []
    for postagGoals2 in arrGoals:
        if(Verb(postagGoals2)!=None):
            resGoals = ["so that I can",Verb(postagGoals2)] 
            finalGoals.append(resGoals)
        else:
            resGoals = ["[ERROR DETECTED: Format not supported]"]
    #    print("HASIL".center(60,"─"))
        
    #print(finalGoals)

    finalHasil = []
    i=0
    for a in resNeeds,resGoals:
        while i<len(finalGoals) and i<len(finalNeeds):
            hasil = ["As a user,"]+finalNeeds[i]+finalGoals[i]
            finalHasil.append(hasil)
            i=i+1
    #print(finalHasil)

    a = []

    for hasil in finalHasil:
        if None not in hasil:
            retv =" ".join([str(item) for item in hasil]) 
            a.append(retv)
            retval = ';\n'.join([str(elem) for elem in a]) #TAPI GAK NGE ENTER
        # if "[ERROR DETECTED: Format not supported]" not in hasil:
        #     print(" ".join([str(item) for item in hasil])) 
        else:
            retval = "No user story generated. Please use the supported format!"
    
    return retval