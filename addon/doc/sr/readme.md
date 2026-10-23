# Unigram Plus

* Autor: Kostya Gladkiy (Ukrajina)
* [Telegram kanal](https://t.me/unigramPlus)
* Telegram: @unigramPlus
* link za donaciju: [https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)

Koristite Unigram na ugodniji i produktivniji način. Ovaj dodatak nudi mnoge tasterske prečice za brzo i ugodno korišćenje Unigrama i čini mnogo malih poboljšanja.

## Neka od velikih poboljšanja su:

* Dodaje značajno poboljšanje u prikazivanju takvih poruka kao što su anketa, link ili poruka s priloženim medijima.
* Kada se kursor fokusira na listu ćaskanja, informacije poput "ćaskanja, kartica, izabrana lista" se ne objavljuju, a kada se kursor nalazi na listi poruka, nećete čuti reč "Lista".
* Kad se fokusirate na dugme Otvori datoteku ili dugme Preuzmi datoteku, izgovara će se naziv i veličina datoteke, a kada se fokusirate na dugme Reprodukuj na audio datoteci, čućete njen naziv i trajanje.
* Kad se fokusirate na glasovnu poruku koja se trenutno reprodukuje, prvo ćete čuti vreme reprodukcije, a zatim ostatak relevantnih informacija.
* Kad se fokusirate na odabranu poruku u ćaskanju, prvo ćete čuti informacije da je odabrana, a zatim i sadržaj poruke.
* Dok se krećete kroz listu poruka u ćaskanju, uopšte nećete čuti reč "Viđeno", ali reč "Nije viđeno" biće izgovorena pre čitanja same poruke. Trenutno ova funkcija radi samo na engleskom, ruskom, ukrajinskom, španskom, portugalskom, hrvatskom, turskom i persijskom jeziku.
* funkcija snimanja glasovnih poruka značajno je modernizovana. Početak snimanja i slanje glasovne poruke popraćeni su karakterističnim zvukovima, a otkazano snimanje Unigram 13.0 i noviji objavljuju sami. Nadalje, dok se ove funkcije izvode, fokus ostaje u istom položaju i ne skače na dugme Snimanje niti u polje za uređivanje.
* Dodata je mogućnost praćenja aktivnosti ćaskanja. Ova funkcija se aktivira dvostrukim pritiskom na kombinaciju "ALT+T".
* Ako se medijske datoteke priložene uz poruku otvore pritiskom na razmak nakon zatvaranja, kursor se vraća na mesto na kojem je bio pre.
* Moguće je onemogućiti zvuk svih indikatora performansi ili samo indikatora toka reprodukcije glasovnih poruka.

## Prilagođeni zvukovi
Zvukovi UnigramPlus nalaze se u fascikli `appModules\media` dodatka. Otvorite NVDA podešavanja > UnigramPlus i pritisnite **Otvori fasciklu zvukova UnigramPlus**. Da prilagodite zvuk, kopirajte zamensku WAV datoteku u tu fasciklu sa istim nazivom kao zvuk koji želite da zamenite, zatim ponovo pokrenite NVDA ili ponovo učitajte dodatke. Ažuriranja dodatka mogu vratiti ugrađene zvukove, zato sačuvajte kopiju svojih datoteka.

## Podaci o donacijama programeru:

Ako Vam se ovaj dodatak zaista sviđa i imate želju, a što je najvažnije priliku, finansijski podržati razvojnog programera i time ga motivisati da nastavi razvijati ovaj dodatak, to možete učiniti prenosom male količine pomoću sledećih bankovnih podataka:
[Link za donaciju](https://unigramplus.diaka.ua/donate) ili broj kartice je 5169360009004502 (Ukrajina).

I zapamtite da su svi koji su pročitali ovaj red mislili da će neko sigurno podržati programera ali to neću biti ja.

<!-- shortcut-table-start -->
## Lista prečica:

> In the Category column, `UnigramPlus` identifies shortcuts provided by the add-on and `Unigram` identifies shortcuts built into Unigram.

> `Unigram (nedokumentovano)` označava prečice ugrađene u trenutni izvorni kod Unigrama koje još nisu navedene u zvaničnom Shortcuts.md dokumentu.

> [!TIP]
> You can customize UnigramPlus shortcuts from NVDA menu > Preferences > Input gestures.

### Kretanje između ćaskanja

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | Next chat |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | Previous chat |
| **Ctrl+Alt+Home** | Unigram (nedokumentovano) | Prvi razgovor |
| **Ctrl+Alt+End** | Unigram (nedokumentovano) | Poslednji razgovor |
| **Ctrl+Alt+Up/Down** | UnigramPlus | Prelazak na sledeće ili prethodno ćaskanje sa nepročitanim pominjanjima |
| **ALT+1** | UnigramPlus | Pomeranje fokusa u listu ćaskanja |
| **ALT+2** | UnigramPlus | Pomeranje fokusa na poslednju poruku u ćaskanju |
| **ALT+3** | UnigramPlus | Premeštanje fokusa na oznaku nepročitane poruke |
| **ALT+4** | UnigramPlus | Pomeranje fokusa u listu fascikli za ćaskanje |
| **ALT+5** | UnigramPlus | pomerite fokus da otvorite profil |
| **ALT+6** | UnigramPlus | Pomeraj fokus na listu grupnih niti |
| **ALT+D** | UnigramPlus | Pomeri fokus u polje za uređivanje. Ako je fokus već u polju za uređivanje, nakon pritiska na interventne tastere on će biti pomeren tamo gde je bio ranije |

### Pretraga

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+E** | Unigram | Chat search |
| **Ctrl+F** | Unigram | Messages search per chat |
| **Ctrl+Shift+F** | Unigram (nedokumentovano) | Chat search |
| **Search key** | Unigram (nedokumentovano) | Pretraži trenutnu stranicu |
| **ALT+I** | UnigramPlus | Idite na listu sa rezultatima pretrage |
| **F3** | UnigramPlus | Idi na sledeći rezultat pretrage |
| **Shift+F3** | UnigramPlus | Idite na prethodni rezultat pretrage |

### Izabrani tekst u polju za unos

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+Z** | Unigram | Undo |
| **Ctrl+Y** | Unigram | Redo |
| **Ctrl+Shift+Z** | Unigram (nedokumentovano) | Ponovi |
| **Alt+X** | Unigram (nedokumentovano) | Pretvori četiri izabrane heksadecimalne cifre u odgovarajući znak |
| **Ctrl+X** | Unigram | Cut |
| **Ctrl+C** | Unigram | Copy |
| **Ctrl+V** | Unigram | Paste |
| **Ctrl+A** | Unigram | Select All |
| **Ctrl+Shift+.** | Unigram | Citat |
| **Ctrl+B** | Unigram | Bold |
| **Ctrl+I** | Unigram | Italic |
| **Ctrl+U** | Unigram | Podvučeno |
| **Ctrl+Shift+X** | Unigram | Strikethrough |
| **Ctrl+Shift+M** | Unigram | Monospace |
| **Ctrl+Shift+P** | Unigram | Spoiler |
| **Ctrl+K** | Unigram | Create Link |
| **Ctrl+Shift+N** | Unigram | Ukloni formatiranje (običan tekst) |

### Fascikle

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+1** | Unigram | First folder (All chats) |
| **Ctrl+2** | Unigram | Second folder |
| **Ctrl+3** | Unigram | Third folder |
| **Ctrl+4** | Unigram | Fourth folder |
| **Ctrl+5** | Unigram | Fifth folder |
| **Ctrl+6** | Unigram | Sixth folder |
| **Ctrl+7** | Unigram | Seventh folder |
| **Ctrl+8** | Unigram | Eighth folder |
| **Ctrl+9** | Unigram | Archive |
| **Ctrl+Shift+Down** | Unigram (nedokumentovano) | Sledeća fascikla |
| **Ctrl+Shift+Up** | Unigram (nedokumentovano) | Prethodna fascikla |

### Radnje sa porukama

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Space** | UnigramPlus | Play or stop the focused voice or video message, or open media attached to the message |
| **Ctrl+C** | UnigramPlus | Kopiraj poruku ako sadrži tekst. Ako je fokus na linku, link će biti kopiran |
| **ALT+Q** | UnigramPlus | Pritisni instant viev ako se nalazi u trenutnoj poruci |
| **ALT+Delete** | UnigramPlus | Brisanje poruke ili ćaskanja |
| **Shift+Delete** | UnigramPlus | Brisanje poruke ili ćaskanja obe strane |
| **Delete** | Unigram (nedokumentovano) | Obriši izabranu ili fokusiranu poruku |
| **Ctrl+ALT+C** | UnigramPlus | Otvori komentare |
| **Enter** | UnigramPlus | Odgovori na poruku |
| **ALT+F** | UnigramPlus | Prosledi poruku |
| **Backspace** | UnigramPlus | Izmeni poruku |
| **ALT+Shift+R** | UnigramPlus | Označi ćaskanje kao pročitano |
| **Ctrl+Space** | UnigramPlus | Prebacivanje u režim izbora |
| **Unassigned** | UnigramPlus | Sačuvaj datoteku kao... |
| **Unassigned** | UnigramPlus | Prikači poruke ili ćaskanje |
| **Left Arrow** | UnigramPlus | Najavi originalnu poruku, poruku na koju je odgovoreno |
| **Right Arrow** | UnigramPlus | Move to the next media attachment in the focused message |
| **ALT+C** | UnigramPlus | Prikaži tekst poruke u iskačućem prozoru |
| **ALT+W** | UnigramPlus | Announces the time a message was sent or received, as well as a list of reactions. Double-clicking toggles the announcement mode for this information. |
| **ALT+[** | UnigramPlus | Prebacuje izgovaranje zaglavlja poruka pre ili posle sadržaja poruke |
| **NVDA+Ctrl+0-9** | UnigramPlus | Review one of the ten most recent messages; 1 is the newest and 0 is the tenth newest |
| **Ctrl+Shift+A** | UnigramPlus | Pritisni priloži datoteku dugme |
| **Ctrl+Shift+E** | Unigram (nedokumentovano) | Otvori birač emodžija |
| **Ctrl+Shift+G** | Unigram (nedokumentovano) | Otvori birač GIF-ova |
| **Ctrl+Shift+S** | Unigram (nedokumentovano) | Otvori birač stikera |
| **Ctrl+O** | Unigram (nedokumentovano) | Otvori birač datoteka za slanje dokumenata |
| **Ctrl+N** | UnigramPlus | Pritisni novi razgovor dugme |
| **Arrow Up** | Unigram | Edit last sent message |
| **Ctrl+Arrow Up** | Unigram | Reply to last sent message |
| **Esc / Alt+Arrow Left** | Unigram | Go back |
| **Alt+Arrow Right** | Unigram | Redo go back |

### Glasovne poruke i mediji

| Prečica | Kategorija | Radnja |
|---|---|---|
| **ALT+P** | UnigramPlus | Pusti/pauziraj glasovnu poruku koja se trenutno reprodukuje |
| **ALT+S** | UnigramPlus | Povećavanje i smanjivanje brzine reprodukcije glasovne poruke |
| **ALT+E** | UnigramPlus | Zatvori audio plejer |
| **NVDA+ALT+R** | UnigramPlus | Pretvori glasovnu poruku u tekst |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | Fast forward a voice message |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | Rewind voice message |

### Snimanje poruka

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+R** | Unigram | Start record |
| **Ctrl+R (again)** | Unigram | Send recorded |
| **Ctrl+D** | Unigram | Stop recording |
| **Space (while recording) / Ctrl+P** | Unigram | Pause recording |

### Pozivi

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+Home** | Unigram | Accept incoming call |
| **Ctrl+End** | Unigram | Reject incoming call |
| **Ctrl+Page Up** | Unigram | Toggle camera |
| **Ctrl+Page Down** | Unigram | Toggle microphone |
| **ALT+Shift+C** | UnigramPlus | Pozovite ako je kontakt ili uđite u glasovno ćaskanje ako je grupa |
| **ALT+Shift+V** | UnigramPlus | Pritisni video poziv dugme |
| **ALT+Y** | UnigramPlus | Prihvati poziv |
| **ALT+N** | UnigramPlus | Pritisni odbij poziv ako postoji dolazni poziv, dugme završi poziv ako je poziv u toku ili napusti glasovno ćaskanje ako je aktivno. |
| **ALT+A** | UnigramPlus | Pritisni "Uključi/isključi mikrofon" dugme |
| **ALT+V** | UnigramPlus | Pritisni "Uključi/isključi kameru" dugme |

### Ostale prečice

| Prečica | Kategorija | Radnja |
|---|---|---|
| **Ctrl+0** | Unigram | Saved messages |
| **Ctrl+W** | Unigram | Close current window |
| **Ctrl+Q** | Unigram | Close Unigram (main window only) |
| **Ctrl+Shift+Y** | Unigram | Change status |
| **Ctrl+Shift+W** | Unigram (nedokumentovano) | Zaustavi reprodukciju medija |
| **Ctrl+F4** | Unigram (nedokumentovano) | Close current window |
| **Ctrl+L** | Unigram (nedokumentovano) | Zaključaj Unigram |
| **Ctrl+M** | Unigram (nedokumentovano) | Umanji Unigram |
| **Ctrl+J** | Unigram (nedokumentovano) | Otvori preuzimanja |
| **ALT+T** | UnigramPlus | Najavi ime i status otvorenog ćaskanja |
| **NVDA+Alt+V** | UnigramPlus | Otvori informacije o verzijama programa Unigram i dodatka UnigramPlus u prozoru samo za čitanje |
| **ALT+M** | UnigramPlus | Otvori meni za navigaciju |
| **ALT+Shift+M** | UnigramPlus | Otvori podešavanja Unigrama |
| **ALT+Shift+P** | UnigramPlus | Otvori trenutni profil za ćaskanje |
| **ALT+L** | UnigramPlus | Omogući automatsko čitanje novih poruka u trenutnom ćaskanju |
| **ALT+H** | UnigramPlus | Prikaži listu svih UnigramPlus prečica |
| **ALT+U** | UnigramPlus | Uključi najave trake napredovanja |
| **ALT+Shift+L** | UnigramPlus | Kopiraj podatke da biste izvršili emitivanje u privermenu memoriju |
| **NVDA+ALT+U** | UnigramPlus | Otvori prozor sa podešavanjima za UnigramPlus |
<!-- shortcut-table-end -->

## Lista promena:

###Verzija 5.5.3

* Dodato je automatsko najavljivanje napretka slanja i preuzimanja datoteka. U podešavanja najave traka napretka dodata je nova opcija „Samo tokom slanja i preuzimanja”, koja je sada podrazumevana. Prečica ALT+U sada se prebacuje između tri stanja: isključeno, samo tokom slanja/preuzimanja i najavljuj sve trake napretka.
* Ažurirani su readme i prevodi.

###Verzija 5.5.2

* Ažurirani su readme i prevodi.
* Promenjen je zvuk indikatora kucanja.

###Verzija 5.5.1

* Ispravljena je prečica za kretanje kroz listu tema grupe (ALT+6). Sada se ispravno prepoznaje lista tema prilikom otvaranja forumske grupe iz liste ćaskanja.
* Dodat je zvuk indikatora kucanja: zvuk se reprodukuje u petlji dok druga strana kuca u ćaskanju i prestaje kada ona završi. Ova funkcija je inspirisana odgovarajućom funkcijom u Unigram JAWS skripti.

###Verzija 5.5.0

* Dodata je kompatibilnost sa NVDA 2026.1.

###Verzija 5.4.2

* Dodata je kompatibilnost sa NVDA 2025.3.3.

###Verzija 5.4.1

* Dodata je kompatibilnost sa NVDA 2025.1.2.

###Verzija 5.4.0

* Rešen je problem sa listom ćaskanja.

###Verzija 5.3.0
*Dodata je prečica na tastaturi koja najavljuje vreme slanja ili primanja poruke i reakcije u poruci. Ovo je korisno kada želite da čujete vreme slanja ili prijema poruke bez prethodnog preslušavanja celog teksta poruke. Podrazumevano, ovo je kombinacija tastera ALT+W. Dvostruki klik uključuje način objavljivanja ove informacije.
* Popravljeni su svi problemi koji su se nedavno nakupili kao rezultat promena u unigram interfejsu.
* Promenjena je prečica na tastaturi za otvaranje korisničkog profila u ALT+shift+p.
* Dodata kompatibilnost sa NVDA 2024.4.
* Promenjene su prečice na tastaturi za navigaciju do sledećeg i prethodnog rezultata pretrage na f3 i pomeranje f3 kao u većini aplikacija.

Verzija 5.2.0
* Dodata je mogućnost odabira datoteka priloženih porukama sa horizontalnim strelicama i otvaranja izabrane datoteke pomoću razmaka.
* Sada se linkovi u porukama neće čitati u podpunosti, već samo do znaka pitanja.
* Sada, kada zatvorite pregledač fotografija ili video zapisa, unigramplus će pokušati da postavi fokus na poruku koju gledate.
* Prečica na tastaturi za otvaranje unigramplus podešavanja je promenjena. Sada je ova funkcija dodeljena kombinaciji nvda+alt+u.
* Urađena je optimizacija koda, što je rezultiralo značajno poboljšanim vremenom odgovora prilikom navigacije po listi za ćaskanje i listi poruka. Ovo je posebno primetno na porukama koje sadrže mnogo ugnežđenih elemenata.
* mnogi manji problemi su popravljeni.
* Mnogo zastarelih kodova je uklonjeno.
Verzija 5.1.0
* Dodate prečice na tastaturi za navigaciju do sledećeg i prethodnog rezultata pretrage u ćaskanju. Podrazumevano, ove funkcije su dodeljene kombinacijama tastera ALT+K i ALT+J.
* Dodata je prečica na tastaturi za otvaranje liste sa svim rezultatima pretrage u ćaskanju. Podrazumevano, ova funkcija je dodeljena kombinaciji tastera ALT+I.
* Sada, dvostrukim pritiskom na strelicu levo na poruci, fokus će se pomeriti na poruku na koju trenutna poruka odgovara.
* Rešen je problem gde se opisi linkova ugrađenih u poruku nisu čitali.
* Unigramplus više neće predlagati ažuriranja na zaštićenim ekranima. Međutim, korisnici će morati još jednom da otvore nvda podešavanja i kliknu na koristi poslednje sačuvane postavke tokom prijavljivanja i čitanja zaštićenih ekrana (potrebna su administratorska prava) dugme.
* Uklonjena je funkcija za premotavanje glasovnih poruka i funkcija podešavanje reakcija na poruke, jer ove funkcije nisu radile pouzdano.
	* Uklonjena je funkcija kopiranja poruka jer unigram sada ima ovu funkciju. Imajte na umu da ponekad kopiranje poruka može dovesti do blagog zamrzavanja programa, ali to nije povezano sa unigramplus dodatkom.
* Ispravljene neke druge manje greške.
Verzija 5.0.0
* Rešen je problem gde su poruke u četovima čitane dva puta.
* Rešen je problem gde prečica za navigaciju do otvorenog profila nije ispravno funkcionisala.
* Rešen je problem gde prečica na tastaturi za otvaranje menija za navigaciju nije radila.
* Rešeni su svi problemi sa dugmetom za uključivanje/isključivanje mikrofona u glasovnim razgovorima.
* Rešen je problem na poljskom jeziku gde je unošenje znaka blokirano kombinacijom ALT+C.
* Ispravljen je izgovor fraza vlasnik i administrator u porukama.
* Rešeno je nekoliko drugih manjih problema.

###Verzija 4.8.0
* Sada u postavkama unigrama, kategorije podešavanja se mogu otvoriti pritiskom na enter. Kada otvorite bilo koju kategoriju podešavanja, fokus će biti stavljen na tu kategoriju.
* Sada kada kliknete na dugme objašnjenje u kvizovima, tekst objašnjenja će se otvoriti u posebnom prozoru radi lakšeg pregleda.
* Rešen je problem gde se imena fascikli za ćaskanje nisu izgovorila prilikom prebacivanja između njih.
* Ispravljena greška koja je onemogućavala onemogućavanje ili promenu redosleda izgovaranja tipa i imena ćaskanja.
* Rešen problem kada nije bilo moguće pronaći tačan odgovor u kvizovima.
* Rešen je problem sa kopiranjem poruke pomoću kombinacije control+shift+C.
* Napravljeno nekoliko manjih popravki, poboljšanja i optimizacija koda.


###Verzija 4.7.0

* UnigramPlus je sada prilagođen najnovijoj verziji unigrama.
* Kompatibilnost sa NVDA 2023 je sada osigurana.
* tasterska prečica ALT+1 sada pomera fokus ne samo na listu za ćaskanje, već i na listu kontakata i listu odeljaka podešavanja.
* Automatsko najavljivanje novih poruka u ćaskanju i automatsko ozvučenje aktivnosti ćaskanja su značajno revidirani, što je rezultiralo poboljšanom stabilnošću.
* Dodata je prečica na tastaturi za prikaz svih UnigramPlus komandi. Podrazumevano, ova funkcija je dodeljena ALT+H.
* Rešeno je i nekoliko manjih problema.

###Verzija 4.6.0

* Dodata je prečica na tastaturi za premeštanje fokusa na listu niti grupe. Prema podrazumevanim podešavanjima, ova je funkcija dodeljena kombinaciji ALT+6. Napominjem da često kada pritisnemo taster enter na grupi koju želimo otvoriti, lista niti se možda neće prikazati i tada je potrebno ponovo postaviti fokus na tu grupu i pritisnuti taster enter. U pravilu, nakon drugog pritiska prikazuje se lista niti, a nakon toga možemo pritisnuti kombinaciju tastera koji će premestiti fokus na tu listu.
* Sada kombinacija ALT+2 postavlja fokus ne samo na listu poruka, već na otvoreni profil, na otvorenu listu niti grupe ili, na otvoreni odeljak sa podešavanjima.
* Sada, u podešavanjima UnigramPlusa možete onemogućiti izgovor izraza "Administrator" i "Vlasnik" na porukama u grupama.
* Kombinacije za prihvatanje i odbijanje poziva sada rade ispravno.
* Sada se funkcija automatskog čitanja novih poruka i praćenja aktivnosti ćaskanja neće isključiti kada se NVDA ponovo pokrene, ali će raditi dok je sami ne isključite.
* Poboljšan prikaz nekih elemenata interfejsa.

### Verzija 4.5.0

* Prilagođeno najnovijoj verziji unigrama.
* Sada ako je poruka poslata kao odgovor na drugu poruku, pritiskom na tastere sa strelicom levo, možete čuti tekst poruke u odgovor na koji je poslat.
* Dodata je francuska lokalizacija.
Uklonjena je mogućnost dodavanja reakcija na poruke sa prečicama na tastaturi, pošto nisam mogao da prilagodim ovu funkciju promenama u unigram interfejsu.
* Ispravljene neke manje greške.

### Verzija 4.4.0

* Dodata je funkcija najave aktivnosti u četovima. Podrazumevano, ova funkcija se aktivira dvostrukim pritiskom na kombinaciju ALT+T. Funkcija ostaje aktivna samo dok se NVDA ne pokrene ponovo.
* Dodata je funkcija automatsko najavljivanje novih poruka u ćaskanju. Podrazumevano, ova funkcija se aktivira pritiskom na ALT+L. Funkcija ostaje aktivna samo dok se NVDA ne pokrene ponovo. Može doći do problema sa stabilnošću ako se previše novih poruka brzo pojavi u ćaskanju.
* Dodata je prečica na tastaturi za funkciju pretvaranje glasovnih poruka u tekst. Podrazumevano, ova funkcija je dodeljena kombinaciji NVDA+ALT+R. Imajte na umu da se u slučajevima kada je glasovna poruka veoma duga, pretvaranje u tekst odvija u delovima. Može se desiti da kada vas UnigramPlus obavesti da je konverzija završena, samo deo glasovne poruke će zapravo biti konvertovan. I nakon nekoliko sekundi, ovaj tekst će biti dodat.
* Sada, kada se krećete kroz listu za ćaskanje, UnigramPlus prijavljuje informacije o premium nalozima i verifikovanim nalozima.

### Verzija 4.3.0

* Sada UnigramPlus radi ispravno kada je nekoliko ćaskanja otvoreno u različitim prozorima.
* Dodata prečica na tastaturi za pomeranje fokusa na oblast korisničkog profila ako je otvorena. Podrazumevani pokret je ALT+5.
* Ispravljene manje greške.

###Verzija 4.2.0

* Mehanizam za čuvanje UnigramPlus podešavanja je značajno redizajniran. Sada podešavanja neće biti sačuvana u NVDA konfiguracionoj datoteci, već će biti sačuvana u sopstvenoj konfiguracionoj datoteci. Ovo bi trebalo da reši problem kada korisnici nakon ažuriranja ili jednostavno iznenada UnigramPlus prestane da radi, zbog problema sa pristupom NVDA konfiguracionoj datoteci. Nažalost, korisnici će morati ponovo da konfigurišu UnigramPlus za sebe, pošto se nakon instaliranja ovog ažuriranja sva podešavanja biti resetovana.
* Rešen problem kompatibilnosti UnigramPlus sa dodatkom bluetooth audio.
* Sada informacija da poruka nije izabrana neće biti prijavljivana. Ako je poruka izabrana, informacije o njoj će biti prijavljene pre sadržaja poruke.
*  Sada će redosled elemenata u ćaskanju biti objavljen ako ste omogućili poziciju elementa u NVDA podešavanjima.
* Dodate oznake nekim dugmadima.

 ###Verzija 4.1.0

* Dodat je pokret za zakačenje poruke ili ćaskanja. Podrazumevano, ovoj funkciji nije dodeljena ni jedna prečica na tastaturi.
* Dodata je prečica na tastaturi za pritiskanje dugmeta „Novi razgovor“. Podrazumevani pokret za ovu funkciju je ctrl+n.
* Dodata je prečica na tastaturi za pritiskanje dugmeta „Priloži medije“. Podrazumevani pokret je ctrl+shift+a.
* Dodata je prečica na tastaturi za odlazak na listu fascikli za ćaskanje. Podrazumevani pokret je ALT+4.
* Sada, kada prelazite između fascikli pomoću strelica, fokus neće skočiti nigde.
* Sada, kada prelazite između foldera pomoću interventnih tastera, pored naziva aktivnog foldera biće najavljen i broj nepročitanih ćaskanja u fascikli.
* Sada, funkcije kao što su „Označi ćaskanje kao pročitano“ i „Zakači poruku ili ćaskanje“ takođe rade obrnuto.

###Verzija 4.0.0

* Obezbeđena kompatibilnost sa unigram 8.8. Pošto se interfejs unigrama promenio, morao sam da prepišem značajan deo koda dodatka.
* Dodata mogućnost premotavanja glasovnih poruka unazad i unapred. Za premotavanje unapred koristite kombinaciju control+ALT i strelica desno, a za premotavanje unazad koristite control+ALT i strelica levo.
* Sada će Unigramplus izveštavati ne samo o prisustvu reakcija u porukama već će izveštavati i detaljne informacije o reakcijama.
* Dodata je mogućnost pregled teksta poruke u uskačućem prozoru. Podrazumevani pokret za ovu funkciju je ALT+V.
* Dodata je tasterska prečica za otvaranje prozora sa podešavanjima UnigramPlus-a. Podrazumevani pokret za ovu funkciju je NVDA+control+u.
* Dodata češka lokalizacija.
* Rešen problem sa ažuriranjem UnigramPlus za stanovnike Ukrajine.

###Verzija 3.2.3

* Dodata kineska lokalizacija.
* Ažurirane postojeće lokalizacije, uključujući engleski.
* Ispravljene manje greške.

###Verzija 3.2.0

* Uklonjene su funkcije kao što su „Praćenje aktivnosti ćaskanja i čitanje novih poruka u otvorenom ćaskanju jer nisam uspeo da ih nateram da ispravno rade u NVDA 2022.1.
* Poboljšana dostupnost uključivanja/isključivanja zvuka i uključivanja/isključivanja kamere u pozivima. Sada nakon pritiska na prečicu za obe funkcije, njihov status će biti objavljen.
* Rešen je problem gde taster enter nije radio ispravno na nekim elementima. Sada još uvek možete da snimate glasovne poruke tako što ćete držati taster enter na dugmetu za snimanje.
* Sada možete da dodelite prečice na tastaturi funkcijama kao što su „Odgovori na poruku i izmeni poruku. Takođe možete dodeliti ove funkcije tasterima kao što su enter, backspace ili čak i strelice nalevo ili nadesno, i neće ometati te tastere na drugim stavkama. Imajte na umu da u početku nikakvi tasteri neće biti dodeljeni ovim funkcijama, ali ćete moći da ih dodelite samo kada je fokus na jednoj od poruka ćaskanja.
* Sada bi funkcija „Izgovori ime pošiljaoca“ trebalo da radi ispravnije.
* Kada se fokusirate na vezu sadržanu u poruci, tekst poruke neće biti izgovoren prvi, ali će tekst prvi biti izgovoren odmah.
* Napravljena su mala poboljšanja i ispravljene su mnoge greške i nedostaci.
* Sada bi UnigramPlus trebalo da radi znatno brže.

###Verzija 3.1.0

* Poboljšano je izražavanje anketa. Imena korisnika koji su učestvovali u anketama sada se objavljuju u prozoru sa rezultatima. Ankete će takođe dati informacije o tome koja je od opcija bila tačna.
* Dodata je mogućnost reagovanja na poruke, ali samo u privatnim četovima. Ova funkcija neće raditi ispravno u grupama i kanalima. U privatnim četovima, pritiskom na NVDA + ALT + brojevi od 1 do 5, možete ukucati sledeće reakcije: 1 - 👍, 2 - 👎, 3 - ❤, 4 - 🔥, 5 - 🥰.
* Dodata je mogućnost glasovnih informacija o postojećim odgovorima na poruke. Nažalost, još nije moguće tačno istaći reakciju #
* Dodata je kombinacija za brzu kopiju podataka potrebnih za emitivanje. #
* Rešen je problem sa prikazivanjem inline rezultata koji su se pojavili u najnovijim verzijama unigrama

###Verzija 3.0.0
Napomena! Od sada će UnigramPlus podržavati NVDA verzije ne starije od 21.2.0.
* Dodate oznake za mnoge stavke interfejsa,
* Ispravke nekih grešaka.

###Verzija 2.9.0
* Sada će polje za uređivanje promeniti svoju oznaku u zavisnosti od toga da li odgovorimo na poruku ili je izmenimo.
* Dodata je mogućnost da se u podešavanjima omogući dijalog za potvrdu za brisanje poruka ili ćaskanja pomoću prečica.
* Dodata srpska lokalizacija.

### Verzija 2.8.0
* Dodata je mogućnost ažuriranja aplikacije. Sada, kako biste proverili ima li ažuriranja i instalirali ih, samo otvorite UnigramPlus podešavanja i kliknite odgovarajuće dugme. Tu takođe možete omogućiti automatsku provjeru ažuriranja kada se NVDA pokrene.
* Dodata arapska lokalizacija.

### Verzija 2.7.0
* Sada ćete biti obavešteni da je poruka prosleđena.
* funkcija kopiranja poruka je modernizovana. Sada, ako je fokus na stavci na koju se može kliknuti u tekstu poruke, nakon pritiska Control + C kopiraće se samo tekst veze u fokusu, a ne celi tekst.
* Dodate prečice za kopiranje poruka uz očuvanje oblikovanja teksta. Ova funkcija oponaša aktiviranje odgovarajuće stavke u meniju aplikacija. Zadate prečice za ovu funkciju su Control + Shift + C. Prečice za otvaranje komentara promenjene su u Control + Alt + C.
* dodata je funkcija za automatsku najavu novih poruka u otvorenom ćaskanju. Standardno je omogućena pritiskom na Alt + L.
* dodate su prečice za brzi pregled poruka u ćaskanju. Morate pritisnuti NVDA + Control + funkcija koja odgovara broju određene poruke obrnutim redosledom, odnosno ako želite pogledati poslednju poruku pritisnite 1, pre poslednje pritisnite 2, itd.
* Sada pritiskom na Alt + T dobićete informacije o aktivnom glasovnom ćaskanju u trenutnoj grupi.

### Verzija 2.6.0
* Osigurana kompatibilnost s NVDA 21.3.
* Dodate prečice za omogućavanje odabira poruka ili ćaskanja.
* Dodate prečice za prosleđivanje poruka.
* Dodate prečice za označavanje ćaskanja kao pročitanog.
* Poboljšana izvedba postojećih funkcija

### Verzija 2.5.0
* Sada postoji odabirni okvir koji, ako je označen, rešava problem sa snimanjem glasovnih poruka s kojim se susreću neki korisnici.
*Dodata je prečica za odgovaranje na poruku. To možete učiniti pritiskom tastera Enter na poruci ili možete dodeliti alternativne tastere za prečice za ovu funkciju nečemu drugom.
* Dodata prečica za uređivanje poruke. zadana kombinacija tastera je Alt + Backspace.

### Verzija 2.4.0
* Kad se usredotočite na poruku, čućete ime njenog pošiljaoca.
* Kad se usredotočite na grupno ćaskanje koje sadrži nepročitane poruke, dobićete obaveštenje ako u ovoj grupi postoje odgovori za Vas.
* Takođe su poboljšane performanse funkcija dodatih u prethodnom ažuriranju.

### Verzija 2.3.0
* Poboljšana pristupačnost poruka koje sadrže nekoliko priloženih medija. Ranije je potpisu poruke koja sadrži više od jednog priloženog medija bilo moguće pristupiti samo uz pomoć navigacije objekta. Sada će se ovaj potpis pročitati izravno nakon fokusiranja na takvu poruku.
* Poboljšana dostupnost poruka koje sadrže ankete. Kad se usredotočite na takve poruke, čućete brojne ljude koji su već glasali, kao i sve opcije odgovora s rezultatom za svaku opciju. Ako se usredotočite na određenu opciju, čućete rezultat za nju.
* Poboljšana pristupačnost poruka koje sadrže URL-ove. Sada, ako URL ima opis, takođe će se pročitati, na primer, ako poruka sadrži URL za YouTube, naziv i opis za ovaj video zapis biće pročitani odmah nakon samog URL-a. Nadalje, ako URL sadrži više od 30 znakova, biće skraćen za lakše čitanje opisa koji sledi.
* Poboljšana pristupačnost table s rezultatima inline upita. Za navigaciju kroz rezultate umetnutih upita koristite sledeće kombinacije: Control + Strelica gore i Control + Strelica dole.
* Dodate prečice za otvaranje komentara.

### Verzija 2.2.0
* Dodate su tasterske prečice za brisanje poruka i ćaskanja, kako za sebe tako i za oba sagovornika. Ova je funkcija povezana s jezikom interfeisa Unigrama, pa možda neće raditi na nekim lokalizacijama. U podešavanjima možete odabrati vrstu obaveštenja o brisanju, tekstualnu i zvučnu.
* U podešavanjima možete odrediti koji jezik interfeisa koristite u Unigramu. To je potrebno kako bi funkcije povezane s lokalizacijom radile ispravno.
* dodata je kombinacija za otvaranje trenutnog profila za chat.
* Sada, nakon zatvaranja ćaskanja, fokus će ići na listu ćaskanja, a ne na dugme za otvaranje menija za navigaciju.

### Verzija 2.1.0
* Prilikom prebacivanja između fascikli na listi ćaskanja izgovaraće se naziv trenutne fascikle.
* Na listi ćaskanja čućete naziv ćaskanja i njegovu vrstu.
* Premeštanje fokusa na funkciju popisa ćaskanja moderizovano je. Sada bi trebao raditi tačnije i bez odlaganja.
* Sada su podešavanja dodatka postala još fleksibilnija, jer se odeljak koji sadrži neke opcije UnigramPlusa pojavio u meniju nvda podešavanja.
* Dodata poljska lokalizacija.
* Mnoge male ispravke i poboljšanja.

### Verzija 2.0.0
* funkcija u kojoj se ne izgovara reč "Viđeno" i izgovara reč "Nije viđeno" pre čitanja sadržaja poruke sada radi na španskom, portugalskom, hrvatskom, turskom i persijskom jeziku.
* funkcija najave trake napredovanja, poboljšana je. Sada, kada je ovaj način omogućen, ne najavljuju se sve trake napredovanjaa, već samo one pod fokusom.
* Ako pritisnete razmak na poruci koja sadrži datoteku čije preuzimanje nije završeno, dobićete obaveštenje da je preuzimanje obustavljeno.
* Dodata je lokalizacija za portugalski.
* Rešeni su neki manji problemi i poboljšane performanse.

### Verzija 1.9.0
* Dodata je kombinacija koja prebacuje nivo najavljivanja zvuka između vrednosti kao što su: "Najavi sve trake napredovanja", "Najavi sve trake napredovanja, osim napredovanja reprodukcije glasovne poruke" i "Ne najavljuj nikakve trake napredovanja". Za one korisnike kojima je onemogućeno automatsko učitavanje medija u Unigramu možete postaviti vrednost "Najavljuj sve trake napredovanja osim napredovanja reprodukcije glasovnih poruka", a za one kojima je omogućeno bolje je postaviti vrednost "Ne objavljuj trake napredovanja".
* Dodate su španske, hrvatske i persijske lokalizacije.
* Ispravljene manje greške iz prethodnih verzija

###Version 1.8.0
* When focused on the Open File button or Download File button the name and size of the file will be spoken, and when focused on the Play button on an audio file you will hear its name and duration.
* Added a combination to move focus to the message input field. If the focus is already in this field, then when you click, the focus will return to the last element that was in focus.
* The chat activity tracking feature is now enabled by double-tapping ALT + T. You can simply enable it, or enable it temporarily, until the next time you close the app.
* Also now added the ability to choose the type of notification for recording voice messages. This is done by double-pressing the control+d combination. There you can choose between an audio alert, a text alert, and you can also return the standard behavior when recording voice messages.

###Version 1.7.0
* The recording voice messages feature has been significantly modernized. Recording, sending voice message and recording cancellation are accompanied by distinctive sounds. Furthermore, while these functions are performed the focus stays in the same position and doesn't jump to the Record button nor to the edit field.###Version 1.7.0
* A possibility of tracking the chat activity was added. This option can be enabled by pressing ALT+shift+T and it stays active until Unigram is closed or the next restart of NVDA.
* hotkeys that activate the More Options button now work in the voice chat window and the call window.

###Version 1.6.0
* If media files attached to a message are opened by pressing space bar after closing them the cursor returns to where it was previously.
* Now you can return to the active voice chat not only from a current group but also from any other chat.
* By pressing ALT+shift+C in an open chat you will return to the voice chat instead of calling the contact.
* If a message is not sent you will be notified about this once this message is in focus.
* If a message in focus contains a link you will hear just the text of the link itself, not the entire message.
* Fixed an issue of not reporting the status change of such buttons as Turn microphone on/off and Turn camera on/off in private calls and voice chats.
* Now the message copying feature allows you to copy the contents of items in the quick view window of a post.

###Version 1.5.1

This update fixes a huge number of bugs and improves the performance of the add-on.

###Version 1.5.0
This update adds a combination that press "Instant View" button in the message, if it contains one. By default, this function is activated by the ALT + Q combination. After opening such an article, the focus will automatically go to the first element of this article, and after closing, the focus will return to the last viewed message. We also fixed an issue where not all article elements in the Instant View Window were read, even if they contained text content.
###Version 1.1.7

Added Turkish localization



###Verzija 5.8.6

* Razmaknica ponovo reprodukuje, otvara i preuzima medije poruke u Unigramu 13.0 i novijim verzijama. Od Unigrama 13.0 sadržaj poruke sa fotografijom, videom, GIF-om, datotekom, pesmom ili glasovne poruke sam je dugme koje to radi. Unigram 13.0.1 je tom dugmetu vratio identifikator koji UnigramPlus traži, osim na glasovnim porukama, gde je identifikator dobilo dugme za pretvaranje govora u tekst, pa razmaknica na glasovnoj poruci nije ništa radila. UnigramPlus sada prepoznaje dugme same glasovne poruke po napretku preuzimanja koji ono javlja. Unigram 13.1.1 i dalje nema radnju za razmaknicu na poruci van režima izbora, pa UnigramPlus pritiska to dugme: razmaknica reprodukuje ili pauzira glasovnu poruku ili pesmu, otvara fotografiju, video ili GIF u pregledaču i preuzima ili otvara datoteku.
* Nakon što razmaknica reprodukuje glasovnu poruku ili pesmu ili preuzme datoteku, fokus ostaje na poruci, a sledeći pritisak tastera Escape ga više ne vraća tamo. To je potrebno samo pregledaču, ali u Unigramu 13.0 i novijim verzijama datoteka ili pesma je široka kao fotografija, pa ju je UnigramPlus smatrao fotografijom.
* Razmaknica više ne otvara nalepnice ni preglede linkova. Unigram 13.0.1 im je dao isti identifikator kao dugmadima za medije, ali oni su linkovi. U pregledu linka koji prikazuje fotografiju ili video razmaknica i dalje otvara fotografiju ili video.
* Strelice desno i levo na poruci sa više medijskih priloga, poput albuma, ponovo najavljuju svaku fotografiju, video, datoteku ili pesmu u Unigramu 13.0 i novijim verzijama. Od Unigrama 13.0 svaki prilog sadrži samo sopstveno dugme svog sadržaja, pa UnigramPlus više nije pronalazio ono po čemu se fotografija razlikuje od videa i za svaki prilog je najavljivao zamensku reč „Медіа”. Sada gleda unutar tog dugmeta: video tamo ima sopstveno dugme za preuzimanje, datoteka ili pesma svoj naslov, a fotografija ni jedno ni drugo.
* Ctrl+Space sada radi i u listi ćaskanja, gde ranije nije radio ništa. Kao i kod poruka, prvi pritisak uključuje režim izbora sa ćaskanjem u fokusu iz kontekstnog menija ćaskanja, a zatim svaki pritisak izabira ćaskanje u fokusu ili poništava njegov izbor, kao što to radi razmaknica u Unigramu. UnigramPlus zatim javlja da li je ćaskanje izabrano. Poništavanje izbora poslednjeg izabranog ćaskanja završava režim izbora. Dok je lista ćaskanja u režimu izbora, UnigramPlus kaže i „Izabrano” pre naziva izabranog ćaskanja kada fokus dođe na njega, kao što to radi kod poruka.
* Dodata je prečica Alt+Shift+M koja otvara podešavanja Unigrama u Unigramu 13.1 i novijim verzijama, kao što to radi UnigramPlusRussianMod. Unigram 13.1 je premestio podešavanja iz bočnog panela u karticu ispod liste ćaskanja. Alt+Shift+M izabira tu karticu, a zatim premešta fokus na vrh podešavanja: na prvi od vaših ostalih naloga ili, ako ste prijavljeni samo na jedan nalog, na „Dodaj nalog”. U verzijama Unigrama starijim od 13.1, kao i u uskom prozoru koji prikazuje samo otvoreno ćaskanje, UnigramPlus javlja „Podešavanja nedostupna”.

###Verzija 5.8.5

* Alt+M ponovo otvara meni za navigaciju u Unigramu 13.1 i novijim verzijama. Unigram 13.1 je zamenio bočni panel menijem koji se otvara istim dugmetom, a to dugme više nije preklopno dugme, pa ga UnigramPlus nije pronalazio i javljao je „Meni za navigaciju nedostupno”.
* Ispravljen je Ctrl+Space u Unigramovom režimu izbora. U tom režimu kontekstni meni izabrane poruke nema komandu Izaberi, pa je UnigramPlus prolazio kroz meni ne pronalazeći je, a poruka je ostajala izabrana. Ctrl+Space sada radi kao u Unigramu 13.1.1: prvi pritisak i dalje uključuje režim izbora iz kontekstnog menija, a zatim svaki pritisak izabira poruku u fokusu ili poništava njen izbor, kao što to radi razmaknica u Unigramu. UnigramPlus zatim javlja da li je poruka izabrana. Poništavanje izbora poslednje izabrane poruke završava režim izbora.
* U režimu izbora razmaknica i Enter na poruci sada je izabiraju ili poništavaju njen izbor, kao u Unigramu, umesto da reprodukuju njene medije ili traže Odgovori u kontekstnom meniju, a Backspace tamo više ne traži Izmeni.
* Ažurirana je kompatibilnost sa NVDA 2026.3. UnigramPlus više ne koristi zastarele delove NVDA API-ja, koje NVDA još podržava, ali ih može ukloniti u nekoj od narednih verzija: okvire sa porukama provere ažuriranja, stari način otvaranja podešavanja UnigramPlusa i konstantu tastera koja se koristi pri premotavanju glasovnih poruka.
* Ažurirani poljski i vijetnamski prevodi.

###Verzija 5.8.4

* Kada je uključena opcija „Automatski premesti fokus na listu ćaskanja pri pokretanju Unigrama”, fokus sada ostaje u iskačućem prozoru koji Unigram prikaže pri pokretanju, poput zahteva za pridruživanje grupi otvorenog preko pozivnog linka. Od verzije 5.6.1 UnigramPlus je premeštao fokus iz iskačućeg prozora na listu ćaskanja iza njega, pa je iskačući prozor bio preskočen.
* Ažuriran vijetnamski prevod.

###Verzija 5.8.3

* Uklonjeno je rukovanje tasterima Enter i razmak koje je UnigramPlus u verziji 4.8.0 dodao listi kategorija podešavanja Unigrama. U Unigramu 13.0 i novijim verzijama svaka kategorija podešavanja je dugme koje se samo otvara tasterom Enter ili razmakom, a fokus dolazi na to dugme, a ne na stavku liste kojom je dodatak rukovao, pa se to rukovanje tu više nije primenjivalo. Pri otvaranju kategorije fokus sada ostaje na njoj, kao i u samom Unigramu, umesto da se pomeri u kategoriju. To rukovanje je obuhvatalo i druge liste kartica, na primer kartice Emoji, GIF-ovi i Nalepnice, gde je presretalo Enter i razmak; sada ti tasteri i tamo stižu do Unigrama.
* U podešavanjima Unigrama Alt+1 sada pomera fokus na otvorenu kategoriju podešavanja ili na prvu kategoriju ako nijedna nije otvorena. Ranije je listu kategorija tražio na fiksnom mestu stranice podešavanja, a zatim pokušavao da pomeri fokus na element koji u Unigramu 13.0 ne može da dobije fokus.
* Uklonjen je kod koji više nije mogao da se izvrši, bez ikakve promene u korišćenju. Pre Unigrama 9.5 neke stavke liste su se objavljivale internim nazivom klase, koji je UnigramPlus zamenjivao čitljivim nazivom; Unigram 9.5 je preimenovao te klase, pa se te zamene više nikad nisu primenjivale. Uklonjen je i rukovalac koji je objašnjenje kviza otvarao u posebnom prozoru, a bio je isključen od verzije 5.2.0.
* Ažurirani poljski i vijetnamski prevodi.

###Verzija 5.8.2

* Ispravljene greške NVDA u novoj beta verziji Unigrama za WinUI 3. Od verzije 5.5.6 greška se beležila pri svakom povratku u Unigram ili pri kucanju pomoću uređivača metoda unosa (IME), na primer za kineski, japanski ili korejski. UWP verzija Unigrama nije bila pogođena.
* UnigramPlus više ne ometa objavljivanje fokusa u Telegram Desktopu kada dodatak Telegram Desktop nije instaliran.
* Uklonjeno obaveštenje koje je UnigramPlus davao pri otkazivanju snimanja glasovne ili video poruke. Unigram 13.0 i noviji sami objavljuju otkazano snimanje, bilo da je otkazano pomoću Ctrl+D ili dugmeta za otkazivanje, pa se više ne čuje dva puta. Takođe se snimak koji se sporo pojavljuje u ćaskanju više ne prijavljuje kao otkazan. Početak i slanje snimka i dalje se objavljuju, a podešavanje za to sada se zove "Obaveštenje pri početku ili slanju snimka glasovne poruke".
* Ažurirani poljski i vijetnamski prevodi.

###Verzija 5.8.1

* Uklonjeno zaobilazno rešenje za trajanje poziva. Unigram 12.10 i noviji sami objavljuju trajanje u poruci o pozivu, pa ga UnigramPlus više ne dodaje i ne čuje se dva puta.
* Ispravljeno pokretanje dodatka na starijim verzijama NVDA koje nemaju modul utils.security.
* Uklonjeni su uvozi koje dodatak više ne koristi.
* Ažuriran vijetnamski prevod.

###Verzija 5.8.0

* Ponavljajuće pozadinske provere dodatka više se ne izvršavaju u glavnoj petlji NVDA, pa se kretanje kroz ćaskanja, kucanje i govor više ne zadržavaju dok Unigram odgovara.
* Svako ponašanje dodato posle verzije 5.4 sada može da se uključi ili isključi u podešavanjima dodatka UnigramPlus, okupljeno pod jednim naslovom: kako se objavljuje dugme za snimanje glasovne poruke, obogaćeni tekst poruke pomoću ALT+C, oznaka dugmeta identiteta na profilu, objava odgovaranja i uređivanja u polju poruke, izostavljena objava "lista" pre poruka, trenutno stanje mikrofona i kamere tokom poziva i broj nepročitanih pri promeni fascikle ćaskanja. Svako podrazumevano zadržava svoje trenutno ponašanje, a svaka oznaka navodi koje ponašanje verzije 5.4 vraća.
* Ispravljen razmak koji nije reprodukovao glasovne poruke, muziku i datoteke.
* Ispravljeno da Enter nije odgovarao na poruku, Backspace je nije uređivao, ALT+C nije prikazivao njen tekst, a ALT+D se nije vraćao na nju.
* Ispravljeno da ALT+E nije zatvarao audio plejer.
* Ispravljeno da Ctrl+ALT+Levo i Ctrl+ALT+Desno nisu premotavali reprodukciju glasovne poruke, uključujući i kada se strelica ponovo pritisne dok su modifikatori i dalje pritisnuti.
* Otkazivanje snimanja glasovne poruke objavljuje se otprilike sekundu i po nakon zaustavljanja, umesto pet sekundi kasnije.
* Uz izabranu opciju dugmeta za snimanje iz verzije 5.4, fokus ostaje u polju poruke kada snimanje počne, dok Tab i dalje dolazi do dugmeta za snimanje.
* Ispravljen niz prečica koje su tiho otkazivale kada je u stablu Unigrama nedostajao element koji su očekivale: ALT+3, ALT+4, ALT+5, ALT+6, ALT+Q, ALT+T, ALT+Shift+L, ALT+Shift+P, Shift+Delete, kretanje kroz medije i kontrole poziva.
* Pretvaranje glasovne poruke u tekst više ne pokreće novu nit svakih pola sekunde dok čeka i odustaje umesto da čeka beskonačno.

###Verzija 5.7.3

* NVDA+Alt+V sada prikazuje verziju dodatka UnigramPlus u novom redu.

###Verzija 5.7.2

* NVDA+Alt+V sada otvara informacije o verzijama u višerednom prozoru samo za čitanje.

###Verzija 5.7.1

* Ispravljeno je pogrešno prepoznavanje dugmadi za reakcije u Unigramu 12.10.2 kao poruka, zbog čega prečice za navigaciju kroz poruke više ne zamenjuju njihovu izvornu radnju prebacivanja.

###Verzija 5.7.0

* Vraćene su najave pri promeni fascikle sa nenultim brojem nepročitanih, uz zadržavanje zaštita praćenja napretka prenosa datoteka.
* Lista prečica je ažurirana prema trenutnom izvornom kodu Unigrama i označene su ugrađene prečice koje još nisu u zvaničnom Shortcuts.md dokumentu.

### Verzija 5.6.9

* Otklonjena je greška do koje je moglo doći kada NVDA uđe na bezbednu radnu površinu, na primer pri UAC upitu, dok je bilo uključeno UnigramPlus praćenje poruka u pozadini.
* Ispravljeno je pogrešno prepoznavanje redova tema Sačuvanih poruka u Unigramu 12.10.1+ kao poruka samo zato što njihovi izvorni sažeci sadrže vreme slanja ili prijema.
* Uklonjeno je zastarelo zaobilazno rešenje za nazive tema Sačuvanih poruka; trenutne verzije Unigrama sada izvorno pružaju pristupačne nazive za razgovore Sačuvanih poruka.
* Ažurirana je kompatibilnost sa NVDA 2026.2.
* Ažurirani su poljski i burmanski prevodi.

### Verzija 5.6.8

* Ispravljen je neuspeh Alt+C kada je instaliran WhatsApp Enhancer, izazvan sukobom naziva pomoćnog modula u appModules.

### Verzija 5.6.7

* Prečica za izgovaranje instaliranih verzija programa Unigram i dodatka UnigramPlus promenjena je sa NVDA+Shift+V na NVDA+Alt+V radi izbegavanja sukoba prečica.
* Ispravljen je Shift+Delete za brisanje ćaskanja i napuštanje grupa ili kanala u trenutnim verzijama Unigrama, uključujući automatsku potvrdu iskačućeg prozora.

### Verzija 5.6.6

* Dodat je NVDA+Shift+V za izgovaranje instaliranih verzija programa Unigram i dodatka UnigramPlus.
* Uklonjeno je privremeno zaobilazno rešenje za umetnuta dugmad u Unigramu 12.9 nakon što je Unigram 12.9.1 ispravio oznake dugmadi; time se izbegavaju zastoji UIA-e u listama botova, kretanju kroz poruke, reakcijama i listi ćaskanja.
* Ažurirani su svi prevodi i priručnici za verziju 5.6.6.

### Verzija 5.6.5

* Ispravljeni su Enter za odgovaranje na poruke i Alt+Shift+R za označavanje ćaskanja kao pročitanih u trenutnim verzijama Unigrama.
* Uklonjeni su režim veb prikaza i njegovo podešavanje; Alt+C sada uvek otvara tekst poruke u originalnom wx iskačućem prozoru.
* Ažurirani su svi prevodi i priručnici za verziju 5.6.5.

### Verzija 5.6.4

* Shift+Delete je ispravljen korišćenjem Unigramove izvorne naredbe Delete i automatskom potvrdom brisanja sa obe strane.
* Alt+2 sada prvo aktivira Unigramovo dugme „Idi na dno”; uklonjena je duplirana prečica Alt+End.
* Dodato je podešavanje za izbor klasičnog wx prozora (podrazumevano) ili veb-prikaza pri prikazu teksta poruke pomoću Alt+C.
* Sada se koristi zvanični pristupačni tekst obogaćenih poruka Unigrama, uz privremenu ispravku neoznačenih ugrađenih dugmadi u Unigramu 12.9.
* Spisak prečica je ažuriran prema zvaničnoj dokumentaciji Unigrama 12.9.
* Dodata je privremena ispravka kako bi redovi tema Sačuvanih poruka izgovarali vidljivi naslov ćaskanja umesto naziva tipa TDLib.

### Verzija 5.6.3

* Ispravljen je povremeni problem zbog kojeg je NVDA izgovarao „lista” pre poruke pri kretanju strelicama gore i dole.
* Dodato je podešavanje za ponašanje Alt+[ koje izgovara zaglavlja poruka posle njihovog sadržaja; podrazumevano je isključeno.
* Dodato je opcionalno zvučno obaveštenje pri dostizanju kraja ćaskanja.

### Verzija 5.6.2

* Ispravljen je Ctrl+Alt+Left/Right Arrow za premotavanje unazad i unapred unutar glasovne poruke koja se reprodukuje.
* Ispravljen je Alt+I tako da prelazi na ugrađenu listu rezultata pretrage u ćaskanju.
* Dodat je Alt+[ za prebacivanje izgovaranja zaglavlja pre ili posle sadržaja poruke. Kada su zaglavlja posle sadržaja, nazivi datoteka se prvi izgovaraju u odeljcima sa datotekama.

### Verzija 5.6.1

* Ispravljeno je praćenje napretka prenosa datoteka tako da se zaustavlja na 100% i više ne pravi novu nit pri svakom ciklusu provere.
* Kada se Unigram otvori, fokus se sada automatski premešta na listu ćaskanja.
* Dodat je Ctrl+Alt+Up/Down za kretanje kroz ćaskanja sa nepročitanim pominjanjima.

### Verzija 5.6.0

* Ispravljeno je prepoznavanje obogaćenih poruka, pa se poruke sa nalepnicama i emodžijima više ne izgovaraju pogrešno kao obogaćene poruke.
* Ctrl+R sada koristi izvorno ponašanje Unigrama za snimanje i slanje glasovnih poruka, uz zadržavanje UnigramPlus obaveštenja o početku i završetku snimanja.
* Prevodi su ažurirani.

### Verzija 5.5.9

* Dodata je podrška za obogaćene poruke. One se izgovaraju kada dobiju fokus i mogu se otvoriti kombinacijom Alt+C u prozoru za pregledanje.
* Linkovi i mešoviti sadržaj se čuvaju, a linkovi se mogu aktivirati iz prozora za pregledanje.

### Verzija 5.5.8

* Ispravljeno je automatsko ažuriranje: izdanja se sada bezbedno preuzimaju sa GitHuba, a preuzeti dodatak se proverava pre instalacije.

* Vraćena je kompatibilnost sa Unigramom 12.7, gde je nekoliko prečica i obaveštenja prestalo da radi.
* Poruke ankete ponovo najavljuju pitanje i opcije odgovora.
* Lista tema foruma ponovo najavljuje pregled poslednje poruke.
* Tokom pojedinačnog poziva ponovo rade prečice za isključivanje mikrofona (ALT+A), uključivanje ili isključivanje kamere (ALT+V) i završavanje poziva (ALT+N).
* ALT+End ponovo prelazi na najnoviju poruku u ćaskanju.

### Verzija 5.5.7

* Odeljak sa prečicama na tastaturi reorganizovan je u kategorizovane tabele i objedinjuje prečice Unigrama i UnigramPlusa.
* Pri snimanju glasovne ili video poruke NVDA sada najavljuje "Snimanje glasovne poruke" ili "Snimanje video poruke" zajedno sa proteklim vremenom umesto "Tn voice message".

### Verzija 5.5.6

* Ispravljeno je da dugme identiteta u profilu grupe ili kanala izgovara „Identity root” pri prelasku tasterom Tab nakon imena; sada izgovara naziv ćaskanja i broj članova.
* Ctrl+C se više ne obrađuje dvaput: kopira vezu kada je fokus na vezi, a u ostalim slučajevima kopiranje poruke prepušta Unigramu.

### Verzija 5.5.5

* Odgovaranje na poruku ili njeno uređivanje sada se izgovara u polju za unos poruke umesto uobičajenog upita za poruku.
* Ispravljeno je to što se zvuk kucanja ponekad nastavljao reprodukovati nakon zatvaranja aplikacije, nakon što druga strana prestane da kuca ili nakon napuštanja ćaskanja; sada se zaustavlja čim niko ne kuca u otvorenom ćaskanju.
* Ažuriran je burmanski prevod.

### Verzija 5.5.4

* Ispravljena su neželjena izgovaranja, kao što su brojači nepročitanih ćaskanja u fasciklama, na primer „Svi 535”. Napredak prenosa datoteka sada je ograničen na Unigram kontrole za otpremanje i preuzimanje i ignoriše se van Unigram prozora.
* Ispravljeno je istovremeno korišćenje sa NVDA dodatkom za Telegram Desktop tako što se UnigramPlus aktivira samo kada je pokrenuta aplikacija prepoznata kao Unigram.
* U podešavanja UnigramPlus dodat je taster za otvaranje fascikle ugrađenih zvukova, radi lakše zamene WAV datoteka datotekama istog naziva.
* Dodata je opcija za strelicu nagore u polju za uređivanje poruke koja premešta fokus na poslednju fokusiranu poruku.
* Tradicionalni kineski je obnovljen kao zh_TW, a dodat je pojednostavljeni kineski zh_CN.
