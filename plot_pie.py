import plotly.graph_objects as go

positif = 0
netral = 0
negatif = 0

with open('simplified_result.txt', "r") as f:
    for baris in f:
        data = baris.split(",")
        positif += int(data[1])
        netral += int(data[2])
        negatif += int(data[3])

fig = go.Figure(data = [go.Pie(labels = ["Positif", "Netral", "Negatif"], values = [positif, netral, negatif])])
fig.show()