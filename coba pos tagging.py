#coba pos tagging
# from nltk.tag import CRFTagger
# ct = CRFTagger()
# ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

# text = "Celya pergi ke Korea untuk membeli makan."
# post_tag = ct.tag_sents([text.split()])
# post_tag = post_tag[0]
# print(post_tag)

# #hasil = ct.tag_sents([['Saya','tidur','di','Rumah']])
# #print(hasil)

# # Perform standard imports
# import spacy
# nlp = spacy.load('en_core_web_sm')
# doc = nlp("I want to buy something but I don't have money.")
# #print(doc[4].text,"|",doc[4].pos_,"|",doc[4].tag_,"|",spacy.explain(doc[4].tag))
#                                                                  ##kata kelima
# for token in doc:
#     print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')

import nltk
import string
import re #regex

needs = "A site that will simplify the planning of my business trips"
tokens = nltk.word_tokenize(needs)
postag = nltk.pos_tag(tokens)
gabung = " ".join([str(item) for item in postag])
gabung = gabung.translate(str.maketrans('', '', string.punctuation))
token2 = nltk.word_tokenize(gabung)
#print(token2)
if gabung.find("NN")!=0: #INI KALAU AWALANNYA NOUN
    kalimat = gabung[:gabung.index("NN")]
    kalimat = kalimat.split()
    kata = kalimat[-1]
    #print(kata) << biar tau kata apa sebelum si NN
    # KALAU CARA INI NGEHAPUS YG AWALANNYA KAPITAL V
    # temp = gabung.split()
    # gabung = " ".join([ele for ele in temp if not ele[0].isupper()])
    gabung = re.sub(r'\b[A-Z]+\b', '', gabung) #ngehapus yg semuanya caps
    output = kata,gabung.split(kata,1)[1]
    output =  "".join([str(item) for item in output]) #join tuple output
    output = re.sub("\s\s+", " ", output)
    print("I want a",output) #biar spasinya gk jelek ok

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