from flask import Flask
import spacy
import negspacy
from negspacy.negation import Negex
neg=Flask(__name__)
@neg.route("/")
def nolikewords(strng):
    wordsLikeNo=['deny','denies','denied','contradict','contradicted','contradicts','refuse','refused','refuses',
                 'dismiss','dismissed','dismisses','disaprove','disaproved','disaproves','repudiate','repudiates',
                 'repudiated','decline','declines','declined','negate','negates','negated','nullify','nullified',
                 'nullifies','unrelated','disagreed','disagree','disagrees','illogical']
    for word in wordsLikeNo:
        if word in strng:
            strng=strng.replace(word, 'no')
    return strng
def make_negation():
    nlp = spacy.load("en_ner_bc5cdr_md")   # nlp object for clinical data
    nlp.add_pipe("negex", config={"ent_types":["DISEASE","CHEMICAL"]})  #entities for which we need negations
    strngs=["The machine negate the chances of diabetes","Mr Smith denied any sign of coronary heart disease","There were visible evidence for proving that it was indeed hypertension"]
    ans=[]
    for s in strngs:
        s=nolikewords(s)
        s=nlp(s)
        for e in s.ents:
            ans.append(not e._.negex)
    return ans
if __name__== "__main__":
    neg.run()
