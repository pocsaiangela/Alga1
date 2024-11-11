# [Counting Rooms](https://cses.fi/problemset/task/1192/)

Egy épület térképét kapod meg, és a feladatod, hogy megszámold a benne található szobákat. A térkép mérete `n * m` négyzet, és minden négyzet vagy padló, vagy fal. A padló négyzeteken keresztül balra, jobbra, fel és le is lehet mozogni.

### Bemenet
Az első bemeneti sorban két egész szám található, `n` és `m`: a térkép magassága és szélessége. Ezután `n` sorban `m` karakter írja le a térképet. Minden karakter vagy `.` (padló), vagy `#` (fal).

### Kimenet
Írj ki egy egész számot: a szobák számát.

#### Korlátok
1 <= n, m <= 1000

### Magyarázat
Először létrehozzuk a szükséges változókat: 
- `directions`: a négy lehetséges irányvektor
- `visited`: n*m méretű tömb a látogatott koordinátákkal
- `room_count`: a talált szobák

Végigmegyünk a `building_map` 2D tömbön és az eddig nem látogatott padló koordinátákra meghívjuk a `DFS()` metódust.

##### DFS
A Depth-first search implementációja. Létrehozunk egy vermet, amibe belerakjuk a kapott koordináta párt. Ezután mind a 4 irányba kiszámoljuk a lehetséges koordinátákat és a megfelelőket meglátogatjuk. Ennek segítségével az összes összefüggő csempét csoportosíthatjuk egy szobává.