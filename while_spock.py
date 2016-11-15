from random import randrange

plichta = "Nevopič se! Znovu, srabe!"
umiram = "Aaaaaarhhgghhhh... *chcíp*"
umiras = "Aha! Žer hlínu, špíno!"
jamam = " Já jsem vybral "

print( ' Hrajeme spock, jester, phaser.\n Jestli se bojis, napis \"odchazim\".')

while True:
    cislo = randrange(3)
    print()
    clovek = input( 'Vyber si: spock, jester, phaser? ' ).lower()

    if cislo == 0:
        pocitac = 'phaser'
    elif cislo == 1:
        pocitac = 'jester'
    else:
        pocitac = 'spock'

    if clovek == 'spock':
        if pocitac == 'spock':
            print( jamam, pocitac, "!\n", plichta, "\n" )
        elif pocitac == 'jester':
            print( jamam, pocitac, "!\n", umiram, "\n" )
            break
        elif pocitac == 'phaser':
            print( jamam, pocitac, "!\n", umiras, "\n" )
    elif clovek =='jester':
        if pocitac == 'jester':
            print( jamam, pocitac, "!\n", plichta, "\n" )
        elif pocitac == 'spock':
            print( jamam, pocitac, "!\n", umiras, "\n" )
        elif pocitac == 'phaser':
            print( jamam, pocitac, "!" )
            print( " Ale né! Můj phaser! Vyplivni to, mrcho!\n" )
    elif clovek == 'phaser':
        if pocitac == 'phaser':
            print( jamam, pocitac, "!\n", plichta, "\n" )
        elif pocitac == 'spock':
            print( jamam, pocitac, "!\n", umiram, "\n" )
            break
        elif pocitac == 'jester':
            print( jamam, pocitac, "!" )
            print( " Chlamst! Nemáš čím hrát! Chachachachacháááá!\n" )
            break
    elif clovek == 'odchazim':
        print()
        print('               ... Live long and prosper!')
        break
    else:
        print( ' Co to meleš, ty vořechu!?' )
        print( ' Nezasloužíš si hrát.' )
        print( ' Du domu... *ťap *ťap *ťap *TŘÍSK' )
        break
