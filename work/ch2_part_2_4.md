## 2.4 Lineáris egyenletrendszerek megoldása

### 2.4.1 Feladatátalakítások

Az $Ax = b$ lineáris egyenletrendszer megoldásához az 1.1.2. szakaszban felvázolt általános stratégia azt sugallja, hogy a rendszert olyan rendszerré kell átalakítanunk, amelynek megoldása megegyezik az eredetiével, de könnyebben kiszámítható. Milyen típusú átalakítás hagyja változatlanul egy lineáris rendszer megoldását? A válasz az, hogy az $Ax = b$ lineáris rendszer mindkét oldalát balról bármely nemszinguláris $M$ mátrixszal megszorozhatjuk anélkül, hogy a megoldást befolyásolnánk. Hogy lássuk, miért, vegyük észre, hogy az $MAz = Mb$ lineáris rendszer megoldása

$$z = (MA)^{-1}Mb = A^{-1}M^{-1}Mb = A^{-1}b = x.$$

**2.9. Példa. Permutációk.** Ilyen átalakítás fontos példája az a tény, hogy $A$ sorai és $b$ megfelelő elemei átrendezhetők az $x$ megoldás megváltoztatása nélkül. Ez intuitíve nyilvánvaló: a rendszer összes egyenletének egyidejűleg teljesülnie kell, ezért az a sorrend, amelyben leírjuk őket, közömbös; akár véletlenszerűen is húzhatnánk őket egy kalapból. Formálisan a sorok ilyen átrendezését úgy valósítjuk meg, hogy az egyenlet mindkét oldalát balról megszorozzuk egy $P$ permutációs mátrixszal, amely olyan négyzetes mátrix, amelynek minden sorában és oszlopában pontosan egy 1-es szerepel, a többi elem pedig nulla (azaz egy egységmátrix, amelynek sorai és oszlopai permutálva vannak). Például

$$\begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = \begin{bmatrix} v_3 \\ v_1 \\ v_2 \end{bmatrix}.$$

Egy permutációs mátrix mindig nemszinguláris; valójában az inverze egyszerűen a transzponáltja, $P^{-1} = P^T$ (egy $M$ mátrix transzponáltja, amelyet $M^T$ jelöl, olyan mátrix, amelynek oszlopai $M$ sorai, azaz ha $N = M^T$, akkor $n_{ij} = m_{ji}$). Így az átrendezett rendszer $PAx = Pb$ alakban írható, és az $x$ megoldás változatlan marad.

Ha jobbról szorzunk meg egy permutációs mátrixszal, akkor az a mátrix oszlopait rendezi át a sorok helyett. Az ilyen átalakítás megváltoztatja a megoldást, de csak úgy, hogy a megoldás komponensei permutálódnak. Ennek belátásához figyeljük meg, hogy az $APz = b$ rendszer megoldása

$$z = (AP)^{-1}b = P^{-1}A^{-1}b = P^{T}A^{-1}b = P^{T}x,$$

és ennélfogva az eredeti $Ax = b$ rendszer megoldása $x = Pz$.

**2.10. Példa. Diagonális skálázás.** Egy másik egyszerű, de fontos átalakítási típus a diagonális skálázás. Emlékezzünk vissza, hogy egy $D$ mátrix diagonális, ha $d_{ij} = 0$ minden $i \neq j$ esetén, azaz az egyetlen nemnulla elemei a főátlón lévő $d_{ii}$, $i = 1, \dots, n$ elemek. Ha az $Ax = b$ lineáris rendszer mindkét oldalát balról megszorozzuk egy nemszinguláris $D$ diagonális mátrixszal, akkor a mátrix minden sorát és a jobb oldalt $D$ megfelelő átlóbeli elemével szorozzuk meg, és ezt ezért sorkénti skálázásnak nevezzük. Elvben a sorkénti skálázás nem változtatja meg a lineáris rendszer megoldását, a gyakorlatban azonban befolyásolhatja a numerikus megoldási folyamatot és az adott feladatnál elérhető pontosságot, mint azt látni fogjuk.

Az oszloponkénti skálázás — egy lineáris rendszer mátrixának jobbról való megszorzása egy nemszinguláris $D$ diagonális mátrixszal — a mátrix minden oszlopát $D$ megfelelő átlóbeli elemével szorozza meg. Az ilyen átalakítás valóban megváltoztatja a megoldást, gyakorlatilag azokat a mértékegységeket változtatja meg, amelyekben a megoldás komponenseit mérjük. A skálázott $ADz = b$ rendszer megoldása

$$z = (AD)^{-1}b = D^{-1}A^{-1}b = D^{-1}x,$$

és ennélfogva az eredeti $Ax = b$ rendszer megoldása $x = Dz$.

### 2.4.2 Háromszögű lineáris egyenletrendszerek

A következő kérdés az, hogy milyen típusú lineáris rendszer könnyen megoldható. Tegyük fel, hogy az $Ax = b$ rendszerben van egy olyan egyenlet, amely csak egy ismeretlen megoldáskomponenst tartalmaz (azaz $A$ ezen sorában csak egy elem nemnulla). Akkor ez az egyenlet könnyen megoldható (osztással) erre az ismeretlenre. Tegyük fel most, hogy a rendszerben van egy másik egyenlet, amely csak két ismeretlent tartalmaz, és ezek egyike a már meghatározott. Ha a már meghatározott megoldáskomponenst behelyettesítjük ebbe a második egyenletbe, akkor könnyen megoldhatjuk a másik ismeretlenre. Ha ez a minta folytatódik — egyenletenként csak egy új ismeretlen komponens lép fel —, akkor a megoldás összes komponense egymás után kiszámítható. Az ilyen speciális tulajdonságú mátrixot *háromszögnek* nevezzük — a név okát hamar látni fogjuk. Mivel a háromszögű lineáris rendszerek ezzel az egymás utáni helyettesítéssel könnyen megoldhatók, alkalmas cél, amelyre egy általános lineáris rendszert átalakíthatunk.

Bár a fentebb leírt általános háromszögalak elegendő ahhoz, hogy a rendszer egymás utáni helyettesítéssel megoldható legyen, számítási célokra kényelmes két speciális háromszögalakot definiálnunk. Egy $L$ mátrix *alsó háromszögmátrix*, ha a főátló feletti összes eleme nulla (azaz $\ell_{ij} = 0$ $i < j$ esetén). Hasonlóan, egy $U$ mátrix *felső háromszögmátrix*, ha a főátló alatti összes eleme nulla (azaz $u_{ij} = 0$ $i > j$ esetén). Egy a fent definiált általánosabb értelemben háromszögalakú mátrix sorainak vagy oszlopainak alkalmas permutációjával felső vagy alsó háromszögalakba hozható.

Egy $Lx = b$ alsó háromszögű rendszer esetén az egymás utáni helyettesítést *előrehelyettesítésnek* nevezzük, és matematikailag így fejezhetjük ki:

$$x_1 = b_1/\ell_{11}, \quad x_i = \left(b_i - \sum_{j=1}^{i-1} \ell_{ij} x_j\right)/\ell_{ii}, \quad i = 2, \dots, n.$$

Megvalósításának egyik módját a 2.1. Algoritmus mutatja.

**2.1. Algoritmus. Előrehelyettesítés alsó háromszögű rendszerre.**

```
for j = 1 to n                       { ciklus az oszlopokra }
    if ℓjj = 0 then stop             { leállás, ha a mátrix szinguláris }
    xj = bj/ℓjj                      { megoldáskomponens kiszámítása }
    for i = j + 1 to n
        bi = bi − ℓij xj             { jobb oldal frissítése }
    end
end
```

Hasonlóan, egy $Ux = b$ felső háromszögű rendszer esetén az egymás utáni helyettesítést *visszahelyettesítésnek* nevezzük, és matematikailag így fejezhetjük ki:

$$x_n = b_n/u_{nn}, \quad x_i = \left(b_i - \sum_{j=i+1}^n u_{ij}x_j\right)/u_{ii}, \quad i = n-1, \dots, 1.$$

Megvalósításának egyik módját a 2.2. Algoritmus mutatja.

Mindkét algoritmusban úgy választottuk meg a ciklusváltozók sorrendjét, hogy a mátrixhoz oszloponként (és nem soronként) férünk hozzá, és a belső ciklus művelete egy skalár szorozva egy vektorral, majd ehhez hozzáadva egy vektor — azaz egy „saxpy" művelet (lásd a 2.7.2. szakaszt).

**2.2. Algoritmus. Visszahelyettesítés felső háromszögű rendszerre.**

```
for j = n to 1                       { ciklus az oszlopokra visszafelé }
    if ujj = 0 then stop             { leállás, ha a mátrix szinguláris }
    xj = bj/ujj                      { megoldáskomponens kiszámítása }
    for i = 1 to j − 1
        bi = bi − uij xj             { jobb oldal frissítése }
    end
end
```

Választhattuk volna a ciklusváltozók fordított sorrendjét is, ekkor a mátrixhoz soronként férnénk hozzá, és a belső ciklus művelete két vektor belső szorzata lenne, azaz „sdot". Ezek a megvalósítási választások jelentős hatással lehetnek a teljesítményre, az alkalmazott programozási nyelvtől és számítógépes rendszertől függően (lásd a 2.16. számítógépes feladatot). Azt is érdemes megjegyezni, hogy egy nulla átlóbeli elem mindkét algoritmust elbukatja, de ez így is várható, mivel egy nulla átlóbeli elemű háromszögmátrix szükségképpen szinguláris.

**2.11. Példa. Háromszögű lineáris egyenletrendszer.** Tekintsük a következő felső háromszögű lineáris rendszert:

$$\begin{bmatrix} 1 & 2 & 2 \\ 0 & -4 & -6 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 \\ -6 \\ 1 \end{bmatrix}.$$

Az utolsó egyenlet, $-x_3 = 1$, közvetlenül megoldható $x_3 = -1$-re. Ezt az értéket ezután behelyettesíthetjük a második egyenletbe, hogy $x_2 = 3$-at kapjunk, végül pedig $x_3$-at és $x_2$-t egyaránt behelyettesítve az első egyenletbe, $x_1 = -1$ adódik.

### 2.4.3 Elemi eliminációs mátrixok

Stratégiánk tehát az, hogy olyan nemszinguláris lineáris transzformációt tervezzünk, amely egy adott általános lineáris rendszert olyan háromszögű lineáris rendszerré alakít, amely utána az egymás utáni helyettesítéssel könnyen megoldható. Ehhez tehát olyan transzformációra van szükségünk, amely az adott mátrix kiválasztott nemnulla elemeit nullákkal helyettesíti. Ez a mátrix sorainak alkalmas lineáris kombinációival érhető el, ahogyan azt most megmutatjuk.

Tekintsük az $a = \begin{bmatrix} a_1 & a_2 \end{bmatrix}^T$ 2-vektort. Ha $a_1 \neq 0$, akkor

$$\begin{bmatrix} 1 & 0 \\ -a_2/a_1 & 1 \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} a_1 \\ 0 \end{bmatrix}.$$

Általánosabban: egy $n$-dimenziós $a$ vektor $k$-adik pozíciója alatti minden elemet annullálhatunk — feltéve, hogy $a_k \neq 0$ — a következő transzformációval:

$$\bm{M}_{k}\,\bm{a} = \begin{bmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & -m_{k+1} & 1 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & -m_{n} & 0 & \cdots & 1 \end{bmatrix} \begin{bmatrix} a_{1} \\ \vdots \\ a_{k} \\ a_{k+1} \\ \vdots \\ a_{n} \end{bmatrix} = \begin{bmatrix} a_{1} \\ \vdots \\ a_{k} \\ 0 \\ \vdots \\ 0 \end{bmatrix},$$

ahol $m_i = a_i/a_k$, $i = k+1, \dots, n$. Az $a_k$ osztót *főelemnek* (pivotnak) nevezzük. Az ilyen alakú mátrixot néha *elemi eliminációs mátrixnak* vagy *Gauss-transzformációnak* nevezzük, és egy vektorra gyakorolt hatása az, hogy a $k$-adik sor többszörösét hozzáadja minden további sorhoz, úgy megválasztva az $m_i$ szorzótényezőket, hogy az eredmény minden esetben nulla legyen. Vegyük észre az elemi eliminációs mátrixok alábbi tulajdonságait:

1. $M_k$ alsó háromszögmátrix, amelynek főátlójában csupa egyes áll, ezért szükségképpen nemszinguláris.
2. $M_k = I - m_k e_k^T$, ahol $m_k = [0, \dots, 0, m_{k+1}, \dots, m_n]^T$, és $e_k$ az egységmátrix $k$-adik oszlopa.
3. $M_k^{-1} = I + m_k e_k^T$, ami azt jelenti, hogy $M_k^{-1}$ — amelyet $L_k$-val fogunk jelölni — ugyanaz, mint $M_k$, csak a szorzótényezők előjele megváltozik.
4. Ha $M_j$, $j > k$, egy másik elemi eliminációs mátrix $m_j$ szorzótényező-vektorral, akkor

$$M_k M_j = I - m_k e_k^T - m_j e_j^T + m_k e_k^T m_j e_j^T = I - m_k e_k^T - m_j e_j^T,$$

mivel $e_k^T m_j = 0$. Így szorzatuk lényegében „uniójuk". Mivel azonos alakúak, hasonló eredmény érvényes inverzeik $L_k L_j$ szorzatára is. Figyeljük meg, hogy a szorzás sorrendje lényeges; ezek az eredmények a fordított szorzatra nem teljesülnek.

**2.12. Példa. Elemi eliminációs mátrixok.** Ha $a = \begin{bmatrix} 2 & 4 & -2 \end{bmatrix}^T$, akkor

$$\bm{M}_1 \bm{a} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 4 \\ -2 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}, \quad \bm{M}_2 \bm{a} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0{,}5 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 4 \\ -2 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \\ 0 \end{bmatrix}.$$

Megjegyezzük továbbá, hogy

$$\bm{L}_1 = \bm{M}_1^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix}, \quad \bm{L}_2 = \bm{M}_2^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -0{,}5 & 1 \end{bmatrix},$$

és

$$\bm{M}_1 \bm{M}_2 = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 1 & 0{,}5 & 1 \end{bmatrix}, \quad \bm{L}_1 \bm{L}_2 = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -0{,}5 & 1 \end{bmatrix}.$$

### 2.4.4 Gauss-kiküszöbölés és LU-felbontás

Elemi eliminációs mátrixokat használva viszonylag egyszerűen redukálhatunk egy általános $Ax = b$ lineáris rendszert felső háromszögalakra. Először a 2.4.3. szakaszban megadott recept szerint választunk egy $M_1$ elemi eliminációs mátrixot, úgy, hogy a főelem az első átlóbeli elem, $a_{11}$ legyen, hogy $A$ első oszlopa nullává váljon az első sor alatt, amikor $M_1$-gyel balról szorozzuk. Természetesen $A$ többi oszlopát, valamint a $b$ jobb oldali vektort is meg kell szorozni $M_1$-gyel, így az új rendszer $M_1 A x = M_1 b$ alakú lesz, de korábbi tárgyalásunk szerint a megoldás változatlan.

Ezután a második átlóbeli elemet használjuk főelemként egy olyan $M_2$ elemi eliminációs mátrix meghatározásához, amely az új $M_1 A$ mátrix második oszlopának minden elemét a második sor alatt annullálja. $M_2$-t ismét az egész mátrixra és a jobb oldali vektorra kell alkalmazni, így a $M_2 M_1 A x = M_2 M_1 b$ módosított lineáris rendszert kapjuk. Megjegyzendő, hogy $M_1 A$ első oszlopát $M_2$ nem befolyásolja, mivel az érintett sorokban minden eleme nulla. Ez a folyamat minden egyes egymás utáni oszlopra folytatódik, amíg a mátrix összes főátló alatti eleme nem annullálódik. Ha bevezetjük az $M = M_{n-1} \cdots M_1$ mátrixot, akkor a transzformált lineáris rendszer

$$MAx = M_{n-1} \cdots M_1 Ax = M_{n-1} \cdots M_1 b = Mb$$

felső háromszögű, és visszahelyettesítéssel megoldható, hogy megkapjuk az eredeti $Ax = b$ lineáris rendszer megoldását.

Az imént leírt eljárást *Gauss-kiküszöbölésnek* nevezzük. *LU-felbontásnak* is nevezik, mert az $A$ mátrixot egy egységnyi átlójú alsó háromszögmátrix, $L$, és egy felső háromszögmátrix, $U$, szorzatára bontja. Ennek belátásához emlékezzünk vissza, hogy az $L_k L_j$ szorzat egységnyi átlójú alsó háromszögű, ha $k < j$, így

$$L = M^{-1} = (M_{n-1} \cdots M_1)^{-1} = M_1^{-1} \cdots M_{n-1}^{-1} = L_1 \cdots L_{n-1}$$

egységnyi átlójú alsó háromszögmátrix. Már láttuk, hogy konstrukció szerint az $U = MA$ mátrix felső háromszögű. Ennek megfelelően $A$-t

$$A = LU$$

szorzatként állítottuk elő, ahol $L$ egységnyi átlójú alsó háromszögmátrix és $U$ felső háromszögmátrix. Egy ilyen felbontás birtokában az $Ax = b$ lineáris rendszer $LUx = b$ alakban írható, és így előbb az $Ly = b$ alsó háromszögű rendszert előrehelyettesítéssel, majd az $Ux = y$ felső háromszögű rendszert visszahelyettesítéssel megoldva megoldható. Megjegyzendő, hogy az $y$ köztes megoldás megegyezik a korábbi megfogalmazásban szereplő transzformált jobb oldali $Mb$ vektorral. Így a Gauss-kiküszöbölés és az LU-felbontás ugyanannak a megoldási folyamatnak két kifejezésmódja. Azzal azonban, hogy az előre- és visszahelyettesítő háromszöges megoldási fázisokat a felbontástól elkülönítve hangsúlyozza, az LU-alak talán világosabbá teszi, hogy a felbontási fázist nem kell megismételni, amikor ugyanazzal az $A$ mátrixszal, de más jobb oldali vektorokkal további rendszereket oldunk meg, mivel az $L$ és $U$ tényezők újra felhasználhatók.

A Gauss-kiküszöbölési eljárást formálisan a 2.3. Algoritmus foglalja össze. Ez az algoritmus egyúttal $A$ LU-felbontását is kiszámítja: $L$ főátló alatti elemeit $\ell_{ik} = m_{ik}$ adja meg, $U$ átlóbeli és főátló feletti elemei pedig $A$ megfelelő elemeit írják felül. A gyakorlatban nem szükséges $A$ főátló alatti elemeit explicit módon nullára állítani, mivel csak a $U$ és $L$ eredményül kapott háromszögmátrixok érdekelnek bennünket. Sőt: $A$ főátló alatti elemei, amelyeket kinulláztunk, tökéletes helyet nyújtanak $L$ főátló alatti elemeinek tárolására; a 2.3. Algoritmus lényegében „helyben" végzi el a felbontást, ha $m_{ik}$ helyett $a_{ik}$-t írunk minden előforduláskor (lásd a 2.4.6. szakaszt ezekről és más megvalósítási részletekről). Egy $Ax = b$ lineáris rendszer megoldása során a $b$ jobb oldali vektor szükséges transzformációját beépíthetjük az LU-felbontási folyamatba, vagy különálló lépésként végezhetjük el, a 2.1. Algoritmust használva az $Ly = b$ alsó háromszögű rendszer megoldására, miután $L$-et a 2.3. Algoritmussal meghatároztuk. Bármelyik esetben a 2.2. Algoritmust használjuk ezután az $Ux = y$ felső háromszögű rendszer megoldására, hogy megkapjuk az $x$ megoldást.

**2.3. Algoritmus. LU-felbontás Gauss-kiküszöböléssel.**

```
for k = 1 to n − 1                       { ciklus az oszlopokra }
    if akk = 0 then stop                 { leállás, ha a főelem nulla }
    for i = k + 1 to n                   { szorzótényezők kiszámítása
        mik = aik/akk                        az aktuális oszlopra }
    end
    for j = k + 1 to n                   { transzformáció alkalmazása
        for i = k + 1 to n                   a maradék részmátrixra }
            aij = aij − mik akj
        end
    end
end
```

**2.13. Példa. Gauss-kiküszöbölés.** A Gauss-kiküszöbölést a következő lineáris egyenletrendszer megoldásán illusztráljuk:

$$x_1 + 2x_2 + 2x_3 = 3,$$
$$4x_1 + 4x_2 + 2x_3 = 6,$$
$$4x_1 + 6x_2 + 4x_3 = 10,$$

vagy mátrix jelöléssel

$$\bm{A}\bm{x} = \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \bm{b}.$$

$A$ első oszlopának főátló alatti elemeinek annullálásához az első sor négyszeresét vonjuk ki a második és a harmadik sorból:

$$M_1 A = \begin{bmatrix} 1 & 0 & 0 \\ -4 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 \\ 0 & -4 & -6 \\ 0 & -2 & -4 \end{bmatrix},$$

$$M_1 b = \begin{bmatrix} 1 & 0 & 0 \\ -4 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 6 \\ 10 \end{bmatrix} = \begin{bmatrix} 3 \\ -6 \\ -2 \end{bmatrix}.$$

Most az $M_1 A$ második oszlopa főátló alatti elemének annullálásához a második sor $0{,}5$-szörösét vonjuk ki a harmadik sorból:

$$\mathbf{M}_{2}\mathbf{M}_{1}\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -0{,}5 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 2 \\ 0 & -4 & -6 \\ 0 & -2 & -4 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 \\ 0 & -4 & -6 \\ 0 & 0 & -1 \end{bmatrix},$$

$$\mathbf{M}_{2}\mathbf{M}_{1}\mathbf{b} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -0{,}5 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ -6 \\ -2 \end{bmatrix} = \begin{bmatrix} 3 \\ -6 \\ 1 \end{bmatrix}.$$

Ezzel az eredeti rendszert a következő ekvivalens felső háromszögű rendszerre redukáltuk:

$$\boldsymbol{U}\boldsymbol{x} = \begin{bmatrix} 1 & 2 & 2 \\ 0 & -4 & -6 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 \\ -6 \\ 1 \end{bmatrix} = \boldsymbol{M}\boldsymbol{b} = \boldsymbol{y},$$

amelyet most visszahelyettesítéssel oldhatunk meg (mint a 2.11. Példában), és így $x = \begin{bmatrix} -1 & 3 & -1 \end{bmatrix}^T$ adódik. Az LU-felbontás explicit felírásához

$$\bm{L}_1\bm{L}_2 = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 4 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0{,}5 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 4 & 0{,}5 & 1 \end{bmatrix} = \bm{L},$$

így

$$\mathbf{A} = \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 4 & 0{,}5 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 2 \\ 0 & -4 & -6 \\ 0 & 0 & -1 \end{bmatrix} = \mathbf{L}\mathbf{U}.$$

### 2.4.5 Főelemkiválasztás

A Gauss-kiküszöbölési eljárással, ahogy eddig leírtuk, van egy kézenfekvő probléma, és van egy másik, némileg finomabb is. A kézenfekvő potenciális nehézség az, hogy az eljárás összeomlik, ha a mátrix még redukálatlan részének vezető átlóbeli eleme valamelyik lépésben nulla, mivel egy adott oszlop $m_i$ szorzótényezőinek kiszámításához az oszlop átlóbeli elemével való osztásra van szükség. A probléma megoldása majdnem ugyanilyen kézenfekvő: ha a $k$-adik lépésben az átlóbeli elem nulla, akkor cseréljük ki a rendszer $k$-adik sorát (mind a mátrixét, mind a jobb oldali vektorét) egy olyan későbbi sorral, amelynek $k$-adik oszlopbeli eleme nemnulla. A 2.9. Példából tudjuk, hogy egy ilyen csere nem változtatja meg a rendszer megoldását. Nemnulla átlóbeli elemet főelemként véve az eljárás a szokásos módon folytatódhat. A sorok ilyen cseréjét *főelemkiválasztásnak* nevezzük.

**2.14. Példa. Főelemkiválasztás és szingularitás.** A főelemkiválasztás esetleges szüksége semmilyen kapcsolatban nem áll azzal, hogy a mátrix szinguláris-e. Például az

$$\boldsymbol{A} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$

mátrix nemszinguláris, mégsincs LU-felbontása, hacsak nem cseréljük fel a sorokat, míg a szinguláris

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$$

mátrixnak van LU-felbontása:

$$A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} = LU.$$

De mi van akkor, ha a $k$-adik oszlop átlóján vagy az alatt nincs nemnulla elem? Akkor ebben a lépésben nincs mit tenni, mivel az annullálandó elemek már eleve nullák, így egyszerűen továbbléphetünk a következő oszlopra (azaz $M_k = I$). Jegyezzük meg, hogy ez a lépés nullát hagy az átlón, és így az eredményül kapott $U$ felső háromszögmátrix szinguláris lesz, de az LU-felbontás még így is befejezhető. Ez viszont azt jelenti, hogy az ezt követő visszahelyettesítés meghiúsul, mert $U$ minden átlóbeli elemével osztani kellene, de ez nem meglepő, hiszen az eredeti mátrixnak mindenképpen szingulárisnak kellett lennie. Sokkal alattomosabb probléma az, hogy lebegőpontos aritmetikában előfordulhat, hogy nem pontosan nullát kapunk, hanem csak egy nagyon kicsi átlóbeli elemet — és ezzel érkezünk meg a finomabb ponthoz.

Elvben bármely nemnulla érték megfelelhet főelemnek a szorzótényezők kiszámítására, de véges pontosságú aritmetikában a választást körültekintően kell meghozni, hogy minimalizáljuk a numerikus hiba terjedését. Konkrétan korlátozni szeretnénk a szorzótényezők nagyságát, hogy a korábbi kerekítési hibák ne erősödjenek fel, amikor a mátrix és a jobb oldal maradék részét megszorozzuk az egyes elemi eliminációs mátrixokkal. A szorzótényezők nagysága soha nem fogja meghaladni az 1-et, ha minden oszlopban az átlón vagy az alatt található legnagyobb abszolút értékű elemet választjuk főelemnek. Az ilyen eljárást *részleges főelemkiválasztásnak* nevezzük, és a gyakorlatban elengedhetetlen az általános lineáris rendszereken végzett Gauss-kiküszöbölés numerikusan stabil megvalósításához.

**2.15. Példa. Kis főelemek.** Véges pontosságú aritmetikában nemcsak a nulla főelemeket, hanem a *kis* főelemeket is kerülnünk kell, hogy megelőzzük az elfogadhatatlan hibanövekedést, mint az alábbi példa mutatja. Legyen

$$A = \begin{bmatrix} \epsilon & 1 \\ 1 & 1 \end{bmatrix},$$

ahol $\epsilon$ egy olyan pozitív szám, amely az adott lebegőpontos rendszer $\epsilon_{\text{mach}}$ egységnyi kerekítési hibájánál kisebb. Ha nem cseréljük fel a sorokat, akkor a főelem $\epsilon$, és a kapott szorzótényező $-1/\epsilon$, így az eliminációs mátrix

$$M = \begin{bmatrix} 1 & 0 \\ -1/\epsilon & 1 \end{bmatrix},$$

és ennélfogva

$$\bm{L} = \begin{bmatrix} 1 & 0 \\ 1/\epsilon & 1 \end{bmatrix} \quad \text{és} \quad \bm{U} = \begin{bmatrix} \epsilon & 1 \\ 0 & 1 - 1/\epsilon \end{bmatrix} = \begin{bmatrix} \epsilon & 1 \\ 0 & -1/\epsilon \end{bmatrix}$$

lebegőpontos aritmetikában. De akkor

$$\bm{L}\bm{U} = \begin{bmatrix} 1 & 0 \\ 1/\epsilon & 1 \end{bmatrix} \begin{bmatrix} \epsilon & 1 \\ 0 & -1/\epsilon \end{bmatrix} = \begin{bmatrix} \epsilon & 1 \\ 1 & 0 \end{bmatrix} \neq \bm{A}.$$

Egy kis főelem és az ennek megfelelő nagy szorzótényező használata a transzformált mátrixban helyrehozhatatlan információvesztést okozott. Ha viszont felcseréljük a sorokat, akkor a főelem 1, és a kapott szorzótényező $-\epsilon$, így az eliminációs mátrix

$$\boldsymbol{M} = \begin{bmatrix} 1 & 0 \\ -\epsilon & 1 \end{bmatrix},$$

és ennélfogva

$$\bm{L} = \begin{bmatrix} 1 & 0 \\ \epsilon & 1 \end{bmatrix} \quad \text{és} \quad \bm{U} = \begin{bmatrix} 1 & 1 \\ 0 & 1 - \epsilon \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

lebegőpontos aritmetikában. Így

$$\boldsymbol{L}\boldsymbol{U} = \begin{bmatrix} 1 & 0 \\ \epsilon & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ \epsilon & 1 \end{bmatrix},$$

ami a permutálás utáni helyes eredmény.

Bár az előbbi példa meglehetősen szélsőséges, az elv általánosan érvényes: a nagyobb főelemek kisebb szorzótényezőkhöz, és így kisebb hibákhoz vezetnek. Különösen, ha minden oszlopban az átlón vagy az alatt található legnagyobb elemet használjuk főelemnek — mint a 2.4. Algoritmusban —, akkor a szorzótényezők nagysága 1-gyel felülről korlátozott. A részleges főelemkiválasztás által megkövetelt sorcserék némileg bonyolultabbá teszik az LU-felbontás korábban megadott formális leírását. Konkrétan minden $M_k$ elemi eliminációs mátrix előtt egy $P_k$ permutációs mátrix áll, amely sorcserékkel a $k$-adik oszlop átlón vagy alatt található legnagyobb abszolút értékű elemét az átlós főelempozícióba hozza. Továbbra is $MA = U$, ahol $U$ felső háromszögű, de most

$$\boldsymbol{M} = \boldsymbol{M}_{n-1} \boldsymbol{P}_{n-1} \cdots \boldsymbol{M}_1 \boldsymbol{P}_1.$$

$M^{-1}$ továbbra is háromszögalakú a korábban definiált általános értelemben, de a permutációk miatt $M^{-1}$ nem szükségképpen alsó háromszögű, bár továbbra is $L$-lel jelöljük. Így az „LU"-felbontás szó szerint már nem „alsó szorozva felső" háromszögmátrixot jelent, de a lineáris rendszerek egymás utáni helyettesítéssel való megoldására ugyanolyan hasznos.

**2.4. Algoritmus. LU-felbontás Gauss-kiküszöböléssel részleges főelemkiválasztással.**

```
for k = 1 to n − 1                           { ciklus az oszlopokra }
    Find index p such that                   { főelem keresése az
        |apk| ≥ |aik| for k ≤ i ≤ n              aktuális oszlopban }
    if p ≠ k then                            { sorok cseréje,
        interchange rows k and p                 ha szükséges }
    if akk = 0 then                          { az aktuális oszlop átugrása,
        continue with next k                     ha már eleve nulla }
    for i = k + 1 to n                       { szorzótényezők kiszámítása
        mik = aik/akk                            az aktuális oszlopra }
    end
    for j = k + 1 to n                       { transzformáció alkalmazása
        for i = k + 1 to n                       a maradék részmátrixra }
            aij = aij − mik akj
        end
    end
end
```

Megjegyezzük, hogy a

$$P = P_{n-1} \cdots P_1$$

permutációs mátrix a részleges főelemkiválasztás által meghatározott sorrendbe rendezi $A$ sorait. Egy másik értelmezés szerint tehát a részleges főelemkiválasztásra úgy is tekinthetünk, mint egy olyan sorrend meghatározásának módjára, amelyben a numerikus stabilitás érdekében nem volna szükség semmilyen cserére (persze egy ilyen sorrendet előre meghatározni nem lehet). Így a

$$PA = LU$$

felbontást kapjuk, ahol most $L$ valóban alsó háromszögmátrix. Az $Ax = b$ lineáris rendszer megoldásához először az $Ly = Pb$ alsó háromszögű rendszert előrehelyettesítéssel, majd az $Ux = y$ felső háromszögű rendszert visszahelyettesítéssel oldjuk meg.

**2.16. Példa. Gauss-kiküszöbölés részleges főelemkiválasztással.** A 2.13. Példában nem használtunk sorcseréket, és néhány szorzótényező nagysága meghaladta az 1-et. Most illusztráció kedvéért megismételjük ezt a példát, ezúttal részleges főelemkiválasztást alkalmazva. A 2.13. Példa rendszere

$$\bm{A}\bm{x} = \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 \\ 6 \\ 10 \end{bmatrix} = \bm{b}.$$

Az első oszlop legnagyobb eleme 4, ezért felcseréljük az első két sort a

$$\mathbf{P}_1 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

permutációs mátrixszal, így a permutált rendszer

$$\boldsymbol{P}_{1}\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} 4 & 4 & 2 \\ 1 & 2 & 2 \\ 4 & 6 & 4 \end{bmatrix} \begin{bmatrix} x_{1} \\ x_{2} \\ x_{3} \end{bmatrix} = \begin{bmatrix} 6 \\ 3 \\ 10 \end{bmatrix} = \boldsymbol{P}_{1}\boldsymbol{b}.$$

Az első oszlop főátló alatti elemeinek annullálásához a

$$\mathbf{M}_1 = \begin{bmatrix} 1 & 0 & 0 \\ -0{,}25 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix}$$

eliminációs mátrixot használjuk, így a transzformált rendszer

$$\bm{M}_1\bm{P}_1\bm{A}\bm{x} = \begin{bmatrix} 4 & 4 & 2 \\ 0 & 1 & 1{,}5 \\ 0 & 2 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 6 \\ 1{,}5 \\ 4 \end{bmatrix} = \bm{M}_1\bm{P}_1\bm{b}.$$

A második oszlopban az átlón vagy az alatt található legnagyobb elem 2, ezért felcseréljük az utolsó két sort a

$$P_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$

permutációs mátrixszal, így a permutált rendszer

$$P_2 M_1 P_1 A x = \begin{bmatrix} 4 & 4 & 2 \\ 0 & 2 & 2 \\ 0 & 1 & 1{,}5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \\ 1{,}5 \end{bmatrix} = P_2 M_1 P_1 b.$$

A második oszlop főátló alatti elemének annullálásához a

$$\mathbf{M}_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -0{,}5 & 1 \end{bmatrix}$$

eliminációs mátrixot használjuk, így a transzformált rendszer

$$\bm{M}_2\bm{P}_2\bm{M}_1\bm{P}_1\bm{A}\bm{x} = \begin{bmatrix} 4 & 4 & 2 \\ 0 & 2 & 2 \\ 0 & 0 & 0{,}5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \\ -0{,}5 \end{bmatrix} = \bm{M}_2\bm{P}_2\bm{M}_1\bm{P}_1\bm{b}.$$

Ezzel az eredeti rendszert egy ekvivalens felső háromszögű rendszerre redukáltuk, amelyet most visszahelyettesítéssel oldhatunk meg, és ugyanazt a megoldást kapjuk, mint korábban: $x = \begin{bmatrix} -1 & 3 & -1 \end{bmatrix}^T$.

Az LU-felbontás explicit felírásához

$$L = M^{-1} = (M_2 P_2 M_1 P_1)^{-1} = P_1^T L_1 P_2^T L_2 =$$

$$\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0{,}25 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0{,}5 & 1 \end{bmatrix} = \begin{bmatrix} 0{,}25 & 0{,}5 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 0 \end{bmatrix},$$

és ennélfogva

$$\mathbf{A} = \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} = \begin{bmatrix} 0{,}25 & 0{,}5 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 0 \end{bmatrix} \begin{bmatrix} 4 & 4 & 2 \\ 0 & 2 & 2 \\ 0 & 0 & 0{,}5 \end{bmatrix} = \mathbf{L}\mathbf{U}.$$

Vegyük észre, hogy $L$ nem alsó háromszögű, de az általánosabb értelemben háromszögű (egy alsó háromszögmátrix permutációja). Alternatívaként választhatjuk a

$$\bm{P} = \bm{P}_2 \bm{P}_1 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix},$$

és

$$\boldsymbol{L} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0{,}25 & 0{,}5 & 1 \end{bmatrix}$$

megválasztást, így

$$\boldsymbol{P}\boldsymbol{A} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0{,}25 & 0{,}5 & 1 \end{bmatrix} \begin{bmatrix} 4 & 4 & 2 \\ 0 & 2 & 2 \\ 0 & 0 & 0{,}5 \end{bmatrix} = \boldsymbol{L}\boldsymbol{U},$$

ahol most $L$ valóban alsó háromszögmátrix, de $A$ permutálva van.

A „részleges" főelemkiválasztás elnevezés abból a tényből ered, hogy csak az aktuális oszlopban keresünk alkalmas főelemet. Egy kimerítőbb főelemkiválasztási stratégia a *teljes főelemkiválasztás*, amelyben a teljes maradék, redukálatlan részmátrixban keressük a legnagyobb elemet, majd azt permutáljuk az átlós főelempozícióba. Vegyük észre, hogy ez a sorok cseréje mellett az oszlopok cseréjét is igényli, és ezért a

$$PAQ = LU$$

alakú felbontáshoz vezet, ahol $L$ egységnyi átlójú alsó háromszögmátrix, $U$ felső háromszögmátrix, $P$ és $Q$ pedig permutációs mátrixok, amelyek rendre $A$ sorait és oszlopait rendezik át. Az $Ax = b$ lineáris rendszer megoldásához először az $Ly = Pb$ alsó háromszögű rendszert előrehelyettesítéssel, majd az $Uz = y$ felső háromszögű rendszert visszahelyettesítéssel oldjuk meg, végül pedig a megoldás komponenseit permutáljuk, hogy megkapjuk $x = Qz$-t. Bár a teljes főelemkiválasztás numerikus stabilitása elméletben jobb, sokkal költségesebb főelem-keresést igényel, mint a részleges főelemkiválasztás. Mivel a részleges főelemkiválasztás numerikus stabilitása a gyakorlatban bőven elegendő, általános lineáris rendszerek Gauss-kiküszöböléssel történő megoldásában szinte univerzálisan ezt használják.

A főelem kiválasztása az egyes mátrixelemek nagyságától függ, így a konkrét választás nyilvánvalóan függ a mátrix skálázásától. A mátrix diagonális skálázása (emlékezzünk a 2.10. Példára) eltérő főelem-sorrendhez vezethet. Például egy adott oszlop bármelyik nemnulla eleme a legnagyobbá tehető abszolút értékben, ha az adott sornak kellően nagy súlyt adunk. Ez azonban nem jelenti azt, hogy tetszőleges főelem-sorrend elfogadható: egy rosszul eltorzított skálázás rosszul kondicionált rendszerhez és ennek megfelelően pontatlan megoldáshoz vezethet (lásd a 2.20. Példát). Egy jól megfogalmazott feladatban az ismeretlen változók mérésére megfelelően arányos mértékegységeket kell használni (oszloponkénti skálázás), és az egyes egyenleteknek a viszonylagos fontosságukat helyesen tükröző súlyozást kell kapniuk (sorkénti skálázás). Figyelembe kell venni a bemeneti adatok viszonylagos pontosságát is. Ezek között a körülmények között a főelemkiválasztási eljárás általában olyan megoldást produkál, amely annyira pontos, amennyire a feladat indokolja (lásd a 2.3.4. szakaszt).

A 2.3.5. szakaszban láttuk, hogy egy kiszámított megoldás relatív maradéka kielégíti a

$$\frac{\|\boldsymbol{r}\|}{\|\boldsymbol{A}\|\cdot\|\hat{\boldsymbol{x}}\|} \leq \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|}$$

egyenlőtlenséget, ahol $E$ az $A$ mátrixhoz tartozó hátraható hiba. De mekkora is $\|E\|$ valójában a gyakorlatban? Wilkinson [499] megmutatta, hogy a Gauss-kiküszöböléssel végzett LU-felbontás esetén

$$\frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|} \le \rho \; n^2 \; \epsilon_{\text{mach}}$$

alakú korlát érvényes, ahol $\rho$ — amelyet *növekedési tényezőnek* nevezünk — $U$ legnagyobb abszolút értékű elemének és $A$ legnagyobb abszolút értékű elemének hányadosa (technikailag a növekedési tényező a felbontási folyamat *bármely* lépésében előállított legnagyobb elemtől függ, de ez rendszerint az utolsó, azaz $U$). Főelemkiválasztás nélkül $\rho$ tetszőlegesen nagy lehet, és ezért a főelemkiválasztás nélküli Gauss-kiküszöbölés instabil, amint azt már láttuk. Részleges főelemkiválasztás mellett a növekedési tényező legrosszabb esetben elérheti a $2^{n-1}$-t (mivel legrosszabb esetben az elemek mérete az elimináció minden lépésében megduplázódhat), de az ilyen viselkedés rendkívül ritka. A gyakorlatban kicsi vagy egyáltalán nincs növekedés, és egy realisztikus korlátot a

$$\frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|} \lessapprox n \ \epsilon_{\mathrm{mach}}$$

reláció ad. Ez a reláció azt jelenti, hogy egy lineáris rendszernek részleges főelemkiválasztásos Gauss-kiküszöböléssel, majd visszahelyettesítéssel való megoldása szinte mindig nagyon kicsi relatív maradékot eredményez, függetlenül attól, mennyire rosszul kondicionált a rendszer. Így egy kicsi relatív maradék önmagában nem feltétlenül jelenti, hogy a kiszámított megoldás pontos, hacsak a rendszer nem jól kondicionált. A teljes főelemkiválasztás még kisebb növekedési tényezőt eredményez, mind elméletben, mind a gyakorlatban, de az általa nyújtott további stabilitási tartalék rendszerint nem éri meg az extra költséget.

**2.17. Példa. Kis maradék.** Tekintsük a

$$\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} 0{,}913 & 0{,}659 \\ 0{,}457 & 0{,}330 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0{,}254 \\ 0{,}127 \end{bmatrix} = \boldsymbol{b}$$

lineáris rendszert a 2.8. Példából. Négyjegyű decimális aritmetika használatával a Gauss-kiküszöbölés a

$$\begin{bmatrix} 0{,}9130 & 0{,}6590 \\ 0 & 0{,}0002 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0{,}2540 \\ -0{,}0001 \end{bmatrix}$$

háromszögű rendszert adja, majd a visszahelyettesítés az

$$\hat{\boldsymbol{x}} = \begin{bmatrix} 0{,}6391 \\ -0{,}5 \end{bmatrix}$$

kiszámított megoldást szolgáltatja. Amint a 2.8. Példában láttuk, ennek a megoldásnak a maradéknormája $\|\boldsymbol{r}\|_1 = 7{,}04 \times 10^{-5}$, ami olyan kicsi, amilyenre négyjegyű aritmetikával számíthatunk. Mégis a rendszer pontos megoldása könnyen ellenőrizhetően $\boldsymbol{x} = [1, -1]^T$, így a hiba ugyanakkora, mint a megoldás. Ennek a jelenségnek az oka az, hogy az $\boldsymbol{A}$ mátrix közel szinguláris: amint a 2.7. Példában láttuk, kondíciószáma nagyobb, mint $10^4$. Az $x_2$-t meghatározó osztás két olyan mennyiség között történik, amelyek mindegyike a kerekítési hiba nagyságrendjébe esik (négyjegyű aritmetikában), és ezért az eredmény lényegében tetszőleges. Mégis, konstrukció szerint, amikor ezt az $x_2$-re vonatkozó tetszőleges értéket ezután behelyettesítjük az első egyenletbe, egy olyan $x_1$ érték adódik, amelyre az első egyenlet teljesül. Így kicsi maradékot, de rossz megoldást kapunk.

Amint az imént láttuk, a Gauss-kiküszöbölés stabilitásához általában szükség van a főelemkiválasztásra. Vannak azonban olyan mátrixosztályok, amelyekre a Gauss-kiküszöbölés főelemkiválasztás nélkül is stabil. Például ha az $\boldsymbol{A}$ mátrix *oszloponként diagonálisan domináns*, ami azt jelenti, hogy minden átlóbeli elem abszolút értéke nagyobb, mint az oszlopa többi eleme abszolút értékeinek összege,

$$\sum_{i=1, i \neq j}^{n} |a_{ij}| < |a_{jj}|, \quad j = 1, \dots, n,$$

akkor az LU-felbontás Gauss-kiküszöböléssel történő kiszámításához nincs szükség főelemkiválasztásra. Ha ilyen mátrixra részleges főelemkiválasztást alkalmazunk, akkor ténylegesen nem történik sorcsere. Egy másik fontos osztály, amelyre nincs szükség főelemkiválasztásra, a szimmetrikus és pozitív definit mátrixok, amelyeket a 2.5. szakaszban fogunk definiálni. A felesleges főelem-keresések elkerülése jelentős időmegtakarítást jelenthet a felbontás kiszámításában.

### 2.4.6 A Gauss-kiküszöbölés megvalósítása

A Gauss-kiküszöbölés, azaz az LU-felbontás, általános alakja egy háromszorosan egymásba ágyazott ciklus, amint azt a 2.5. Algoritmus sematikusan mutatja. A `for` ciklusok $i$, $j$ és $k$ indexeit tetszőleges sorrendben használhatjuk, így a ciklusok összesen $3! = 6$-féleképpen rendezhetők el. Néhány jelzett aritmetikai művelet nagyobb hatékonyság érdekében kivihető a legbelső ciklusból (mint például a 2.3. Algoritmusban), és a műveletek olyan további átrendezései is lehetségesek, amelyek esetleg nem szigorúan egymásba ágyazott ciklusokat eredményeznek. Az alapalgoritmus ezen változatainak eltérő hozzáférési mintáik (például sorkénti vagy oszloponkénti) vannak, és eltérőek abban, mennyire képesek kihasználni egy adott számítógép architekturális jellemzőit (például gyorsítótár, lapozás, vektorizáció, több processzor). Így teljesítményük adott számítógépen vagy különböző számítógépeken nagyon eltérő lehet, és nincs olyan egyetlen elrendezés, amely egyöntetűen felsőbbrendű volna.

**2.5. Algoritmus. Általános Gauss-kiküszöbölés.**

```
for ______

    for ______

        for ______

            aij = aij − (aik/akk) akj
        end
    end
end
```

Számos megvalósítási részlet ehhez hasonló módon változó lehet. Például az általunk leírt részleges főelemkiválasztási eljárás oszlopok mentén keres és sorokat cserél, de alternatívaként keresni lehetne sorok mentén és oszlopokat cserélni. Úgy is vettük, hogy $\boldsymbol{L}$-nek egységnyi átlója van, de intézhetnénk úgy is, hogy $\boldsymbol{U}$-nak legyen egységnyi átlója. A Gauss-kiküszöbölés ezen változatai közül némelyiket olyan fontosnak tartják, hogy nevet is kaptak, mint például a Crout- és Doolittle-módszer.

Bár a Gauss-kiküszöbölés sokféle lehetséges változata drámai hatással lehet a teljesítményre, nemszinguláris $A$ mátrix esetén mind lényegében ugyanazt a felbontást produkálják. Ha a sorok főelem-kiválasztási sorrendje ugyanaz, akkor két LU-felbontás, $PA = LU = \hat{L}\hat{U}$, esetén ez a kifejezés azt jelenti, hogy $\hat{L}^{-1}L = \hat{U}U^{-1} = D$ egyszerre alsó és felső háromszögű, és ennélfogva diagonális. Ha mind $L$-ről, mind $\hat{L}$-ről feltesszük, hogy egységnyi átlójú alsó háromszögmátrix, akkor $D$ valójában az $I$ egységmátrix kell legyen, és így $L = \hat{L}$ és $U = \hat{U}$, vagyis a felbontás egyértelmű. E feltevés nélkül azonban még mindig következtethetünk arra, hogy az LU-felbontás a tényezők diagonális skálázása erejéig egyértelmű. Ezt az egyértelműséget az LDU-felbontás, $PA = LDU$, teszi explicitté, ahol $L$ egységnyi átlójú alsó háromszögmátrix, $U$ egységnyi átlójú felső háromszögmátrix, $D$ pedig diagonális.

A tárkezelés egy másik fontos megvalósítási kérdés. A tárgyalt számos mátrix — az $M_k$ elemi eliminációs mátrixok, azok $L_k$ inverzei és a $P_k$ permutációs mátrixok — csupán formálisan írja le a felbontási folyamatot. A gyakorlati megvalósításban nem képezzük őket explicit módon. A tárhely megtakarítása érdekében az $L$ és $U$ tényezők felülírják a bemeneti $A$ mátrix kezdeti tárterületét: a transzformált $U$ mátrix $A$ felső háromszögét (az átlót is beleértve) foglalja el, a szigorú alsó háromszögű $L$-t alkotó szorzótényezők pedig $A$ (most már nulla) szigorú alsó háromszögét. $L$ egységnyi átlóját nem kell tárolni.

Az adatmozgatás minimalizálása érdekében a főelemkiválasztás által megkövetelt sorcseréket rendszerint nem végezzük el ténylegesen. Ehelyett a sorok eredeti helyükön maradnak, és egy segéd egészértékű vektor nyilvántartja az új sorsorrendet. Megjegyzendő, hogy egyetlen ilyen vektor elegendő, mivel az összes csere nettó hatása még mindig csak az $1, \ldots, n$ egészek egy permutációja.

### 2.4.7 A lineáris egyenletrendszerek megoldásának komplexitása

Egy $n \times n$-es mátrix LU-felbontásának Gauss-kiküszöböléssel való kiszámítása körülbelül $n^3/3$ lebegőpontos szorzást és hasonló számú összeadást igényel. Az eredményül kapott háromszögű rendszer egyetlen jobb oldali vektorra való megoldása előre- és visszahelyettesítéssel körülbelül $n^2$ szorzást és hasonló számú összeadást igényel. Így ahogy a mátrix $n$ mérete nő, a lineáris rendszerek megoldásának költségében az LU-felbontás fázisa egyre dominánsabbá válik.

Egy lineáris rendszert a mátrix explicit invertálásával is megoldhatunk, úgy, hogy a megoldást $x = A^{-1}b$ adja. De $A^{-1}$ kiszámítása egyenértékű $n$ darab lineáris rendszer megoldásával: $A$ egy LU-felbontását, majd $n$ darab előre- és visszahelyettesítést igényel, egyet az egységmátrix minden oszlopára. A teljes műveletszám körülbelül $n^3$ szorzás és hasonló számú összeadás (kihasználva a jobb oldali vektorok nullait az előrehelyettesítésnél). Az explicit invertálás tehát háromszor költségesebb, mint az LU-felbontás.

Az azt követő $x = A^{-1}b$ mátrix-vektor szorzás, amellyel a lineáris rendszert megoldjuk, körülbelül $n^2$ szorzást és hasonló számú összeadást igényel, ami hasonló az előre- és visszahelyettesítés összköltségéhez. Így, még több jobb oldali vektor esetén is, a mátrixinverzió költségesebb, mint az LU-felbontás, ha lineáris rendszereket szeretnénk megoldani. Ezen felül az explicit invertálás pontatlanabb választ ad. Egyszerű példaként, ha a $3x = 18$ $1 \times 1$-es lineáris rendszert osztással oldjuk meg, akkor $x = 18/3 = 6$-ot kapunk, de az explicit invertálás $x = 3^{-1} \times 18 = 0{,}333 \times 18 = 5{,}99$-et adna háromjegyű aritmetikát használva. Ebben a kis példában az invertáláshoz egy plusz aritmetikai műveletre van szükség, és kevésbé pontos eredményt ad. Az invertálás ezen hátrányai csak súlyosbodnak, ahogy a rendszer mérete nő.

Az explicit mátrixinverzek kényelmes jelölésként gyakran előfordulnak különféle képletekben, de ez a gyakorlat nem jelenti azt, hogy egy ilyen képlet megvalósításához explicit inverzre volna szükség. Csupán megfelelő jobb oldallal — amely maga is lehet mátrix — egy lineáris rendszert kell megoldani. Így például egy $A^{-1}B$ alakú szorzatot $A$ LU-felbontásával, majd $B$ minden oszlopát használva elvégzett előre- és visszahelyettesítésekkel kell kiszámítani. A gyakorlatban rendkívül ritka, hogy tényleg explicit mátrixinverzre volna szükség, így amikor csak egy mátrixinverzet látsz egy képletben, mindig arra gondolj: „oldj meg egy rendszert", ne arra, hogy „invertálj egy mátrixot".

Egy másik lineáris rendszer megoldási módszer, amelyet kerülni kell, a Cramer-szabály, amelyben a megoldás minden komponensét determinánsok hányadosaként számítjuk ki. Bár elemi lineáris algebrai kurzusokon gyakran tanítják, ez a módszer nem triviális méretű teli mátrixok esetén csillagászatilag drága. A Cramer-szabály főként elméleti eszközként hasznos.

### 2.4.8 Gauss–Jordan-kiküszöbölés

A Gauss-kiküszöbölés mögötti motiváció az, hogy egy általános mátrixot háromszögalakra redukáljunk, mivel az így kapott lineáris rendszer könnyen megoldható. A diagonális lineáris rendszerek azonban még könnyebben megoldhatók, így a diagonális alak még kívánatosabb célnak tűnik. A *Gauss–Jordan-kiküszöbölés* a standard Gauss-kiküszöbölés olyan változata, amelyben a mátrixot nemcsak háromszög-, hanem diagonális alakra redukáljuk. A mátrixelemek kiküszöbölésére ugyanolyan jellegű sorkombinációkat használunk, mint a standard Gauss-kiküszöbölésben, de ezeket mind az átló alatti, mind az átló feletti elemek annullálására alkalmazzuk. Így egy adott $\boldsymbol{a}$ oszlopvektorra alkalmazott eliminációs mátrix alakja

$$\begin{bmatrix} 1 & \cdots & 0 & -m_1 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & 1 & -m_{k-1} & 0 & \cdots & 0 \\ 0 & \cdots & 0 & 1 & 0 & \cdots & 0 \\ 0 & \cdots & 0 & -m_{k+1} & 1 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & 0 & -m_n & 0 & \cdots & 1 \end{bmatrix} \begin{bmatrix} a_1 \\ \vdots \\ a_{k-1} \\ a_k \\ a_{k+1} \\ \vdots \\ a_n \end{bmatrix} = \begin{bmatrix} 0 \\ \vdots \\ 0 \\ a_k \\ 0 \\ \vdots \\ 0 \end{bmatrix},$$

ahol $m_i = a_i/a_k$, $i = 1, \dots, n$. Ez az eljárás körülbelül $n^3/2$ szorzást és hasonló számú összeadást igényel, ami 50 százalékkal drágább, mint a standard Gauss-kiküszöbölés.

A kiküszöbölési fázis során ugyanezeket a sorműveleteket alkalmazzuk a lineáris egyenletrendszer jobb oldali vektorára (vagy vektoraira) is. Ha egyszer a kiküszöbölési fázis befejeződött, és a mátrix diagonális alakba került, akkor a lineáris rendszer megoldásának komponensei egyszerűen úgy számíthatók ki, hogy a transzformált jobb oldal minden elemét a mátrix megfelelő átlóbeli elemével elosztjuk. Ez a számítás összesen csak $n$ osztást igényel, ami jelentősen olcsóbb, mint egy háromszögű rendszer megoldása, de nem elég a költségesebb kiküszöbölési fázis kompenzálására. A Gauss–Jordan-kiküszöbölésnek az a numerikus hátránya is megvan, hogy a szorzótényezők nagysága még főelemkiválasztás esetén is meghaladhatja az 1-et.

Nagyobb összköltsége ellenére bizonyos helyzetekben a Gauss–Jordan-kiküszöbölés előnyben részesíthető, mert végső megoldási fázisa rendkívül egyszerű. Például néha párhuzamos számítógépekre való megvalósításhoz ajánlják, mivel a felbontási fázis alatt egyenletes a munkaterhelés, és a megoldás minden komponense egyszerre számítható ki — nem pedig egyesével, ahogyan a közönséges visszahelyettesítésnél.

A Gauss–Jordan-kiküszöbölést néha egy mátrix inverzének explicit kiszámítására is használják, ha arra szükség van. Ha a jobb oldali mátrixot az $I$ egységmátrixra inicializáljuk, és az adott $A$ mátrixot Gauss–Jordan-kiküszöböléssel az egységmátrixra redukáljuk, akkor a transzformált jobb oldali mátrix $A$ inverze lesz. Az inverz kiszámításához a Gauss–Jordan-kiküszöbölés körülbelül ugyanannyi műveletet igényel, mint a Gauss-kiküszöböléssel végzett explicit invertálás, amelyet előre- és visszahelyettesítés követ.

**2.18. Példa. Gauss–Jordan-kiküszöbölés.** A Gauss–Jordan-kiküszöbölést annak használatával illusztráljuk, hogy kiszámítjuk a 2.13. Példa mátrixának inverzét. Az egyszerűség kedvéért a főelemkiválasztást kihagyjuk. Az $\boldsymbol{A}$ mátrixszal kezdünk, jobb oldalon az $\boldsymbol{I}$ egységmátrixszal bővítve, és ismételten eliminációs mátrixokat alkalmazunk $\boldsymbol{A}$ átlón kívüli elemeinek annullálására, amíg el nem érjük a diagonális alakot; majd a megmaradt átlóbeli elemekkel skálázva a bal oldalon az egységmátrixot, így a jobb oldalon az $A^{-1}$ inverz mátrixot állítjuk elő.

$$\begin{bmatrix} 1 & 0 & 0 \\ -4 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 2 & 1 & 0 & 0 \\ 4 & 4 & 2 & 0 & 1 & 0 \\ 4 & 6 & 4 & 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 & 1 & 0 & 0 \\ 0 & -4 & -6 & -4 & 1 & 0 \\ 0 & -2 & -4 & -4 & 0 & 1 \end{bmatrix},$$

$$\begin{bmatrix} 1 & 0{,}5 & 0 \\ 0 & 1 & 0 \\ 0 & -0{,}5 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 2 & 1 & 0 & 0 \\ 0 & -4 & -6 & -4 & 1 & 0 \\ 0 & -2 & -4 & -4 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & -1 & -1 & 0{,}5 & 0 \\ 0 & -4 & -6 & -4 & 1 & 0 \\ 0 & 0 & -1 & -2 & -0{,}5 & 1 \end{bmatrix},$$

$$\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -6 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -1 & -1 & 0{,}5 & 0 \\ 0 & -4 & -6 & -4 & 1 & 0 \\ 0 & 0 & -1 & -2 & -0{,}5 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 1 & 1 & -1 \\ 0 & -4 & 0 & 8 & 4 & -6 \\ 0 & 0 & -1 & -2 & -0{,}5 & 1 \end{bmatrix},$$

$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & -0{,}25 & 0 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & 1 & 1 & -1 \\ 0 & -4 & 0 & 8 & 4 & -6 \\ 0 & 0 & -1 & -2 & -0{,}5 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 1 & 1 & -1 \\ 0 & 1 & 0 & -2 & -1 & 1{,}5 \\ 0 & 0 & 1 & 2 & 0{,}5 & -1 \end{bmatrix},$$

így

$$A^{-1} = \begin{bmatrix} 1 & 1 & -1 \\ -2 & -1 & 1{,}5 \\ 2 & 0{,}5 & -1 \end{bmatrix}.$$

### 2.4.9 Módosított feladatok megoldása

Számos gyakorlati helyzetben a lineáris rendszerek nem elszigetelten fordulnak elő, hanem rokon feladatok olyan sorozatának részeként, amelyek valamilyen szisztematikus módon változnak. Előfordulhat például, hogy olyan $Ax = b$ lineáris rendszerek sorozatát kell megoldani, amelyeknek ugyanaz az $A$ mátrixuk, de eltérőek a $b$ jobb oldalaik. Az első rendszer Gauss-kiküszöböléssel való megoldása után a már kiszámított $L$ és $U$ tényezőket fel lehet használni a további rendszereknek előre- és visszahelyettesítéssel való megoldására. A felbontási fázist a későbbi lineáris rendszerek megoldása során nem kell megismételni, hacsak a mátrix nem változik. Ez az eljárás jelentős munkamegtakarítást jelent, mivel a további háromszögű megoldások költsége csupán $\mathcal{O}(n^2)$, ellentétben egy felbontás $\mathcal{O}(n^3)$ költségével.

Sőt: bizonyos fontos különleges esetekben még akkor is elkerülhető egy új felbontás, ha a mátrix változik. Ilyen, gyakran előforduló eset egy olyan $n \times n$-es mátrix hozzáadása vagy kivonása, amely két nemnulla $n$-dimenziós vektor, $\boldsymbol{u}$ és $\boldsymbol{v}$, $\boldsymbol{u}\boldsymbol{v}^T$ külső szorzata. Ezt *egyrangú módosításnak* nevezzük, mert az $\boldsymbol{u}\boldsymbol{v}^T$ külső szorzatmátrix rangja egy (azaz csak egy lineárisan független sora vagy oszlopa van), és bármely egyrangú mátrix kifejezhető két vektor ilyen külső szorzataként (lásd a 2.25. Feladatot). Például ha az $\boldsymbol{A}$ mátrix egyetlen eleme változik meg — például a $(j, k)$ elem $a_{jk}$-ról $\tilde{a}_{jk}$-ra —, akkor az új mátrix $\boldsymbol{A} - \alpha \boldsymbol{e}_j \boldsymbol{e}_k^T$, ahol $\boldsymbol{e}_j$ és $\boldsymbol{e}_k$ az egységmátrix megfelelő oszlopai, és $\alpha = a_{jk} - \tilde{a}_{jk}$.

A Sherman–Morrison-formula,

$$(A - uv^T)^{-1} = A^{-1} + A^{-1}u (1 - v^T A^{-1}u)^{-1} v^T A^{-1},$$

ahol $u$ és $v$ $n$-dimenziós vektorok, megadja egy olyan mátrix inverzét, amely egy olyan mátrix egyrangú módosításából származik, amelynek inverze már ismert; ez közvetlen szorzással könnyen igazolható (lásd a 2.27. Feladatot). Ennek a képletnek a kiértékelése csak $\mathcal{O}(n^2)$ munkát (mátrix-vektor szorzásokat) igényel, szemben a módosított mátrix nulláról való invertálásához szükséges $\mathcal{O}(n^3)$ munkával.

Az $(A - uv^T)x = b$ új mátrixú lineáris rendszerre a Sherman–Morrison-formula az

$$x = (A - uv^T)^{-1}b = A^{-1}b + A^{-1}u(1 - v^T A^{-1}u)^{-1} v^T A^{-1}b$$

megoldást adja, de kerüljük az explicit inverzeket. Ha van LU-felbontásunk az eredeti $A$ mátrixra, akkor a módosított rendszer megoldása a 2.6. Algoritmussal számítható, amely háromszögű rendszerek megoldását és vektorok belső szorzatának kiszámítását tartalmazza, így nem igényel explicit inverzet, és csak $\mathcal{O}(n^2)$ munkát igényel. Megjegyzendő, hogy az első lépés $b$-től független, és ezért nem kell megismételni, ha több $b$ jobb oldali vektor van.

**2.6. Algoritmus. Megoldás egyrangú frissítése.**

```
Oldjuk meg Az = u-t z-re, így z = A^{-1} u
Oldjuk meg Ay = b-t y-ra, így y = A^{-1} b
x = y + ((v^T y) / (1 - v^T z)) z
```

Hasonló technikákkal az inverz vagy a megoldás helyett a felbontást is frissíthetjük. Ezeknek a frissítési képleteknek a használatakor azonban óvatosnak kell lennünk, mert a mátrix változása során az egymást követő frissítésekben általánosságban nincs garancia a numerikus stabilitásra. A Woodbury-formula,

$$(A - UV^T)^{-1} = A^{-1} + A^{-1}U(I - V^T A^{-1} U)^{-1} V^T A^{-1},$$

ahol $U$ és $V$ $n \times k$-as mátrixok, általánosítja a Sherman–Morrison-formulát a mátrix egy $k$-rangú módosítására (lásd a 2.28. Feladatot).

**2.19. Példa. Megoldás egyrangú frissítése.** Az egyrangú frissítést a

$$\begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 4 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 \\ 6 \\ 10 \end{bmatrix}$$

lineáris rendszer megoldásán illusztráljuk, amely a 2.13. Példa rendszerének egyrangú módosítása, mivel csak az $A$ mátrix $(3, 2)$ eleme változott 6-ról 4-re. A frissítővektorok egyik választási lehetősége

$$\bm{u} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \quad \text{és} \quad \bm{v} = \begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix},$$

így a módosított rendszer mátrixa $A - uv^T =$

$$\begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \begin{bmatrix} 0 & 2 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 6 & 4 \end{bmatrix} - \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 2 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 \\ 4 & 4 & 2 \\ 4 & 4 & 4 \end{bmatrix},$$

a $b$ jobb oldali vektor pedig nem változott.

A 2.13. Példában korábban kiszámított LU-felbontást felhasználva megoldhatjuk $Az = u$-t, így $z = \begin{bmatrix} -1 & 1{,}5 & -1 \end{bmatrix}^T$, és $Ay = b$-t már megoldottuk, így $y = \begin{bmatrix} -1 & 3 & -1 \end{bmatrix}^T$. Az utolsó lépés ezek után a frissített megoldás kiszámítása:

$$\boldsymbol{x} = \boldsymbol{y} + \frac{\boldsymbol{v}^T \boldsymbol{y}}{1 - \boldsymbol{v}^T \boldsymbol{z}} \, \boldsymbol{z} = \begin{bmatrix} -1 \\ 3 \\ -1 \end{bmatrix} + \frac{6}{1 - 3} \begin{bmatrix} -1 \\ 1{,}5 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 \\ -1{,}5 \\ 2 \end{bmatrix}.$$

Így a módosított rendszer megoldását anélkül számítottuk ki, hogy a módosított mátrixot újra felbontottuk volna.

### 2.4.10 A pontosság javítása

Bár egy lineáris rendszer megoldásában várható pontosság látszólag kőbe vésett, bizonyos esetekben a pontosság javítható a rendszer átskálázásával vagy a kezdetben kiszámított megoldás iteratív javításával. Ezek az eszközök nem mindig vihetők véghez, de kipróbálásuk megérheti, különösen erősen rosszul kondicionált rendszerek esetén.

A 2.10. Példából emlékezhetünk rá, hogy egy lineáris rendszer diagonális skálázása vagy változatlanul hagyja a megoldást (sorkénti skálázás), vagy úgy változtatja meg, hogy a megoldás könnyen visszanyerhető (oszloponkénti skálázás). A gyakorlatban azonban a skálázás befolyásolja a rendszer kondicionáltságát és a Gauss-kiküszöbölésben a főelemek kiválasztását, amelyek mindegyike viszont a kiszámított megoldás pontosságát befolyásolja. Így egy lineáris rendszer sorkénti és oszloponkénti skálázása lehetőséget adhat a numerikus stabilitás és pontosság javítására (vagy rontására).

A pontosság rendszerint javul, ha a mátrix minden eleme körülbelül azonos nagyságrendű — vagy ami még jobb, ha a mátrixelemekben lévő bizonytalanságok is körülbelül azonos méretűek. Néha puszta ránézésre is nyilvánvaló, hogyan skálázzuk a mátrixot úgy, hogy ilyen egyensúly álljon elő: az egyes változókhoz tartozó mértékegységek megválasztásával és az egyes egyenleteknek a viszonylagos fontosságuk és bizonytalanságuk szerinti súlyozásával. Olyan általános, automatikus technikát azonban még soha nem fejlesztettek ki, amely hatékony és megbízható módon optimális skálázást eredményezne. Ráadásul maga a skálázási folyamat is bevezethet kerekítési hibákat, hacsak nem vigyázunk (például ha csak az aritmetikai alap hatványait használjuk skálázási tényezőként).

**2.20. Példa. Rossz skálázás.** Egyszerű példaként az

$$\begin{bmatrix} 1 & 0 \\ 0 & \epsilon \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 \\ \epsilon \end{bmatrix}$$

lineáris rendszer kondíciószáma $1/\epsilon$, és ezért nagyon rosszul kondicionált, ha $\epsilon$ nagyon kicsi. Ez a rossz kondicionáltság azt jelenti, hogy a bemeneti adatok kis perturbációi viszonylag nagy változásokat okozhatnak a megoldásban. Például ha a jobb oldalt a $\begin{bmatrix} 0 & -\epsilon \end{bmatrix}^T$ vektorral perturbáljuk, a megoldás $\begin{bmatrix} 1 & 1 \end{bmatrix}^T$-ról $\begin{bmatrix} 1 & 0 \end{bmatrix}^T$-ra változik. Ha viszont a második sort előbb $1/\epsilon$-nal szorozzuk, akkor a rendszer tökéletesen jól kondicionálttá válik, és ugyanaz a perturbáció most a megoldásban ezzel arányos kis változást eredményez. Így a látszólagos rossz kondicionáltság pusztán a rossz skálázásnak volt köszönhető. Sajnos az, hogy általános mátrixok esetén hogyan korrigáljuk a rossz skálázást, sokkal kevésbé kézenfekvő.

Az *iteratív finomítás* egy másik eszköz, amellyel egy kiszámított megoldás pontossága esetleg javítható. Tegyük fel, hogy az $Ax = b$ lineáris rendszerre kiszámítottunk egy közelítő $x_0$ megoldást — például valamilyen LU-felbontási alakkal —, és kiszámítjuk a

$$\boldsymbol{r}_0 = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}_0$$

maradékot. Természetesen azt szeretnénk, ha a maradék megfelelően kicsi volna, ha viszont nem az, akkor a korábban kiszámított LU-tényezőkkel megoldhatjuk az

$$As_0 = r_0$$

lineáris rendszert $s_0$-ra, és az

$$\boldsymbol{x}_1 = \boldsymbol{x}_0 + \boldsymbol{s}_0$$

értéket vesszük új, „jobb" közelítő megoldásnak, mivel

$$Ax_1 = A(x_0 + s_0) = Ax_0 + As_0 = (b - r_0) + r_0 = b.$$

Ez az eljárás ismételhető a megoldás egymás utáni finomítására, konvergenciáig, esetleg olyan megoldást előállítva, amelynek maradéka olyan kicsi, amennyire az alkalmazott aritmetikai pontosságon csak lehet.

Sajnos az iteratív finomítás dupla tárhelyet igényel, mivel mind az eredeti mátrixra, mind annak LU-felbontására szükség van (rendre a maradék kiszámításához és a későbbi rendszerek megoldásához). Ráadásul ahhoz, hogy az iteratív finomítás maximális haszonnal járjon, a maradékot rendszerint a kezdeti megoldás kiszámításához használt pontosságnál nagyobb pontossággal kell kiszámítani (emlékezzünk az 1.17. Példára).

Ezen okok miatt az iteratív finomítás gyakran nem praktikus rutinszerű használatra, bizonyos körülmények között azonban mégis hasznos lehet. Az iteratív finomítással például visszanyerhető a teljes pontosság a rosszul skálázott rendszerek esetén, és olykor stabilizálhatók vele az egyébként potenciálisan instabil megoldási módszerek. Ironikus módon, ha a kezdeti megoldás viszonylag rossz, akkor a maradék elegendően nagy lehet ahhoz, hogy extra pontosság nélkül is kielégítő pontossággal legyen kiszámítható. Az iteratív finomításra a 11.7. Példában térünk vissza.
