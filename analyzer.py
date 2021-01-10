import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import time

df = pd.read_csv("hasil_cleaning.csv", delimiter = ";")
print(df+"\n")

count = 0
for data in df.index:
    tweet = df["tweet"][data]
    sentiment = 1

    from googletrans import Translator
    penerjemah = Translator()
    hasil_translate = penerjemah.translate(tweet, dest="en")
    analyzer = TextBlob(hasil_translate.text, analyzer = NaiveBayesAnalyzer())
    test = TextBlob(hasil_translate.text)
    
    if analyzer.polarity < 0:
        sentiment = -1
    elif analyzer.polarity == 0:
        sentiment = 0
    df.at[count, "polarity"] = analyzer.polarity
    df.at[count, "subjectivity"] = analyzer.subjectivity
    df.at[count, "sentiment"] = sentiment
    print(tweet)
    print(analyzer.sentiment)
    print(test.sentiment)
    print()
    count += 1
    time.sleep(2)

df.to_csv("hasil_analisa.csv", index = False)