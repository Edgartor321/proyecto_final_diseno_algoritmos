def descifra_sustitucion(cadena, llave):
    clave=llave.lower()
    print(cadena)
    print(llave)
    print("Desenciptado")
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    cadena = cadena.lower()
    for letra in cadena:
        if letra in clave:
            pos = clave.index(letra)
            nueva=alfabeto[pos]
            cifrado += nueva
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
#llave = 'daclzqutisgeomrfykbwpjhvxn'
llave = 'bscalpkwivrdnzmufojhgxtyqe'
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
#Faltantes:  p q    r t no están(k w usalas indistintamente)    v pendiente
posA="d"
posB="a"
posC="c"
posD="l" #o=r entonces
posE="z"
posF="q"
posG="u" #uni - ou
posH="t"
posI="i"
posJ="s"
posK="g"
posL="e" #letra más común, posible "e" CONFIRMADA
posM="o"
posN="m"
posO="r"
posP="f" #revisar paso
posQ="y"   #revisar paso
posR="k"
posS="b"
posT="w"
posU="p"
posV="j"
posW="h"
posX="v"
posY="x"
posZ="n"

# probando con bgy
c = 0
prueba = ''
for p in dic1:
    if len(p) ==3 and len(set(p)) == 3:
        if p[0] in posB and p[1] in posG :

            #print(p)
            if not (p[0] in prueba):
                prueba += p[0]
            c = c + 1
#print('cumplen:', c)
#print(prueba)

#print(descifra_sustitucion(cifrado, llave))

#and p[2] in posE
#and p[3]in posG

out=open("../resultado/resultado","w",encoding="utf-8")
out.write(descifra_sustitucion(cifrado,llave))
