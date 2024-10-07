nev = input("szia, hogy hívnak?: ")
print(f"Hello, {nev}!")
print(f"milyen szép név az, hogy {nev}! <3")
valasz = input(f'szeretsz programozni {nev}?: ')
if valasz == 'igen':
    print('akkor még sokra viheted itt! :)')
else:
    print('nem baj, majd megszereted!')
szam = int(input('hányszor írjam ki, hogy babán?: '))
for x in range(szam):
    print('banán')