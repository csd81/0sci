## 2.8 Történeti jegyzetek és további olvasnivaló

Gauss 1810-ben fogalmazta meg a kiküszöbölési módszerét, de nem egy mátrix felbontásaként, hanem egy kvadratikus alak egyszerűsítéseként írta le. A mátrixokat ugyanis csak 1855-ben vezette be Cayley, és a Gauss-kiküszöbölés mátrixfelbontásként való értelmezését csak az 1940-es években ismerte fel Dwyer, von Neumann és mások (lásd [431]). A digitális számítások korai úttörőit — például von Neumannt [487] és Turingot [471] (a mátrix kondíciószámának fogalma Turingtól származik) — súlyosan aggasztotta, hogy a nagy lineáris rendszerek Gauss-kiküszöböléssel történő megoldásakor felhalmozódó kerekítési hiba használhatatlanná teszi-e az eredményeket, és kezdetben jelentős pesszimizmus övezte ezt a kérdést. A számítási tapasztalatok hamarosan megmutatták azonban, hogy a módszer a gyakorlatban meglepően stabil és pontos, és a hibaelemzések végül követték a tapasztalatot, hogy magyarázatot adjanak erre a szerencsére (lásd különösen Wilkinson munkáit [499, 500, 501]).

Mint kiderült, a részleges főelemkiválasztással végzett Gauss-kiküszöbölés műveletszáma rosszabb az optimálisnál [444], a legrosszabb esetben instabil [499], és elméleti értelemben nem valósítható meg hatékonyan párhuzamosan [485]. Mégis a gyakorlatban — még párhuzamos számítógépeken is — következetesen eredményes, és a tudományos számítások egyik fő igáslova. A legtöbb numerikus algoritmus Murphy törvényének engedelmeskedik — „ha valami elromolhat, el is romlik" —, ám úgy tűnik, a Gauss-kiküszöbölés boldog kivétel. E figyelemre méltó algoritmus egyes „rejtélyeinek" további tárgyalásához lásd [461, 467]-et; „számítási ellenpéldákhoz" lásd [156, 510]-et.

A lineáris algebra hátteréhez az olvasó Strang kiváló tankönyveit [436, 441] veheti kézbe. Haladóbb mátrixelmélethez lásd [241, 242]-t. További példák, feladatok és a számítási lineáris algebra gyakorlati alkalmazásai megtalálhatók [238, 276, 314]-ben. A mátrixszámítások enciklopédikus referenciája [198]; tankönyvi tárgyalások közé tartoznak [40, 96, 104, 185, 220, 257, 426, 430, 466, 493, 496]. A lineáris rendszerek megoldásának egyik nagy hatású korai műve — és az elsők egyike, amely magas színvonalú szoftvert is tartalmaz — a [153]. A mátrixszámítások hasznos, Fortran és MATLAB nyelvű gyakorlati kézikönyve a [82].

A lineáris rendszerek és a lineáris algebra számos egyéb feladatának hibaelemzéséről és perturbációelméletéről szóló átfogó tárgyaláshoz lásd [237, 433]-at. A kondíciószám-becslésről áttekintést ad [235]. A lineáris algebrában a (normaszerű helyett) komponensenkénti perturbációelmélet részletes áttekintését adja [236]. A LINPACK és a LAPACK dokumentációja [116], illetve [9]. A BLAS (Basic Linear Algebra Subprograms) könyvtárról lásd [114, 115, 300]-at. A számítási környezetnek a Gauss-kiküszöbölés és más mátrixszámítások teljesítményére gyakorolt hatását vizsgáló egyik legkorábbi cikk [330] volt. Az erről a mára igen terjedelmessé vált témáról egy ízelítőhöz lásd [105, 117, 118, 357]-et.

### Áttekintő kérdések

- **2.1.** Igaz vagy hamis: Ha egy $A$ mátrix nemszinguláris, akkor az $Ax = b$ lineáris egyenletrendszer megoldásainak száma a $b$ jobb oldali vektor konkrét választásától függ.
- **2.2.** Igaz vagy hamis: Ha egy mátrix determinánsa nagyon kicsi, akkor a mátrix majdnem szinguláris.
- **2.3.** Igaz vagy hamis: Szimmetrikus $A$ mátrixra mindig $\|A\|_1 = \|A\|_\infty$.
- **2.4.** Igaz vagy hamis: Ha egy háromszögmátrixnak van nullával egyenlő eleme a főátlóban, akkor a mátrix szükségképpen szinguláris.
- **2.5.** Igaz vagy hamis: Ha egy tetszőleges mátrixnak van nullával egyenlő eleme a főátlóban, akkor a mátrix szükségképpen szinguláris.
- **2.6.** Igaz vagy hamis: Egy alulhatározott $Ax = b$ lineáris egyenletrendszernek, ahol $A$ egy $m \times n$-es mátrix $m < n$-nel, mindig van megoldása.
- **2.7.** Igaz vagy hamis: Két felső háromszögmátrix szorzata felső háromszögmátrix.
- **2.8.** Igaz vagy hamis: Két szimmetrikus mátrix szorzata szimmetrikus.
- **2.9.** Igaz vagy hamis: Egy nemszinguláris felső háromszögmátrix inverze felső háromszögmátrix.
- **2.10.** Igaz vagy hamis: Ha egy $n \times n$-es $A$ mátrix sorai lineárisan összefüggők, akkor az oszlopai is lineárisan összefüggők.
- **2.11.** Igaz vagy hamis: Az $Ax = b$ lineáris egyenletrendszernek akkor és csak akkor van megoldása, ha az $m \times n$-es $A$ mátrix és az $m \times (n+1)$-es $[\,A\ b\,]$ kibővített mátrix rangja azonos.
- **2.12.** Igaz vagy hamis: Ha $A$ tetszőleges $n \times n$-es mátrix és $P$ tetszőleges $n \times n$-es permutációs mátrix, akkor $PA = AP$.
- **2.13.** Igaz vagy hamis: Ha sorcserék megengedettek, akkor az LU-felbontás mindig létezik, még szinguláris $A$ mátrixra is.
- **2.14.** Igaz vagy hamis: Ha egy lineáris rendszer jól kondicionált, akkor a Gauss-kiküszöbölésben nincs szükség főelemkiválasztásra.
- **2.15.** Igaz vagy hamis: Ha egy mátrix szinguláris, akkor nem lehet LU-felbontása.
- **2.16.** Igaz vagy hamis: Ha egy nemszinguláris szimmetrikus mátrix nem pozitív definit, akkor nem lehet Cholesky-felbontása.
- **2.17.** Igaz vagy hamis: Egy szimmetrikus pozitív definit mátrix mindig jól kondicionált.
- **2.18.** Igaz vagy hamis: A főelemkiválasztás nélküli Gauss-kiküszöbölés csak akkor hiúsul meg, ha a mátrix rosszul kondicionált vagy szinguláris.
- **2.19.** Igaz vagy hamis: Ha egy mátrix LU-felbontását már kiszámítottuk egy lineáris rendszer megoldásához, akkor az ugyanazzal a mátrixszal, de eltérő jobb oldali vektorokkal adott további lineáris rendszerek a mátrix újrafelbontása nélkül megoldhatók.
- **2.20.** Igaz vagy hamis: LU-felbontáson és háromszögű megoldáson alapuló explicit mátrixinvertálásban a munka többségét a felbontás adja.
- **2.21.** Igaz vagy hamis: Ha $x$ tetszőleges $n$-dimenziós vektor, akkor $\|x\|_1 \ge \|x\|_\infty$.
- **2.22.** Igaz vagy hamis: Egy szinguláris mátrix normája nulla.
- **2.23.** Igaz vagy hamis: Ha $\|A\| = 0$, akkor $A = 0$.
- **2.24.** Igaz vagy hamis: $\|A\|_1 = \|A^T\|_\infty$.
- **2.25.** Igaz vagy hamis: Ha $A$ tetszőleges $n \times n$-es nemszinguláris mátrix, akkor $\operatorname{cond}(A) = \operatorname{cond}(A^{-1})$.
- **2.26.** Igaz vagy hamis: Nemszinguláris lineáris egyenletrendszer megoldásakor a részleges főelemkiválasztással végzett Gauss-kiküszöbölés általában kis maradékot ad, még ha a mátrix rosszul kondicionált is.
- **2.27.** Igaz vagy hamis: A részleges főelemkiválasztással végzett Gauss-kiküszöbölésben a szorzótényezők abszolút értékben $1$-gyel korlátosak, ezért az egymást követő redukált mátrixok elemei abszolút értékben nem növekedhetnek.
- **2.28.** Lehet-e egy $Ax = b$ lineáris egyenletrendszernek pontosan két különböző megoldása?
- **2.29.** Meghatározható-e egy $Ax = b$ lineáris rendszer megoldásainak száma valaha is pusztán az $A$ mátrixból, a $b$ jobb oldali vektor ismerete nélkül?
- **2.30.** Egy $Ax = b$ négyzetes lineáris egyenletrendszer megoldásakor melyik volna a súlyosabb nehézség: ha $A$ sorai lineárisan összefüggők, vagy ha $A$ oszlopai lineárisan összefüggők? Magyarázd meg.
- **2.31.** (a) Mondj ki egy definiáló tulajdonságot egy $A$ szinguláris mátrixra. (b) Tegyük fel, hogy az $Ax = b$ lineáris rendszernek két különböző $x$ és $y$ megoldása van. Az (a)-ban megadott tulajdonsággal bizonyítsd be, hogy $A$ szükségképpen szinguláris.
- **2.32.** Adott egy nemszinguláris $Ax = b$ lineáris egyenletrendszer. Az alábbi műveletek mindegyikének milyen hatása van az $x$ megoldásvektorra? (a) $[\,A\ b\,]$ sorainak permutálása; (b) $A$ oszlopainak permutálása; (c) az egyenlet mindkét oldalának balról való szorzása egy $M$ nemszinguláris mátrixszal.
- **2.33.** Tegyük fel, hogy egy $Ax = b$ lineáris egyenletrendszer mindkét oldalát megszorozzuk egy nem nulla $\alpha$ skalárral. (a) Megváltozik-e ettől a valódi $x$ megoldás? (b) Megváltozik-e ettől egy adott $x$-re az $r = b - Ax$ maradékvektor? (c) Milyen következtetés vonható le egy számított megoldás minőségének megítéléséről?
- **2.34.** Tegyük fel, hogy egy $Ax = b$ lineáris egyenletrendszer mindkét oldalát balról megszorozzuk egy nemszinguláris diagonális mátrixszal. (a) Megváltozik-e ettől a valódi $x$ megoldás? (b) Befolyásolhatja-e ez a rendszer kondicionáltságát? (c) Befolyásolhatja-e ez a Gauss-kiküszöbölésben a főelemek választását?
- **2.35.** Adj meg egy elemi eliminációs mátrixot, amely az alábbi vektor utolsó két komponensét nullává teszi:

$$\begin{bmatrix} 3 \\ 2 \\ -1 \\ 4 \end{bmatrix}.$$

- **2.36.** (a) Adj meg egy $4 \times 4$-es permutációs mátrixot, amely bármely $4$-dimenziós vektor 2. és 4. komponensét felcseréli. (b) Adj meg egy $4 \times 4$-es permutációs mátrixot, amely bármely $4$-dimenziós vektor komponenseinek sorrendjét megfordítja.
- **2.37.** Szinguláris mátrix és egzakt aritmetika használata esetén egy lineáris rendszer Gauss-kiküszöböléssel történő megoldásában hol fog a megoldási folyamat megakadni (a) részleges főelemkiválasztással? (b) főelemkiválasztás nélkül?
- **2.38.** (a) Mi a különbség a Gauss-kiküszöbölésben a részleges és a teljes főelemkiválasztás között? (b) Mondj a másikhoz képest egy-egy előnyt mindkét típusú főelemkiválasztásra.
- **2.39.** Tekintsük az alábbi $A$ mátrixot, amelynek LU-felbontását Gauss-kiküszöböléssel szeretnénk kiszámítani:

$$\boldsymbol{A} = \begin{bmatrix} 4 & -8 & 1 \\ 6 & 5 & 7 \\ 0 & -10 & -3 \end{bmatrix}.$$

Mi lesz a kezdeti főelem, ha (a) nem használunk főelemkiválasztást? (b) részleges főelemkiválasztást használunk? (c) teljes főelemkiválasztást használunk?

- **2.40.** Adj két okot arra, hogy a Gauss-kiküszöbölés numerikusan stabil megvalósításához miért lényeges a főelemkiválasztás.
- **2.41.** Ha $A$ egy rosszul kondicionált mátrix, és az LU-felbontását részleges főelemkiválasztással végzett Gauss-kiküszöböléssel számítjuk, azt várnád-e, hogy a rossz kondicionáltság $L$-ben, $U$-ban vagy mindkettőben tükröződik? Miért?
- **2.42.** (a) Mi az alábbi mátrix inverze?

$$\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & m_1 & 1 & 0 \\ 0 & m_2 & 0 & 1 \end{bmatrix}$$

(b) Hogyan merülhet fel egy ilyen mátrix a számítási gyakorlatban?

- **2.43.** (a) Felírható-e minden $n \times n$-es nemszinguláris $\boldsymbol{A}$ mátrix $\boldsymbol{A} = \boldsymbol{L}\boldsymbol{U}$ szorzat alakban, ahol $\boldsymbol{L}$ alsó háromszögmátrix és $\boldsymbol{U}$ felső háromszögmátrix? (b) Ha igen, milyen algoritmus valósítja ezt meg? Ha nem, adj ellenpéldát a szemléltetésre.
- **2.44.** Adott egy $n \times n$-es nemszinguláris $\boldsymbol{A}$ mátrix és egy további $n \times n$-es $\boldsymbol{B}$ mátrix. Mi a legjobb módja az $n \times n$-es $\boldsymbol{A}^{-1}\boldsymbol{B}$ mátrix kiszámításának?
- **2.45.** Ha $A$ és $B$ $n \times n$-es mátrixok, $A$ nemszinguláris, és $c$ egy $n$-dimenziós vektor, hogyan számítanád ki hatékonyan az $A^{-1}Bc$ szorzatot?
- **2.46.** Ha $A$ egy $n \times n$-es mátrix és $x$ egy $n$-dimenziós vektor, az alábbi számítások közül melyik igényel kevesebb munkát? Magyarázd meg. (a) $\boldsymbol{y} = (\boldsymbol{x}\,\boldsymbol{x}^T)\,\boldsymbol{A}$; (b) $\boldsymbol{y} = \boldsymbol{x}\,(\boldsymbol{x}^T\,\boldsymbol{A})$.
- **2.47.** Hogyan viszonyul egy $n \times n$-es háromszögű lineáris egyenletrendszer megoldásához szükséges számítási munka egy általános $n \times n$-es rendszer megoldásához szükségesével?
- **2.48.** Tegyük fel, hogy egy nemszinguláris $A$ mátrix $A = LU$ LU-felbontását már kiszámítottad. Hogyan használnád fel az $A^T x = b$ lineáris rendszer megoldásához?
- **2.49.** Ha $L$ egy nemszinguláris alsó háromszögmátrix, $P$ egy permutációs mátrix, és $b$ egy adott vektor, hogyan oldanád meg az alábbi lineáris rendszerek mindegyikét? (a) $LPx = b$; (b) $PLx = b$.
- **2.50.** Az $\mathbb{R}^2$ síkban lehetséges-e olyan $\boldsymbol{x} \neq \boldsymbol{0}$ vektor, amelyre $\|\boldsymbol{x}\|_1 = \|\boldsymbol{x}\|_\infty$? Ha igen, adj példát.
- **2.51.** Az $\mathbb{R}^2$ síkban lehetséges-e olyan $\boldsymbol{x}$ és $\boldsymbol{y}$ vektor, amelyekre $\|\boldsymbol{x}\|_1 > \|\boldsymbol{y}\|_1$, de $\|\boldsymbol{x}\|_\infty < \|\boldsymbol{y}\|_\infty$? Ha igen, adj példát.
- **2.52.** Általában melyik mátrixnormát könnyebb kiszámítani, $\|A\|_1$-et vagy $\|A\|_2$-t? Miért?
- **2.53.** (a) Egy mátrix determinánsának nagysága jó mutatója-e annak, hogy a mátrix majdnem szinguláris-e? (b) Ha igen, miért? Ha nem, mi a közelszingularitás jobb mutatója?
- **2.54.** (a) Hogyan definiáljuk egy $A$ mátrix kondíciószámát egy adott mátrixnormára? (b) Hogyan használjuk a kondíciószámot az $Ax = b$ lineáris rendszer számított megoldásának pontosságbecslésére?
- **2.55.** Miért nem triviális feladat egy általános mátrix kondíciószámának kiszámítása?
- **2.56.** Adj példát egy $3 \times 3$-as $A$ mátrixra — az egységmátrixtól különbözőre —, amelyre $\operatorname{cond}(A) = 1$.
- **2.57.** (a) Mi az alábbi mátrix kondíciószáma az $1$-normát használva?

$$\begin{bmatrix} 4 & 0 & 0 \\ 0 & -6 & 0 \\ 0 & 0 & 2 \end{bmatrix}$$

(b) Eltér-e a válaszod, ha a $\infty$-normát használjuk?

- **2.58.** Tegyük fel, hogy az $n \times n$-es $A$ mátrix tökéletesen jól kondicionált, azaz $\operatorname{cond}(A) = 1$. Az alábbi mátrixok közül melyek szükségképpen szintén ezzel a tulajdonsággal rendelkeznek? (a) $c\boldsymbol{A}$, ahol $c$ tetszőleges nem nulla skalár; (b) $\boldsymbol{D}\boldsymbol{A}$, ahol $\boldsymbol{D}$ egy nemszinguláris diagonális mátrix; (c) $PA$, ahol $P$ tetszőleges permutációs mátrix; (d) $\boldsymbol{B}\boldsymbol{A}$, ahol $\boldsymbol{B}$ tetszőleges nemszinguláris mátrix; (e) $A^{-1}$, azaz $A$ inverze; (f) $\boldsymbol{A}^T$, azaz $\boldsymbol{A}$ transzponáltja.
- **2.59.** Legyen $\boldsymbol{A} = \operatorname{diag}(1/2)$ egy $n \times n$-es diagonális mátrix, amelynek minden diagonális eleme $1/2$. (a) Mi $\det(\boldsymbol{A})$ értéke? (b) Mi $\operatorname{cond}(A)$ értéke? (c) Milyen következtetést lehet levonni ezekből az eredményekből?
- **2.60.** Tegyük fel, hogy az $n \times n$-es $\boldsymbol{A}$ mátrix egzaktul szinguláris, de a lebegőpontos ábrázolása, $fl(\boldsymbol{A})$, nemszinguláris. Ebben az esetben mit várnál a $\operatorname{cond}(fl(\boldsymbol{A}))$ kondíciószám nagyságrendjének?
- **2.61.** Sorold be az alábbi mátrixok mindegyikét, hogy jól vagy rosszul kondicionált-e:

$$\begin{array}{lll}
(a) & \begin{bmatrix} 10^{10} & 0 \\ 0 & 10^{-10} \end{bmatrix} \\
(b) & \begin{bmatrix} 10^{10} & 0 \\ 0 & 10^{10} \end{bmatrix} \\
(c) & \begin{bmatrix} 10^{-10} & 0 \\ 0 & 10^{-10} \end{bmatrix} \\
(d) & \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}
\end{array}$$

- **2.62.** Az alábbiak közül melyek jó mutatói annak, hogy egy mátrix majdnem szinguláris? (a) Determinánsa kicsi. (b) Normája kicsi. (c) Normája nagy. (d) Kondíciószáma nagy.
- **2.63.** (a) Egy $Ax = b$ lineáris rendszer megoldásakor mit értünk egy $\hat{x}$ közelítő megoldás maradékán? (b) Kis relatív maradék mindig azt jelenti-e, hogy a megoldás pontos? Miért? (c) Nagy relatív maradék mindig azt jelenti-e, hogy a megoldás pontatlan? Miért?
- **2.64.** Egy $10$ decimális jegy precíziójú lebegőpontos rendszerben, ha egy olyan lineáris rendszert oldunk meg részleges főelemkiválasztással végzett Gauss-kiküszöböléssel, amelynek mátrixa $10^3$ kondíciószámú, és amelynek bemeneti adatai teljes gépi precízióval pontosak, körülbelül hány értékes jegyet várnál a megoldásban?
- **2.65.** Tegyük fel, hogy egy $Ax = b$ lineáris egyenletrendszert egy olyan számítógépen oldasz meg, amelynek lebegőpontos számrendszere $12$ decimális jegy precíziójú, és hogy a feladat adatai teljes gépi precízióval pontosak. Körülbelül milyen nagy lehet az $A$ mátrix kondíciószáma, mielőtt a számított $x$ megoldás egyetlen értékes jegyet sem tartalmaz?
- **2.66.** Milyen körülmények között jelenti-e egy kis $r = b - Ax$ maradékvektor, hogy $x$ az $Ax = b$ lineáris rendszer pontos megoldása?
- **2.67.** Legyen $A$ egy tetszőleges négyzetes mátrix, és $c$ egy tetszőleges skalár. Az alábbi állítások közül melyek kell szükségképpen teljesüljenek? (a) $\|cA\| = |c| \cdot \|A\|$. (b) $\operatorname{cond}(cA) = |c| \cdot \operatorname{cond}(A)$.
- **2.68.** (a) Mi a fő különbség a Gauss-kiküszöbölés és a Gauss–Jordan-kiküszöbölés között? (b) Mondj a másikhoz képest egy-egy előnyt mindkét típusú kiküszöbölésre.
- **2.69.** Rangsorold az alábbi módszereket az $n$-ed rendű általános lineáris egyenletrendszer megoldásához szükséges munka mennyisége szerint: (a) Gauss–Jordan-kiküszöbölés; (b) részleges főelemkiválasztással végzett Gauss-kiküszöbölés; (c) Cramer-szabály; (d) explicit mátrixinvertálás, majd mátrix-vektor szorzás.
- **2.70.** (a) Mennyi tárhely szükséges egy egyrangú $n \times n$-es mátrix hatékony tárolásához? (b) Hány aritmetikai művelet szükséges egy $n$-dimenziós vektor és egy egyrangú $n \times n$-es mátrix szorzatának hatékony kiszámításához?
- **2.71.** Egy $Ax = b$ lineáris rendszer megoldásához a közönséges Gauss-kiküszöbölés és a Gauss–Jordan-kiküszöbölés összehasonlításakor (a) melyiknek költségesebb a felbontása? (b) melyiknek költségesebb a visszahelyettesítése? (c) melyiknek nagyobb az összköltsége?
- **2.72.** A lineáris rendszerek megoldására szolgáló alábbi kiküszöbölési algoritmusok mindegyikére: van-e olyan főelemválasztási stratégia, amely biztosítani tudja, hogy minden szorzótényező abszolút értéke legfeljebb $1$? (a) Gauss-kiküszöbölés; (b) Gauss–Jordan-kiküszöbölés.
- **2.73.** Egy $A$ mátrix mely két tulajdonsága együtt implikálja, hogy $A$-nak van Cholesky-felbontása?
- **2.74.** Sorolj fel három előnyt, amelyet a Cholesky-felbontás az LU-felbontáshoz képest nyújt.
- **2.75.** Egy $n \times n$-es szimmetrikus pozitív definit mátrix Cholesky-felbontásának kiszámításához hány négyzetgyökre van szükség?
- **2.76.** Legyen $A = \{a_{ij}\}$ egy $n \times n$-es szimmetrikus pozitív definit mátrix. (a) Mi a Cholesky-tényezőjének $(1,1)$ eleme? (b) Mi a Cholesky-tényezőjének $(n,1)$ eleme?
- **2.77.** Mi az alábbi mátrix Cholesky-felbontása?

$$\begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix}$$

- **2.78.** (a) Lehetséges-e általában egy szimmetrikus indefinit lineáris rendszert hasonló költséggel megoldani, mint amennyibe egy szimmetrikus pozitív definit lineáris rendszer Cholesky-felbontással történő megoldása kerül? (b) Ha igen, milyen algoritmus valósítja ezt meg? Ha nem, miért?
- **2.79.** Adj két okot arra, hogy a lineáris rendszerek megoldására szolgáló iteratív finomítás miért gyakran nem valósítható meg a gyakorlatban.
- **2.80.** Tegyük fel, hogy egy $n \times n$-es $Ax = b$ lineáris rendszert LU-felbontással és visszahelyettesítéssel már megoldottál. Mi a további költsége (a nagyságrendi becslés elegendő) egy új rendszer megoldásának (a) ugyanazzal a mátrixszal, de más jobb oldali vektorral? (b) ha a mátrixot egy egyrangú mátrix hozzáadásával módosítjuk? (c) ha a mátrix teljesen megváltozik?

### Feladatok

- **2.1.** A 2.2. szakaszban négy definiáló tulajdonságot adtunk meg egy szinguláris mátrixra. Mutasd meg, hogy ez a négy tulajdonság valóban ekvivalens.
- **2.2.** Tegyük fel, hogy egy $n \times n$-es $A$ mátrix minden sorösszege nulla. Mutasd meg, hogy $A$ szükségképpen szinguláris.
- **2.3.** Tegyük fel, hogy $A$ egy szinguláris $n \times n$-es mátrix. Bizonyítsd be, hogy ha az $Ax = b$ lineáris rendszernek van legalább egy $x$ megoldása, akkor végtelen sok megoldása van.
- **2.4.** (a) Mutasd meg, hogy az alábbi mátrix szinguláris.

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 1 & 3 & 2 \end{bmatrix}$$

(b) Ha $b = \begin{bmatrix} 2 & 4 & 6 \end{bmatrix}^T$, hány megoldása van az $Ax = b$ rendszernek?

- **2.5.** Mi az alábbi mátrix inverze?

$$\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & -1 & 0 \\ 1 & -2 & 1 \end{bmatrix}$$

- **2.6.** Legyen $A$ olyan $n \times n$-es mátrix, amelyre $A^2 = O$, azaz a nullmátrix. Mutasd meg, hogy $A$ szükségképpen szinguláris.
- **2.7.** Legyen

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1+\epsilon \\ 1-\epsilon & 1 \end{bmatrix}.$$

(a) Mi $A$ determinánsa? (b) Lebegőpontos aritmetikában $\epsilon$ mely értéktartományára lesz a determináns számított értéke nulla? (c) Mi $A$ LU-felbontása? (d) Lebegőpontos aritmetikában $\epsilon$ mely értéktartományára lesz $U$ számított értéke szinguláris?

- **2.8.** Legyen $A$ és $B$ tetszőleges két $n \times n$-es mátrix. (a) Bizonyítsd be, hogy $(AB)^T = B^T A^T$. (b) Ha $A$ és $B$ mindkettő nemszinguláris, bizonyítsd be, hogy $(AB)^{-1} = B^{-1} A^{-1}$.
- **2.9.** Ha $A$ tetszőleges nemszinguláris valós mátrix, mutasd meg, hogy $(A^{-1})^T = (A^T)^{-1}$. Ennek következtében az $A^{-T}$ jelölés egyértelműen használható e mátrix jelölésére. Hasonlóan, ha $A$ tetszőleges nemszinguláris komplex mátrix, akkor $(A^{-1})^H = (A^H)^{-1}$, és az $A^{-H}$ jelölés egyértelműen használható e mátrix jelölésére.
- **2.10.** Legyen $P$ egy tetszőleges permutációs mátrix. (a) Bizonyítsd be, hogy $P^{-1} = P^T$. (b) Bizonyítsd be, hogy $P$ kifejezhető páronkénti cserék szorzataként.
- **2.11.** Írj részletes algoritmust egy $Lx = b$ alsó háromszögű lineáris rendszer előrehelyettesítéssel történő megoldására.
- **2.12.** Ellenőrizd, hogy egy $n$-ed rendű alsó háromszögű rendszer előrehelyettesítéssel történő megoldásának műveletszámában (szorzások vagy összeadások számában) a domináns tag $n^2/2$.
- **2.13.** Hogyan oldanád meg a következő alakú particionált lineáris rendszert?

$$\begin{bmatrix} \boldsymbol{L}_1 & \boldsymbol{O} \\ \boldsymbol{B} & \boldsymbol{L}_2 \end{bmatrix} \begin{bmatrix} \boldsymbol{x} \\ \boldsymbol{y} \end{bmatrix} = \begin{bmatrix} \boldsymbol{b} \\ \boldsymbol{c} \end{bmatrix},$$

ahol $\boldsymbol{L}_1$ és $\boldsymbol{L}_2$ nemszinguláris alsó háromszögmátrixok, és a megoldás- és jobb oldali vektorokat ennek megfelelően particionáljuk. Mutasd be a konkrét lépéseket a megadott almátrixok és vektorok segítségével.

- **2.14.** Bizonyítsd be az elemi eliminációs mátrixok 2.4.3. szakaszban felsorolt négy tulajdonságát.
- **2.15.** (a) Bizonyítsd be, hogy két alsó háromszögmátrix szorzata alsó háromszögmátrix. (b) Bizonyítsd be, hogy egy nemszinguláris alsó háromszögmátrix inverze alsó háromszögmátrix.
- **2.16.** (a) Mi az alábbi mátrix LU-felbontása?

$$\begin{bmatrix} 1 & a \\ c & b \end{bmatrix}$$

(b) Milyen feltétel mellett szinguláris ez a mátrix?

- **2.17.** Írd fel az alábbi mátrix LU-felbontását (mutasd be mind az $L$-t, mind az $U$-t explicit módon):

$$\begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}.$$

- **2.18.** Bizonyítsd be, hogy az

$$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$

mátrixnak nincs LU-felbontása, azaz nem létezik olyan $L$ alsó háromszögmátrix és $U$ felső háromszögmátrix, amelyekre $A = LU$.

- **2.19.** Legyen $A$ egy $n \times n$-es nemszinguláris mátrix. Tekintsük az alábbi algoritmust: 1. Végigfutva $A$ $1$-től $n$-ig terjedő oszlopain, permutáljuk a sorokat szükség szerint úgy, hogy minden oszlopban a főátlón vagy az alatta lévő elemek közül a főátlóbeli elem legyen az abszolút értékben legnagyobb. Az eredmény $PA$ valamilyen $P$ permutációs mátrixszal. 2. Ezután főelemkiválasztás nélküli Gauss-kiküszöböléssel számítsuk ki $PA$ LU-felbontását. (a) Numerikusan stabil-e ez az algoritmus? (b) Ha igen, magyarázd meg miért. Ha nem, adj ellenpéldát a szemléltetésre.
- **2.20.** Bizonyítsd be, hogy ha részleges főelemkiválasztással végzett Gauss-kiküszöbölést alkalmazunk egy oszloponként diagonálisan domináns $A$ mátrixra, akkor sorcserék nem fognak bekövetkezni.
- **2.21.** Ha $A$, $B$ és $C$ $n \times n$-es mátrixok, $B$ és $C$ nemszinguláris, és $b$ egy $n$-dimenziós vektor, hogyan implementálnád az

$$x = B^{-1}(2A + I)(C^{-1} + A)b$$

képletet anélkül, hogy bármelyik mátrixinverzet kiszámítanád?

- **2.22.** Ellenőrizd, hogy egy $n$-ed rendű mátrix Gauss-kiküszöböléssel történő LU-felbontásának műveletszámában (szorzások vagy összeadások számában) a domináns tag $n^3/3$.
- **2.23.** Ellenőrizd, hogy egy $n$-ed rendű mátrix Gauss-kiküszöböléssel történő inverzének kiszámításához tartozó műveletszámban (szorzások vagy összeadások számában) a domináns tag $n^3$.
- **2.24.** Ellenőrizd, hogy egy $n$-ed rendű mátrixon végrehajtott Gauss–Jordan-kiküszöbölés műveletszámában (szorzások vagy összeadások számában) a domináns tag $n^3/2$.
- **2.25.** (a) Ha $u$ és $v$ nem nulla $n$-dimenziós vektorok, bizonyítsd be, hogy a $uv^T$ $n \times n$-es külső szorzat mátrix rangja $1$. (b) Ha $A$ egy olyan $n \times n$-es mátrix, amelyre $\operatorname{rank}(A) = 1$, bizonyítsd be, hogy léteznek olyan nem nulla $u$ és $v$ $n$-dimenziós vektorok, amelyekre $A = uv^T$.
- **2.26.** Egy $n \times n$-es $A$ mátrixot *elemi*nek nevezünk, ha az egységmátrixtól egy egyrangú mátrixban tér el, azaz $A = I - uv^T$ valamilyen $u$ és $v$ $n$-dimenziós vektorokkal. (a) Ha $A$ elemi, milyen feltétel biztosítja $u$-ra és $v$-re, hogy $A$ nemszinguláris? (b) Ha $A$ elemi és nemszinguláris, bizonyítsd be, hogy $A^{-1}$ is elemi, megmutatva, hogy $A^{-1} = I - \sigma u v^T$ valamilyen $\sigma$ skalárral. Mi a konkrét $\sigma$ érték $u$ és $v$ függvényében? (c) Elemi-e egy a 2.4.3. szakaszban definiált elemi eliminációs mátrix? Ha igen, mik $u$, $v$ és $\sigma$ ebben az esetben?
- **2.27.** Bizonyítsd be, hogy a 2.4.9. szakaszban megadott Sherman–Morrison-formula,

$$(\boldsymbol{A} - \boldsymbol{u}\boldsymbol{v}^T)^{-1} = A^{-1} + A^{-1}u(1 - v^T A^{-1}u)^{-1}v^T A^{-1},$$

helyes. (*Útmutatás:* Szorozd meg mindkét oldalt $A - uv^T$-tal.)

- **2.28.** Bizonyítsd be, hogy a 2.4.9. szakaszban megadott Woodbury-formula,

$$(\boldsymbol{A} - \boldsymbol{U}\boldsymbol{V}^T)^{-1} = A^{-1} + A^{-1}U(I - V^T A^{-1}U)^{-1}V^T A^{-1},$$

helyes. (*Útmutatás:* Szorozd meg mindkét oldalt $A - UV^T$-tal.)

- **2.29.** $p = 1, 2$ és $\infty$ esetén bizonyítsd be, hogy a vektor $p$-normák teljesítik a 2.3.1. szakasz végén megadott három tulajdonságot.
- **2.30.** $p = 1$ és $\infty$ esetén bizonyítsd be, hogy a mátrix $p$-normák teljesítik a 2.3.2. szakasz végén megadott öt tulajdonságot.
- **2.31.** Legyen $A$ egy szimmetrikus pozitív definit mátrix. Mutasd meg, hogy az

$$\|\boldsymbol{x}\|_A = (\boldsymbol{x}^T \boldsymbol{A} \boldsymbol{x})^{1/2}$$

függvény teljesíti a vektornorma 2.3.1. szakasz végén megadott három tulajdonságát. Ezt a vektornormát az $A$ mátrix által *indukáltnak* mondjuk.

- **2.32.** Mutasd meg, hogy egy $m \times n$-es $A$ mátrix alábbi függvényei teljesítik a mátrixnorma 2.3.2. szakasz végén megadott első három tulajdonságát, és ezért mátrixnormák az ott említett általánosabb értelemben. (a)

$$\|\boldsymbol{A}\|_{\max} = \max_{i,j} |a_{ij}|$$

Figyeljük meg, hogy ez egyszerűen $A$-nak az $\mathbb{R}^{mn}$-beli vektorként tekintett $\infty$-normája. (b)

$$\|A\|_F = \left(\sum_{i,j} |a_{ij}|^2\right)^{1/2}$$

Figyeljük meg, hogy ez egyszerűen $A$-nak az $\mathbb{R}^{mn}$-beli vektorként tekintett $2$-normája. Ezt *Frobenius-mátrixnormának* nevezzük.

- **2.33.** Bizonyítsd be vagy adj ellenpéldát: Ha $A$ nemszinguláris mátrix, akkor $\|A^{-1}\| = \|A\|^{-1}$.
- **2.34.** Tegyük fel, hogy $\boldsymbol{A}$ pozitív definit mátrix. (a) Mutasd meg, hogy $\boldsymbol{A}$ szükségképpen nemszinguláris. (b) Mutasd meg, hogy $A^{-1}$ szükségképpen pozitív definit.
- **2.35.** Tegyük fel, hogy az $A$ mátrixnak van $A = BB^T$ alakú felbontása, ahol $B$ nemszinguláris. Mutasd meg, hogy $A$ szükségképpen szimmetrikus és pozitív definit.
- **2.36.** Vezess le egy algoritmust, amely egy $n \times n$-es szimmetrikus pozitív definit $\boldsymbol{A}$ mátrix $\boldsymbol{L}\boldsymbol{L}^T$ Cholesky-felbontásának kiszámításához $\boldsymbol{A}$ és $\boldsymbol{L}\boldsymbol{L}^T$ megfelelő elemeinek egyenlővé tételével kapható.
- **2.37.** Tegyük fel, hogy az

$$\boldsymbol{B} = \begin{bmatrix} \alpha & \boldsymbol{a}^T \\ \boldsymbol{a} & \boldsymbol{A} \end{bmatrix}$$

$(n+1)$-ed rendű szimmetrikus mátrix pozitív definit. (a) Mutasd meg, hogy az $\alpha$ skalár szükségképpen pozitív, és az $n \times n$-es $\boldsymbol{A}$ mátrix szükségképpen pozitív definit. (b) Mi $\boldsymbol{B}$ Cholesky-felbontása az alkotó almátrixok segítségével?

- **2.38.** Tegyük fel, hogy az

$$\boldsymbol{B} = \begin{bmatrix} \boldsymbol{A} & \boldsymbol{a} \\ \boldsymbol{a}^T & \alpha \end{bmatrix}$$

$(n+1)$-ed rendű szimmetrikus mátrix pozitív definit. (a) Mutasd meg, hogy az $\alpha$ skalár szükségképpen pozitív, és az $n \times n$-es $\boldsymbol{A}$ mátrix szükségképpen pozitív definit. (b) Mi $\boldsymbol{B}$ Cholesky-felbontása az alkotó almátrixok segítségével?

- **2.39.** Ellenőrizd, hogy egy $n$-ed rendű szimmetrikus pozitív definit mátrix Cholesky-felbontásának műveletszámában (szorzások vagy összeadások számában) a domináns tag $n^3/6$.
- **2.40.** Legyen $\boldsymbol{A}$ egy $\beta$ sávszélességű sávos mátrix, és tegyük fel, hogy a $\boldsymbol{P}\boldsymbol{A} = \boldsymbol{L}\boldsymbol{U}$ LU-felbontást részleges főelemkiválasztással végzett Gauss-kiküszöböléssel számítjuk. Mutasd meg, hogy az $\boldsymbol{U}$ felső háromszögű tényező sávszélessége legfeljebb $2\beta$.
- **2.41.** Legyen $A$ egy nemszinguláris tridiagonális mátrix. (a) Mutasd meg, hogy általában $A^{-1}$ sűrű. (b) Hasonlítsd össze az $Ax = b$ lineáris rendszer Gauss-kiküszöböléssel és visszahelyettesítéssel történő megoldásához, valamint a rendszer explicit mátrixinvertálással történő megoldásához szükséges munkát és tárhelyet.

Ez a példa egy további okot szemléltet arra, hogy az explicit mátrixinvertálás miért rendszerint rossz ötlet.

- **2.42.** (a) Készíts algoritmust egy nemszinguláris $n \times n$-es háromszögmátrix inverzének helyben történő kiszámítására, azaz további tömbtárhely nélkül. (b) Lehetséges-e egy általános nemszinguláris $n \times n$-es mátrix inverzét helyben kiszámítani? Ha igen, vázolj egy erre szolgáló algoritmust, ha nem, magyarázd meg miért. E feladat céljaira feltételezheted, hogy főelemkiválasztásra nincs szükség.
- **2.43.** Tegyük fel, hogy egy $Cz = d$ lineáris rendszert kell megoldanod, ahol $C$ egy komplex $n \times n$-es mátrix, $d$ és $z$ pedig komplex $n$-dimenziós vektorok, de a lineáris egyenletrendszer-megoldód csak valós rendszereket kezel. Legyen $C = A + iB$ és $d = b + ic$, ahol $A$, $B$, $b$ és $c$ valósak, és $i = \sqrt{-1}$. Mutasd meg, hogy a $z = x + iy$ megoldást a

$$\begin{bmatrix} A & -B \\ B & A \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} b \\ c \end{bmatrix}$$

$2n \times 2n$-es valós lineáris rendszer adja. Jó módja-e ez a feladat megoldásának? Miért?

### Számítógépes feladatok

- **2.1.** (a) Mutasd meg, hogy az

$$\mathbf{A} = \begin{bmatrix} 0{,}1 & 0{,}2 & 0{,}3 \\ 0{,}4 & 0{,}5 & 0{,}6 \\ 0{,}7 & 0{,}8 & 0{,}9 \end{bmatrix}$$

mátrix szinguláris. Írd le az $Ax = b$ rendszer megoldásainak halmazát, ha

$$\boldsymbol{b} = \begin{bmatrix} 0{,}1 \\ 0{,}3 \\ 0{,}5 \end{bmatrix}.$$

(b) Ha részleges főelemkiválasztással végzett Gauss-kiküszöböléssel akarnánk megoldani ezt a rendszert egzakt aritmetikával, hol akadna meg a folyamat? (c) Mivel $A$ néhány eleme nem ábrázolható egzaktul egy bináris lebegőpontos rendszerben, a mátrix a számítógépbe bevitel után már nem egzaktul szinguláris, így a rendszer Gauss-kiküszöböléssel történő megoldása nem feltétlenül hiúsul meg. Oldd meg ezt a rendszert számítógépen egy Gauss-kiküszöbölést végző könyvtári rutinnal. Hasonlítsd össze a számított megoldást az (a) részben adott megoldáshalmaz leírásával. Ha a szoftvered tartalmaz kondícióbecslőt, mi a $\operatorname{cond}(A)$ becsült értéke? Mennyi értékes jegyet várnál e becslés alapján a megoldásban?

- **2.2.** (a) Egy Gauss-kiküszöbölést végző könyvtári rutinnal oldd meg az $Ax = b$ rendszert, ahol

$$\boldsymbol{A} = \begin{bmatrix} 2 & 4 & -2 \\ 4 & 9 & -3 \\ -2 & -1 & 7 \end{bmatrix}, \quad \boldsymbol{b} = \begin{bmatrix} 2 \\ 8 \\ 10 \end{bmatrix}.$$

(b) Az $\boldsymbol{A}$ mátrix már kiszámított LU-felbontását felhasználva — a mátrix újrafelbontása nélkül — oldd meg az $Ay = c$ rendszert, ahol

$$\boldsymbol{c} = \begin{bmatrix} 4 \\ 8 \\ -6 \end{bmatrix}.$$

(c) Ha az $A$ mátrix úgy változik, hogy $a_{1,2} = 2$, a Sherman–Morrison-féle frissítési technikával — a mátrix újrafelbontása nélkül — számítsd ki az új $x$ megoldást az eredeti $b$ jobb oldali vektort használva.

- **2.3.** Az alábbi ábra egy síkbeli rácsszerkezetet ábrázol, amely 13 rúdból (a számozott egyenesek) és 10 csomópontból (a számozott körök) áll. A jelzett terhelések, tonnában, a 2., az 5. és a 6. csomópontra hatnak, és meg szeretnénk határozni a rácsszerkezet egyes rúdjaira ható eredő erőt.

![](_page_51_Figure_16.jpeg)

Ahhoz, hogy a rácsszerkezet statikus egyensúlyban legyen, minden csomópontban se vízszintes, se függőleges irányú eredő erő ne lépjen fel. Így a rúderőket úgy határozhatjuk meg, hogy minden csomópontban a balról és a jobbról ható vízszintes erőket, hasonlóképpen a felfelé és a lefelé ható függőleges erőket egyenlővé tesszük. A nyolc csomópontra ez 16 egyenletet adna, ami több, mint a 13 meghatározandó ismeretlen erő. Ahhoz, hogy a rácsszerkezet statikailag határozott legyen, azaz hogy egyetlen megoldás létezzen, feltételezzük, hogy az 1. csomópont vízszintesen és függőlegesen is mereven rögzített, a 8. csomópont pedig függőlegesen rögzített. A rúderőket vízszintes és függőleges komponensekre felbontva és $\alpha = \sqrt{2}/2$-t bevezetve a rúderőkre, $f_i$-re, a következő egyenletrendszert kapjuk:

Egy könyvtári rutinnal oldd meg ezt a lineáris egyenletrendszert az $f$ rúderővektorra. Megjegyzendő, hogy e rendszer mátrixa meglehetősen ritka, így érdemes lehet sávos rendszer-megoldóval vagy általánosabb ritka megoldóval is kísérletezned, bár ez a konkrét feladatpéldány túl kicsi ahhoz, hogy ezek egy általános megoldóhoz képest jelentős előnyt jelentsenek.

- **2.4.** Írj rutint egy $\boldsymbol{A}$ mátrix kondíciószámának becslésére. Használhatod akár az $1$-normát, akár a $\infty$-normát (vagy próbáld ki mindkettőt, és hasonlítsd össze az eredményeket). Ki kell majd számítanod $\|\boldsymbol{A}\|$-t, ami könnyű, és meg kell becsülnöd $\|\boldsymbol{A}^{-1}\|$-t, ami nagyobb kihívás. Ahogy a 2.3.3. szakaszban tárgyaltuk, $\|\boldsymbol{A}^{-1}\|$ becslésének egy módja, hogy olyan $\boldsymbol{y}$ vektort választunk, amelyre a $\|\boldsymbol{z}\|/\|\boldsymbol{y}\|$ arány nagy, ahol $\boldsymbol{z}$ az $\boldsymbol{A}\boldsymbol{z} = \boldsymbol{y}$ megoldása. Próbálj ki két különböző megközelítést $\boldsymbol{y}$ választására: (a) Válaszd $\boldsymbol{y}$-t az $A^T y = c$ rendszer megoldásaként, ahol $c$ egy olyan vektor, amelynek minden komponense $\pm 1$, és az egyes komponensekhez tartozó előjelet az alábbi heurisztikával választjuk. Az $\mathbf{A} = \mathbf{L}\mathbf{U}$ felbontást felhasználva az $\mathbf{A}^T \mathbf{y} = \mathbf{c}$ rendszert két lépésben oldjuk meg: egymás után megoldjuk az $\mathbf{U}^T \mathbf{v} = \mathbf{c}$ és az $\mathbf{L}^T \mathbf{y} = \mathbf{v}$ háromszögű rendszereket. Az első háromszögű megoldás minden lépésében $c$ megfelelő komponensét $1$-nek vagy $-1$-nek választjuk, attól függően, hogy melyik választás teszi a kapott $v$-komponenst abszolút értékben nagyobbá. (Ehhez egy saját háromszögű megoldó rutint kell majd írnod e logika megvalósítására.) Ezután oldd meg a második háromszögű rendszert a szokott módon $\boldsymbol{y}$-ra. Az ötlet az, hogy az $A$-ban jelen lévő rossz kondicionáltság $U$-ban fog tükröződni, viszonylag nagy $v$-t eredményezve. A viszonylag jól kondicionált egységháromszögű $\boldsymbol{L}$ mátrix aztán megőrzi ezt a viszonyt, viszonylag nagy $\boldsymbol{y}$-t eredményezve. (b) Válassz néhány — mondjuk öt — különböző $\boldsymbol{y}$ vektort véletlenszerűen, és azt használd, amelyik a legnagyobb $\|\boldsymbol{z}\|/\|\boldsymbol{y}\|$ arányt adja. (Ehhez közönséges háromszögű megoldó rutint használhatsz.)

Az $\boldsymbol{A}$ szükséges LU-felbontásához könyvtári rutint használhatsz. Teszteld mindkét megközelítést az alábbi mátrixokon:

$$\mathbf{A}_1 = \begin{bmatrix} 10 & -7 & 0 \\ -3 & 2 & 6 \\ 5 & -1 & 5 \end{bmatrix},$$

$$\mathbf{A}_2 = \begin{bmatrix} -73 & 78 & 24 \\ 92 & 66 & 25 \\ -80 & 37 & 10 \end{bmatrix}.$$

Hogyan viszonyulnak egymáshoz a két módszerrel kapott eredmények? A becsléseid minőségének ellenőrzéséhez számítsd ki $\mathbf{A}^{-1}$-et explicit módon, hogy meghatározd a valódi normáját (ehhez a számításhoz is felhasználhatod a már kiszámított LU-felbontást). Ha van hozzáférésed olyan lineáris egyenletrendszer-szoftverhez, amely már tartalmaz kondícióbecslőt, hogyan viszonyulnak az eredményeid az övéhez?

- **2.5.** (a) Egy egyszeres pontosságú, Gauss-kiküszöbölést végző rutinnal oldd meg az $Ax = b$ rendszert, ahol

$$\boldsymbol{A} = \begin{bmatrix} 21{,}0 & 67{,}0 & 88{,}0 & 73{,}0 \\ 76{,}0 & 63{,}0 & 7{,}0 & 20{,}0 \\ 0{,}0 & 85{,}0 & 56{,}0 & 54{,}0 \\ 19{,}3 & 43{,}0 & 30{,}2 & 29{,}4 \end{bmatrix},$$

$$\boldsymbol{b} = \begin{bmatrix} 141{,}0 \\ 109{,}0 \\ 218{,}0 \\ 93{,}7 \end{bmatrix}.$$

(b) Számítsd ki az $r = b - Ax$ maradékot dupla pontosságú aritmetikával, ha elérhető (de a végső eredményt egyszeres pontosságú $r$ vektorba tárolva). Megjegyzendő, hogy a megoldó rutin elpusztíthatja az $A$-t tartalmazó tömböt, így külön másolatot kell majd megőrizned a maradék számításához. (Ha a használt számítási környezetben csak egyetlen precízió érhető el, akkor végezd el a teljes feladatot abban a precízióban.) (c) Oldd meg az $Az = r$ lineáris rendszert a „javított" $x + z$ megoldás megkapásához. Megjegyzendő, hogy $A$-t nem kell újrafelbontani. (d) Ismételd a (b) és (c) lépéseket, amíg további javulást nem tapasztalsz.

- **2.6.** Egy $n \times n$-es $\boldsymbol{H}$ Hilbert-mátrix elemei $h_{ij} = 1/(i+j-1)$, így az alakja

$$\begin{bmatrix} 1 & 1/2 & 1/3 & \cdots \\ 1/2 & 1/3 & 1/4 & \cdots \\ 1/3 & 1/4 & 1/5 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{bmatrix}.$$

$n = 2, 3, \ldots$ esetén generáld az $n$-ed rendű Hilbert-mátrixot, valamint a $\boldsymbol{b} = \boldsymbol{H}\boldsymbol{x}$ $n$-dimenziós vektort, ahol $\boldsymbol{x}$ az az $n$-dimenziós vektor, amelynek minden komponense $1$. Egy Gauss-kiküszöbölést (vagy Cholesky-felbontást, mivel a Hilbert-mátrix szimmetrikus és pozitív definit) végző könyvtári rutinnal oldd meg a kapott $\boldsymbol{H}\boldsymbol{x} = \boldsymbol{b}$ lineáris rendszert, $\hat{x}$ közelítő megoldást kapva. Számítsd ki az $\mathbf{r} = \mathbf{b} - \mathbf{H}\hat{x}$ maradék és a $\Delta \mathbf{x} = \hat{x} - \mathbf{x}$ hiba $\infty$-normáját, ahol $\mathbf{x}$ a csupa egyes vektor. Milyen nagyra veheted $n$-et, mielőtt a hiba 100 százalékossá válik (azaz a megoldásban nincs egyetlen értékes jegy sem)? Emellett egy kondícióbecslővel határozd meg $\operatorname{cond}(\boldsymbol{H})$-t minden $n$-re. Próbáld meg jellemezni a kondíciószámot $n$ függvényében. Ahogy $n$ változik, hogyan viszonyul a számított megoldás komponenseiben lévő helyes számjegyek száma a mátrix kondíciószámához?

- **2.7.** (a) Mi történik, ha részleges főelemkiválasztással végzett Gauss-kiküszöbölést alkalmazunk a következő alakú mátrixra?

$$\begin{bmatrix}
1 & 0 & 0 & 0 & 1 \\
-1 & 1 & 0 & 0 & 1 \\
-1 & -1 & 1 & 0 & 1 \\
-1 & -1 & -1 & 1 & 1 \\
-1 & -1 & -1 & -1 & 1
\end{bmatrix}$$

Nőnek-e a transzformált mátrix elemei? Mi történik, ha ehelyett teljes főelemkiválasztást használunk? (Megjegyzendő, hogy az (a) rész nem igényel számítógépet.)

(b) Egy részleges főelemkiválasztással végzett Gauss-kiküszöbölést alkalmazó könyvtári rutinnal oldj meg ilyen alakú, különböző méretű lineáris rendszereket, olyan jobb oldali vektorokat választva, amelyek esetén a megoldás ismert. Hogyan viselkedik a hiba, a maradék és a kondíciószám, ahogy a rendszerek egyre nagyobbak lesznek? Ez a mesterségesen megkonstruált rendszer a 2.4.5. szakaszban idézett, legrosszabb esetben fellépő növekedési tényezőt illusztrálja, és nem jellemző a részleges főelemkiválasztással végzett Gauss-kiküszöbölés szokásos viselkedésére.

- **2.8.** Egy $Ax = b$ lineáris rendszer mindkét oldalának egy $D$ nemszinguláris diagonális mátrixszal való szorzása, hogy egy új $DAx = Db$ rendszert kapjunk, egyszerűen átskálázza a rendszer sorait, és elméletben nem változtatja meg a megoldást. Az ilyen skálázás azonban befolyásolja a mátrix kondíciószámát és a Gauss-kiküszöbölésben a főelemek választását, így véges precíziójú aritmetikában befolyásolhatja a megoldás pontosságát. Megjegyzendő, hogy a skálázás némi kerekítési hibát vihet a mátrixba, hacsak $D$ elemei nem a használt lebegőpontos aritmetikai rendszer alapjának hatványai (miért?).

Véletlenszerűen választott $\boldsymbol{A}$ mátrixú lineáris rendszer és olyan $\boldsymbol{b}$ jobb oldali vektor használatával, amely mellett a megoldás ismert, kísérletezz különféle $D$ skálázó mátrixokkal, hogy milyen hatással vannak a $DA$ mátrix kondíciószámára és a $DAx = Db$ lineáris rendszer megoldására egy erre szolgáló könyvtári rutin által adott megoldásra. Mindenképpen próbálj ki elég torz skálázásokat is, amelyeknél $D$ diagonális elemeinek nagyságrendje jelentősen különbözik egymástól (a cél egy rosszul megválasztott mértékegységekkel adott rendszer szimulálása). Hasonlítsd össze mind a relatív maradékokat, mind a különféle skálázások által adott hibát. Találsz-e olyan skálázást, amely nagyon rossz pontosságot ad? Ebben az esetben a maradék továbbra is kicsi marad-e?

- **2.9.** (a) Főelemkiválasztás nélküli Gauss-kiküszöböléssel oldd meg az

$$\begin{bmatrix} \epsilon & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1+\epsilon \\ 2 \end{bmatrix}$$

lineáris rendszert $\epsilon = 10^{-2k}$ esetén, $k = 1, \ldots, 10$. Az egzakt megoldás $x = \begin{bmatrix} 1 & 1 \end{bmatrix}^T$, $\epsilon$ értékétől függetlenül. Hogyan viselkedik a számított megoldás pontossága, ahogy $\epsilon$ értéke csökken?

(b) Ismételd meg az (a) részt, továbbra is főelemkiválasztás nélküli Gauss-kiküszöbölést használva, de ezúttal a megoldás javítására egy lépés iteratív finomítást is alkalmazz, a maradékot ugyanolyan precízióval számítva, mint a számítások többi részét. Most hogyan viselkedik a számított megoldás pontossága, ahogy $\epsilon$ értéke csökken?

- **2.10.** Tekintsük az

$$\begin{bmatrix} 1 & 1+\epsilon \\ 1-\epsilon & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1+(1+\epsilon)\epsilon \\ 1 \end{bmatrix}$$

lineáris rendszert, ahol $\epsilon$ egy rögzítendő kis paraméter. Az egzakt megoldás nyilvánvalóan

$$\boldsymbol{x} = \begin{bmatrix} 1 \\ \epsilon \end{bmatrix}$$

$\epsilon$ bármely értékére.

Egy Gauss-kiküszöbölésen alapuló könyvtári rutinnal oldd meg ezt a rendszert. Kísérletezz $\epsilon$ különféle értékeivel, különösen a saját számítógéped $\sqrt{\epsilon_{\text{mach}}}$-ához közeli értékekkel. $\epsilon$ minden kipróbált értékére becsüld meg a mátrix kondíciószámát és a megoldás minden komponensében lévő relatív hibát. Milyen pontosan van meghatározva az egyes komponensek? Hogyan viszonyul az egyes komponensekre kapott pontosság a mátrix kondíciószáma és a 2.3.4. szakaszban megadott hibakorlátok alapján várhatóhoz? Milyen következtetéseket tudsz levonni ebből a kísérletből?

- **2.11.** (a) Írj programokat, amelyek megvalósítják a főelemkiválasztás nélküli, a részleges főelemkiválasztással és a teljes főelemkiválasztással végzett Gauss-kiküszöbölést. (b) Generálj több véletlen mátrixú lineáris rendszert (azaz a mátrix elemeinek előállítására használj véletlenszám-generátort), valamint olyan jobb oldali vektorokat, amelyek mellett a megoldás ismert, és hasonlítsd össze a három implementáció pontosságát, maradékait és teljesítményét. (c) Tudsz-e alkotni egy (nem véletlen) mátrixot, amelyre a teljes főelemkiválasztás lényegesen pontosabb, mint a részleges főelemkiválasztás?
- **2.12.** Írj rutint tridiagonális lineáris egyenletrendszerek megoldására a 2.5.3. szakaszban megadott algoritmussal, és teszteld néhány mintapéldán. Írd le, hogyan változna a rutinod, ha részleges főelemkiválasztást vennél be. Írd le, hogyan változna a rutinod, ha a rendszer pozitív definit volna, és LU-felbontás helyett a Cholesky-felbontást számítanád ki.
- **2.13.** Egy háromszögmátrix determinánsa a főátlóbeli elemeinek szorzatával egyenlő. Használd ezt a tényt egy olyan rutin kidolgozásához, amely egy tetszőleges $n \times n$-es $\boldsymbol{A}$ mátrix determinánsát számítja ki az LU-felbontása segítségével. Használhatsz egy részleges főelemkiválasztással végzett Gauss-kiküszöbölést megvalósító könyvtári rutint az LU-felbontás megszerzésére, vagy tervezheted saját rutinodat. Hogyan tudod meghatározni a determináns megfelelő előjelét? A túlcsordulás vagy alulcsordulás veszélyének elkerülésére érdemes lehet a determináns tényleges értéke helyett a logaritmusának kiszámítását fontolóra venned.
- **2.14.** Írj programokat, amelyek megvalósítják a $C = AB$ mátrixszorzást — ahol $A$ egy $m \times n$-es és $B$ egy $n \times k$-s mátrix — két különböző módon: (a) Számítsd ki az $\boldsymbol{A}$ sorainak és $\boldsymbol{B}$ oszlopainak $mk$ darab belső szorzatát. (b) $C$ minden oszlopát $A$ oszlopainak lineáris kombinációjaként állítsd elő.

BLAS-terminológiában (lásd a 2.7.2. szakaszt) az első implementáció az `sdot`-ot, a második pedig az `saxpy`-t használja. Hasonlítsd össze e két implementáció teljesítményét a saját számítógépeden. Előfordulhat, hogy elég nagy mátrixokat kell kipróbálnod, mielőtt a teljesítménykülönbségek jelentőssé válnának. Tudj meg annyit a számítógéprendszeredről, amennyit csak tudsz (pl. a gyorsítótár mérete és kezelési stratégiája), és használd fel ezt az információt a megfigyelt eredmények magyarázatára.

- **2.15.** Valósítsd meg a Gauss-kiküszöbölést a hármas egymásba ágyazott ciklus mind a hat különböző sorrendjével, és hasonlítsd össze a teljesítményüket a saját számítógépeden. E feladat céljaira a numerikus stabilitás érdekében végzett főelemkiválasztást figyelmen kívül hagyhatod, de mindenképpen olyan tesztmátrixokat használj, amelyek nem igényelnek főelemkiválasztást. Előfordulhat, hogy elég nagy rendszert kell kipróbálnod, mielőtt a teljesítménykülönbségek jelentőssé válnának. Tudj meg annyit a számítógéprendszeredről, amennyit csak tudsz (pl. a gyorsítótár mérete és kezelési stratégiája), és használd fel ezt az információt a megfigyelt eredmények magyarázatára.
- **2.16.** Háromszögű lineáris rendszerek megoldásához mind az előre-, mind a visszahelyettesítés olyan egymásba ágyazott ciklusokat tartalmaz, amelyek két indexe bármelyik sorrendben futhat. Valósítsd meg mind az előre-, mind a visszahelyettesítést a két indexsorrend mindegyikével (összesen négy algoritmust), és hasonlítsd össze teljesítményüket különböző méretű háromszögű tesztmátrixokon. Előfordulhat, hogy elég nagy rendszert kell kipróbálnod, mielőtt a teljesítménykülönbségek jelentőssé válnának. Az indexsorrendek legjobb választása ugyanaz-e mindkét algoritmusnál? Tudj meg annyit a számítógéprendszeredről, amennyit csak tudsz (pl. a gyorsítótár mérete és kezelési stratégiája), és használd fel ezt az információt a megfigyelt eredmények magyarázatára.
- **2.17.** Tekintsünk egy vízszintes, egyik végén befogott, a hossza fennmaradó részén szabad tartót. A tartón ható erők egy diszkrét modellje egy $Ax = b$ lineáris egyenletrendszert ad, ahol az $n \times n$-es $A$ mátrix a következő sávos alakú:

$$\begin{bmatrix} 9 & -4 & 1 & 0 & \cdots & \cdots & 0 \\ -4 & 6 & -4 & 1 & \ddots & & \vdots \\ 1 & -4 & 6 & -4 & 1 & \ddots & \vdots \\ 0 & \ddots & \ddots & \ddots & \ddots & \ddots & 0 \\ \vdots & \ddots & 1 & -4 & 6 & -4 & 1 \\ \vdots & & \ddots & 1 & -4 & 5 & -2 \\ 0 & \cdots & \cdots & 0 & 1 & -2 & 1 \end{bmatrix},$$

a $\boldsymbol{b}$ $n$-dimenziós vektor a tartóra ható ismert terhelés (a saját súlyával együtt), a $\boldsymbol{x}$ $n$-dimenziós vektor pedig a tartó meghatározandó, eredő lehajlását jelöli. A tartót egyenletesen terheltnek tekintjük, úgy, hogy a terhelésvektor minden komponensére $b_i = 1/n^4$.

(a) $n = 100$ esetén oldd meg ezt a lineáris rendszert mind egy sűrű lineáris rendszerekhez szolgáló standard könyvtári rutinnal, mind egy sávos (vagy általánosabb ritka) rendszerekhez tervezett könyvtári rutinnal. Hogyan viszonyul egymáshoz a két rutin a megoldás kiszámításához szükséges időben? Mennyire egyeznek meg a kapott válaszok egymással?

(b) Ellenőrizd, hogy az $A$ mátrixnak van $A = RR^T$ UL-felbontása, ahol $R$ a következő alakú felső háromszögmátrix:

| $\lceil 2 \rceil$ | -2            | 1  | 0  |    | 0 ]                                     |
|-------------------|---------------|----|----|----|-----------------------------------------|
| 0                 | -2<br>1<br>∴. | -2 | 1  | ٠. | :                                       |
| :                 | ٠.            | ٠  | ٠. | ٠  | 0                                       |
| :                 |               | ٠. |    | -2 |                                         |
| :                 |               |    | ٠. | 1  | $\begin{bmatrix} -2 \\ 1 \end{bmatrix}$ |
|                   |               |    |    | 0  | 1                                       |

$n = 1000$ esetén oldd meg a lineáris rendszert e felbontással (két háromszögű megoldásra lesz szükség). Emellett oldd meg a rendszert az eredeti alakjában is egy sávos (vagy általános ritka) rendszer-megoldóval, ahogy az (a) részben. Mennyire egyeznek meg a kapott válaszok egymással? Melyik megközelítés tűnik pontosabbnak? Mi $\boldsymbol{A}$ kondíciószáma, és milyen pontosságot sugall, hogy várnunk kellene? Próbáld ki az iteratív finomítást, hogy lássad, a kevésbé pontos módszernél javul-e a pontosság vagy a maradék.
