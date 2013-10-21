#!/usr/bin/env python3

from sys import argv

default = 1000
upTo = default if len(argv) < 2 else int(argv[1])
bottom = 1 if len(argv) < 3 or argv[2] != 'only' else upTo

class English:
    def __init__(self):
        self.kids = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                      'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                      'seventeen', 'eighteen', 'nineteen' ]

        self.scores = [ 'twenty', 'thirty', 'forty', 'fifty', 
                        'sixty', 'seventy', 'eighty', 'ninety' ]

        self.higher = [ 'hundred', 'thousand', 'million', 'billion', 
                        'trillion', 'quadrillion', 'quintillion', 'sextillion',
                        'septillion', 'octillian', 'nontillion', 
                        'brazilian'] + ['getthefuckoutillion' for _ in range(94)]

        self.andWord = 'and'

locale = English()

def decomposeIntoTriples(n):
    triples = []
    numStr = str(n)
    while len(numStr) > 0:
        triples.insert(0, numStr[-3:])
        numStr = numStr[:-3]
    return triples

def sayScores(doubleStr, locale):
    said = ''
    if len(doubleStr) == 2 and int(doubleStr[0]) > 1:
        said = said + locale.scores[int(doubleStr[0]) - 2]
        if int(doubleStr[1]) > 0:
            said = said + '-' + locale.kids[int(doubleStr[1]) - 1]
    elif int(doubleStr) > 0:
        said = said + locale.kids[int(doubleStr) - 1]
    return said

def sayTriple(tripleStr, locale):
    said = ''

    if len(tripleStr) == 3 and int(tripleStr[0]) > 0:
        said = said + locale.kids[int(tripleStr[0]) - 1] + ' ' + locale.higher[0]
        scores = sayScores(tripleStr[-2:], locale)
        if len(scores) > 0:
            said = said + ' ' + locale.andWord + ' ' + scores
    elif int(tripleStr) > 0:
        said = said + sayScores(tripleStr, locale)
    return said

# for triple in decomposeIntoTriples(str(upTo)):
#     print( sayTriple(triple, locale) )
def sayNumber(num, locale):
    triples = decomposeIntoTriples(str(num))
    statement = ''
    for i, triple in enumerate(triples):
        higherIndex = len(triples) - i - 1
        higher = ' ' + locale.higher[higherIndex] if higherIndex > 0 else ''
        statement = statement + ' ' + sayTriple(str(int(triple)), locale) + higher
    return statement[1:] # trim leading space

totalCount = 0
for i in range(bottom, upTo + 1):
    said = sayNumber(i, locale)
    count = len(said.replace(',','').replace(' ','').replace('-',''))
    print('"{}" has {} letters'.format(sayNumber(i, locale), count))
    totalCount += count

print('There were a total of {} letters'.format(totalCount))
print(totalCount)
