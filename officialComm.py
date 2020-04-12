#given the body of the article
#use POS tagging to find official statement

import en_core_web_sm
from spacy.matcher import Matcher

nlp = en_core_web_sm.load()
pPt = Matcher(nlp.vocab)

pPt.add("pat1",None,
        [{"POS": "PROPN"},{"POS": "PUNCT", "OP":"?"}, {"POS": "DET", "OP":"?"},{"LEMMA": {"IN": [
                            "director","engineer","governer","mayor","manager",
                           "official","CEO","COO","commissioner","spokesperson",
                           "spokeswoman","spokesman","representative", "chief", "coordinator"]}}]
        )
pPt.add("pat2",None,
        [{"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued", "warned"]}},
        {"POS":"NOUN","OP":"*"},{"LEMMA": {"IN": ["director","engineer","governer","mayor","manager",
                           "official","CEO","COO","commissioner","spokesperson",
                           "spokeswoman","spokesman","representative","cheif","coordinator"]}}]
        )
pPt.add("pat3",None,[{"LEMMA": {"IN": ["official","Official"]}},
                     {"LEMMA": {"IN": ["announce", "hazard", "say", "stated", "issued","warned"]}}]) #lemmatized words (said/discussed/etc.)

pPt.add("pat4",None,
        [{"LEMMA": {"IN": ["According", "according"]}}])


def convertScrapedtoSent(splitContent):
    tokenizedSent = []
    #tokenize
    NLPtxt = nlp(splitContent)
    for eachSent in NLPtxt.sents:
        tokenizedSent.append(eachSent.string.strip())
    return tokenizedSent


def officialComment(articleBody):
    results = []
    people = []
    for para in articleBody:
        temp = convertScrapedtoSent(para)
        for sent in temp:
            nER = nlp(sent)

            matchesInSent = pPt(nER)
            lowersent = nlp(sent.lower())
            secondMatch = pPt(lowersent)
            if matchesInSent or secondMatch: 
                for entity in nER.ents:
                    if entity.label_=="PERSON":
                        people.append(entity.text)
                results.append(sent)
    return results, people





