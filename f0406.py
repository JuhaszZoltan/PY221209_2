szoveg:str = input('írj be valamit: ')

c:int = 0
for b in szoveg:
    if b in 'EeÉé': c += 1
print(f'e betűk száma: {c}')