class TweetFreq():
    def __init__(self):
        self.posFreq = 0
        self.neuFreq = 0
        self.negFreq = 0

import pandas as pd

df = pd.read_csv("hasil_analisa.csv", delimiter = ";")
summary = {}

for data in df.index:
    tanggal = df["time"][data]
    print(tanggal)
    if tanggal not in summary.keys():
        summary[tanggal] = TweetFreq()
        sentiment = df["sentiment"][data]
        if int(sentiment) == 1:
            summary[tanggal].posFreq += 1
        elif int(sentiment) == 0:
            summary[tanggal].neuFreq += 1
        elif int(sentiment) == -1:
            summary[tanggal].negFreq += 1
    else:
        if int(sentiment) == 1:
            summary[tanggal].posFreq += 1
        elif int(sentiment) == 0:
            summary[tanggal].neuFreq += 1
        elif int(sentiment) == -1:
            summary[tanggal].negFreq += 1

with open("simplified_result.txt", "w") as w:
    # w.write("tanggal, total_pos, total_neu, total_neg\n")
    for k in summary.keys():
        w.write(str(k)+", "+str(summary[k].posFreq)+", "+str(summary[k].neuFreq)+", "+str(summary[k].negFreq)+"\n")