from time import sleep

prica_igre = [["Pa Hajde da se zapustimo u pricu i pustimo masti na volju.."],
              ["Bezis bezis beziiis, juri te pajton pobrkao si ocene u skoli"],
              ["informatika ti je slabija strana, ali pajton hoce da ga svi znaju"],
              ["i bacio si se u beg, bezis iz skole i kreces ka kuci, medjutim"],
              ["odrzavaju se radovi i ne mozes kuci brzim putem sta ces raditi?"]
             ]


odgovor = input("Da li zelis da pokrenes avanturu u pajtonu?? (da/ne)\n")

igraPocinje = False


if odgovor.upper().strip() == "DA":
    igraPocinje = True
    for deo in prica_igre:
        print(deo)
        sleep(2)
    print("a) - Dali ces se vratiti nazad u skolu i pokusati da nadjes drugi put")
    odgovor = input("b) - Ili ces ici suprotno od kuce kroz ulicu??\n")
    if odgovor.upper().strip() == 'A':
        print("Strasni pajton te je stigao, sva ostala vrata su bila zakljucana")
        print("I progtao te je komandom INPUT")
        igraPocinje = False
    if odgovor.upper().strip() == 'B':
        print("Otisao si suprotno od kuce, 'Hmm, malo sam mu odmakao'\nKazes sebi, ODJEDNOM SE POJAVLJUJE I TRCII\nMORAMO NESTO BRZO DA SMISLIMO!!!!")
        odgovor = input("a) - Da li da nastavim pravo ulicom\nb) - Ili da skrenem desno da sebi zavaram trag???\n")
        if odgovor.upper().strip() == 'A':
            print("Ah, ah, ah, Previse sam umoran mislim da cu se suociti sa njim ne mogu vise da bezim")
            print("Bice ti ponudjene dve reci moras da odaberes onu koja je zapravo kod u pajtonu")
            odgovor = input("a) - input, b) - cin>>: ")
            if odgovor.upper().strip() == 'A':
                odgovor = input("a) - form, b) - for: ")
                if odgovor.upper().strip() == 'B':
                    odgovor = input("a) - if, b) - Qaternion: ")
                    if odgovor.upper().strip() == 'A':
                        odgovor = input("a) - Else If, b) - elif: ")
                        if odgovor.upper().strip() == 'B':
                            odgovor = input("a) - sleep , b) - while: ")
                            if odgovor.upper().strip() == 'B':
                                odgovor = 'igra je zavrsena'
                                print("Python: ArrAAAararaaa porazen sam znanjem koje ja donosim JA NE MOGU DA VERUJEEEM")
                                print("Bila je tlaka poraziti ga, ali nije tesko da se nauci nista kada se hoce")
                                print("Polazeci kroz ovo bar sam naucio Python i pocecu da pravim slovne avanture")
                                print("Bas poput ove")
                                igraPocinje = False
                            if odgovor.upper().strip() == 'A':
                                print("Ovo je bilo zadnje pitanje, ali si odgovorio\nPogresno i samim tim moras sve ponovooo")
                                igraPocinje = False
                        if odgovor.upper().strip() == 'A':
                            print("Else if je sastavni deo if naredbe u drugim\nProgramskim jezicima ali ne i u\nPython-u")
                            igraPocinje = False
                    if odgovor.upper().strip() == 'B':
                        print("Quaternion je termin u matematici za Kvaternione")
                        print("Mnogo je tesko i povezano je sa Vektorima i skalarima")
                        print("Koristi se u Unity Game Enginu za programiranje igara")
                        print("Ali nije ono sto nama treba Vise srece drugi put")
                        igraPocinje = False
                if odgovor.upper().strip() == 'A':
                    print("Form nije deo pajtona i nije kljucan rec")
                    print("Ispadas ... ali Pokusaj ponovo uvek ima nade..")
                    igraPocinje = False
            if odgovor.upper().strip() == 'B':
                print("Pogresan odgovor cin>> je naredba iz programskog jezika C++")
                print("Ahhh tako blizu a tako daleko C C C (Da ne dodajem jos 3 plusa :D )")
                igraPocinje = False
        if odgovor.upper().strip() == 'B':
            print("Mislim da sam mu odbegao dosta\n TAKO JE NE JURI ME VISE")
            print("Pobedio si, Ali nisi naucio pajton, nekim drugim nacinom bi dosao do drugog kraja :)")
            print("Hvala sto si igrao moju avanturu sa pajtonom")
            igraPocinje = False
else:
    print("Bar si usao u fajl da vidis sta je :/ vidimo se")

print("Hvala sto ste zaigrali moju slovnu avanturu :D")
print("Python 3.8/2020, Lazar Petrovic")