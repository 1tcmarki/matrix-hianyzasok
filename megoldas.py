#0. feladat A hianyzasok.txt beolvasasa listaban listakba !!THE MATRIX IS ATTACKING US!!

hinayzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        segedlista=(sor.strip().split(","))
        # l=[]
        # for szam in segedlista:
        #     l.append(int(szam))
        # hinayzasok.append(l)
        hinayzasok.append(list(map(int,segedlista)))

print(hinayzasok)