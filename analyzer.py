import csv
from bottle import route,run,Bottle,template, response, request
import nltk,random
from nltk.corpus import stopwords
from json import dumps

train_data_csv = csv.reader(open("train_data.csv"))
stop = stopwords.words('english')
temp = []
labels = []
tweets = []
tweets_tokens = []
for rows in train_data_csv:
    temp.append(rows)

print(temp)
random.shuffle(temp)
print(temp)
for rows in temp:
    labels.append(rows[0])
    tweets.append(rows[1])
    tweets_tokens.append([i.lower() for i in nltk.word_tokenize(rows[1]) if i.lower() not in stop])



print(len(labels))
words = []
for i in tweets_tokens:
    words.extend(i)

wordfeatures = nltk.FreqDist(words).keys()

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in wordfeatures:
        features['contains(%s)' % word] = (word in document_words)
    return features

train_tweets = []
k=0
for i in tweets_tokens:
    train_tweets.append((i,labels[k]))
    k=k+1

train_tweets_five = train_tweets[:100]
print('building training set')
training_set = nltk.classify.apply_features(extract_features, train_tweets_five)
print('training')
classifier = nltk.NaiveBayesClassifier.train(training_set)
print(classifier.show_most_informative_features(32))

app = Bottle()
@app.post('/classify')
def classify():
    data = {}

    if(request.json["tweet"]):
        data["class"] = classifier.classify(extract_features(request.json["tweet"].split()))
    else:
        data["class"] = "unclassified"

    response.content_type = "application/json"
    print(data)
    return dumps(data)


run(app, host='localhost', port=8082)

# print(classifier.classify(extract_features("This is the best book in the eductional domain".split())))
# print(classifier.classify(extract_features("I hate this weather badly".split())))
# print(classifier.classify(extract_features("She is a freaked out, gotta get back".split())))


