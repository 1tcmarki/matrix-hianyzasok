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


print(f"1. feladat: {osszeg} óra hiányzás volt összesen?")
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
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])<5):
    index+=1
if index<len(hianyzasok):
    print(f"3. feladat : Volt olyan hét amikor 5-nel kevesebb hianyzo volt.")
else:
    print(f"3. feladat : Nem volt olyan het amikor 5-nel kevesebb hianyzo volt.")

# 4. Melyik héten volt a legtöbb hiányzás?
#4. feladat: A legtöbb hiányzás a 3. héten volt (16 óra)
# legtobbheti=osszeg.index(max(osszeg))+1
# print(legtobbheti)
# heti_hianyzasok=[]
# heti_hianyzasok.append(sum(hianyzasok[3]))
# heti_hianyzasok.append(sum(hianyzasok[0]))
# heti_hianyzasok.append(sum(hianyzasok[1]))
# heti_hianyzasok.append(sum(hianyzasok[2]))
# heti_legtobb=(max(heti_hianyzasok))
# print(f"4. feladat: Az . héten volt a legtöbb , {heti_legtobb} hianyzas.")
# Melyik héten volt a legtöbb hiányzás?
# legtobb_hianyzas = max(heti_hianyzasok)
# legtobb_hianyzas_index = heti_hianyzasok.index(legtobb_hianyzas) + 1
# print(f"A legtöbb hiányzás a(z) {legtobb_hianyzas_index}. héten volt, összesen {legtobb_hianyzas} hiányzás.")
max_index=0
for index in range(len(hianyzasok)):
    if sum(hianyzasok[index])>sum(hianyzasok[max_index]):
        max_index=index

print(f"4. feladat : A legtobb hianyzas a {max_index+1}. héten volt. {sum(hianyzasok[max_index])}.")

#5. feladat hanyadik héten volt egyetlen hianyzas?
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])==1):
    index+=1
van=index<len(hianyzasok)
if van:
    sorszam=index
    print(f"5. feladat : A {sorszam+1}. héten volt egyetlen hianyzas")
else:
    sorszam=-1
    print(f"5. feladat : Egyik heten sem volt egyetlen hianyzas.")