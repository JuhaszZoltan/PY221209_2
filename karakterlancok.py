szoveg:str = 'nagyon szeretem a FAGYIT!'

for betu in szoveg:
    print(betu, end='\n')

hossz:int = len(szoveg)
print(f'karakterszám: {hossz}')

print(f'első betű: {szoveg[0]}')

# 'csak olvasható' listaként, tehát ez nem működik:
# szoveg[0] = 'N'
print(szoveg)

van_benne_1:bool = 'FAGYI' in szoveg
print(van_benne_1)
van_benne_2:bool = 'CICA' in szoveg
print(van_benne_2)

# -----------------------

kisbetus:str = szoveg.lower()
print(kisbetus)
nagybetus:str = szoveg.upper()
print(nagybetus)
kapitalizalt:str = szoveg.capitalize()
print(kapitalizalt)
cimszeru:str = szoveg.title()
print(cimszeru)

kezdodik:bool = szoveg.startswith('nagyon')
print(kezdodik)
vegzodik:bool = szoveg.endswith('cica!')
print(vegzodik)

# 0 1 2 3 4 5 6  7
# n a g y o n   [szeretem]  a FAGYIT! 
kezdoindex_1:int = szoveg.index('szeretem')
print(kezdoindex_1)
kezdoindex_2:int = szoveg.index('a')
print(kezdoindex_2)

# kezdoindex_3:int = szoveg.index('cica!')
# print(kezdoindex_3)

# szoveg = "a cica! ebben már benne van"

if 'cica!' in szoveg:
    print(f'itt kezdödik, hogy "cica!": {szoveg.index("cica!")}')
else: print('nincs benne, hogy "cica!"')

cserelt_1:str = szoveg.replace('n', 'N')
print(cserelt_1)
cserelt_2:str = szoveg.replace('n', 'N').replace('e', 'ö')
print(cserelt_2)
cserelt_3:str = szoveg.replace('nagyon', 'már kevésbé')
print(cserelt_3)
szoveg_2:str = szoveg.replace('nagyon', 'már kevésbé').capitalize()
print(szoveg_2)

szoveg:str = '          John Doe;1992-07-05;Budapest;+36301233211\n\n'

csupasz:str = szoveg.strip()
print(szoveg)
print(csupasz)

szavak:list[str] = csupasz.split(';')
print(szavak)

szoveg = 'Alma     a \n\n fa\talatt'
print(szoveg.split())
print(f'szavak száma: {len(szoveg.split())}')