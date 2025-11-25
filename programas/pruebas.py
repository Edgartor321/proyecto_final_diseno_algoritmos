def descifra_sustitucion(cadena, llave):
    print(cadena)
    print(llave)
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    cadena = cadena.lower()
    for letra in cadena:
        if letra in alfabeto:
            pos = llave.lower().index(letra)
            cifrado += alfabeto[pos]
        else:
            cifrado += letra
    return cifrado


def carga_dic(nombre):
    arch = open(nombre, 'r')
    texto = arch.read()
    arch.close()
    return texto.split()


alfabeto = 'abcdefghijklmnopqrstuvwxyz'
cifrado = "Hmgh cmnnl dlj bgholj pldizj, dl dimz b al zmnsolgjlj nmgjhbcwlj lubijjlj. Clj dmzkj umidj jlzjisdlj bgy xisobhimzj bialzh dl dimz b jl aioiklo abzj d'msjcgoihl, mg fgbza jmz cwbnu xijgld ljh msjhogl. Db nbvlgol ubohil al jb cwbjjl jl alomgdbzh db zgih, idj d'bialzh uoljfgl b jlzhio jmz cwlniz abzj d'msjcgoihl, dl zle xloj dl cild. Dlj udgj dmzkglj nmgjhbcwlj jmzh jgo jb dlxol jguloilgol cl jmzh dlj xisoijjlj nqjhbcibdlj. Dlj nmgjhbcwlj bg-aljjgj alj qlgy jmzh buuldllj dlj xisoijjlj jgulocidibiolj. Id q b lkbdlnlzh alj xisoijjlj jgo d'gzl mg d'bghol vmgl, buuldllj dlj xisoijjlj klzibdlj. Dlj xisoijjlj ulgxlzh jl alxldmuulo zmz jlgdlnlzh jgo dl xijbkl, nbij bgjji silz jgo dl amj alj ubhhlj : clj alozilolj jmzh buuldllj umidj al cboulddl lh jmzh ghidijllj umgo oljjlzhio alj xisobhimzj hlooljholj."
llave = 'abcdefghijklmnopqrstuvwxyz'
dic1 = carga_dic('../diccionarios/dic_fran')

"""Hmgh cmnnl dlj bgholj pldizj, dl dimz b al zmnsolgjlj nmgjhbcwlj lubijjlj. 
Clj dmzkj umidj jlzjisdlj bgy xisobhimzj bialzh dl dimz b jl aioiklo abzj d'msjcgoihl, mg fgbza jmz 
cwbnu xijgld ljh msjhogl. Db nbvlgol ubohil al jb cwbjjl jl alomgdbzh db zgih, idj d'bialzh uoljfgl b jlzhio 
jmz cwlniz abzj d'msjcgoihl, dl zle xloj dl cild. Dlj udgj dmzkglj nmgjhbcwlj jmzh jgo jb dlxol jguloilgol cl 
jmzh dlj xisoijjlj nqjhbcibdlj. Dlj nmgjhbcwlj bg-aljjgj alj qlgy jmzh buuldllj dlj xisoijjlj jgulocidibiolj. 
Id q b lkbdlnlzh alj xisoijjlj jgo d'gzl mg d'bghol vmgl, buuldllj dlj xisoijjlj klzibdlj. Dlj xisoijjlj ulgxlzh 
jl alxldmuulo zmz jlgdlnlzh jgo dl xijbkl, nbij bgjji silz jgo dl amj alj ubhhlj : clj alozilolj jmzh buuldllj 
umidj al cboulddl lh jmzh ghidijllj umgo oljjlzhio alj xisobhimzj hlooljholj.
"""

posA="cdmp"
posB="a"
posC="c"
posD=""
posE=""
posF=""
posG="u" #uni - ou
posH="t"
posI="i"
posJ="s"
posK=""
poaL="e" #letra más común, posible "e" CONFIRMADA
posM="o"
posN="m"
posO="nrt"
posP=""
posQ=""
posR=""
posS=""
posT=""
posU="p"
posV=""
posW="h"
posX=""
posY=""
posZ="tnm"

# probando con buuldllj
c = 0
prueba = ''
for p in dic1:
    if len(p) == 8:
        if p[-2]==p[-3] and p[-2] == p[3] and p[0]=='a' and p[3]=="e" and p[-1]=="s":
            print(p)
            if not (p[0] in prueba):
                prueba += p[0]
            c = c + 1
print('cumplen:', c)
print(prueba)

#print(descifra_sustitucion(cifrado, llave))