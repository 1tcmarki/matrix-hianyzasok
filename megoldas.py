#0. feladat a hianyzasok.txt beolvasása listában listába.

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        seged_lista=(sor.strip().split(","))
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))
print("a beolvasott matrix")
print(hianyzasok)

# 1. Hány óra hiányzás volt összesen?
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het)
print(f"1. feladat : {osszeg} ora hianyzas volt osszesen")

# 2. Volt-e olyan hét, amikor nem volt hiányzó?
volt_e=False
for het in hianyzasok:
    if not('1') in het:
        volt_e=False
if volt_e==False:
    print(f"2. feladat: Nem volt olyan hét, amikor nem volt hiányzó")
else:
    print(f"Volt olyan hét amikor nem volt hianyzo.")



# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
print(f"3. feladat: Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt")
