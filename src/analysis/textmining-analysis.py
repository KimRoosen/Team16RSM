import pandas as pd
import os



try:
    os.makedirs("../../gen/analysis/output/")
except OSError:
    print ("Directory already exists")
else:
    print ("Successfully created the directory")

##From first cell of jupyter notebook

import json #Load json library
import matplotlib.pyplot as plt


#Counters
tweetcount = 0
users1 = 0
users2ormore = 0
#Initialize empty string
totaltext = ""
#Users dictionary
users = {}

schooltext = ""

#Positve / negative
positivetweets = 0
negativetweets = 0

positivetime = [0,0,0,0,0,0]
negativetime = [0,0,0,0,0,0]

print("Going to read the data from the json and do some analysis")

with open('../../gen/data-preparation/temp/collected_tweets_persconferentie_corona.json') as json_file: # Load the file
    for line in json_file.readlines(): # For all lines in the file

        if not line.strip (): # skip empty lines
            continue

        tweetcount += 1 # add + 1 to tweet count
        json_data = json.loads (line) # json_data contains data from curent line
        if(json_data['truncated']): # If extended tweet
            linetext = json_data['extended_tweet']['full_text'] # Use full text
        else:
            linetext = json_data['text'] # Else use smaller text
        if('school' in linetext or 'scholen' in linetext or 'onderwijs' in linetext): #Search for scholen in text
            if('geweldig' in linetext or 'super' in linetext or 'goed' in linetext or 'fantastisch' in linetext or 'amazing' in linetext or 'fijn' in linetext or 'gelukkig' in linetext or 'opluchting' in linetext or 'eindelijk' in linetext or 'verstandig' in linetext):
                positivetweets += 1
                time = json_data['created_at']
                positivetime[int(time[14])] += 1

            elif('stom' in linetext or 'achterlijk' in linetext or 'kut' in linetext or 'verschrikkelijk' in linetext or 'fack' in linetext or 'erg' in linetext or 'ramp' in linetext or 'geen' in linetext or 'niet' in linetext or 'boos' in linetext or 'verdrietig' in linetext or 'onverstandig' in linetext):
                negativetweets += 1
                time = json_data['created_at']
                negativetime[int(time[14])] += 1

            schooltext = schooltext + " " + linetext # Add all the text together

        totaltext = totaltext + " " + linetext # Add all the text together

        user = json_data['user']['screen_name'] # we want the user screenname of the tweet
        if user not in users: # if not in dictionary add
            users[user] = 0 # with count 0 (will be 1)
        users[user] += 1 # Add 1 to amount of tweets


userslist = [] # New list
for key, value in users.items(): # Go through all users
    if value == 1: # if user has 1 tweet
        users1 += 1 # Add to that counter
    elif value >= 2: # if user has 2 or more
        users2ormore += 1 # Add to that counter
    userslist.append((value, key)) # Add to list

userslist.sort(reverse=True) # Sort the list


totaltext = totaltext.lower() # All lower case
totaltext = totaltext.replace('.','') # remove all dots
totaltext = totaltext.replace(':','') # remove all doubledots (These occur after @)
word_list = totaltext.split() # Split all words

schooltext = schooltext.lower() # All lower case
schooltext = schooltext.replace('.','') # remove all dots
schooltext = schooltext.replace(':','') # remove all doubledots (These occur after @)
word_list_school = schooltext.split() # Split all words

# https://codeburst.io/python-basics-11-word-count-filter-out-punctuation-dictionary-manipulation-and-sorting-lists-3f6c55420855

# Initializing Dictionary
d = {}
d_school = {}

# Count number of times each word comes up in list of words (in dictionary)
for word in word_list:
    if word not in d:
        d[word] = 0
    d[word] += 1

# Count number of times each word comes up in list of words (in dictionary)
for word in word_list_school:
    if word not in d_school:
        d_school[word] = 0
    d_school[word] += 1

word_freqhashtag = [] # New list
word_freqat = [] # New list
for key, value in d.items():
    if '#' in key: # Only want hashtags ######
        word_freqhashtag.append((value, key))
    elif '@' in key: # If at is in text
        word_freqat.append((value,key))
word_freqhashtag.sort(reverse=True)
word_freqat.sort(reverse=True)

text_output = 'Amount of tweets: ' + str(tweetcount) + '\n'
text_output = text_output + 'Unique users that tweet ' + str(users1 + users2ormore) + '\n'
text_output = text_output + 'Users with 1 tweet: ' + str(users1) + '\n'
text_output = text_output + 'Users with 2 or more tweets: ' + str(users2ormore) + '\n'
text_output = text_output + '50 most common hashtags in text' + '\n'
text_output = text_output + str(word_freqhashtag[:50]) + '\n' #Only print 50 most common hashtags
text_output = text_output + '50 most common @ in tekst' + '\n'
text_output = text_output + str(word_freqat[:50]) + '\n' #Only print 50 most common hashtags

text_output = text_output + 'Users with most tweets' + '\n'
text_output = text_output + str(userslist[:20]) + '\n'

word_school = [] # New list
for key, value in d.items():
    if(len(key) > 4):
        word_school.append((value,key))
word_school.sort(reverse=True)

print("Going to save our analysis data in gen/analysis/output/")

text_output = text_output + 'Most common words in schooltext including hashtags' + '\n'
text_output = text_output + str(word_school[:50]) + '\n'
text_output_file = open("../../gen/analysis/output/text_output.txt", 'w', encoding="utf-8")
text_output_file.write(text_output)
text_output_file.close()

## first graph

labels = 'Postive', 'Negative'
sizes = [positivetweets, negativetweets]
plt.title('Amount of Positive tweets compared to negative tweets about school')
plt.pie(sizes, labels=labels)
plt.savefig("../../gen/analysis/output/Positive-negative-piechart.png")
plt.close()

## Second graph

plt.title('Positve tweets per 10 minutes about school')
plt.ylabel('Amount of tweets')
plt.xlabel('Minutes')
x = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60']
plt.plot(x, positivetime)
plt.savefig("../../gen/analysis/output/Positive-graph.png")
plt.close()

## Third graph
plt.title('Negative tweets per 10 minutes about school')
plt.ylabel('Amount of tweets')
plt.xlabel('Minutes')
x = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60']
plt.plot(x, negativetime)
plt.savefig("../../gen/analysis/output/Negative-graph.png")
plt.close()

## Fourth graph

plt.title('Postive vs Negative tweets per 10 minutes about school')
plt.ylabel('Amount of tweets')
plt.xlabel('Minutes')
x = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60']

plt.plot(x, positivetime, 'g--', label="positive")
plt.plot(x, negativetime, 'r--', label="negative")
plt.legend()
plt.savefig("../../gen/analysis/output/Positive-negative-graph.png")
plt.close()
