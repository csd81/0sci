### Áttekintő kérdések

- **3.1.** Igaz vagy hamis: Egy lineáris legkisebb négyzetes feladatnak mindig van megoldása.
- **3.2.** Igaz vagy hamis: Egyenes illesztése adatpontok halmazához lineáris legkisebb négyzetes feladat, míg másodfokú polinom illesztése ugyanezen adatokhoz nemlineáris legkisebb négyzetes feladat.
- **3.3.** Igaz vagy hamis: Az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldásában az $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ maradékvektor ortogonális a $\operatorname{span}(\boldsymbol{A})$ altérre.
- **3.4.** Igaz vagy hamis: Egy túlhatározott $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladatnak mindig van olyan egyértelmű $\boldsymbol{x}$ megoldása, amely minimalizálja az $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ maradékvektor euklideszi normáját.
- **3.5.** Igaz vagy hamis: Egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldásakor, ha a $\boldsymbol{b}$ vektor a $\operatorname{span}(\boldsymbol{A})$-ban fekszik, akkor a maradék $\boldsymbol{0}$.
- **3.6.** Igaz vagy hamis: Egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldásakor, ha a maradék $\boldsymbol{0}$, akkor az $\boldsymbol{x}$ megoldás szükségképpen egyértelmű.
- **3.7.** Igaz vagy hamis: Egy Householder-transzformáció és egy Givens-forgatás szorzata mindig ortogonális mátrix.
- **3.8.** Igaz vagy hamis: Ha az $n \times n$-es $\boldsymbol{Q}$ mátrix egy Householder-transzformáció, és $\boldsymbol{x}$ egy tetszőleges $n$-dimenziós vektor, akkor a $\boldsymbol{Q}\boldsymbol{x}$ vektor utolsó $k$ komponense nulla valamely $k < n$-re.
- **3.9.** Igaz vagy hamis: Az ortogonális felbontáson alapuló módszerek általában számítási szempontból költségesebbek, mint a normálegyenleteken alapuló módszerek a lineáris legkisebb négyzetes feladatok megoldására.
- **3.10.** (a) Egy adatillesztési feladatban, ahol $m$ darab $(t_i, y_i)$ adatpontot illesztünk egy $f(t, \boldsymbol{x})$ modellfüggvénnyel – ahol $t$ a független változó, $\boldsymbol{x}$ pedig a meghatározandó paraméterek $n$-dimenziós vektora –, mit jelent az, hogy $f$ lineáris az $\boldsymbol{x}$ komponenseiben? (b) Adj példát ilyen értelemben vett lineáris $f(t, \boldsymbol{x})$ modellfüggvényre. (c) Adj példát nemlineáris $f(t, \boldsymbol{x})$ modellfüggvényre.
- **3.11.** Egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladatban, ahol $\boldsymbol{A}$ egy $m \times n$-es mátrix, ha $\operatorname{rank}(\boldsymbol{A}) < n$, akkor az alábbi helyzetek közül melyek lehetségesek? (a) Nincs megoldás. (b) Egyetlen megoldás van. (c) Van megoldás, de nem egyértelmű.
- **3.12.** Egy túlhatározott $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladat megoldásakor melyik volna a súlyosabb nehézség: ha $\boldsymbol{A}$ sorai lineárisan összefüggők, vagy ha $\boldsymbol{A}$ oszlopai lineárisan összefüggők? Magyarázd meg.
- **3.13.** Egy túlhatározott lineáris legkisebb négyzetes feladatban, ahol a modellfüggvény $f(t, \boldsymbol{x}) = x_1 \varphi_1(t) + x_2 \varphi_2(t) + x_3 \varphi_3(t)$, mi lesz a kapott legkisebb négyzetes $\boldsymbol{A}$ mátrix rangja, ha $\varphi_1(t) = 1$, $\varphi_2(t) = t$ és $\varphi_3(t) = 1 - t$?
- **3.14.** Mi az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat normálegyenleteinek rendszere?
- **3.15.** Sorolj fel két módot, amelyeken a normálegyenletek használata a lineáris legkisebb négyzetes feladatok megoldására a numerikus pontosság elvesztésétől szenvedhet.
- **3.16.** Legyen $\boldsymbol{A}$ egy $m \times n$-es mátrix. Milyen feltételek mellett lesz az $\boldsymbol{A}^T \boldsymbol{A}$ mátrix (a) szimmetrikus? (b) nemszinguláris? (c) pozitív definit?
- **3.17.** Egy $m \times n$-es $\boldsymbol{A}$ mátrix ($m > n$) alábbi tulajdonságai közül melyek jelzik, hogy az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladat minimális maradékú megoldása nem egyértelmű? (a) $\boldsymbol{A}$ oszlopai lineárisan összefüggők. (b) $\boldsymbol{A}$ sorai lineárisan összefüggők. (c) Az $\boldsymbol{A}^T \boldsymbol{A}$ mátrix szinguláris.
- **3.18.** (a) Használható-e a főelemkiválasztással végzett Gauss-kiküszöbölés arra, hogy egy téglalap alakú $m \times n$-es $\boldsymbol{A}$ mátrix $\boldsymbol{L}\boldsymbol{U}$-felbontását kiszámítsuk, ahol $\boldsymbol{L}$ egy $m \times k$-s mátrix, amelynek a főátló feletti összes eleme nulla, $\boldsymbol{U}$ egy $k \times n$-es mátrix, amelynek a főátló alatti összes eleme nulla, és $k = \min\{m, n\}$? (b) Ha ez lehetséges volna, megoldási módot adna-e egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ túlhatározott legkisebb négyzetes feladatra, ahol $m > n$? Miért?
- **3.19.** (a) Mit jelent az, hogy két $\boldsymbol{x}$ és $\boldsymbol{y}$ vektor ortogonális egymásra? (b) Bizonyítsd be, hogy ha két nem nulla vektor ortogonális egymásra, akkor szükségképpen lineárisan függetlenek is. (c) Adj példát $\mathbb{R}^2$-ben két olyan nem nulla vektorra, amelyek ortogonálisak egymásra. (d) Adj példát $\mathbb{R}^2$-ben két olyan nem nulla vektorra, amelyek nem ortogonálisak egymásra. (e) Sorolj fel két módot, ahogyan az ortogonalitás fontos a lineáris legkisebb négyzetes feladatok kontextusában.
- **3.20.** Az euklideszi $n$-dimenziós térben tranzitív reláció-e az ortogonalitás? Azaz ha $\boldsymbol{x}$ ortogonális $\boldsymbol{y}$-ra, és $\boldsymbol{y}$ ortogonális $\boldsymbol{z}$-re, akkor $\boldsymbol{x}$ szükségképpen ortogonális-e $\boldsymbol{z}$-re?
- **3.21.** Mit értünk ortogonális projektor alatt? Miért releváns ez a fogalom a lineáris legkisebb négyzetek szempontjából?
- **3.22.** (a) Miért használnak gyakran ortogonális transzformációkat – például Householder- vagy Givens-típusúakat – a legkisebb négyzetes feladatok megoldására? (b) Miért nem használják gyakran az ilyen módszereket négyzetes lineáris egyenletrendszerek megoldására? (c) Van-e valamilyen előnye az ortogonális transzformációknak a Gauss-kiküszöböléssel szemben a négyzetes lineáris egyenletrendszerek megoldásában? Ha igen, nevezz meg egyet.
- **3.23.** Az alábbi mátrixok közül melyek ortogonálisak? (a) $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ (b) $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ (c) $\begin{bmatrix} 2 & 0 \\ 0 & 1/2 \end{bmatrix}$ (d) $\begin{bmatrix} \sqrt{2}/2 & \sqrt{2}/2 \\ -\sqrt{2}/2 & \sqrt{2}/2 \end{bmatrix}$
- **3.24.** Egy $n \times n$-es ortogonális mátrix szükségképpen mely tulajdonságokkal rendelkezik az alábbiak közül? (a) Nemszinguláris. (b) Megőrzi egy vektor euklideszi normáját, amikor a vektorral szorozzák. (c) A transzponáltja az inverze. (d) Az oszlopai ortonormáltak. (e) Szimmetrikus. (f) Diagonális. (g) Az euklideszi mátrixnormája $1$. (h) Az euklideszi kondíciószáma $1$.
- **3.25.** Az alábbi mátrixtípusok közül melyek szükségképpen ortogonálisak? (a) Permutáció. (b) Szimmetrikus pozitív definit. (c) Householder-transzformáció. (d) Givens-forgatás. (e) Nemszinguláris. (f) Diagonális.
- **3.26.** Mutasd meg, hogy egy ortogonális mátrixszal való szorzás megőrzi egy vektor euklideszi normáját.
- **3.27.** Milyen feltételt kell teljesítenie egy nem nulla $n$-dimenziós $\boldsymbol{w}$ vektornak ahhoz, hogy a $\boldsymbol{H} = \boldsymbol{I} - 2\boldsymbol{w}\boldsymbol{w}^T$ mátrix ortogonális legyen?
- **3.28.** Ha $\boldsymbol{Q}$ egy olyan $2 \times 2$-es ortogonális mátrix, amelyre

$$\boldsymbol{Q}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \end{bmatrix},$$

akkor mi $\alpha$ értéke?

- **3.29.** Hány skalárszorzásra van szükség ahhoz, hogy egy tetszőleges $n$-dimenziós vektort megszorozzunk egy $n \times n$-es $\boldsymbol{H} = \boldsymbol{I} - 2\boldsymbol{w}\boldsymbol{w}^T$ Householder-transzformációs mátrixszal, ahol $\boldsymbol{w}$ egy $n$-dimenziós vektor $\|\boldsymbol{w}\|_2 = 1$-gyel?
- **3.30.** Adott egy $\boldsymbol{a}$ vektor; egy olyan $\boldsymbol{H}$ Householder-transzformáció tervezésekor, amelyre $\boldsymbol{H}\boldsymbol{a} = \alpha \boldsymbol{e}_1$, tudjuk, hogy $\alpha = \pm \|\boldsymbol{a}\|_2$. Milyen alapon kell az előjelet megválasztani?
- **3.31.** Sorolj fel egy előnyt és egy hátrányt, amelyeket a Givens-forgatások nyújtanak a QR-felbontásban a Householder-transzformációkkal szemben.
- **3.32.** Amikor egy $2$-dimenziós vektor második komponensének nullázására használjuk, mindig ugyanazt az eredményt adja-e egy Householder-transzformáció, mint egy Givens-forgatás?
- **3.33.** Az $\boldsymbol{A}$ mátrixot tartalmazó – felülírható – bemeneti tömbön túl mennyi további kisegítő tömbmemória szükséges az alábbiak kiszámításához és tárolásához? (a) $\boldsymbol{A}$ LU-felbontása részleges főelemkiválasztással végzett Gauss-kiküszöböléssel, ahol $\boldsymbol{A}$ egy $n \times n$-es mátrix. (b) $\boldsymbol{A}$ QR-felbontása Householder-transzformációkkal, ahol $\boldsymbol{A}$ egy $m \times n$-es mátrix.
- **3.34.** Egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldásakor – ahol $\boldsymbol{A}$ egy $m \times n$-es mátrix, $m \ge n$ és $\operatorname{rank}(\boldsymbol{A}) < n$ – a legkisebb négyzetes megoldási folyamat melyik pontján fog megakadni (egzakt aritmetikát feltételezve)? (a) A normálegyenletek Cholesky-felbontással történő megoldása esetén. (b) Householder-transzformációkkal végzett QR-felbontás esetén.
- **3.35.** A klasszikus Gram–Schmidt-eljáráshoz képest az alábbiak közül melyek a módosított Gram–Schmidt-ortogonalizáció előnyei? (a) Kevesebb memóriát igényel. (b) Kevesebb munkát igényel. (c) Numerikusan stabilabb.
- **3.36.** Egy $m \times n$-es mátrix ($m \ge n$) QR-felbontásához $n$-nek milyen nagynak kell lennie, mielőtt a klasszikus és a módosított Gram–Schmidt-eljárás között különbség mutatkozna?
- **3.37.** Magyarázd meg, miért igényel kevesebb memóriát a Householder-módszer az $\boldsymbol{A}$ mátrix QR-felbontásának kiszámítására, mint a módosított Gram–Schmidt-módszer.
- **3.38.** Magyarázd meg, hogyan használható az oszloponkénti főelemkiválasztással végzett QR-felbontás egy mátrix rangjának meghatározására.
- **3.39.** Magyarázd meg, hogy az oszloponkénti főelemkiválasztás miért használható a módosított Gram–Schmidt-ortogonalizációs eljárással, a klasszikus Gram–Schmidt-eljárással azonban nem.
- **3.40.** Az $\boldsymbol{A}$ mátrix kondíciószámának függvényében hasonlítsd össze a normálegyenletek módszerének és a Householder-féle QR-módszernek az alkalmazhatósági tartományát az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldására [azaz $\operatorname{cond}(\boldsymbol{A})$ mely értékeire várható, hogy az egyes módszerek megakadnak?].
- **3.41.** Legyen $\boldsymbol{A}$ egy $m \times n$-es mátrix. (a) Mi a legnagyobb száma azoknak a nem nulla szinguláris értékeknek, amelyek $\boldsymbol{A}$-nak lehetnek? (b) Ha $\operatorname{rank}(\boldsymbol{A}) = k$, hány nem nulla szinguláris értéke van $\boldsymbol{A}$-nak?
- **3.42.** Legyen $\boldsymbol{a}$ egy nem nulla oszlopvektor. $n \times 1$-es mátrixnak tekintve $\boldsymbol{a}$-nak csak egyetlen pozitív szinguláris értéke van. Mennyi ez az érték?
- **3.43.** Fejezd ki egy mátrix euklideszi kondíciószámát a szinguláris értékeivel.
- **3.44.** Sorolj fel két megbízható módszert egy téglalap alakú mátrix rangjának numerikus meghatározására.
- **3.45.** Ha $\boldsymbol{A}$ egy $2n \times n$-es mátrix, rangsorold az alábbi módszereket az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldásához szükséges munka mennyisége szerint. (a) Householder-transzformációkkal végzett QR-felbontás. (b) Normálegyenletek. (c) Szingulárisérték-felbontás.
- **3.46.** Sorolj fel legalább két alkalmazást egy mátrix szingulárisérték-felbontására (SVD) a legkisebb négyzetes feladatok megoldásán kívül.

### Feladatok

- **3.1.** Ha egy függőleges tartóra a rúd alsó végén lefelé ható erő nehezedik, akkor a tartó megnyúlásának mértéke arányos lesz az erő nagyságával. Így a tartó teljes $y$ hosszát az

$$y = x_1 + x_2 t$$

egyenlet adja, ahol $x_1$ az eredeti hossza, $t$ a ható erő, $x_2$ pedig az arányossági állandó. Tegyük fel, hogy az alábbi méréseket végezzük:

$$\begin{array}{c|ccc} t & 10 & 15 & 20 \\ \hline y & 11{,}60 & 11{,}85 & 12{,}25 \end{array}$$

- (a) Írd fel a gyűjtött adatoknak megfelelő $3 \times 2$-es túlhatározott lineáris egyenletrendszert!
- (b) Konzisztens-e ez a rendszer? Ha nem, számítsd ki $(x_1, x_2)$ minden lehetséges értékpárját, amelyet a rendszerből bármely két egyenlet kiválasztásával kapunk! Van-e bármilyen ok, amiért ezen eredmények közül bármelyiket előnyben részesítenénk?
- (c) Írd fel a normálegyenletek rendszerét, és oldd meg, hogy megkapd a túlhatározott rendszer legkisebb négyzetes megoldását! Hasonlítsd össze az eredményed a (b) részben kapottakkal!

- **3.2.** Tegyük fel, hogy egy egyenest illesztesz a $(0, 1)$, $(1, 2)$, $(3, 3)$ három adatponthoz.
- (a) Írd fel a legkisebb négyzetes feladat túlhatározott lineáris egyenletrendszerét!
- (b) Írd fel a hozzá tartozó normálegyenleteket!
- (c) Számítsd ki a legkisebb négyzetes megoldást Cholesky-felbontással!

- **3.3.** Írd fel az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes rendszert az $f(t, \boldsymbol{x}) = x_1 t + x_2 e^t$ modellfüggvénynek az $(1, 2)$, $(2, 3)$, $(3, 5)$ három adatponthoz való illesztéséhez!

- **3.4.** Egy $y = x_0 + x_1 t$ egyenesnek a $(t_i, y_i) = (0, 0), (1, 0), (1, 1)$ három adatponthoz való illesztésekor egyértelmű-e a legkisebb négyzetes megoldás? Miért?

- **3.5.** Legyen $\boldsymbol{x}$ az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldása, ahol

$$\boldsymbol{A} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}.$$

Legyen $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ a hozzá tartozó maradékvektor. Az alábbi három vektor közül melyik lehet $\boldsymbol{r}$ lehetséges értéke? Miért?

$$(a)\ \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} \qquad (b)\ \begin{bmatrix} -1 \\ -1 \\ 1 \\ 1 \end{bmatrix} \qquad (c)\ \begin{bmatrix} -1 \\ 1 \\ 1 \\ -1 \end{bmatrix}$$

- **3.6.** (a) Mi a minimális maradékvektor euklideszi normája az alábbi lineáris legkisebb négyzetes feladat esetén?

$$\begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \cong \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix}$$

(b) Mi ennek a feladatnak az $\boldsymbol{x}$ megoldásvektora?

- **3.7.** Legyen $\boldsymbol{A}$ egy $m \times n$-es mátrix és $\boldsymbol{b}$ egy $m$-dimenziós vektor. (a) Bizonyítsd be, hogy az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladatnak mindig van megoldása! (b) Bizonyítsd be, hogy az ilyen megoldás akkor és csak akkor egyértelmű, ha $\operatorname{rank}(\boldsymbol{A}) = n$!

- **3.8.** Tegyük fel, hogy $\boldsymbol{A}$ egy $n$ rangú $m \times n$-es mátrix. Bizonyítsd be, hogy az $\boldsymbol{A}^T \boldsymbol{A}$ mátrix pozitív definit!

- **3.9.** Bizonyítsd be, hogy a 3.4.2. szakaszban szereplő bővített rendszer mátrixa *nem* lehet pozitív definit!

- **3.10.** Legyen $\boldsymbol{B}$ egy $n \times n$-es mátrix, és tegyük fel, hogy $\boldsymbol{B}$ egyszerre ortogonális és háromszögmátrix.
- (a) Bizonyítsd be, hogy $\boldsymbol{B}$-nek diagonálisnak kell lennie!
- (b) Melyek $\boldsymbol{B}$ főátlóbeli elemei?
- (c) Legyen $\boldsymbol{A}$ egy $n \times n$-es nemszinguláris mátrix. Az (a) és (b) részek felhasználásával bizonyítsd be, hogy $\boldsymbol{A}$ QR-felbontása egyértelmű az $\boldsymbol{R}$ főátlóbeli elemeinek előjelétől eltekintve! Konkrétabban, léteznek olyan egyértelmű $\boldsymbol{Q}$ és $\boldsymbol{R}$ mátrixok, amelyekre $\boldsymbol{Q}$ ortogonális, $\boldsymbol{R}$ felső háromszögmátrix pozitív elemekkel a főátlóban, és $\boldsymbol{A} = \boldsymbol{Q}\boldsymbol{R}$.

- **3.11.** Tegyük fel, hogy a

$$\begin{bmatrix} \boldsymbol{A} & \boldsymbol{B} \\ \boldsymbol{O} & \boldsymbol{C} \end{bmatrix}$$

particionált mátrix ortogonális, ahol az $\boldsymbol{A}$ és $\boldsymbol{C}$ almátrixok négyzetesek. Bizonyítsd be, hogy $\boldsymbol{A}$ és $\boldsymbol{C}$ szükségképpen ortogonálisak, és $\boldsymbol{B} = \boldsymbol{O}$!

- **3.12.** (a) Legyen $\boldsymbol{A}$ egy $n \times n$-es mátrix. Mutasd meg, hogy az alábbi feltételek közül bármely kettőből következik a harmadik:
- 1. $\boldsymbol{A}^T = \boldsymbol{A}$
- 2. $\boldsymbol{A}^T \boldsymbol{A} = \boldsymbol{I}$
- 3. $\boldsymbol{A}^2 = \boldsymbol{I}$
- (b) Adj konkrét példát – az $\boldsymbol{I}$ egységmátrixon vagy annak permutációján kívül – egy olyan $3 \times 3$-as mátrixra, amely mindhárom tulajdonsággal rendelkezik!
- (c) Nevezz meg egy nemtriviális mátrixosztályt, amelynek elemei mindhárom tulajdonsággal rendelkeznek!

- **3.13.** Ha $\boldsymbol{A}$ egyszerre ortogonális mátrix és ortogonális projektor, mit tudsz mondani $\boldsymbol{A}$-ról?

- **3.14.** Mutasd meg, hogy ha a $\boldsymbol{v} \neq \boldsymbol{0}$ vektor, akkor a

$$\boldsymbol{H} = \boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T \boldsymbol{v}}$$

mátrix ortogonális és szimmetrikus!

- **3.15.** Legyen $\boldsymbol{a}$ tetszőleges nem nulla vektor. Ha $\boldsymbol{v} = \boldsymbol{a} - \alpha \boldsymbol{e}_1$, ahol $\alpha = \pm \|\boldsymbol{a}\|_2$, és

$$\boldsymbol{H} = \boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T \boldsymbol{v}},$$

mutasd meg, hogy $\boldsymbol{H}\boldsymbol{a} = \alpha \boldsymbol{e}_1$!

- **3.16.** Tekintsd az $\boldsymbol{a}$ vektort $n \times 1$-es mátrixként.
- (a) Írd fel a redukált QR-felbontását, és mutasd be explicit módon a $\boldsymbol{Q}$ és $\boldsymbol{R}$ mátrixokat!
- (b) Mi az $\boldsymbol{a}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldása, ahol $\boldsymbol{b}$ egy adott $n$-dimenziós vektor?

- **3.17.** Határozd meg azt a Householder-transzformációt, amely az $\begin{bmatrix} 1 & 1 & 1 & 1 \end{bmatrix}^T$ vektor első elemén kívül minden elemét nullázza! Konkrétabban, ha

$$\left(\boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T \boldsymbol{v}}\right) \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \\ 0 \\ 0 \end{bmatrix},$$

melyek az $\alpha$ és $\boldsymbol{v}$ értékei?

- **3.18.** Tegyük fel, hogy az

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \\ 1 & 4 & 16 \end{bmatrix}$$

mátrix QR-felbontását Householder-transzformációkkal számítod.
- (a) Hány Householder-transzformációra van szükség?
- (b) Mivé válik $\boldsymbol{A}$ első oszlopa az első Householder-transzformáció alkalmazásának eredményeként?
- (c) Mivé válik ezután az első oszlop a második Householder-transzformáció alkalmazásának eredményeként?
- (d) Hány Givens-forgatásra lenne szükség $\boldsymbol{A}$ QR-felbontásának kiszámításához?

- **3.19.** Tekintsd az

$$\boldsymbol{a} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$$

vektort.
- (a) Adj meg egy elemi eliminációs mátrixot, amely $\boldsymbol{a}$ harmadik komponensét nullázza!
- (b) Adj meg egy Householder-transzformációt, amely $\boldsymbol{a}$ harmadik komponensét nullázza!
- (c) Adj meg egy Givens-forgatást, amely $\boldsymbol{a}$ harmadik komponensét nullázza!
- (d) Egy tetszőleges vektor adott nem nulla komponensének nullázásakor lehetséges-e valaha, hogy a megfelelő elemi eliminációs mátrix és Householder-transzformáció azonos? Miért?
- (e) Egy tetszőleges vektor adott nem nulla komponensének nullázásakor lehetséges-e valaha, hogy a megfelelő Householder-transzformáció és Givens-forgatás azonos? Miért?

- **3.20.** Tegyük fel, hogy egy

$$\boldsymbol{a} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$$

vektor második komponensét szeretnéd nullázni egy Givens-forgatással, de $a_1$ már eleve nulla.
- (a) Lehetséges-e még mindig nullázni $a_2$-t egy Givens-forgatással? Ha igen, adj meg egy megfelelő Givens-forgatást; ha nem, magyarázd meg, miért!
- (b) Ilyen körülmények között nullázható-e $a_2$ elemi eliminációs mátrixszal? Ha igen, hogyan? Ha nem, miért?

- **3.21.** Egy Givens-forgatást két paraméter, $c$ és $s$ határoz meg, és így egy számítógépes implementációban látszólag két tárolóhelyet igényelne. A két paraméter azonban egyetlen forgatási szögtől függ, így elvileg lehetséges volna a forgatás csupán egyetlen szám tárolásával történő feljegyzése. Dolgozz ki egy sémát a Givens-forgatások tárolására és visszaállítására, amely forgatásonként mindössze egy tárolóhelyet használ!

- **3.22.** Legyen $\boldsymbol{A}$ egy $n$ rangú $m \times n$-es mátrix. Legyen

$$\boldsymbol{A} = \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}$$

$\boldsymbol{A}$ QR-felbontása, ahol $\boldsymbol{Q}$ ortogonális és $\boldsymbol{R}$ egy $n \times n$-es felső háromszögmátrix. Legyen $\boldsymbol{A}^T \boldsymbol{A} = \boldsymbol{L}\boldsymbol{L}^T$ az $\boldsymbol{A}^T \boldsymbol{A}$ Cholesky-felbontása.
- (a) Mutasd meg, hogy $\boldsymbol{R}^T \boldsymbol{R} = \boldsymbol{L}\boldsymbol{L}^T$!
- (b) Következtethetjük-e, hogy $\boldsymbol{R} = \boldsymbol{L}^T$? Miért?

- **3.23.** A 3.4.1. szakaszban megfigyeltük, hogy az $\boldsymbol{A}^T \boldsymbol{A}$ keresztszorzat-mátrix lebegőpontos aritmetikában egzaktul szinguláris, ha

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 \\ \epsilon & 0 \\ 0 & \epsilon \end{bmatrix},$$

ahol $\epsilon$ egy olyan pozitív szám, amely kisebb, mint $\sqrt{\epsilon_{\text{mach}}}$ egy adott lebegőpontos rendszerben. Mutasd meg, hogy ha $\boldsymbol{A} = \boldsymbol{Q}\boldsymbol{R}$ ennek az $\boldsymbol{A}$ mátrixnak a redukált QR-felbontása, akkor $\boldsymbol{R}$ nem szinguláris, még lebegőpontos aritmetikában sem!

- **3.24.** Ellenőrizd, hogy egy $m \times n$-es lineáris legkisebb négyzetes feladat normálegyenletekkel és Cholesky-felbontással történő megoldásának műveletszámában (szorzások vagy összeadások számában) a domináns tag $mn^2/2 + n^3/6$!

- **3.25.** Ellenőrizd, hogy egy $m \times n$-es mátrix Householder-transzformációkkal végzett QR-felbontásának műveletszámában (szorzások vagy összeadások számában) a domináns tag $mn^2 - n^3/3$!

- **3.26.** Legyen $c = \cos(\theta)$ és $s = \sin(\theta)$ valamilyen $\theta$ szögre. Adj részletes geometriai leírást az alábbi $2 \times 2$-es ortogonális mátrixok mindegyikének $\mathbb{R}^2$ euklideszi síkbeli vektorokra gyakorolt hatásairól!

$$(a)\ \boldsymbol{G} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} \qquad (b)\ \boldsymbol{H} = \begin{bmatrix} -c & s \\ s & c \end{bmatrix}$$

- **3.27.** (a) Tegyük fel, hogy $\boldsymbol{Q}$ egy olyan $n \times k$-s mátrix, amelynek oszlopai ortonormált bázist alkotnak $\mathbb{R}^n$ egy $S$ alterének. Mutasd meg, hogy $\boldsymbol{Q}\boldsymbol{Q}^T$ ortogonális projektor $S$-re!
- (b) Ha $\boldsymbol{A}$ lineárisan független oszlopokkal rendelkező mátrix, mutasd meg, hogy $\boldsymbol{A}(\boldsymbol{A}^T \boldsymbol{A})^{-1}\boldsymbol{A}^T$ ortogonális projektor a $\operatorname{span}(\boldsymbol{A})$-ra! Hogyan kapcsolódik ez az eredmény a lineáris legkisebb négyzetes feladathoz?
- (c) Ha $\boldsymbol{P}$ ortogonális projektor egy $S$ altérre, mutasd meg, hogy $\boldsymbol{I} - \boldsymbol{P}$ ortogonális projektor $S$ ortogonális komplementumára!
- (d) Legyen $\boldsymbol{v}$ egy tetszőleges nem nulla $n$-dimenziós vektor. Mi a $\boldsymbol{v}$ által kifeszített altérre vett ortogonális projektor?

- **3.28.** (a) A 3.5.3. szakasz Gram–Schmidt-eljárásában, ha a $\boldsymbol{P}_k = \boldsymbol{q}_k \boldsymbol{q}_k^T$ ($k = 1, \ldots, n$) ortogonális projektorokat definiáljuk – ahol $\boldsymbol{q}_k$ a kapott QR-felbontásbeli $\boldsymbol{Q}$ $k$-adik oszlopa –, mutasd meg, hogy

$$(\boldsymbol{I} - \boldsymbol{P}_k)(\boldsymbol{I} - \boldsymbol{P}_{k-1}) \cdots (\boldsymbol{I} - \boldsymbol{P}_1) = \boldsymbol{I} - \boldsymbol{P}_k - \boldsymbol{P}_{k-1} - \cdots - \boldsymbol{P}_1!$$

(b) Mutasd meg, hogy a klasszikus Gram–Schmidt-eljárás ekvivalens a

$$\boldsymbol{q}_k = (\boldsymbol{I} - (\boldsymbol{P}_1 + \cdots + \boldsymbol{P}_{k-1}))\boldsymbol{a}_k$$

formulával!

(c) Mutasd meg, hogy a módosított Gram–Schmidt-eljárás ekvivalens a

$$\boldsymbol{q}_k = (\boldsymbol{I} - \boldsymbol{P}_{k-1}) \cdots (\boldsymbol{I} - \boldsymbol{P}_1)\boldsymbol{a}_k$$

formulával!

(d) A klasszikus eljárás stabilizálásának egy másik módja, hogy többször alkalmazzuk (azaz iteratív finomítás), ami azt jelenti, hogy

$$\boldsymbol{q}_k = (\boldsymbol{I} - (\boldsymbol{P}_1 + \cdots + \boldsymbol{P}_{k-1}))^m \boldsymbol{a}_k,$$

ahol $m = 2$ tipikusan elegendő. Mutasd meg, hogy mindhárom változat matematikailag ekvivalens (bár véges precíziós aritmetikában jelentősen eltérhetnek)!

- **3.29.** Legyen $\boldsymbol{v}$ egy nem nulla $n$-dimenziós vektor. A $\boldsymbol{v}$-re merőleges hipersík azoknak a $\boldsymbol{z}$ vektoroknak az $(n-1)$-dimenziós altere, amelyekre $\boldsymbol{v}^T \boldsymbol{z} = 0$. Egy $\boldsymbol{R}$ reflektor olyan lineáris transzformáció, amelyre $\boldsymbol{R}\boldsymbol{x} = -\boldsymbol{x}$, ha $\boldsymbol{x}$ a $\boldsymbol{v}$ skalárszorosa, és $\boldsymbol{R}\boldsymbol{x} = \boldsymbol{x}$, ha $\boldsymbol{v}^T \boldsymbol{x} = 0$. Így a hipersík tükörként viselkedik: tetszőleges vektor hipersíkon belüli komponense változatlan marad, míg a hipersíkra ortogonális komponense előjelet vált.
- (a) Mutasd meg, hogy $\boldsymbol{R} = 2\boldsymbol{P} - \boldsymbol{I}$, ahol $\boldsymbol{P}$ a $\boldsymbol{v}$-re merőleges hipersíkra vett ortogonális projektor! Rajzolj ábrát az eredmény szemléltetésére!
- (b) Mutasd meg, hogy $\boldsymbol{R}$ szimmetrikus és ortogonális!
- (c) Mutasd meg, hogy a

$$\boldsymbol{H} = \boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T \boldsymbol{v}}$$

Householder-transzformáció reflektor!
- (d) Mutasd meg, hogy bármely két $\boldsymbol{s}$ és $\boldsymbol{t}$ vektorra, amelyekre $\boldsymbol{s} \neq \boldsymbol{t}$ és $\|\boldsymbol{s}\|_2 = \|\boldsymbol{t}\|_2$, létezik olyan $\boldsymbol{R}$ reflektor, amelyre $\boldsymbol{R}\boldsymbol{s} = \boldsymbol{t}$!
- (e) Mutasd meg, hogy bármely $\boldsymbol{Q}$ ortogonális mátrix reflektorok szorzata!
- (f) Szemléltesd az előző eredményt azzal, hogy a

$$\begin{bmatrix} c & s \\ -s & c \end{bmatrix}$$

síkbeli forgatást – ahol $c^2 + s^2 = 1$ – két reflektor szorzataként fejezed ki! Konkrét forgatási szögre rajzolj ábrát a tükrök bemutatására!

- **3.30.** (a) Tekintsd az $\boldsymbol{a}$ oszlopvektort $n \times 1$-es mátrixként. Írd fel a redukált szingulárisérték-felbontását, és mutasd be explicit módon az $\boldsymbol{U}$, $\boldsymbol{\Sigma}$ és $\boldsymbol{V}$ mátrixokat!
- (b) Tekintsd az $\boldsymbol{a}^T$ sorvektort $1 \times n$-es mátrixként. Írd fel a redukált SVD-jét, és mutasd be explicit módon az $\boldsymbol{U}$, $\boldsymbol{\Sigma}$ és $\boldsymbol{V}$ mátrixokat!

- **3.31.** Ha $\boldsymbol{A}$ egy $m \times n$-es mátrix és $\boldsymbol{b}$ egy $m$-dimenziós vektor, bizonyítsd be, hogy az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladat minimális euklideszi normájú $\boldsymbol{x}$ megoldását a

$$\boldsymbol{x} = \sum_{\sigma_i \neq 0} \frac{\boldsymbol{u}_i^T \boldsymbol{b}}{\sigma_i}\,\boldsymbol{v}_i$$

képlet adja, ahol a $\sigma_i$, $\boldsymbol{u}_i$ és $\boldsymbol{v}_i$ az $\boldsymbol{A}$ szinguláris értékei és a megfelelő szinguláris vektorai!

- **3.32.** Bizonyítsd be, hogy egy $m \times n$-es $\boldsymbol{A}$ mátrix $\boldsymbol{A}^{+}$ pszeudoinverze – ahogyan azt a 3.6.1. szakaszban az SVD segítségével definiáltuk – teljesíti az alábbi négy tulajdonságot, amelyeket Moore–Penrose-feltételeknek nevezünk.
- (a) $\boldsymbol{A}\boldsymbol{A}^{+}\boldsymbol{A} = \boldsymbol{A}$.
- (b) $\boldsymbol{A}^{+}\boldsymbol{A}\boldsymbol{A}^{+} = \boldsymbol{A}^{+}$.
- (c) $(\boldsymbol{A}\boldsymbol{A}^{+})^T = \boldsymbol{A}\boldsymbol{A}^{+}$.
- (d) $(\boldsymbol{A}^{+}\boldsymbol{A})^T = \boldsymbol{A}^{+}\boldsymbol{A}$.

- **3.33.** Bizonyítsd be, hogy egy $m \times n$-es $\boldsymbol{A}$ mátrix $\boldsymbol{A}^{+}$ pszeudoinverze – ahogyan azt a 3.6.1. szakaszban az SVD segítségével definiáltuk – az alábbi speciális esetek mindegyikében a megadott értéket veszi fel.
- (a) Ha $m = n$ és $\boldsymbol{A}$ nemszinguláris, akkor $\boldsymbol{A}^{+} = \boldsymbol{A}^{-1}$.
- (b) Ha $m > n$ és $\boldsymbol{A}$ rangja $n$, akkor $\boldsymbol{A}^{+} = (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T$.
- (c) Ha $m < n$ és $\boldsymbol{A}$ rangja $m$, akkor $\boldsymbol{A}^{+} = \boldsymbol{A}^T (\boldsymbol{A}\boldsymbol{A}^T)^{-1}$.

- **3.34.** (a) Mi az alábbi mátrix pszeudoinverze?

$$\boldsymbol{A}_0 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$

(b) Ha $\epsilon > 0$, mi az alábbi mátrix pszeudoinverze?

$$\boldsymbol{A}_\epsilon = \begin{bmatrix} 1 & 0 \\ 0 & \epsilon \end{bmatrix}$$

(c) Mit implikálnak ezek az eredmények egy adott mátrix pszeudoinverzének kiszámítási feladatának kondicionáltságára?

### Számítógépes feladatok

- **3.1.** $n = 0, 1, \ldots, 5$ esetén illessz legkisebb négyzetek módszerével $n$-edfokú polinomot az alábbi adatokra:

$$\begin{array}{c|ccccccccccc}
t & -1{,}0 & -0{,}5 & 0{,}0 & 0{,}5 & 1{,}0 & 1{,}5 & 2{,}0 & 2{,}5 & 3{,}0 & 3{,}5 & 4{,}0 \\ \hline
y & 1{,}0 & 0{,}5 & 0{,}0 & 0{,}5 & 2{,}0 & 3{,}5 & 3{,}0 & 2{,}5 & 2{,}5 & 3{,}0 & 3{,}5
\end{array}$$

Készíts ábrát az eredeti adatpontokról és mindegyik kapott polinomgörbéről (készíthetsz külön grafikont minden görbéhez, vagy egyetlen, az összes görbét tartalmazó grafikont). Melyik polinomot mondanád olyannak, amely jobban megragadja az adatok általános trendjét? Nyilvánvalóan ez szubjektív kérdés, és a válasza egyaránt függ az adott adatok természetétől (pl. az adatértékek bizonytalanságától) és az illesztés céljától. Magyarázd meg a válaszadáshoz tett feltételezéseidet!

- **3.2.** A földmérésben gyakori feladat egy sor pont magasságának meghatározása egy referenciaponthoz képest. A mérések hibával terheltek, ezért több megfigyelést végzünk, mint amennyi a magasságok meghatározásához szigorú értelemben szükséges volna, és a kapott túlhatározott rendszert legkisebb négyzetes értelemben oldjuk meg a hibák kisimítására. Tegyük fel, hogy négy pont van, amelyek $x_1, x_2, x_3, x_4$ magasságát kell meghatározni. Az egyes $x_i$-k referenciaponthoz viszonyított közvetlen mérésein túl méréseket végzünk az egyes pontokra a többi pont mindegyikéhez viszonyítva is. A kapott mérések:

$$\begin{aligned}
x_1 &= 2{,}95, & x_2 &= 1{,}74, & x_3 &= -1{,}45, & x_4 &= 1{,}32, \\
x_1 - x_2 &= 1{,}23, & x_1 - x_3 &= 4{,}45, & x_1 - x_4 &= 1{,}61, \\
x_2 - x_3 &= 3{,}21, & x_2 - x_4 &= 0{,}45, & x_3 - x_4 &= -2{,}75.
\end{aligned}$$

Írd fel a hozzá tartozó $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes rendszert, és egy könyvtári rutinnal – vagy egy saját tervezésűvel – oldd meg, hogy a magasságok legjobb értékeit megkapd! Hogyan viszonyulnak a számított értékek a közvetlen mérésekhez?

- **3.3.** (a) Egy sor $n$-ed rendű $\boldsymbol{A}$ mátrixra jegyezd fel egy könyvtári rutin $\boldsymbol{A}$ LU-felbontásának kiszámításához szükséges futási idejét! Egy lineáris legkisebb négyzetes rutin – vagy egy saját tervezésű – használatával illessz harmadfokú polinomot a futási időkre $n$ függvényében! Megbízható eredmények elérése érdekében használj meglehetősen széles $n$-tartományt, mondjuk $100$-tól kezdve több százig, $100$-as lépésekben, az általad használt számítógép sebességétől és rendelkezésre álló memóriájától függően. Pontosabb időmérést kaphatsz, ha adott mátrixméretnél több futást átlagolsz. A kapott harmadfokú polinom felhasználható lenne más, ki nem próbált $n$-értékekre – például nagyon nagy $n$-értékekre – való futási idő előrejelzésére. Mi az előrejelzett futási idő egy $10\,000$-ed rendű mátrixra?
- (b) Próbáld meg meghatározni a számítógéped alapvető végrehajtási sebességét (lebegőpontos műveletek másodpercenkénti számában, azaz FLOP-okban) egy ismert számítás – például mátrixszorzás – időmérésével! Ezután ezt az információt felhasználhatod arra, hogy a futási időkre illesztett polinom alapján meghatározd az LU-felbontás komplexitását. Lebegőpontos műveletekre átváltva hogyan viszonyul a domináns tag a $4n^3/3$ elméletileg várt értékhez (mind az összeadásokat, mind a szorzásokat számolva)? Próbáld megmagyarázni az eltérést! Ha olyan rendszert használsz, amely automatikusan szolgáltat műveletszámokat, próbáld ki ugyanezt a kísérletet úgy is, hogy közvetlenül a műveletszámokra illesztesz!

- **3.4.** (a) Oldd meg az alábbi legkisebb négyzetes feladatot tetszőleges módszerrel!

$$\begin{bmatrix} 0{,}16 & 0{,}10 \\ 0{,}17 & 0{,}11 \\ 2{,}02 & 1{,}29 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \cong \begin{bmatrix} 0{,}26 \\ 0{,}28 \\ 3{,}31 \end{bmatrix}.$$

(b) Most oldd meg ugyanazt a legkisebb négyzetes feladatot újra, de ezúttal használd az enyhén perturbált

$$\boldsymbol{b} = \begin{bmatrix} 0{,}27 \\ 0{,}25 \\ 3{,}33 \end{bmatrix}$$

jobb oldali vektort!

(c) Hasonlítsd össze az (a) és (b) részekből származó eredményeidet! Meg tudod-e magyarázni ezt a különbséget?

- **3.5.** Egy bolygó ellipszispályán mozog, amely egy $(x, y)$ derékszögű koordináta-rendszerben az

$$ay^2 + bxy + cx + dy + e = x^2$$

egyenlettel ábrázolható.

(a) Egy lineáris legkisebb négyzetes könyvtári rutinnal – vagy egy saját tervezésűvel – határozd meg az $a, b, c, d, e$ pályaparamétereket a bolygó helyzetének alábbi megfigyelései alapján:

$$\begin{array}{c|cccccccccc}
x & 1{,}02 & 0{,}95 & 0{,}87 & 0{,}77 & 0{,}67 & 0{,}56 & 0{,}44 & 0{,}30 & 0{,}16 & 0{,}01 \\ \hline
y & 0{,}39 & 0{,}32 & 0{,}27 & 0{,}22 & 0{,}18 & 0{,}15 & 0{,}13 & 0{,}12 & 0{,}13 & 0{,}15
\end{array}$$

A pályaparaméterek értékeinek kinyomtatása mellett ábrázold a kapott pályát és a megadott adatpontokat is az $(x, y)$ síkon.

- (b) Ez a legkisebb négyzetes feladat majdnem ranghiányos. Hogy lásd, ennek milyen hatása van a megoldásra, perturbáld az input adatokat enyhén úgy, hogy minden adatpont minden koordinátájához adsz egy $[-0{,}005, 0{,}005]$ intervallumon egyenletes eloszlású véletlen számot (lásd a 13.5. szakaszt), és oldd meg a legkisebb négyzetes feladatot a perturbált adatokkal! Hasonlítsd össze a paraméterek új értékeit a korábban kiszámítottakkal! Milyen hatással van ez a különbség a pálya ábrájára? Meg tudod-e magyarázni ezt a viselkedést?
- (c) Oldd meg ugyanazt a legkisebb négyzetes feladatot újra, mind az eredeti, mind a perturbált adatokra, ezúttal olyan könyvtári rutinnal (vagy egy saját tervezésűvel), amelyet kifejezetten ranghiány kezelésére terveztek (például oszloponkénti főelemkiválasztással)! Egy ilyen rutin általában bemeneti paraméterként tartalmaz egy toleranciát a mátrix numerikus rangjának meghatározásához. Kísérletezz különböző toleranciaértékekkel, mondjuk $10^{-k}$-val, $k = 1, \ldots, 5$ mellett. Mi a mátrix kapott rangja az egyes toleranciaértékekre? Hasonlítsd össze a két megoldás (az eredeti és a perturbált adatokra vonatkozó) viselkedését egymással, ahogy a tolerancia és a kapott rang változik! Mennyire jól illeszkednek a kapott pályák az adatpontokra, ahogy a tolerancia és a rang változik? Melyik megoldást tartanád jobbnak: azt, amelyik szorosabban illeszkedik az adatokra, vagy azt, amelyik kevésbé érzékeny az adatok kis perturbációira? Miért?
- (d) Egy könyvtári rutinnal számítsd ki a $10 \times 5$-ös legkisebb négyzetes mátrix szingulárisérték-felbontását!
- (e) A szingulárisérték-felbontás segítségével számítsd ki a legkisebb négyzetes feladat megoldását! A szinguláris értékeket nagyságuk szerinti csökkenő sorrendbe rendezve számítsd ki a megoldásokat az első $k$ szinguláris érték használatával, $k = 1, \ldots, 5$ mellett. A kapott öt megoldás mindegyikére nyomtasd ki a pályaparaméterek értékeit, és ábrázold is a kapott pályákat a megadott adatpontokkal együtt az $(x, y)$ síkon!
- (f) Perturbáld az input adatokat enyhén úgy, hogy minden adatpont minden koordinátájához adsz egy $[-0{,}005, 0{,}005]$ intervallumon egyenletes eloszlású véletlen számot (lásd a 13.5. szakaszt)! Számítsd ki az új legkisebb négyzetes mátrix szingulárisérték-felbontását, és oldd meg a legkisebb négyzetes feladatot a perturbált adatokkal az (e) résznek megfelelően! Hasonlítsd össze a paraméterek új értékeit a korábban kiszámítottakkal minden $k$-ra! Milyen hatással van ez a különbség a pályák ábrájára? Meg tudod-e magyarázni ezt a viselkedést? Melyik megoldást tartanád jobbnak: azt, amelyik szorosabban illeszkedik az adatokra, vagy azt, amelyik kevésbé érzékeny az adatok kis perturbációira? Miért?
- (g) Az egyszerűség kedvéért közönséges legkisebb négyzeteket használtunk ebben a feladatban, valójában azonban minden adat ugyanúgy ki van téve a megfigyelési hibáknak (valóban, $x$ az egyenlet mindkét oldalán megjelenik), ami kérdésessé teszi a közönséges legkisebb négyzetek alkalmazhatóságát. Fogalmazd át ezt a feladatot teljes legkisebb négyzetes feladattá, és oldd meg az utóbbit a szingulárisérték-felbontással, ahogy a 3.6.1. szakaszban leírtuk!

- **3.6.** Írj rutint egy tetszőleges $m \times n$-es mátrix pszeudoinverzének kiszámítására! Hívhatsz könyvtári rutint a szingulárisérték-felbontás kiszámítására, majd a kimenete alapján számítsd ki a pszeudoinverzet (lásd a 3.6.1. szakaszt)! Vedd figyelembe a viszonylag kis szinguláris értékek nullának nyilvánításához használt tolerancia alkalmazását. Teszteld a rutinodat szinguláris és nemszinguláris mátrixokon egyaránt! Az utóbbi esetben természetesen az eredményeidnek egyezniük kell a standard mátrixinvertálás eredményeivel. Mi történik, ha a mátrix nemszinguláris, de súlyosan rosszul kondicionált (pl. egy Hilbert-mátrix)?

- **3.7.** Írj rutint egy tetszőleges, esetlegesen ranghiányos $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetes feladat megoldására a szingulárisérték-felbontás segítségével! Hívhatsz könyvtári rutint az SVD kiszámítására, majd a kimenete alapján számítsd ki a legkisebb négyzetes megoldást (lásd a 3.6. szakaszt)! A rutinod bemenetének tartalmaznia kell az $\boldsymbol{A}$ mátrixot, a $\boldsymbol{b}$ jobb oldali vektort és egy toleranciát az $\boldsymbol{A}$ numerikus rangjának meghatározásához. Teszteld a rutinodat a fejezet egyéb számítógépes feladataiban szereplő lineáris legkisebb négyzetes feladatok némelyikén!

- **3.8.** Annak bemutatására, hogy a normálegyenletek módszere és a QR-felbontás eredményei numerikusan hogyan térhetnek el, olyan legkisebb négyzetes feladatra van szükségünk, amely rosszul kondicionált és emellett kis maradékkal rendelkezik. Ilyen feladatot a következőképpen generálhatunk. $n-1$-edfokú polinomot,

$$p_{n-1}(t) = x_1 + x_2 t + x_3 t^2 + \cdots + x_n t^{n-1},$$

illesztünk $m$ darab $(t_i, y_i)$ adatpontra, ahol $m > n$. A $t_i = (i - 1)/(m - 1)$, $i = 1, \ldots, m$ választással az adatpontok egyenletesen oszlanak el a $[0, 1]$ intervallumon. A hozzájuk tartozó $y_i$ értékeket úgy generáljuk, hogy először értékeket választunk az $x_j$-kre, mondjuk $x_j = 1$, $j = 1, \ldots, n$, és a kapott polinomot kiértékeljük, hogy megkapjuk az $y_i = p_{n-1}(t_i)$, $i = 1, \ldots, m$ értékeket. Most megnézhetnénk, vissza tudjuk-e nyerni azokat az $x_j$-ket, amelyeket az $y_i$-k generálására használtunk, de hogy érdekesebbé tegyük, először véletlenszerűen perturbáljuk az $y_i$ értékeket, hogy a legkisebb négyzetes feladatokra jellemző adathibát szimuláljuk. Konkrétan az $y_i = y_i + (2u_i - 1) * \epsilon$, $i = 1, \ldots, m$ értékeket vesszük, ahol minden $u_i$ egy $[0, 1)$ intervallumon egyenletes eloszlású véletlen szám (lásd a 13.5. szakaszt), és $\epsilon$ egy kicsi pozitív szám, amely a maximális perturbációt határozza meg. Ha IEEE dupla precíziót használsz, ehhez a feladathoz ésszerű paraméterek az $m = 21$, $n = 12$ és $\epsilon = 10^{-10}$.

Miután a fent vázolt módon generáltad a $(t_i, y_i)$ adathalmazt, most összehasonlítjuk a két módszert a legkisebb négyzetes megoldás kiszámítására ehhez a polinomillesztési feladathoz. Először írd fel a feladathoz tartozó normálegyenletek rendszerét, és oldd meg egy Cholesky-felbontást végző könyvtári rutinnal! Ezután oldd meg a legkisebb négyzetes rendszert egy QR-felbontást végző könyvtári rutinnal! Hasonlítsd össze a két kapott $\boldsymbol{x}$ megoldásvektort! Melyik módszernél érzékenyebb a megoldás az adatokba bevitt perturbációra? Melyik módszer közelíti meg jobban azt az $\boldsymbol{x}$-et, amelyet az adatok generálására használtunk? Az, hogy a megoldások eltérnek, befolyásolja-e azt, hogy a $(t_i, y_i)$ adatpontokat közel tudjuk-e illeszteni a polinommal? Miért?

- **3.9.** Használd a 3.4.2. szakasz bővített rendszer módszerét az előző feladatban levezetett legkisebb négyzetes feladat megoldására! A bővített rendszer szimmetrikus, de nem pozitív definit, ezért a Cholesky-felbontás nem alkalmazható, de használhatsz szimmetrikus indefinit vagy LU-felbontást. Kísérletezz az $\alpha$ skálázási paraméter különféle értékeivel! Hogyan viszonyul ennek a módszernek a pontossága és futási ideje a normálegyenletek és a QR-felbontás módszereinek pontosságához és futási idejéhez?

- **3.10.** Az $m \times n$-es $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladat kovarianciamátrixát $\sigma^2 (\boldsymbol{A}^T \boldsymbol{A})^{-1}$ adja, ahol $\sigma^2 = \|\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}\|_2^2 / (m - n)$ a legkisebb négyzetes $\boldsymbol{x}$ megoldásnál. E mátrix elemei fontos információt tartalmaznak az illesztés jóságáról és az illesztett paraméterek közötti keresztkorrelációkról. A kovarianciamátrix kivételt képez azon általános szabály alól, hogy mátrixok inverzét nem szabad explicit módon kiszámítani. Ha a legkisebb négyzetes feladat megoldására ortogonalizációs módszert használunk, akkor az $\boldsymbol{A}^T \boldsymbol{A}$ keresztszorzat-mátrix sosem képződik, tehát alternatív módszerre van szükségünk a kovarianciamátrix kiszámítására.
- (a) Mutasd meg, hogy $(\boldsymbol{A}^T \boldsymbol{A})^{-1} = (\boldsymbol{R}^T \boldsymbol{R})^{-1}$, ahol $\boldsymbol{R}$ az $\boldsymbol{A}$ QR-felbontásával kapott felső háromszögű tényező!
- (b) Erre a tényre alapozva valósíts meg egy rutint, amely a kovarianciamátrixot csak a már kiszámított $\boldsymbol{R}$ segítségével számítja ki! (E feladat céljaira figyelmen kívül hagyhatod a $\sigma^2$ skalártényezőt.) Teszteld a rutinodat néhány példamátrixon, hogy megerősítsd: ugyanazt az eredményt adja, mint $(\boldsymbol{A}^T \boldsymbol{A})^{-1}$ kiszámítása!

- **3.11.** Az $m \times n$-es $\boldsymbol{A}$ mátrix QR-felbontásának kiszámítására szolgáló legtöbb könyvtári rutin az $\boldsymbol{R}$ mátrixot az $\boldsymbol{A}$ tárolási területének felső háromszögében, a Householder-vektorokat pedig $\boldsymbol{A}$ alsó háromszögében adja vissza, egy további vektorral a főátló menti átfedés kezelésére. Írj egy rutint, amely ezt a kimeneti tömböt és kisegítő vektort fogadja, és explicit módon előállítja a $\boldsymbol{Q}$ ortogonális mátrixot úgy, hogy a Householder-transzformációk megfelelő sorozatával megszoroz egy $m \times m$-es mátrixot, amelyet az $\boldsymbol{I}$ egységmátrixra inicializáltunk. Természetesen ehhez külön tömbre lesz szükség. Teszteld a programodat több mátrixon, és erősítsd meg, hogy a számított $\boldsymbol{Q}$ valóban ortogonális, és hogy a

$$\boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}$$

szorzat visszaadja $\boldsymbol{A}$-t!

- **3.12.** (a) Valósítsd meg mind a klasszikus, mind a módosított Gram–Schmidt-eljárást, és mindkettővel generálj olyan $\boldsymbol{Q}$ ortogonális mátrixot, amelynek oszlopai ortonormált bázist alkotnak a $\boldsymbol{H}$ Hilbert-mátrix oszlopterére, ahol $h_{ij} = 1/(i + j - 1)$, $n = 2, \ldots, 12$ esetén (lásd a 2.6. számítógépes feladatot). Az eredmények minőségének mérésére (konkrétabban az ortogonalitás esetleges elvesztésének) ábrázold a $-\log_{10}(\|\boldsymbol{I} - \boldsymbol{Q}^T \boldsymbol{Q}\|)$ mennyiséget – amelyet „pontosságjegyek” értelmében lehet értelmezni – minden módszernél $n$ függvényében! Emellett próbáld meg a klasszikus eljárást kétszer alkalmazni (azaz alkalmazd a klasszikus Gram–Schmidt-rutinodat a saját $\boldsymbol{Q}$ kimenetére, hogy új $\boldsymbol{Q}$-t kapj), és megint ábrázold a kapott ortogonalitástól való eltérést! Hogyan viszonyul a három módszer sebességben, memóriában és pontosságban?
- (b) Ismételd meg az előző kísérletet, de ezúttal használd a Householder-módszert, azaz az explicit módon kiszámított $\boldsymbol{Q}$ ortogonális mátrixot, amely a Hilbert-mátrix Householder-féle QR-felbontásából származik! Ne feledd, hogy ha a Householder-féle QR-felbontáshoz használt rutin nem állítja elő explicit módon a $\boldsymbol{Q}$-t, akkor a $\boldsymbol{Q}$-t úgy kaphatod meg, hogy a Householder-transzformációk sorozatát megszorzod egy $\boldsymbol{I}$ egységmátrixra inicializált mátrixszal (lásd az előző feladatot). Megint ábrázold ennek a módszernek az ortogonalitástól való eltérését, és hasonlítsd össze a korábbi módszerekével!
- (c) Ismételd meg az előző kísérletet, de ezúttal az SVD-t használd az ortonormált bázis megszerzésére (lásd a 3.6.1. szakaszt)!
- (d) Ortonormált bázis kiszámításának még egy módja a normálegyenletek használata. Ha képezzük a keresztszorzat-mátrixot, és kiszámítjuk az $\boldsymbol{A}^T \boldsymbol{A} = \boldsymbol{L}\boldsymbol{L}^T$ Cholesky-felbontását, akkor

$$\boldsymbol{I} = \boldsymbol{L}^{-1}(\boldsymbol{A}^T \boldsymbol{A})\boldsymbol{L}^{-T} = (\boldsymbol{A}\boldsymbol{L}^{-T})^T (\boldsymbol{A}\boldsymbol{L}^{-T}),$$

ami azt jelenti, hogy a $\boldsymbol{Q} = \boldsymbol{A}\boldsymbol{L}^{-T}$ ortogonális, és az oszloptere nyilvánvalóan ugyanaz, mint $\boldsymbol{A}$-é. Ismételd meg az előző kísérletet megint Hilbert-mátrixokkal, ezúttal az így a normálegyenletekből kapott $\boldsymbol{Q}$-t használva (a szükséges háromszögű megoldás kiszámítása az általad használt szoftvertől függően kissé trükkös lehet)! Megint ábrázold a kapott ortogonalitástól való eltérést, és hasonlítsd össze a korábbi módszerekével!
- (e) Meg tudod-e magyarázni az ezekben a kísérletekben a különféle módszerekkel kapott eredmények relatív minőségét?

- **3.13.** Mi az egzakt $\boldsymbol{x}$ megoldása az

$$\begin{bmatrix} 1 & 1 & 1 \\ \epsilon & 0 & 0 \\ 0 & \epsilon & 0 \\ 0 & 0 & \epsilon \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$

lineáris legkisebb négyzetes feladatnak $\epsilon$ függvényében?

Oldd meg ezt a legkisebb négyzetes feladatot az alábbi módszerek mindegyikével! Minden módszernél kísérletezz az $\epsilon$ paraméter értékével, hogy lásd, milyen kicsire veheted, és még mindig pontos megoldást kapj! Különös figyelmet fordíts az $\epsilon \approx \sqrt{\epsilon_{\text{mach}}}$ és $\epsilon \approx \epsilon_{\text{mach}}$ körüli értékekre.

- (a) Normálegyenletek.
- (b) Bővített rendszer.
- (c) Householder-féle QR.
- (d) Givens-féle QR.
- (e) Klasszikus Gram–Schmidt-ortogonalizáció.
- (f) Módosított Gram–Schmidt-ortogonalizáció.
- (g) Klasszikus Gram–Schmidt iteratív finomítással (azaz kétszer alkalmazott CGS).
