import plotly.graph_objects as go

tanggal = []
positif = []
netral = []
negatif = []

with open('simplified_result.txt', "r") as f:
    for baris in f:
        data = baris.split(",")

        tanggal.append(data[0])
        positif.append(data[1])
        netral.append(data[2])
        negatif.append(data[3])

fig = go.Figure(data = [go.Bar(name = "Baik", x = tanggal, y = positif), go.Bar(name = "Sedang", x = tanggal, y = netral), 
                go.Bar(name = "Buruk", x = tanggal, y = negatif)])
fig.update_layout(barmode = "group")
fig.show()