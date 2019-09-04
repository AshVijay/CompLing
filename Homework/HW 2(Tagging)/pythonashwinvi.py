import csv

items = []
HMMpair = []
HMMvalue = []
previous = tags[0]
words = []
tags = []
wordHMM = dict()
wordTagPairs = dict()
HMMindex = 0

with open('C:/Users/ashwi/Desktop/Computational Linguistics/HW 3/TDA.txt', 'r') as file:
    reader = csv.reader(file,delimiter=' ')
    for x in reader:
        items = x
        
for item in items:
    if(item == "@_IN" or item == "@_SYM"):
        item = "@_@"
    try:
        word, tag = item.split("_")
    except:
        continue
    words.append(word)
    tags.append(tag)
    
print(len(words))

for i in range(1,len(tags)):
    current = tags[i]
    tagPair = str(previous + "," + current)
    if(tagPair in HMMpair):
        HMMvalue[HMMpair.index(tagPair)] = HMMvalue[HMMpair.index(tagPair)] + 1;
    else:      
        HMMpair.append(tagPair)
        HMMvalue.append(1)
        HMMindex = HMMindex + 1
    previous = current
    
print(len(HMMpair))
print(len(HMMvalue))

HMM = dict(zip(HMMpair, HMMvalue))
uniqueTagNames = set(tags)
uniqueTags = dict.fromkeys(uniqueTagNames, 0)

for tag in tags:
    uniqueTags[tag] = uniqueTags[tag] + 1
    
for key, value in uniqueTags.items():
    print(key + "=" + str(value))
    
HMM = dict(zip(HMMpair, HMMvalue))
uniqueTagNames = set(tags)
uniqueTags = dict.fromkeys(uniqueTagNames, 0)

for tag in tags:                 
    uniqueTags[tag] = uniqueTags[tag] + 1
for key, value in uniqueTags.items():
    print(key + "=" + str(value))
    
for key, value in HMM.items():
    first, second = key.split(",")
    HMM[key] = value / uniqueTags[first]
    
for i in range(len(words)):
    pair = str(words[i] + "," + tags[i])
    if(pair in wordTagPairs):
        wordTagPairs[pair] = wordTagPairs[pair] + 1
    else:
        wordTagPairs[pair] = 1
        
for key, value in wordTagPairs.items():
    first, second = key.split(",")
    wordHMM[key] = value / uniqueTags[second]
    
File = open("C:/Users/ashwi/Desktop/Computational Linguistics/HW 3/sigmas.txt", "w")
for key, value in HMM.items():
    first, second = key.split(",")
    first = str("\'" + first + "\'")
    second = str("\'" + second + "\'")
    key = str(first + "," + second)
    File.write("sigma(" + key + "," + str(value) + ")\n")
File.close()

File = open("C:/Users/ashwi/Desktop/Computational Linguistics/HW 3/taus.txt", "w")
for key, value in wordHMM.items():
    first, second = key.split(",")
    first = str("\'" + first + "\'")
    second = str("\'" + second + "\'")
    key = str(first + "," + second)
    File.write("tau(" + key + "," + str(value) + ")\n")
File.close()

