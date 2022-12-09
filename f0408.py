mondat:str = input('írj be valamit: ')
if mondat[-1] == '!':
    print('a beírt mondat típusa felkiáltó, felszólító vagy óhajtó')
elif mondat[-1] == '.':
    print('a beírt mondat típusa kijelentő')
elif mondat[-1] == '?':
    print('a beírt mondat típusa kérdőmondat')
else:
    print('nem meghatározható a beírt mondat típusa')

# mondat[-1] == mondat[len(mondat) - 1]