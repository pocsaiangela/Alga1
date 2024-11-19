# [PRIME1 - Prime Generator](https://www.spoj.com/problems/PRIME1/)

Péter szeretne prímszámokat generálni a kriptorendszeréhez. Segíts neki! A feladatod, hogy generáld le az összes prímszámot két megadott szám között!

### Bemenet
A bemenet első sora tartalmazza a tesztesetek számát, `t`-t (1 <= t <= 10). A következő `t` sorban két szám található, `m` és `n` (1 <= m <= n <= 1 000 000 000, n - m <= 100 000), szóközzel elválasztva.

### Kimenet
Minden tesztesethez írd ki az összes prímszámot `p`, amelyre igaz, hogy `m <= p <= n`, soronként egy számot. Az egyes tesztesetek kimeneteit egy üres sor választja el.

### Magyarázat
Létrehozzuk a `isPrime` függvényt, ami visszaadja, hogy a paraméterben kapott szám prím-e. Egy szám akkor prím, ha csak önmagával és eggyel osztható, tehát ha egy szám osztható mással, akkor az nem prím. Ezért végigmegyünk a számokon `2`-től `num`-ig (ha a `num` <= 2 már le van kezelve). Hogy ha találunk egy olyan számot, amivel osztható a `num`, akkor meg is találtuk, hogy nem prím.

A `cache`-t fel tudjuk használni az algoritmus optimalizálására, mivel az ellenőrzött számokat el tudjuk menteni, hogy prím-e vagy nem.

