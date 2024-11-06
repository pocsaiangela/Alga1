# [Closest Numbers](https://www.hackerrank.com/challenges/closest-numbers/problem)

A rendezés hasznos lehet első lépésként sok különböző feladatban. A leggyakoribb felhasználás az, hogy megkönnyíti a keresést, de más célokra is használható. Ebben az esetben a rendezés segít meghatározni, hogy melyik elem-pároknak van a legkisebb abszolút különbsége.

### Példa
`arr = [5,2,3,4,1]`

Rendezve: `arr = [1,2,3,4,5]` Több pár is van, amely minimális különbséggel rendelkezik: `1: [(1,2), (2,3), (3,4), (4,5)]`. Az eredményként visszaadandó tömb `[1,2,2,3,3,4,4,5]`.

### Megjegyzés
Amint a példában látható, a párok átfedhetik egymást.

Egy rendezetlen egész számokat tartalmazó listát kapunk: , találjuk meg azt a párelemet, amelynek a legkisebb az abszolút különbsége. Ha több ilyen pár is van, találjuk meg mindet.

### A függvény leírása

Írd meg a `closestNumbers` nevű függvényt az alábbi paraméterekkel:

- **Paraméterek**:
  - `int arr[n]`: egy egész számokat tartalmazó tömb
- **Visszatérési érték**:
  - `int[]`: egy tömb a leírásnak megfelelően

### Bemeneti formátum

Az első sor egyetlen egész számot tartalmaz, , a tömb hosszát.
A második sor  szóközzel elválasztott egész számot tartalmaz, amelyek az `arr` elemei.

### Megkötések
- 2 <= n <= 200000
- -10^7 <= arr[i] <= 10^7
- Minden a[i] egyedi az `arr`-ban.

