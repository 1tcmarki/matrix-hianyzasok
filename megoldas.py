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
# 2. Volt-e olyan hét , amikor ötnél kevesebb hiányzás volt? 
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])==0):
    index+=1
van=index<(len(hianyzasok))
if van:
    print(f"2. feladat , Volt olyan het amikor nem volt hianyzo.")
else:
    print(f"2. feladat: , Nem volt olyan hét amikor nem volt hianyzo.")


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

# 4. Melyik héten volt a legtöbb hiányzás?
#4. feladat: A legtöbb hiányzás a 3. héten volt (16 óra)
# legtobbheti=osszeg.index(max(osszeg))+1
# print(legtobbheti)
heti_hianyzasok=[]
heti_hianyzasok.append(sum(hianyzasok[0]))
heti_hianyzasok.append(sum(hianyzasok[1]))
heti_hianyzasok.append(sum(hianyzasok[2]))
heti_hianyzasok.append(sum(hianyzasok[3]))
heti_legtobb=(max(heti_hianyzasok))
print(f"4. feladat: Az . héten volt a legtöbb , {heti_legtobb} hianyzas.")
# Melyik héten volt a legtöbb hiányzás?
# legtobb_hianyzas = max(heti_hianyzasok)
# legtobb_hianyzas_index = heti_hianyzasok.index(legtobb_hianyzas) + 1
# print(f"A legtöbb hiányzás a(z) {legtobb_hianyzas_index}. héten volt, összesen {legtobb_hianyzas} hiányzás.")


