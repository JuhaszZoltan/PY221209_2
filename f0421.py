from random import shuffle

szavak:list[str] = ['lyuk', 'papagáj', 'hajó', 'gálya', 'folyó', 'milyen', 'muszáj', 'jég']

shuffle(szavak)

hvsz:int = 0
for i in range(len(szavak)):
    betu:str = input(f'{i+1}.) {szavak[i].replace("j", "_").replace("ly", "_")}: ')
    if betu.lower() in szavak[i]:
        hvsz += 1
        print('\thelyes!')
    else: print('\tnem jó!')

print(f'találatok száma: {hvsz}/{len(szavak)}')