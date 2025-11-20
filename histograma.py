import matplotlib.pyplot as plt
archivo= open("espanol.txt","r",encoding="utf-8")
texto=archivo.read()
archivo.close()
abecedario="abcdefghijklmnopqrstuvwxyz "
texto = texto.lower()

histo={}
print(len(texto))
for c in abecedario:
    histo[c]=0

for c in texto:
    if c in abecedario:
        histo[c] +=1
histo=dict(sorted(histo.items(),key=lambda item:item[1]))
print(histo)
plt.bar(histo.keys(),histo.values())
plt.show()

"""
destino=""
for c in texto:
    if c in abecedario:
        destino +=c
datos=destino.split()
dic1 = []
for p in datos:
    if not (p in dic1):
        dic1.append(p)
dic1.sort()
print(dic1)

salida= open("dic_ital","w",encoding="utf-8")
salida.write(str(dic1))
"""