# [PICAD - Crime at Piccadily Circus](https://www.spoj.com/problems/PICAD/)

Sherlock Holmes egy nyomozást folytat egy bűntény ügyében a Piccadily Circus-on. Holmes megpróbálja meghatározni, hogy hány ember tartózkodott egyszerre a bűntény helyszínén minimálisan és maximálisan a bűntény elkövetésének idejében. A Scotland Yard már elvégzett egy alapos nyomozást, kikérdezték az összes embert, akit a bűntény helyszínén láttak, és meghatározták, hogy mikor érkeztek és távoztak. Watson doktor felajánlotta segítségét a Scotland Yard által összegyűjtött adatok feldolgozásában és Holmes számára érdekes számok meghatározásában, de némi nehézségbe ütközött. Segíts neki!
## Feladat
Írj egy programot, amely:

- Beolvassa a standard inputról a bűntény elkövetésének időintervallumát, valamint a Scotland Yard által összegyűjtött adatokat.
- Meghatározza a minimális és maximális számát azoknak az embereknek, akik egyszerre tartózkodtak a bűntény helyszínén az adott időintervallumban (ezek a számok lehetnek akár nullák is, habár furcsa lenne, ha senki sem lett volna a helyszínen a bűntény elkövetésekor — de Holmes és Watson ilyen típusú bűnesettel foglalkozik).
- Kiírja az eredményt a standard kimenetre.


### Bemenet
Tíz teszteset (egymás alatt megadva, mindegyiket fel kell dolgoznod!).  
Minden teszteset első sora két egész számot tartalmaz, `p` és `k`, ahol `0 <= p <= k <= 100000000`. Ezek azt jelzik, hogy a bűntény elkövetése az első és az utolsó időpont között történt.  
A második sor egy egész számot, `n`, tartalmaz, ahol `3 <= n <= 5000`. Ez a Scotland Yard által kihallgatott emberek száma.  
A következő `n` sorban két egész szám található, `a_i` és `b_i`, amelyek egy szóközzel vannak elválasztva, ahol `0 <= a_i <= b_i <= 1000000000`. Ezek azt jelzik, hogy az `i`-edik személy mikor érkezett (`a_i`) és távozott (`b_i`) a helyszínről. Ez azt jelenti, hogy az `i`-edik személy végig jelen volt a helyszínen az `a_i` és `b_i` időpontok között (beleértve ezeket az időpontokat is).
### Kimenet
Minden tesztesethez a programnak a standard output-ra csak egy sort kell kiírnia, amely két egész számot tartalmaz, egy szóközzel elválasztva:  
- a minimális és a maximális számát azoknak az embereknek, akik egyszerre tartózkodtak a bűntény helyszínén az `p` és `k` közötti időintervallumban (beleértve ezt az intervallumot is).
### Magyarázat
A feladat megoldása a `picad` nevű függvényben található. Először beolvasunk a standard inputról egy sort, amit felbontunk szóköz mentén és elmentjük a `start_of_crime` és `end_of_crime` váltózókba.

Ezután még egy sort beolvasunk a `scotland_yard_interrogations` változóba, ennyi sort kell majd beolvasni következőnek.

Ezekben a sorokban lévő értkékek is szóközzel vannak elválasztva, így itt is felbontjuk a korábbi a módon (`appeared`, `left`), és elmentjük őket egy listába (`appearances`).

Ezt kővetően megnézzük az egyes időpontokat a bűncselekmény kezdő és végpontja (beleszámítva) között. Végigznézzük hogy az egyes kikérdezett emberek az adott időpontban jelen voltak-e (`appearance[0] <= time <= appearance[1]`). Miután megvan az adott időponthoz az emberek száma, ezt hozzáadjuk egy listához.

Ennek a listának a minimuma és maximuma lesz a minimális és maximális száma azoknak az embereknek, akik egyszerre tartózkodtak a bűntény helyszínén.

A `main` függvényben pedig 10x meghívjuk.