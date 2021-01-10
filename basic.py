x = int(input("nomor : "))
print("nomor tadi : " + str(x))

for i in range(3):
    print(str(i)+" terbang")

a = 0
while(a < 3):
    print(str(a))
    a += 1

d = 1
f = 2
if (d < f and f == 2):
    print("benar")

buah = {'jeruk': 'orange', 'pisang': 'kuning', 'apel': 'merah'}

for k in buah.keys():
    print(str(k)+" : "+buah[k])