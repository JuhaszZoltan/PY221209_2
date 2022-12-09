szoveg:str = input('írj be valamit: ')

print(szoveg[::-1])

for i in range(len(szoveg)):
    print(szoveg[len(szoveg) - 1 - i], end='\0')
