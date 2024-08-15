print("[+] initializing dependencies")

from re import search, IGNORECASE
from random import shuffle
from pickle import dump
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.pipeline import Pipeline


print("[+] collecting advertisement data")
adverts_train = fetch_20newsgroups(subset="train", categories=["misc.forsale"]).data[:125]
adverts_test = fetch_20newsgroups(subset="test", categories=["misc.forsale"]).data[:125]
adverts_data = adverts_train + adverts_test
chats = open("data/cuData.txt", "r", encoding="utf-8").read().split(":~:")
for sent in chats[:510]:
    if search(r"[A-Za-z]", sent, IGNORECASE):
        adverts_data.append(sent)

print("[+] collecting politics data")
politics_train = fetch_20newsgroups(subset="train", categories=["talk.politics.misc"]).data
politics_test = fetch_20newsgroups(subset="test", categories=["talk.politics.misc"]).data
politics_data = politics_train + politics_test[:-50]
chats = open("data/politics.txt", "r", encoding="utf-8").read().split("~")
for sent in chats:
    politics_data.append(sent)

print("[+] collecting science data")
science_train = fetch_20newsgroups(subset="train", categories=["sci.med", "sci.space"], shuffle=True).data[:375]
science_test = fetch_20newsgroups(subset="test", categories=["sci.med", "sci.space"], shuffle=True).data[:375]
science_data = science_train + science_test

print("[+] collecting religion data")
religion_train = fetch_20newsgroups(subset="train", categories=["soc.religion.christian"], shuffle=True).data[:375]
religion_test = fetch_20newsgroups(subset="train", categories=["soc.religion.christian"], shuffle=True).data[:375]
religion_data = religion_train + religion_test

print("[+] collecting computer and tech data")
comps1 = fetch_20newsgroups(subset="train", shuffle=True, categories=['comp.graphics', 'comp.os.ms-windows.misc',
                            'comp.windows.x', "sci.electronics", 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware'])
comps2 = open("data/2001_2500.csv", "r").read().split("J\t\t\t\t\t\t\t\t")
data = []
chats = open("data/arduino.txt", "r", encoding="utf-8").read().split("~")
for sent in chats:
    data.append(sent)
comps_data = comps1.data[:125] + comps2[:125] + data[:500]

print("[+] collecting sports data")
sports_data = []
names = ["athletics", "cricket", "football", "rugby", "tennis"]
number = ["55", "55", "55", "55", "55"]
for (file, num) in zip(names, number):
    for name in [f"{i:0>3}" for i in range(1, int(num))]:
        sports_data.append(open(f"data/bbcsport/{file}/{name}.txt").read())
chats = open("data/vetland.txt", "r", encoding="utf-8").read().split("~")
for sent in chats[:480]:
    sports_data.append(sent)

print("[+] collecting learning data")
learning_data = []
chats1 = open("data/comp chats.txt", "r", encoding="utf-8").read().split("~")
for sent1 in chats1:
    learning_data.append(sent1)
chats2 = open("data/hbsct.txt", "r", encoding="utf-8").read().split("~")
for sent2 in chats2:
    learning_data.append(sent2)
shuffle(learning_data, lambda: 0.3)

print("[+] collecting dropped data")
dropped_data = []
chats = open("data/dropped.txt", "r", encoding="utf-8").read().split("~")
for sent in chats:
    dropped_data.append(sent)
shuffle(dropped_data, lambda: 0.7)

training_data = []
training_target = []

print("[+] compiling all data")
x = 0
sets = [learning_data[:750], adverts_data, comps_data, politics_data[:750], religion_data, science_data, sports_data, dropped_data[:800]]

for item in sets:
    training_data.extend(item)
    training_target.extend([i for i in [x] for j in range(len(item))])
    x += 1

shuffle(training_data, random=lambda: 0.42)
shuffle(training_target, random=lambda: 0.42)

print("[+] training model")
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("tfidf", TfidfTransformer())
])
processed = pipeline.fit_transform(training_data)

classifier = MultinomialNB()
classifier.fit(processed, training_target)

print("[+] saving model")
with open("AppModel.bin", "wb") as model:
    dump((classifier, pipeline), model)

print("[+] finished")
