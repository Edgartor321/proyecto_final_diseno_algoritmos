import matplotlib.pyplot as plt

archivo = open("../textos/italiano.txt", "r", encoding="utf-8")
#texto = archivo.read()
archivo.close()
texto="Qy iuoxukdldut mb wydkdt gywdz kzqut eb'dq k'ysdl mz wydkdtk jqytik ub tudwk. Mytk qzk mzbn iyk, mzbn lpxzk mz tblwdoztlk kz mdkldtsbztl : qzk kbiwzk, xwdtidxyqzoztl qz sqbiukz zl qz cwbilukz, xqbk yjutmytlk mytk qz wydkdt jqyti, zl qzk gdlyodtzk (yidmz cuqdebz zl gdlyodtz J6). Iz mzwtdzw zt ebytldlz ebd t'zkl kbwxykkz ebz xyw qzk cwbdlk kzik zl qzk cwbdlk lwuxdiybn iuooz q'yguiyl, qy jytytz, q'ytutz, qy supygz zl qy oytsbz. Ky wdifzkkz zt kbiwzk zt cydl q'bt mzk cwbdlk qzk xqbk iyquwdebzk. Qzk wydkdtk ibqldgzk mytk qzk wzsdutk cwudmzk utl lztmytiz y iutlztdw oudtk mz kbiwzk ebz izbn ibqldgzk mytk bt kuq ifybm zl kzi. Xywod qzk odtzwybn, qz xulykkdbo zkl qz xqbk yjutmytl zl kz wzlwubgz zt xqbk swytmz ebytldlz mytk qz wydkdt tudw ; lytmdk ebz qz oystzkdbo zl qz iyqidbo kz lwubgztl zt ebytldlzk oumzwzzk zl kutl xqbk yjutmytlk mytk qzk wydkdtk jqytik. Q'bldqdkyldut mytk q'uwsytdkoz mz iz mzwtdzw odtzwyq t'zkl xyk ybkkd doxuwlytlz ebz izqqz ebd xwugdztl mzk xwumbdlk qydldzwk ub m'yblwzk yqdoztlk ebd kutl btz juttz kubwiz mbmdl odtzwyq."

abecedario = "abcdefghijklmnopqrstuvwxyz"
texto = texto.lower()

histo = {c:0 for c in abecedario}

datos = texto.split()

for p in datos:
    if p[0] in abecedario:
        histo[p[0]] += 1

histo = dict(sorted(histo.items(), key=lambda item:item[1]))
print(histo)

plt.bar(histo.keys(), histo.values())
plt.show()