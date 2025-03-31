L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def de(mot):
    for i in range(1,26):
        motOriginal=[]
        for el in mot:
            if el==" ":
                motOriginal.append(el)
            else:
                motOriginal.append(L[L.index(el)-i])
        print("cle "+str(i)+" : "+"".join(motOriginal))
def encoder(mot,cle=3):
    code=[]
    for el in mot:
        if el==" ":
            code.append(el)
        else:
            code.append(L[(L.index(el)+cle)%26])
    print("".join(code))   
#PQR
#GSRWGMIRGI
#ERQMRXU
#PCBQVWSB
#GZWJFZ
#QGPKD KDJH PKTO DQITCJ AT BTHHPVT XCXIXPA

def ascii_decode(tab):return "".join(chr(int(el)) for el in tab.split(" "))
def ascii_encode(tab):return " ".join(str(ord(el)) for el in tab)
#'108 97 109 98 101 114 116 32 97 109 111 117 103 111 117'

"""
for i in range(99999999):
    if decode(encode(i))!=i:print(i)"""
    
"""
#def encode(n):return (n+12345)^67890
#def decode(n):return (n^67890)-12345
def lvl(xp):return int((1 + (1 + 8 * xp / 100) ** 0.5) // 2)

#def decoupe(l, n):return [l[i:i+4] for i in range(0, 4*n, 4) if i < len(l)]
#def decoupe(l, n):return [l[i:i+4] for i in range(0, min(n, len(l)), 4)]
def decoupe(l,lignes): return (l[:lignes][i:i+4] for i in range(0,len(l[:lignes]),4))


#bottle flip 1000d game: 80303
KEY = 314159  # Une clé arbitraire pour encoder/décoder

def encode(xp, flips_total, flips_success):
    return (xp * KEY + flips_total) * KEY + flips_success

def decode(n):
    flips_success = n % KEY
    n //= KEY
    flips_total = n % KEY
    xp = n // KEY
    return xp, flips_total, flips_success
"""






