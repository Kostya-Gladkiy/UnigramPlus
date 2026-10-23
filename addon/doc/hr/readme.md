# Unigram Plus

* Autor: Kostya Gladkiy (Ukrajina)
* [Telegram kanal](https://t.me/unigramPlus)
* Telegram: @unigramPlus
* Veza za donaciju:[https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)
* PayPal: gladkiy.kostya@gmail.com

Koristite Unigram na udobniji i produktivniji način. Ovaj dodatak nudi mnogo prečaca za brzu i udobnu upotrebu Unigrama i čini puno malih poboljšanja.
##Neka od glavnih poboljšanja su:

* Dodaje značajno poboljšanje prikaza poruka kao što su anketa, poveznica ili poruka s priloženim medijima.
* Kada fokus uđe na popis razgovora, uklanja izraze kao što su: "razgovori, kartica, odabrani popis". A kada fokus pogodi popis poruka, izraz "popis" neće biti izgovoren.
* Naziv i veličina datoteke će se izgovoriti kada je pokazivač fokusiran na gumb "Otvori datoteku" ili gumb "Preuzmi datoteku", a kada je pokazivač fokusiran na gumb za reprodukciju audiodatoteke, čut ćete njezin naziv i trajanje.
* Kada se fokus premjesti na glasovnu poruku koja se trenutno reproducira, prvo se oglasi informacija o vremenu njezine reprodukcije, a zatim sve ostale informacije.
* Prilikom fokusiranja na odabranu poruku u razgovoru, prvo ćete čuti informaciju da je odabrana, a zatim sadržaj poruke.
* Sada, kada se krećete po razgovoru, fraza "Viđeno" se uopće neće izgovarati, a fraza "Nije viđeno" će se izgovarati prije sadržaja poruke. Ova značajka trenutno radi samo na engleskom, ruskom, ukrajinskom, španjolskom, portugalskom, poljskom, hrvatskom, turskom i perzijskom jeziku.
* Značajno poboljšana funkcija snimanja glasovnih poruka. Početak snimanja i slanje glasovne poruke popraćeni su karakterističnim zvukovima, a otkazano snimanje Unigram 13.0 i noviji najavljuju sami. Također, prilikom izvođenja ovih funkcija, fokus ostaje na svom mjestu i ne skače niti na gumb za snimanje niti na polje za unos poruke.
* Ako se medij priložen poruci otvori pomoću razmaknice, tada će se nakon zatvaranja fokus vratiti na zadnji element koji je bio u fokusu.
* Dodatak vam omogućuje da potpuno onemogućite najavu trake napretka, kao i da onemogućite samo najavu trake napretka za reprodukciju glasovnih poruka.

## Prilagođeni zvukovi
Zvukovi UnigramPlus nalaze se u mapi `appModules\media` dodatka. Otvorite NVDA postavke > UnigramPlus i pritisnite **Otvori mapu zvukova UnigramPlus**. Za prilagodbu zvuka kopirajte zamjensku WAV datoteku u tu mapu s istim nazivom kao zvuk koji želite zamijeniti, zatim ponovno pokrenite NVDA ili ponovno učitajte dodatke. Ažuriranja dodatka mogu vratiti ugrađene zvukove, stoga sačuvajte kopiju svojih datoteka.

##Informacije o mogućnosti doniranja programeru:
Ako vam se jako sviđa ovaj dodatak i imate želju, a što je najvažnije priliku, financijski podržati programera i time ga motivirati za daljnji razvoj ovog dodatka, to možete učiniti prijenosom manjeg iznosa na sljedeću bankovni račun:
[Poveznica za donaciju](https://unigramplus.diaka.ua/donate)
ili broj kartice: 5169360009004502 (Ukrajina).
I zapamtite da su svi koji su pročitali ovaj red mislili da će netko sigurno podržati programera, ali to neću biti ja.

<!-- shortcut-table-start -->
## Popis prečaca:

> In the Category column, `UnigramPlus` identifies shortcuts provided by the add-on and `Unigram` identifies shortcuts built into Unigram.

> `Unigram (nedokumentirano)` označava prečace implementirane u trenutačnom izvornom kodu Unigrama koji još nisu navedeni u službenoj datoteci Shortcuts.md.

> [!TIP]
> You can customize UnigramPlus shortcuts from NVDA menu > Preferences > Input gestures.

### Kretanje između razgovora

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | Next chat |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | Previous chat |
| **Ctrl+Alt+Home** | Unigram (nedokumentirano) | Prvi razgovor |
| **Ctrl+Alt+End** | Unigram (nedokumentirano) | Posljednji razgovor |
| **Ctrl+Alt+Up/Down** | UnigramPlus | Premješta se na sljedeći ili prethodni razgovor s nepročitanim spominjanjima |
| **ALT+1** | UnigramPlus | Premješta fokus na popis razgovora |
| **ALT+2** | UnigramPlus | Premješta fokus na posljednju poruku u otvorenom razgovoru |
| **ALT+3** | UnigramPlus | Premješta fokus na oznaku "nepročitane poruke" |
| **ALT+4** | UnigramPlus | Premješta fokus na popis mapa razgovora |
| **ALT+5** | UnigramPlus | Premješta fokus na otvoreni profil |
| **ALT+6** | UnigramPlus | Premješta fokus na popis niti grupe |
| **ALT+D** | UnigramPlus | Premješta fokus na polje za uređivanje. Ako je fokus već u polju za uređivanje, tada će se nakon pritiskanja tipke prečaca pomaknuti na mjesto gdje je bio prije |

### Pretraživanje

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Ctrl+E** | Unigram | Chat search |
| **Ctrl+F** | Unigram | Messages search per chat |
| **Ctrl+Shift+F** | Unigram (nedokumentirano) | Chat search |
| **Search key** | Unigram (nedokumentirano) | Pretraži trenutačnu stranicu |
| **ALT+I** | UnigramPlus | Prelazi na popis rezultata pretraživanja |
| **F3** | UnigramPlus | Prelazi na sljedeći rezultat pretraživanja |
| **Shift+F3** | UnigramPlus | Prelazi na prethodni rezultat pretraživanja |

### Odabrani tekst u polju za unos

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Ctrl+Z** | Unigram | Undo |
| **Ctrl+Y** | Unigram | Redo |
| **Ctrl+Shift+Z** | Unigram (nedokumentirano) | Ponovi |
| **Alt+X** | Unigram (nedokumentirano) | Pretvori četiri odabrane heksadekadske znamenke u odgovarajući znak |
| **Ctrl+X** | Unigram | Cut |
| **Ctrl+C** | Unigram | Copy |
| **Ctrl+V** | Unigram | Paste |
| **Ctrl+A** | Unigram | Select All |
| **Ctrl+Shift+.** | Unigram | Citat |
| **Ctrl+B** | Unigram | Bold |
| **Ctrl+I** | Unigram | Italic |
| **Ctrl+U** | Unigram | Podcrtano |
| **Ctrl+Shift+X** | Unigram | Strikethrough |
| **Ctrl+Shift+M** | Unigram | Monospace |
| **Ctrl+Shift+P** | Unigram | Spoiler |
| **Ctrl+K** | Unigram | Create Link |
| **Ctrl+Shift+N** | Unigram | Ukloni oblikovanje (običan tekst) |

### Mape

| Prečac | Kategorija | Radnja |
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
| **Ctrl+Shift+Down** | Unigram (nedokumentirano) | Sljedeća mapa |
| **Ctrl+Shift+Up** | Unigram (nedokumentirano) | Prethodna mapa |

### Radnje s porukama

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Space** | UnigramPlus | Play or stop the focused voice or video message, or open media attached to the message |
| **Ctrl+C** | UnigramPlus | Kopira poruku ako sadrži tekst. Ako je fokus na poveznici, poveznica će se kopirati |
| **ALT+Q** | UnigramPlus | Pritišće gumb "Trenutni prikaz", ako je uključen u trenutnu poruku |
| **ALT+Delete** | UnigramPlus | Briše poruku ili razgovor |
| **Shift+Delete** | UnigramPlus | Briše poruku ili razgovor za obje strane |
| **Delete** | Unigram (nedokumentirano) | Izbriši odabranu ili fokusiranu poruku |
| **Ctrl+ALT+C** | UnigramPlus | Otvara komentare |
| **Enter** | UnigramPlus | Odgovara na poruku |
| **ALT+F** | UnigramPlus | Prosljeđuje poruku |
| **Backspace** | UnigramPlus | Uređuje poruku |
| **ALT+Shift+R** | UnigramPlus | Označava razgovor kao pročitan |
| **Ctrl+Space** | UnigramPlus | Prebacuje na način odabira |
| **Unassigned** | UnigramPlus | Spremi datoteku kao... |
| **Unassigned** | UnigramPlus | Prikvačuje poruku ili razgovor |
| **Left Arrow** | UnigramPlus | Najavljuje izvornu poruku, onu na koju je odgovoreno |
| **Right Arrow** | UnigramPlus | Move to the next media attachment in the focused message |
| **ALT+C** | UnigramPlus | Prikazuje poruku u skočnom prozoru |
| **ALT+W** | UnigramPlus | Announces the time a message was sent or received, as well as a list of reactions. Double-clicking toggles the announcement mode for this information. |
| **ALT+[** | UnigramPlus | Prebacuje izgovaranje zaglavlja poruka prije ili nakon sadržaja poruke |
| **NVDA+Ctrl+0-9** | UnigramPlus | Review one of the ten most recent messages; 1 is the newest and 0 is the tenth newest |
| **Ctrl+Shift+A** | UnigramPlus | Pritišće gumb "Priloži datoteku" |
| **Ctrl+Shift+E** | Unigram (nedokumentirano) | Otvori birač emojija |
| **Ctrl+Shift+G** | Unigram (nedokumentirano) | Otvori birač GIF-ova |
| **Ctrl+Shift+S** | Unigram (nedokumentirano) | Otvori birač naljepnica |
| **Ctrl+O** | Unigram (nedokumentirano) | Otvori birač datoteka za slanje dokumenata |
| **Ctrl+N** | UnigramPlus | Pritišće gumb "Novi razgovor" |
| **Arrow Up** | Unigram | Edit last sent message |
| **Ctrl+Arrow Up** | Unigram | Reply to last sent message |
| **Esc / Alt+Arrow Left** | Unigram | Go back |
| **Alt+Arrow Right** | Unigram | Redo go back |

### Glasovne poruke i mediji

| Prečac | Kategorija | Radnja |
|---|---|---|
| **ALT+P** | UnigramPlus | Reproducira/pauzira glasovnu poruku koja se trenutno reproducira |
| **ALT+S** | UnigramPlus | Povećava/smanjuje reprodukciju glasovnih poruka |
| **ALT+E** | UnigramPlus | Zatvara reproduktor zvuka |
| **NVDA+ALT+R** | UnigramPlus | Pretvara glasovnu poruku u tekst |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | Fast forward a voice message |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | Rewind voice message |

### Snimanje poruka

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Ctrl+R** | Unigram | Start record |
| **Ctrl+R (again)** | Unigram | Send recorded |
| **Ctrl+D** | Unigram | Stop recording |
| **Space (while recording) / Ctrl+P** | Unigram | Pause recording |

### Pozivi

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Ctrl+Home** | Unigram | Accept incoming call |
| **Ctrl+End** | Unigram | Reject incoming call |
| **Ctrl+Page Up** | Unigram | Toggle camera |
| **Ctrl+Page Down** | Unigram | Toggle microphone |
| **ALT+Shift+C** | UnigramPlus | Poziva ako je u pitanju kontakt ili se pridružuje glasovnom razgovoru ako je u pitanju grupa |
| **ALT+Shift+V** | UnigramPlus | Pritišće gumb za videopoziv |
| **ALT+Y** | UnigramPlus | Prihvaća poziv |
| **ALT+N** | UnigramPlus | Pritišće "Odbij poziv" ako postoji dolazni poziv, gumb "Završi poziv" ako je poziv u tijeku ili napušta glasovni razgovor ako je aktivan. |
| **ALT+A** | UnigramPlus | Pritišće gumb "Uključi/isključi mikrofon" |
| **ALT+V** | UnigramPlus | Pritišće gumb "Omogući/onemogući kameru" |

### Ostali prečaci

| Prečac | Kategorija | Radnja |
|---|---|---|
| **Ctrl+0** | Unigram | Saved messages |
| **Ctrl+W** | Unigram | Close current window |
| **Ctrl+Q** | Unigram | Close Unigram (main window only) |
| **Ctrl+Shift+Y** | Unigram | Change status |
| **Ctrl+Shift+W** | Unigram (nedokumentirano) | Zaustavi reprodukciju medija |
| **Ctrl+F4** | Unigram (nedokumentirano) | Close current window |
| **Ctrl+L** | Unigram (nedokumentirano) | Zaključaj Unigram |
| **Ctrl+M** | Unigram (nedokumentirano) | Minimiziraj Unigram |
| **Ctrl+J** | Unigram (nedokumentirano) | Otvori preuzimanja |
| **ALT+T** | UnigramPlus | Najavljuje naziv i status otvorenog razgovora |
| **NVDA+Alt+V** | UnigramPlus | Otvori podatke o verziji programa Unigram i dodatka UnigramPlus u prozoru samo za čitanje |
| **ALT+M** | UnigramPlus | Otvara navigacijski izbornik |
| **ALT+Shift+M** | UnigramPlus | Otvara postavke Unigrama |
| **ALT+Shift+P** | UnigramPlus | Otvara profil trenutnog razgovora |
| **ALT+L** | UnigramPlus | Omogućava automatsko čitanje novih poruka u trenutnom razgovoru |
| **ALT+H** | UnigramPlus | Prikazuje popis svih UnigramPlus prečaca |
| **ALT+U** | UnigramPlus | Uključuje/isključuje obavijesti trake napretka |
| **ALT+Shift+L** | UnigramPlus | Kopira podatke za emitiranje u međuspremnik |
| **NVDA+ALT+U** | UnigramPlus | Otvara prozor postavki UnigramPlusa |
<!-- shortcut-table-end -->

##Popis promjena:

### Verzija 5.8.6

* Razmaknica ponovno reproducira, otvara i preuzima medije poruke u Unigramu 13.0 i novijim verzijama. Od Unigrama 13.0 sadržaj poruke s fotografijom, videozapisom, GIF-om, datotekom, pjesmom ili glasovne poruke sam je gumb koji to radi. Unigram 13.0.1 vratio je tom gumbu identifikator koji UnigramPlus traži, osim na glasovnim porukama, gdje je identifikator dobio gumb za pretvaranje govora u tekst, pa razmaknica na glasovnoj poruci nije ništa radila. UnigramPlus sada prepoznaje gumb same glasovne poruke po napretku preuzimanja koji javlja. Unigram 13.1.1 i dalje nema radnju za razmaknicu na poruci izvan načina odabira, pa UnigramPlus pritišće taj gumb: razmaknica reproducira ili pauzira glasovnu poruku ili pjesmu, otvara fotografiju, videozapis ili GIF u pregledniku te preuzima ili otvara datoteku.
* Nakon što razmaknica reproducira glasovnu poruku ili pjesmu ili preuzme datoteku, fokus ostaje na poruci, a sljedeći pritisak tipke Escape više ga ne vraća onamo. To treba samo preglednik, ali u Unigramu 13.0 i novijim verzijama datoteka ili pjesma široka je kao fotografija, pa ju je UnigramPlus smatrao fotografijom.
* Razmaknica više ne otvara naljepnice ni preglede poveznica. Unigram 13.0.1 dao im je isti identifikator kao gumbima za medije, ali one su poveznice. U pregledu poveznice koji prikazuje fotografiju ili videozapis razmaknica i dalje otvara fotografiju ili videozapis.
* Strelice desno i lijevo na poruci s više medijskih privitaka, poput albuma, ponovno najavljuju svaku fotografiju, videozapis, datoteku ili pjesmu u Unigramu 13.0 i novijim verzijama. Od Unigrama 13.0 svaki privitak sadrži samo vlastiti gumb svojeg sadržaja, pa UnigramPlus više nije pronalazio ono po čemu se fotografija razlikuje od videozapisa i za svaki je privitak najavljivao zamjensku riječ „Медіа”. Sada gleda unutar tog gumba: videozapis ondje ima vlastiti gumb za preuzimanje, datoteka ili pjesma svoj naslov, a fotografija ni jedno ni drugo.
* Ctrl+Space sada radi i na popisu razgovora, gdje prije nije činio ništa. Kao i kod poruka, prvi pritisak uključuje način odabira s razgovorom u fokusu iz kontekstnog izbornika razgovora, a zatim svaki pritisak odabire razgovor u fokusu ili poništava njegov odabir, kao što to čini razmaknica u Unigramu. UnigramPlus zatim javlja je li razgovor odabran. Poništavanje odabira posljednjeg odabranog razgovora završava način odabira. Dok je popis razgovora u načinu odabira, UnigramPlus kaže i „Odabrano” prije naziva odabranog razgovora kad fokus dođe na njega, kao što to čini kod poruka.
* Dodan je prečac Alt+Shift+M koji otvara postavke Unigrama u Unigramu 13.1 i novijim verzijama, kao što to čini UnigramPlusRussianMod. Unigram 13.1 premjestio je postavke iz bočnog okna u karticu ispod popisa razgovora. Alt+Shift+M odabire tu karticu, a zatim premješta fokus na vrh postavki: na prvi od vaših ostalih računa ili, ako ste prijavljeni samo s jednim računom, na „Dodaj račun”. U verzijama Unigrama starijima od 13.1 te u uskom prozoru koji prikazuje samo otvoreni razgovor UnigramPlus javlja „Postavke su nedostupne”.

### Verzija 5.8.5

* Alt+M ponovno otvara navigacijski izbornik u Unigramu 13.1 i novijim verzijama. Unigram 13.1 zamijenio je bočno okno izbornikom koji se otvara istim gumbom, a taj gumb više nije preklopni gumb, pa ga UnigramPlus nije pronalazio i javljao je „Navigacijski izbornik je nedostupan”.
* Ispravljen je Ctrl+Space u Unigramovu načinu odabira. U tom načinu kontekstni izbornik odabrane poruke nema naredbu Odaberi, pa je UnigramPlus prolazio kroz izbornik ne pronalazeći je, a poruka je ostajala odabrana. Ctrl+Space sada radi kao u Unigramu 13.1.1: prvi pritisak i dalje uključuje način odabira iz kontekstnog izbornika, a zatim svaki pritisak odabire poruku u fokusu ili poništava njezin odabir, kao što to čini razmaknica u Unigramu. UnigramPlus zatim javlja je li poruka odabrana. Poništavanje odabira posljednje odabrane poruke završava način odabira.
* U načinu odabira razmaknica i Enter na poruci sada je odabiru ili poništavaju njezin odabir, kao u Unigramu, umjesto da reproduciraju njezine medije ili traže Odgovori u kontekstnom izborniku, a Backspace ondje više ne traži Uredi.
* Ažurirana je kompatibilnost s NVDA 2026.3. UnigramPlus više ne koristi zastarjele dijelove NVDA API-ja, koje NVDA još podržava, ali ih može ukloniti u nekoj od sljedećih verzija: okvire s porukama provjere ažuriranja, stari način otvaranja postavki UnigramPlusa i konstantu tipke koja se koristi pri premotavanju glasovnih poruka.
* Ažurirani poljski i vijetnamski prijevodi.

### Verzija 5.8.4

* Kada je uključena opcija „Automatski premjesti fokus na popis razgovora pri pokretanju Unigrama”, fokus sada ostaje u skočnom prozoru koji Unigram prikaže pri pokretanju, poput zahtjeva za pridruživanje grupi otvorenog iz pozivne poveznice. Od verzije 5.6.1 UnigramPlus je premještao fokus iz skočnog prozora na popis razgovora iza njega, pa je skočni prozor bio preskočen.
* Ažuriran vijetnamski prijevod.

### Verzija 5.8.3

* Uklonjeno je rukovanje tipkama Enter i razmaknica koje je UnigramPlus u verziji 4.8.0 dodao popisu kategorija postavki Unigrama. U Unigramu 13.0 i novijima svaka je kategorija postavki gumb koji se sam otvara tipkom Enter ili razmaknicom, a fokus dolazi na taj gumb, a ne na stavku popisa kojom je dodatak rukovao, pa se to rukovanje ondje više nije primjenjivalo. Pri otvaranju kategorije fokus sada ostaje na njoj, kao i u samom Unigramu, umjesto da se premjesti u kategoriju. To je rukovanje obuhvaćalo i druge popise kartica, primjerice kartice Emoji, GIF-ovi i Naljepnice, gdje je presretalo Enter i razmaknicu; sada te tipke i ondje dolaze do Unigrama.
* U postavkama Unigrama Alt+1 sada premješta fokus na otvorenu kategoriju postavki ili na prvu kategoriju ako nijedna nije otvorena. Prije je popis kategorija tražio na fiksnom mjestu stranice postavki, a zatim pokušavao premjestiti fokus na element koji u Unigramu 13.0 ne može primiti fokus.
* Uklonjen je kôd koji se više nije mogao izvršiti, bez ikakve promjene u korištenju. Prije Unigrama 9.5 neke su se stavke popisa najavljivale internim nazivom klase, koji je UnigramPlus zamjenjivao čitljivim nazivom; Unigram 9.5 preimenovao je te klase, pa se te zamjene više nikad nisu primjenjivale. Uklonjen je i rukovatelj koji je objašnjenje kviza otvarao u zasebnom prozoru, a bio je isključen od verzije 5.2.0.
* Ažurirani poljski i vijetnamski prijevodi.

### Verzija 5.8.2

* Ispravljene pogreške NVDA-a u novoj beta verziji Unigrama za WinUI 3. Od verzije 5.5.6 pogreška se bilježila pri svakom povratku u Unigram ili pri tipkanju pomoću uređivača načina unosa (IME), primjerice za kineski, japanski ili korejski. UWP verzija Unigrama nije bila zahvaćena.
* UnigramPlus više ne ometa najave fokusa u Telegram Desktopu kada dodatak Telegram Desktop nije instaliran.
* Uklonjena obavijest koju je UnigramPlus davao pri otkazivanju snimanja glasovne ili video poruke. Unigram 13.0 i noviji sami najavljuju otkazano snimanje, bilo da je otkazano pomoću Ctrl+D ili gumba za otkazivanje, pa se više ne čuje dvaput. Također se snimka koja se sporo pojavljuje u razgovoru više ne prijavljuje kao otkazana. Početak i slanje snimke i dalje se najavljuju, a postavka za to sada se zove "Obavijest pri početku ili slanju snimke glasovne poruke".
* Ažurirani poljski i vijetnamski prijevodi.

### Verzija 5.8.1

* Uklonjeno zaobilazno rješenje za trajanje poziva. Unigram 12.10 i noviji sami najavljuju trajanje u poruci o pozivu, pa ga UnigramPlus više ne dodaje i ne čuje se dvaput.
* Ispravljeno pokretanje dodatka na starijim verzijama NVDA-a koje nemaju modul utils.security.
* Uklonjeni su uvozi koje dodatak više ne koristi.
* Ažuriran vijetnamski prijevod.

### Verzija 5.8.0

* Ponavljajuće pozadinske provjere dodatka više se ne izvode u glavnoj petlji NVDA-a, pa se kretanje razgovorima, tipkanje i govor više ne zaustavljaju dok Unigram odgovara.
* Svako ponašanje dodano nakon verzije 5.4 sada se može uključiti ili isključiti u postavkama dodatka UnigramPlus, okupljeno pod jednim naslovom: kako se najavljuje gumb za snimanje glasovne poruke, obogaćeni tekst poruke pomoću ALT+C, oznaka gumba identiteta na profilu, najava odgovaranja i uređivanja u polju poruke, izostavljena najava "popis" prije poruka, trenutačno stanje mikrofona i kamere tijekom poziva te broj nepročitanih pri promjeni mape razgovora. Svako zadržava svoje trenutačno ponašanje kao zadano, a svaka oznaka navodi koje ponašanje verzije 5.4 vraća.
* Ispravljena razmaknica koja nije reproducirala glasovne poruke, glazbu i datoteke.
* Ispravljeno da Enter nije odgovarao na poruku, Backspace je nije uređivao, ALT+C nije prikazivao njezin tekst, a ALT+D se nije vraćao na nju.
* Ispravljeno da ALT+E nije zatvarao audioreproduktor.
* Ispravljeno da Ctrl+ALT+Lijevo i Ctrl+ALT+Desno nisu premotavali reprodukciju glasovne poruke, uključujući i kad se strelica ponovno pritisne dok su modifikatori i dalje pritisnuti.
* Otkazivanje snimanja glasovne poruke najavljuje se otprilike sekundu i pol nakon zaustavljanja, umjesto pet sekundi kasnije.
* Uz odabranu mogućnost gumba za snimanje iz verzije 5.4, fokus ostaje u polju poruke kad snimanje započne, dok Tab i dalje dolazi do gumba za snimanje.
* Ispravljen niz prečaca koji su tiho zakazivali kad je u stablu Unigrama nedostajao element koji su očekivali: ALT+3, ALT+4, ALT+5, ALT+6, ALT+Q, ALT+T, ALT+Shift+L, ALT+Shift+P, Shift+Delete, kretanje medijima i upravljanje pozivom.
* Pretvaranje glasovne poruke u tekst više ne pokreće novu dretvu svakih pola sekunde dok čeka i odustaje umjesto da čeka beskonačno.

### Verzija 5.7.3

* NVDA+Alt+V sada prikazuje verziju programa UnigramPlus u novom retku.

### Verzija 5.7.2

* NVDA+Alt+V sada otvara podatke o verziji u višerednom prozoru samo za čitanje.

### Verzija 5.7.1

* Ispravljeno je da se gumbi reakcija u Unigramu 12.10.2 tretiraju kao poruke, pa prečaci za navigaciju porukama više ne poništavaju njihovu izvornu radnju prebacivanja.

### Verzija 5.7.0

* Vraćene su najave pri promjeni mape s brojem nepročitanih većim od nule, uz zadržavanje zaštita praćenja napretka prijenosa datoteka.
* Popis prečaca ažuriran je prema trenutačnom izvornom kodu Unigrama, a označeni su ugrađeni prečaci koji još nisu u službenom Shortcuts.md dokumentu.

### Verzija 5.6.9

* Ispravljena je pogreška koja se mogla pojaviti kada je NVDA ušao u sigurnu radnu površinu, primjerice pri UAC upitu, dok je bilo uključeno UnigramPlus praćenje poruka u pozadini.
* Ispravljeno je da se retci tema Spremljenih poruka u Unigramu 12.10.1+ tretiraju kao poruke samo zato što njihovi izvorni sažeci sadrže vremenske oznake slanja ili primanja.
* Uklonjeno je zastarjelo zaobilazno rješenje za nazive tema Spremljenih poruka; trenutne verzije Unigrama sada izvorno pružaju pristupačne nazive za razgovore Spremljenih poruka.
* Ažurirana je kompatibilnost s NVDA 2026.2.
* Ažurirani su poljski i burmanski prijevodi.

### Verzija 5.6.8

* Ispravljen je neuspjeh prečaca Alt+C kada je instaliran WhatsApp Enhancer zbog sukoba naziva pomoćnog modula u appModules.

### Verzija 5.6.7

* Prečac za izgovaranje instaliranih verzija programa Unigram i dodatka UnigramPlus promijenjen je s NVDA+Shift+V na NVDA+Alt+V kako bi se izbjegli sukobi prečaca.
* Ispravljen je Shift+Delete za brisanje chatova i napuštanje grupa ili kanala u trenutačnim verzijama Unigrama, uključujući automatsku potvrdu skočnog prozora.

### Verzija 5.6.6

* Dodan je NVDA+Shift+V za izgovaranje instaliranih verzija programa Unigram i dodatka UnigramPlus.
* Uklonjeno je privremeno zaobilazno rješenje za umetnute gumbe u Unigramu 12.9 nakon što je Unigram 12.9.1 ispravio oznake gumba; time se izbjegavaju zastoji UIA-e u popisima botova, kretanju porukama, reakcijama i popisu razgovora.
* Ažurirani su svi prijevodi i priručnici za verziju 5.6.6.

### Verzija 5.6.5

* Ispravljena je tipka Enter za odgovaranje na poruke i Alt+Shift+R za označavanje razgovora kao pročitanih u trenutačnim verzijama Unigrama.
* Uklonjeni su način web-prikaza i njegova postavka; Alt+C sada uvijek otvara tekst poruke u izvornom wx skočnom prozoru.
* Ažurirani su svi prijevodi i priručnici za verziju 5.6.5.

### Verzija 5.6.4

* Shift+Delete je ispravljen korištenjem Unigramove izvorne naredbe Delete i automatskom potvrdom brisanja s obje strane.
* Alt+2 sada najprije aktivira Unigramov gumb „Idi na dno”; uklonjen je dvostruki prečac Alt+End.
* Dodana je postavka za odabir klasičnog wx prozora (zadano) ili web-prikaza pri prikazu teksta poruke tipkom Alt+C.
* Sada se koristi službeni pristupačni tekst obogaćenih poruka Unigrama, uz privremeni popravak neoznačenih ugrađenih gumba u Unigramu 12.9.
* Popis prečaca ažuriran je prema službenoj dokumentaciji Unigrama 12.9.
* Dodan je privremeni popravak kako bi retci tema Spremljenih poruka izgovarali vidljivi naslov razgovora umjesto naziva vrste TDLib.

### Verzija 5.6.3

* Ispravljen je povremeni problem pri kojem je NVDA izgovarao „popis” prije poruke pri kretanju strelicama gore i dolje.
* Dodana je postavka za ponašanje Alt+[ koja izgovara zaglavlja poruka nakon njihova sadržaja; prema zadanim postavkama je isključena.
* Dodana je neobavezna zvučna obavijest pri dosezanju kraja razgovora.

### Verzija 5.6.2

* Ispravljen je Ctrl+Alt+Left/Right Arrow za premotavanje unatrag i unaprijed unutar glasovne poruke koja se reproducira.
* Ispravljen je Alt+I tako da otvara ugrađeni popis rezultata pretraživanja razgovora.
* Dodan je Alt+[ za prebacivanje izgovaranja zaglavlja prije ili nakon sadržaja poruke. Kada su zaglavlja nakon sadržaja, nazivi datoteka izgovaraju se prvi u odjeljcima s datotekama.

### Verzija 5.6.1

* Ispravljeno je praćenje napretka prijenosa datoteka tako da se zaustavlja na 100% i više ne stvara novu dretvu u svakom ciklusu provjere.
* Pri otvaranju Unigrama fokus se sada automatski premješta na popis razgovora.
* Dodan je Ctrl+Alt+Up/Down za kretanje kroz razgovore s nepročitanim spominjanjima.

### Verzija 5.6.0

* Ispravljeno je prepoznavanje obogaćenih poruka tako da se poruke s naljepnicama i emotikonima više pogrešno ne izgovaraju kao obogaćene poruke.
* Ctrl+R sada koristi izvorno Unigramovo ponašanje za snimanje i slanje glasovnih poruka, uz zadržavanje UnigramPlus obavijesti o početku i završetku snimanja.
* Ažurirani su prijevodi.

### Verzija 5.5.9

* Dodana je podrška za obogaćene poruke. Izgovaraju se kada prime fokus i mogu se otvoriti pomoću Alt+C u prozoru za pregledavanje.
* Poveznice i mješoviti sadržaj ostaju sačuvani, a poveznice se mogu aktivirati iz prozora za pregledavanje.

### Verzija 5.5.8

* Ispravljena su automatska ažuriranja: izdanja se sada sigurno dohvaćaju s GitHuba, a preuzeti dodatak provjerava se prije instalacije.

* Vraćena je kompatibilnost s Unigramom 12.7, gdje je nekoliko prečaca i najava prestalo raditi.
* Poruke ankete ponovno najavljuju pitanje i mogućnosti odgovora.
* Popis tema foruma ponovno najavljuje pretpregled posljednje poruke.
* Tijekom pojedinačnog poziva ponovno rade prečaci za isključivanje mikrofona (ALT+A), uključivanje ili isključivanje kamere (ALT+V) i završetak poziva (ALT+N).
* ALT+End ponovno prelazi na najnoviju poruku u razgovoru.

### Verzija 5.5.7

* Odjeljak tipkovničkih prečaca reorganiziran je u kategorizirane tablice te objedinjuje prečace Unigrama i UnigramPlusa.
* Pri snimanju glasovne ili videoporuke NVDA sada najavljuje "Snimanje glasovne poruke" ili "Snimanje videoporuke" zajedno s proteklim vremenom umjesto "Tn voice message".

### Verzija 5.5.6

* Ispravljeno je da gumb identiteta u profilu grupe ili kanala izgovara „Identity root” pri prolasku tipkom Tab nakon imena; sada izgovara naziv razgovora i broj članova.
* Ctrl+C se više ne obrađuje dvaput: kopira poveznicu kada je fokus na poveznici, a u ostalim slučajevima kopiranje poruke prepušta Unigramu.

### Verzija 5.5.5

* Odgovaranje na poruku ili njezino uređivanje sada se izgovara u polju za unos poruke umjesto uobičajenog upita za poruku.
* Ispravljeno je da se zvuk tipkanja ponekad nastavljao reproducirati nakon zatvaranja aplikacije, nakon što druga strana prestane tipkati ili nakon napuštanja razgovora; sada se zaustavlja čim nitko ne tipka u otvorenom razgovoru.
* Ažurirana je burmanska lokalizacija.

### Verzija 5.5.4

* Ispravljena su neželjena čitanja, poput broja nepročitanih chatova u mapama, primjerice „Svi 535”. Napredak prijenosa datoteka sada je ograničen na Unigram kontrole za slanje i preuzimanje te se zanemaruje izvan Unigram prozora.
* Ispravljeno je supostojanje s NVDA dodatkom za Telegram Desktop tako da se UnigramPlus uključuje samo kada je pokrenuta aplikacija prepoznata kao Unigram.
* U postavke UnigramPlus dodan je gumb za otvaranje mape ugrađenih zvukova, radi lakše zamjene WAV datoteka datotekama istog naziva.
* Dodana je opcija za strelicu gore u polju za uređivanje poruke koja premješta fokus na zadnju fokusiranu poruku.
* Tradicionalni kineski obnovljen je kao zh_TW, a dodan je pojednostavljeni kineski zh_CN.

### Verzija 5.5.3

* Dodano automatsko najavljivanje napretka slanja i preuzimanja datoteka. Nova opcija "Samo tijekom slanja i preuzimanja" dodana je u postavke najave traka napretka i sada je zadana postavka. Tipka ALT+U sada izmjenjuje tri stanja: isključeno, samo tijekom slanja/preuzimanja i najavljuj sve trake napretka.
* Ažuriran readme i prijevodi.

### Verzija 5.5.2

* Ažuriran readme i prijevodi.
* Promijenjen zvuk indikatora tipkanja.

### Verzija 5.5.1

* Popravljen prečac za kretanje kroz popis tema grupe (ALT+6). Sada ispravno prepoznaje popis tema prilikom otvaranja forumske grupe iz popisa razgovora.
* Dodan zvuk indikatora tipkanja: zvuk se reproducira u petlji dok druga strana tipka u razgovoru i prestaje kada prestane tipkati. Ova je značajka inspirirana odgovarajućom značajkom u Unigram JAWS skripti.

### Verzija 5.5.0

* Dodana kompatibilnost s NVDA 2026.1.

### Verzija 5.4.2

* Dodana kompatibilnost s NVDA 2025.3.3.

### Verzija 5.4.1

* Dodana kompatibilnost s NVDA 2025.1.2.

### Verzija 5.4.0

* Riješen problem s popisom razgovora.

### Verzija 5.2.0

* Dodana je mogućnost odabira datoteka priloženih porukama strelicama lijevo i desno i otvaranja odabrane datoteke razmaknicom.
* Sada se poveznice u porukama neće čitati u cijelosti, već samo do upitnika.
* Sada, kada zatvorite preglednik fotografija ili videa, UnigramPlus će pokušati postaviti fokus na poruku koju ste gledali.
* Tipkovni prečac za otvaranje UnigramPlus postavki je promijenjen. Sada je ova značajka dodijeljena kombinaciji NVDA+Alt+U.
* Izvršena je optimizacija koda, što je rezultiralo značajno poboljšanim vremenom odgovora pri kretanju popisom razgovora i popisom poruka. To je posebno vidljivo na porukama koje sadrže mnogo ugniježđenih elemenata.
* Popravljeni su mnogi manji problemi.
* Mnogo zastarjelog koda je uklonjeno.

### Verzija 5.1.0

* Dodani su tipkovnički prečaci za navigiranje do sljedećih i prethodnih rezultata pretraživanja u razgovoru. Prema zadanim postavkama, ove su funkcije dodijeljene kombinacijama tipki Alt+K i Alt+J.
* Dodan je tipkovnički prečac za otvaranje popisa svih rezultata pretraživanja u razgovoru. Prema zadanim postavkama, ova je funkcija dodijeljena kombinaciji tipki Alt+I.
* Sada, dvostruki pritisak na tipku Strelica lijevo na poruci premjestit će fokus na poruku na koju trenutna poruka odgovara.
* Riješen je problem u kojem se opisi poveznica ugrađenih u poruke nisu čitali.
* UnigramPlus više neće predlagati ažuriranja na zaštićenim zaslonima. Međutim, korisnici će morati još jednom otvoriti NVDA postavke i kliknuti gumb "Koristi trenutačno spremljene postavke na zaslonu za prijavu te na sigurnim zaslonima (zahtijeva administratorska prava)".
* Uklonjena je značajka za premotavanje glasovnih poruka i značajka za postavljanje reakcija na poruke jer one nisu radile pouzdano.
* Uklonjena je značajka kopiranja poruka, jer Unigram sada ima tu značajku. Imajte na umu da ponekad kopiranje poruka može uzrokovati lagano zamrzavanje programa, ali to nije povezano s UnigramPlus dodatkom.
* Ispravljene su neke druge manje greške.

### Verzija 5.0.0

* Riješen je problem u kojem su se poruke u razgovorima čitale dvaput.
* Riješen je problem u kojem tipkovnički prečac za prikazivanje otvorenog profila nije ispravno funkcionirao.
* Riješen je problem gdje tipkovnički prečac za otvaranje navigacijskog izbornika nije radio.
* Riješeni su svi problemi s gumbom za uključivanje/isključivanje mikrofona u glasovnim razgovorima.
* Riješen je problem na poljskom jeziku gdje je unos znaka blokirala kombinacija ALT+C.
* Ispravljen je izgovor fraza "Vlasnik" i "Administrator" u porukama.
* Riješeno je nekoliko drugih manjih problema.

### Verzija 4.9.0

* Dodana je opcija za promjenu ponašanja kada se pritisne strelica gore u praznom polju za unos poruke. Možete birati između sljedećih opcija: aktivirati funkciju uređivanja posljednje poslane poruke, premjestiti fokus na posljednju poruku u razgovoru ili ne učiniti ništa.
* Popravljeno je odgovaranje i odbijanje poziva pomoću prečaca.
* Popravljeni su manji problemi kao što je kombinacija tipki Alt+H koja nije radila i problem kada poruka na koju je napisan odgovor nije bila izgovorena kada se pritisne strelica lijevo.
* Popravljen je prikaz nekih elemenata.

### Verzija 4.8.0

* Sada se u postavkama Unigrama kategorije postavki mogu otvoriti pritiskom na Enter. Kada otvorite bilo koju kategoriju postavki, fokus će biti premješten na tu kategoriju.
* Sada, kada kliknete na gumb "Objašnjenje" u kvizovima, tekst objašnjenja će se otvoriti u zasebnom prozoru radi lakšeg pregleda.
* Riješen je problem u kojem se nazivi mapa razgovora nisu izgovarali prilikom prebacivanja između njih.
* Ispravljena je greška koja je onemogućavala onemogućavanje ili promjenu redoslijeda izgovora vrste i naziva razgovora.
* Riješen problem kada nije bilo moguće saznati točan odgovor u kvizovima.
* Riješen je problem s kopiranjem poruke korištenjem kombinacije Control+Shift+C.
* Napravljeno je nekoliko manjih popravaka, poboljšanja i optimizacija koda.

### Verzija 4.7.0

* UnigramPlus je sada prilagođen najnovijoj verziji Unigrama.
* Sada je osigurana kompatibilnost s NVDA-2023.
* Tipkovnički prečac Alt+1 sada premješta fokus ne samo na popis za razgovor, već i na popis kontakata i popis odjeljaka postavki.
* Automatska najava novih poruka u razgovoru i automatsko najavljivanje aktivnosti razgovora značajno su revidirani, što je rezultiralo poboljšanom stabilnošću.
* Dodan je tipkovnički prečac za prikaz svih UnigramPlus naredbi. Prema zadanim postavkama, ova je funkcija dodijeljena kombinaciji Alt+H.
* Također je popravljeno nekoliko manjih problema.

### Verzija 4.6.0

* Dodan je tipkovnički prečac za premještanje fokusa na popis niti grupe. Prema zadanim postavkama, ova je funkcija dodijeljena kombinaciji Alt+6. Napominjem da često kada pritisnemo tipku Enter na grupi koju želimo otvoriti, popis niti se možda neće prikazati i tada je potrebno ponovno postaviti fokus na tu grupu i pritisnuti tipku Enter. U pravilu, nakon drugog pritiska prikazuje se popis niti, a nakon toga možemo pritisnuti kombinaciju tipki koja će pomaknuti fokus na taj popis.
* Sada kombinacija Alt+2 pomiče fokus ne samo na popis poruka, već i na otvoreni profil, na otvoreni popis niti grupe ili na otvoreni odjeljak s postavkama.
* Sada u postavkama UnigramPlusa možete onemogućiti izgovor izraza "Administrator" i "Vlasnik" na porukama u grupama.
* Kombinacije za prihvaćanje i odbijanje poziva sada rade ispravno.
* Sada se značajka automatskog čitanja novih poruka i praćenja aktivnosti razgovora neće isključiti kada se NVDA ponovno pokrene, ali će raditi dok je sami ne isključite.
* Poboljšan prikaz nekih elemenata sučelja.

###Verzija 4.5.0

* Prilagođeno za najnoviju verziju Unigrama.
* Ako je poruka poslana kao odgovor na drugu poruku, pritiskom na strelicu lijevo možete čuti tekst poruke na koju je odgovoreno.
* Dodana francuska lokalizacija.
* Uklonjena mogućnost dodavanja reakcija na poruke s tipkovničkim prečacima, jer nisam mogao prilagoditi ovu značajku promjenama u Unigram sučelju.
* Ispravljene su neke manje pogreške.

###Verzija 4.4.0

* Dodana je funkcija najave aktivnosti u razgovorima. Prema zadanim postavkama, ova se funkcija aktivira dvostrukim pritiskom kombinacije ALT+T. Funkcija ostaje aktivna samo dok se NVDA ponovno ne pokrene.
* Dodana je funkcija automatske najave novih poruka u razgovoru. Prema zadanim postavkama, ova se funkcija aktivira pritiskom na ALT+L. Značajka ostaje aktivna samo dok se NVDA ponovno ne pokrene. Može doći do problema sa stabilnošću ako se u razgovoru brzo pojavi previše novih poruka.
* Dodan tipkovnički prečac za funkciju pretvaranja glasovnih poruka u tekst. Prema zadanim postavkama, ova je funkcija dodijeljena kombinaciji NVDA+ALT+R. Imajte na umu da se u slučajevima kada je glasovna poruka jako duga, pretvaranje u tekst odvija u dijelovima. Odnosno, može se dogoditi da kada vas UnigramPlus obavijesti da je pretvaranje završeno, samo dio glasovne poruke će zapravo biti pretvoren. I nakon nekoliko sekundi, ovaj tekst će biti dodan.
* Sada, kada se krećete kroz popis razgovora, UnigramPlus javlja informacije o premium računima i potvrđenim računima.

###Verzija 4.3.0

* Sada UnigramPlus radi ispravno kada je nekoliko razgovora otvoreno u različitim prozorima.
* Dodan tipkovnički prečac za premještanje fokusa na područje korisničkog profila ako je otvoren. Zadana gesta je alt+5.
* Ispravljene manje pogreške.

###Verzija 4.2.0

* Mehanizam za spremanje UnigramPlus postavki značajno je redizajniran. Sada postavke neće biti pohranjene u NVDA konfiguracijskoj datoteci, već će biti pohranjene u vlastitoj konfiguracijskoj datoteci. Ovo bi trebalo riješiti problem kada korisnici nakon ažuriranja ili samo iznenada UnigramPlus prestane raditi, zbog problema s pristupom NVDA konfiguracijskoj datoteci. Nažalost, korisnici će morati ponovno konfigurirati UnigramPlus za sebe, jer će nakon instaliranja ovog ažuriranja sve postavke biti poništene.
* Riješen problem kompatibilnosti UnigramPlusa s dodatkom Bluetooth zvuk.
* Sada informacija da poruka nije odabrana neće biti prijavljena. Ako je poruka odabrana, informacije o njoj bit će objavljene prije sadržaja poruke.
* Sada će redoslijed elemenata u razgovoru biti objavljen ako ste omogućili poziciju elementa u NVDA postavkama.
* Dodane su oznake nekim gumbima.

###Verzija 4.2.0

* Prilagođeno za najnoviju verziju Unigrama.
* Ako je poruka poslana kao odgovor na drugu poruku, pritiskom na strelicu lijevo možete čuti tekst poruke na koju je odgovoreno.
* Dodana francuska lokalizacija.
* Uklonjena mogućnost dodavanja reakcija na poruke s tipkovničkim prečacima, jer nisam mogao prilagoditi ovu značajku promjenama u Unigram sučelju.
* Ispravljene su neke manje pogreške.

###Verzija 4.1.0

* Dodan tipkovnički prečac za prikvačivanje poruke ili razgovora. Prema zadanim postavkama ovoj značajki nije dodijeljen nijedan tipkovnički prečac.
* Dodan tipkovnički prečac za pritiskanje gumba "Novi razgovor". Zadani tipkovnički prečac za ovu značajku je Control+N.
* Dodan tipkovnički prečac za pritiskanje gumba "Priloži datoteku". Zadani tipkovnički prečac je Control+Shift+A.
* Dodan tipkovnički prečac za odlazak na popis mapa razgovora. Zadani tipkovnički prečac je ALT+4. Ova će značajka biti korisna onima koji koriste više od devet mapa razgovora.
* Sada, kada se prebacujete između mapa pomoću strelica, fokus neće nikamo skočiti.
* Sada, prilikom prebacivanja između mapa pomoću prečaca, uz naziv aktivne mape, bit će objavljen i broj nepročitanih razgovora u ovoj mapi.
* Sada će značajke kao što su "Označava razgovor kao pročitan" i "Prikvačuje poruku ili razgovor" također raditi obrnuto.
* Dodana rumunjska lokalizacija.

###Verzija 4.1.0

* Dodana gesta za prikvačivanje poruke ili razgovora. Prema zadanim postavkama ovoj značajci nije dodijeljen nijedan tipkovnički prečac.
* Dodan tipkovnički prečac za pritiskanje gumba "Novi razgovor". Zadana gesta za ovu značajku je Control+N.
* Dodan tipkovnički prečac za pritiskanje gumba "Priloži datoteku". Zadana gesta je Control+Shift+A.
* Dodan tipkovnički prečac za odlazak na popis mapa razgovora. Zadana gesta je Alt+4. Ova će značajka biti korisna onima koji koriste više od devet mapa razgovora.
* Sada, kada se prebacujete između mapa pomoću strelica, fokus neće nikamo skočiti.
* Sada, prilikom prebacivanja između mapa pomoću prečaca, uz naziv aktivne mape, bit će objavljen i broj nepročitanih razgovora u toj mapi.
* Sada će značajke kao što su "Označava razgovor kao pročitan" i "Prikvačuje poruku ili razgovor" također raditi obrnuto.
* Dodana rumunjska lokalizacija.

###Verzija 4.0.0

* Omogućena kompatibilnost s Unigramom 8.8. Budući da se sučelje Unigrama promijenilo, morao sam prepisati značajan dio koda dodatka.
* Dodana mogućnost premotavanja glasovnih poruka unatrag i unaprijed. Za premotavanje unaprijed upotrijebite kombinaciju Control+Alt+Strelica desno, a za premotavanje unatrag upotrijebite Control+Alt+Strelica lijevo.
* Sada će UnigramPlus izvijestiti ne samo o prisutnosti reakcija u porukama, već i objaviti detaljne informacije o reakcijama.
* Dodana mogućnost pregleda teksta poruke u skočnom prozoru. Zadana gesta za ovu značajku je Alt+C.
* Dodan tipkovnički prečac za otvaranje prozora postavki UnigramPlusa. Zadana gesta za ovu značajku je NVDA+Control+U.
* Dodana češka i rumunjska lokalizacija.
* Riješen problem s ažuriranjem UnigramPlusa za stanovnike Ukrajine.

###Verzija 3.2.3

* Dodana kineska lokalizacija.
* Ažurirane postojeće lokalizacije, uključujući engleski.
* Ispravljene manje pogreške.

###Verzija 3.2.0

* Uklonjene značajke kao što su praćenje aktivnosti razgovora i čitanje novih poruka u otvorenom razgovoru jer ih nisam uspio natjerati da ispravno rade u NVDA 2022.1.
* Poboljšana dostupnost uključivanja/isključivanja mikrofona i uključivanja/isključivanja kamere u pozivima. Sada, nakon pritiska na prečac za obje funkcije, objavit će se njihov status.
* Riješen je problem u kojem tipka Enter nije ispravno radila na nekim elementima. Sada još uvijek možete snimati glasovne poruke držeći tipku Enter na gumbu za snimanje.
* Sada možete ponovno dodijeliti tipkovničke prečace značajkama kao što su "Odgovara na poruku" i "Uređuje poruku". Također možete dodijeliti ove funkcije tipkama kao što su Enter, Backspace ili čak strelice lijevo ili desno i to neće ometati te tipke na drugim stavkama. Imajte na umu da u početku ovim značajkama neće biti dodijeljene tipke, ali ćete ih moći dodijeliti samo kada je fokus na jednoj od poruka razgovora.
* Sada bi funkcija "Izgovori ime pošiljatelja" trebala raditi ispravnije.
* Kada se usredotočite na vezu sadržanu u poruci, tekst poruke neće biti prvi izgovoren, već će se odmah izgovoriti tekst veze.
* Napravljeno mnogo malih poboljšanja i popravljene mnoge greške i nedostaci.
* Sada bi UnigramPlus trebao raditi osjetno brže.

###Verzija 3.1.0

* Poboljšana je najava ankete. Imena korisnika koji su sudjelovali u anketama sada se objavljuju u prozoru s rezultatima. Ankete će također dati informaciju koja je opcija bila točna.
* Dodana je mogućnost reagiranja na poruke, ali samo u privatnim razgovorima. Ova značajka neće ispravno raditi u grupama i kanalima. U privatnim razgovorima, pritiskom na NVDA+Alt+brojevi od 1 do 5, možete upisati sljedeće reakcije: 1 - 👍, 2 - 👎, 3 - ❤, 4 - 🔥, 5 - 🥰.
* Dodana mogućnost objave informacija o postojećim odgovorima na poruke. Nažalost, još nije moguće objaviti nazive dostupnih reakcija.
* Dodana tipka prečaca za brzo kopiranje podataka potrebnih za emitiranje.
* Riješen je problem s prikazom ugrađenih rezultata koji se pojavio u najnovijim verzijama Unigrama.

###Verzija 3.0.0

Upozorenje! UnigramPlus će sada podržavati NVDA verzije ne starije od 21.2.0.
* Dodane oznake za mnoge elemente korisničkog sučelja.
* Ispravljene su neke greške.

###Verzija 2.9.0

* Sada će polje za uređivanje promijeniti svoju oznaku ovisno o tome odgovaramo li na poruku ili je uređujemo.
* Dodana je mogućnost omogućavanja dijaloškog okvira potvrde za brisanje poruka ili razgovora pomoću prečaca u postavkama.
* Dodana srpska lokalizacija.
* Popravljeni mali problemi.

###Verzija 2.8.0

* Dodana mogućnost ažuriranja dodatka iz samog dodatka. Sada, kako biste provjerili ima li ažuriranja i instalirali ih, samo otvorite postavke UnigramPlusa i kliknite odgovarajući gumb. Također možete omogućiti automatsku provjeru ažuriranja pri pokretanju NVDA.
* Dodana arapska lokalizacija.

###Verzija 2.7.0

* Sada ćete dobiti obavijest da je poruka proslijeđena.
* Poboljšana funkcija kopiranja poruka. Sada, ako tekst sadrži vezu koju je moguće kliknuti i fokus je na toj vezi, pritiskom na Control+C kopirat ćete vezu umjesto cijelog teksta.
* Dodana tipka prečaca za kopiranje poruka uz zadržavanje oblikovanja teksta. Ova funkcija oponaša aktivaciju odgovarajuće stavke u izborniku aplikacije. Zadana tipka prečaca za ovu značajku je Control+Shift+C. Zbog ove značajke, prečac za otvaranje komentara promijenjen je u Control+Alt+C.
* Dodana mogućnost automatske najave novih poruka u otvorenom razgovoru. Prema zadanim postavkama, može se omogućiti pritiskom na Alt+L.
* Dodani prečaci za brzo pregledavanje poruka razgovora. Pritisnite NVDA+Control+broj koji odgovara broju određene poruke obrnutim redoslijedom, to jest, ako želite pogledati posljednju poruku, pritisnite 1, ako želite pogledati prethodnu poruku, pritisnite 2, i tako dalje.
* Sada pritiskom na Alt+T dobit ćete informacije o aktivnom glasovnom razgovoru u trenutnoj grupi.

###Verzija 2.6.0

* Omogućena kompatibilnost s NVDA 21.3.
* Dodana tipka prečaca za omogućavanje odabira poruka ili razgovora.
* Dodana tipka prečaca za prosljeđivanje poruka.
* Dodana tipka prečaca za označavanje razgovora kao pročitanog.
* Poboljšana izvedba postojećih značajki.

###Verzija 2.5.0

* Sada postoji potvrdni okvir koji, ako je označen, rješava problem snimanja glasovnih poruka s kojim se neki korisnici susreću.
* Dodana tipka prečaca za odgovaranje na poruku. To možete učiniti pritiskom na Enter na poruci ili možete promijeniti alternativne prečace za ovu značajku na nešto drugo.
* Dodana tipka prečaca za uređivanje poruka. Zadana tipkovnička prečica je Alt+Backspace.

###Verzija 2.4.0

* Sada ćete čuti ime pošiljatelja kada se fokusirate na poruku.
* Kada se fokusirate na grupni razgovor koji sadrži nepročitane poruke, dobit ćete obavijest ako u toj grupi ima odgovora za vas.
* Izvedba značajki dodanih u prethodnom ažuriranju također je poboljšana.

###Verzija 2.3.0

* Poboljšana dostupnost poruka koje sadrže više medijskih privitaka. Ranije se naslovu poruke koja sadrži više od jednog medijskog privitka moglo pristupiti samo korištenjem objektnoj navigaciji. Sada će se ovaj natpis pročitati odmah nakon fokusiranja na takvu poruku.
* Poboljšana dostupnost poruka koje sadrže ankete. Sada kada se fokusirate na takvu poruku, čut ćete broj ljudi koji su već glasali, kao i sve opcije odgovora s rezultatom za svaku opciju.
* Poboljšana dostupnost poruka koje sadrže URL-ove. Sada, ako URL ima opis, on će također biti pročitan, to jest, na primjer, ako poruka ima URL za YouTube, naslov i opis za taj videozapis bit će pročitani odmah nakon samog URL-a. Također, ako je URL duži od 30 znakova, bit će skraćen kako bi sljedeći opis bio čitljiviji.
* Poboljšana dostupnost ploče s "InZa navigaciju kroz rezultate ugrađenih upita koristite sljedeće kombinacije: Control+Strelica gore i Control+Strelica dolje.
* Dodana tipka prečaca za otvaranje komentara.

###Verzija 2.2.0

* Dodana tipka prečaca za brisanje poruka ili razgovora samo za vas i za obje strane. Ova je funkcija povezana s jezikom sučelja Unigrama, pa možda neće raditi u nekim lokalizacijama. U postavkama možete odabrati vrstu obavijesti, tekst ili zvuk.
* Dodana je mogućnost da u postavkama odredite koji jezik sučelja koristite u Unigramu. To je neophodno za ispravan rad funkcija povezanih s određenim lokalizacijama.
* Dodana tipka prečaca za otvaranje trenutnog profila razgovora.
* Sada, nakon zatvaranja razgovora, fokus će se premjestiti na popis razgovora a ne na gumb "Otvori navigacijski izbornik".

###Verzija 2.1.0

* Prilikom prebacivanja između mapa na popisu razgovora, naziv trenutne mape bit će objavljen.
* Na popisu razgovora čut ćete naziv razgovora, a zatim njegovu vrstu.
* Poboljšana funkcija pomicanja fokusa na popis razgovora. Sada bi trebao raditi točnije i bez kašnjenja.
* Sada su postavke dodatka postale još fleksibilnije, jer se u izborniku NVDA Postavke pojavio odjeljak s nekim UnigramPlus opcijama.
* Dodana poljska lokalizacija.
* Mnogo malih popravaka i poboljšanja.

###Verzija 2.0.0

* Značajka u kojoj se riječ "Viđeno" ne najavljuje i riječ "Nije viđeno se izgovara prije čitanja sadržaja poruke sada radi na španjolskoj, portugalskoj, hrvatskoj, turskoj i perzijskoj lokalizaciji.
* Poboljšana funkcija najava trake napretka. Sada, kada je ovaj način rada uključen, ne oglašavaju se svi indikatori napretka, već samo oni koji su u fokusu.
* Ako pritisnete razmaknicu u poruci koja sadrži datoteku čije preuzimanje nije dovršeno, dobit ćete obavijest da je preuzimanje pauzirano.
* Dodana portugalska lokalizacija.
* Popravljeni su neki sitni problemi i poboljšana izvedba.

###Verzija 1.9.0

* Dodana je tipka prečaca koja mijenja razinu najave trake napretka između vrijednosti kao što su: "Najavi sve trake napretka", "Najavi neke trake napretka", "Najavi sve trake napretka osim trake napretka reprodukcije glasovne poruke" i "Ne najavljuj trake napretka". Za one korisnike kojima je u Unigramu onemogućeno automatsko preuzimanje medija, razina najave na traci napretka može se postaviti na "Najavi sve trake napretka osim trake napretka reprodukcije glasovne poruke", a za one koji imaju uključenu, bolje je postaviti na "Ne najavljuj trake napretka".
* Dodana španjolska, hrvatska i perzijska lokalizacija.
* Ispravljene manje pogreške iz prethodnih verzija.

###Verzija 1.8.0

* Naziv i veličina datoteke će se izgovoriti kada je pokazivač fokusiran na gumb "Otvori datoteku" ili gumb "Preuzmi datoteku", a kada je pokazivač fokusiran na gumb za reprodukciju audiodatoteke, čut ćete njezin naziv i trajanje.
* Dodana tipka prečaca za premještanje fokusa na polje za uređivanje. Ako je fokus već u polju za uređivanje, tada će se nakon pritiska tipke prečaca pomaknuti na mjesto gdje je bio prije.
* Značajka praćenja aktivnosti razgovora sada je omogućena dvostrukim pritiskom na Alt+T. Možete je jednostavno uključiti ili je privremeno uključiti do sljedećeg zatvaranja aplikacije.
* Dodana mogućnost odabira vrste obavijesti za snimanje glasovnih poruka. To se radi dvostrukim pritiskom tipke prečaca control+d. Tamo možete birati između zvuka, tekstualne obavijesti ili se vratiti na standardno ponašanje snimanja glasovnih poruka.

###Verzija 1.7.0

Značajno poboljšana funkcija snimanja glasovnih poruka. Snimanje, slanje i otkazivanje snimanja glasovne poruke popraćeni su karakterističnim zvukovima. Također, prilikom izvođenja ovih funkcija, fokus ostaje na svom mjestu i ne skače niti na gumb za snimanje niti na polje za unos poruke.

###Verzija 1.7.0

* Dodana mogućnost praćenja aktivnosti razgovora. Ova se opcija može omogućiti pritiskom na Alt+Shift+T i ostaje aktivna dok se Unigram ne zatvori ili NVDA ponovno ne pokrene.
* Prečac koji aktivira gumb "Više opcija" sada radi u prozoru za glasovni razgovor i prozoru za pozive.

###Verzija 1.6.0

* Ako se medij priložen poruci otvori pomoću razmaknice, nakon zatvaranja fokus će se vratiti na zadnji element koji je bio u fokusu.
* Sada se možete vratiti na aktivni glasovni razgovor ne samo iz trenutne grupe, već i iz bilo kojeg drugog razgovora.
* Pritiskom na Alt+Shift+C u otvorenom razgovoru vratit ćete se na glasovni razgovor umjesto pozivanja kontakta.
* Ako poruka nije poslana, bit ćete obaviješteni čim poruka bude fokusirana.
* Ako fokusirana poruka sadrži vezu, čut ćete samo tekst same veze, a ne cijelu poruku.
* Riješen je problem u kojem se promjene statusa gumba kao što su Uključi/isključi mikrofon i Omogući/onemogući kameru nisu prijavljivale u privatnim pozivima i glasovnim razgovorima.
* Sada vam funkcija kopiranja poruke omogućuje kopiranje sadržaja stavki u prozoru za brzi pregled poruke.

###Verzija 1.5.1

Ovo ažuriranje ispravlja veliki broj grešaka i poboljšava izvedbu dodatka.

###Verzija 1.5.0

Ovo ažuriranje dodaje prečac koji pritišće gumb "Trenutni prikaz" u poruci ako je uključen u poruku. Prema zadanim postavkama, ova je značajka aktivirana tipkom prečaca Alt+Q. Nakon otvaranja takvog članka fokus će automatski prijeći na prvi element ovog članka, a nakon zatvaranja fokus će se vratiti na zadnju pregledanu poruku. Također smo popravili problem zbog kojeg nisu svi elementi članka u prozoru Instant View bili čitljivi, čak i ako su sadržavali tekstualni sadržaj.

###Verzija 1.1.7

Dodana turska lokalizacija.
