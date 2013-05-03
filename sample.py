#!/usr/bin/env python
import mincemeat
import glob


# Test data
data = [
    "./data/x0052",
    "./data/x0062"
]

def getData():
    array = []
    for f in glob.glob("./data/*"):
        lines = [line.strip() for line in open(f)]
        array.extend(lines)
    return array

def mapfn(k, v):
    # v = filename
    allStopWords = {'about':1, 'above':1, 'after':1, 'again':1, 'against':1, 'all':1, 'am':1, 'an':1, 'and':1, 'any':1, 'are':1, 'arent':1, 'as':1, 'at':1, 'be':1, 'because':1, 'been':1, 'before':1, 'being':1, 'below':1, 'between':1, 'both':1, 'but':1, 'by':1, 'cant':1, 'cannot':1, 'could':1, 'couldnt':1, 'did':1, 'didnt':1, 'do':1, 'does':1, 'doesnt':1, 'doing':1, 'dont':1, 'down':1, 'during':1, 'each':1, 'few':1, 'for':1, 'from':1, 'further':1, 'had':1, 'hadnt':1, 'has':1, 'hasnt':1, 'have':1, 'havent':1, 'having':1, 'he':1, 'hed':1, 'hell':1, 'hes':1, 'her':1, 'here':1, 'heres':1, 'hers':1, 'herself':1, 'him':1, 'himself':1, 'his':1, 'how':1, 'hows':1, 'i':1, 'id':1, 'ill':1, 'im':1, 'ive':1, 'if':1, 'in':1, 'into':1, 'is':1, 'isnt':1, 'it':1, 'its':1, 'its':1, 'itself':1, 'lets':1, 'me':1, 'more':1, 'most':1, 'mustnt':1, 'my':1, 'myself':1, 'no':1, 'nor':1, 'not':1, 'of':1, 'off':1, 'on':1, 'once':1, 'only':1, 'or':1, 'other':1, 'ought':1, 'our':1, 'ours ':1, 'ourselves':1, 'out':1, 'over':1, 'own':1, 'same':1, 'shant':1, 'she':1, 'shed':1, 'shell':1, 'shes':1, 'should':1, 'shouldnt':1, 'so':1, 'some':1, 'such':1, 'than':1, 'that':1, 'thats':1, 'the':1, 'their':1, 'theirs':1, 'them':1, 'themselves':1, 'then':1, 'there':1, 'theres':1, 'these':1, 'they':1, 'theyd':1, 'theyll':1, 'theyre':1, 'theyve':1, 'this':1, 'those':1, 'through':1, 'to':1, 'too':1, 'under':1, 'until':1, 'up':1, 'very':1, 'was':1, 'wasnt':1, 'we':1, 'wed':1, 'well':1, 'were':1, 'weve':1, 'were':1, 'werent':1, 'what':1, 'whats':1, 'when':1, 'whens':1, 'where':1, 'wheres':1, 'which':1, 'while':1, 'who':1, 'whos':1, 'whom':1, 'why':1, 'whys':1, 'with':1, 'wont':1, 'would':1, 'wouldnt':1, 'you':1, 'youd':1, 'youll':1, 'youre':1, 'youve':1, 'your':1, 'yours':1, 'yourself':1, 'yourselves':1}

    for l in open(v):
        l = l.strip()
        data  = l.split(':::')
        authors = data[1].split('::')
        title = data[2] # Last is always title
        title = title.replace('.','')
        title = title.replace(',','')
        title = title.replace('-',' ')

        words = title.split()

        useWords = []
        # Remove stopwords
        for w in words:
            if not w in allStopWords.keys():
                useWords.append(w.lower())

        for author in authors:
            #print author
            #print useWords
            #print '--------------'
            yield author, dict(enumerate(useWords))

def reducefn(k, vs):
    result = {}

    # vs = many dict { { 0: 'a' , 1 : 'b', 2: 'a' }, { 0 : 'x', 1 : 'y' } }
    for v in vs:
        # v = { 0: 'a' , 1 : 'b', 2: 'a' }
        for k in v.keys():
            w = v[k]
            if not w in result.keys():
                result[w] = 1
            else:
                result[w] = result[w]+1

    return result

s = mincemeat.Server()

#s.datasource = dict(enumerate(data)) # Test
s.datasource = dict(enumerate(glob.glob("./data/*")))
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results['Alberto Pettorossi']
#print results['Munindar P. Singh']
#print results
