### [Palindrome Reorder](https://cses.fi/problemset/task/1755)

Adott egy szöveg, amelynek betűit olyan sorrendbe kell rendezned, hogy palindrómává váljon (azaz előre és visszafelé is ugyanazt olvashassuk). 

#### Bemenet
Az egyetlen bemeneti sor egy `n` hosszúságú szöveg, amely az `A–Z` karaktereket tartalmazza.

#### Kimenet
Írj ki egy olyan palindrómát, amely az eredeti szöveg karaktereiből áll. Bármilyen érvényes megoldás elfogadható. Ha nem lehetséges palindróma létrehozása, akkor írj ki „NO SOLUTION” üzenetet.

#### Magyarázat
A fő metódus a `create_palindrome_recursive()`, aminek egy paramétere van, a vizsgált `string`. 
Létre kell hozni egy `dict`-et amiben megszámoljuk az egyes karakterek előfordulását.
Amennyiben 1-nél több páratlan gyakoriságú karakterünk van, akkor ebben az esetben nem lehetséges a palindróma és vissza adjuk a "NO SOLUTION" eredményt. 

Ezután `build_palindrome()` segédmetódussal hozzuk létre a palindrómát. Az alapeset az amikor üres a karakereket tartalmazó `chars`, ekkor visszaadjuk a paraméterként kapott `left_half` változót, hozzáfűzve a palindróma középső karakterét és végül a `left_half` megfordítottját.

Rekurzív esetben pedig, a `left_half` változót feltöltjük a `chars`-ban visszamaradó karakterekkel, és megállapítjuk a középső karaktert, ha van ilyen.

