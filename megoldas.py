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


print(f"# 1. feladat: {osszeg} óra hiányzás volt összesen?")


# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
print(f"3. feladat: Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt?")

van_otos_het = False
for het in hianyzasok:
    if sum(het) <= 5:
        van_otos_het=True

if van_otos_het:
    print("Volt olyan hét, amikor ötnél kevesebb hiányzás volt.")
else:
    print("Nem volt olyan hét, amikor ötnél kevesebb hiányzás volt.")

