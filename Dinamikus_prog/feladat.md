# [Substring Diff](https://www.hackerrank.com/challenges/substring-diff/problem)

Ebben a feladatban a "leghosszabb közös részszöveg" kifejezést lazán használjuk. Olyan részszövegekre utal, amelyek indexenként összehasonlítva legfeljebb egy bizonyos számú karakterben különböznek. Például, az 'abc' és 'adc' egy pozícióban tér el, az 'aab' és 'aba' pedig kettőben.

Adott két szöveg és egy egész szám, k, határozd meg a két szöveg olyan leghosszabb közös részszövegeinek hosszát, amelyek legfeljebb k pozícióban térnek el egymástól.

Például, k = 1. Szövegek: s1 = "abcd" és s2 = "bbca". Ellenőrizzük, hogy a teljes szöveg (a leghosszabb részszövegek) egyeznek-e. Tekintve, hogy sem az első, sem az utolsó karakterek nem egyeznek, és 2 > k, rövidebb részszövegeket kell vizsgálnunk. A következő leghosszabb részszövegek: s1' = [abc, bcd] és s2' = [bbc, bca]. Ezek közül két pár legfeljebb egy pozícióban tér el: [abc, bbc] és [bcd, bca]. Ezek hossza 3.

### Funkció leírása

Egészítsd ki a `substringDiff` nevű függvényt az alábbiak szerint. A függvény egy egész számot adjon vissza, amely a leghosszabb közös részszöveg hosszát jelenti a megadott definíció szerint.

#### `substringDiff` paraméterei:
- **k**: egy egész szám, amely a különböző karakterek maximális számát jelöli egy egyező párban.
- **s1**: az első szöveg.
- **s2**: a második szöveg.

### Magyarázat
Először létrehozunk egy 3D-s tömböt (`dp`), amiben eltároljuk, hogy bizonyos indexekig legfeljebb hány eltérést tartalmaznak a szövegek. Pl: `dp[i][j][d]` azt jelenti, hogy `s1` az i-edik karakterig és az `s2` j-edik karakterig legfeljebb `d` eltérést tartalmaznak.

Ezután végigmegyünk az `s1` és `s2` összes karakterén, és megnézzük hogy a két karakter megegyezik-e. Ha igen, akkor meghosszabbítjuk a közös résszöveget az előző pozíció értékével. Ha nem, akkor (ha van még megengedett eltérések száma) növeljük az előző pozíció értékét. 

Illetve a feltöltés közben folyamatosan frissítjük az eddigi legnagyobb értéket.  
