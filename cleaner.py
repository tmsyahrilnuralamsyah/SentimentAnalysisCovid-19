import pandas as pd
import demoji
import re

def isMustDeleted(tweet, threshold):
    must_deleted = 1 #jika 0 berarti data akan dihapus
    hashtags_count = 0
    words_count = 0

    for words in str(tweet).split():
        if words[0] == "#":
            hashtags_count += 1
        elif words[0].isalpha():
            words_count += 1
    
    #mulai eliminasi chi-square
    if hashtags_count >= words_count:
        chi_score = words_count/hashtags_count
        if chi_score > threshold:
            must_deleted = 0
        else:
            must_deleted = 1
    elif words_count > hashtags_count:
        must_deleted = 0
    return int(must_deleted)

def clean_tweet(tweet):
    text = tweet
    text = re.sub(r"https\S+", " ", text)
    text = re.sub(r"pic.twitter\S+", " ", text)
    text = re.sub(r"#\S+", " ", text)
    text = re.sub(r"@\S+", " ", text)
    text = re.sub(r"[,.:;+=]", " ", text)
    text = re.sub(r"[...]", " ", text)
    text = re.sub(r"[/\n/\t]", " ", text)
    text = re.sub(r" +", " ", text)
    text = demoji.replace(text, "") 
    return str(text)

df = pd.read_json("tweets.json", lines=True)
print(df)

count = 0
threshold = 0.5
for data in df.index:
    tweet = df["tweet"][data]
    if isMustDeleted(tweet, threshold) == 0: #jika 0 data tidak dihapus
        tweet = clean_tweet(tweet)
        df.at[count, "tweet"] = tweet
    else:
        df = df.drop([count], axis = 0)
    count +=1

df.drop(df.columns.difference(["date", "time", "tweet", "hashtags"]), 1, inplace=True)

for data in df.index:
    print(df["tweet"][data]+"\n")

df.to_csv("hasil_cleaning.csv", index = False)