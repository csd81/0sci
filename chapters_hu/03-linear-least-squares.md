# Lineáris legkisebb négyzetek

# 3.1 Lineáris legkisebb négyzetek feladatok

Tegyük fel, hogy szeretnénk tudni, mennyi a tipikus havi csapadékmennyiség Seattle-ben. Elegendő lenne ehhez egyetlen hónap mérései? Természetesen nem – egy adott hónap szokatlanul napos vagy viharos is lehet. Ehelyett inkább több hónapon át – legalább egy éven, vagy talán tíz éven át – végeznénk méréseket, majd ezeket átlagolnánk. Az így kapott átlag ugyan nem lesz pontosan helyes egyetlen konkrét hónapra sem, mégis valamiféle megérzés azt súgja, hogy a tipikus csapadékmennyiségről sokkal pontosabb képet ad, mint amekkorát bármelyik egyedi mérés valaha is adhatna. Ez az elv – azaz hogy sok mérés elvégzésével elsimítjuk a mérési hibákat és más véletlen ingadozásokat – szinte általánosan elterjedt a megfigyeléses és kísérleti tudományokban. A földmérők szándékosan több mérést is végeznek, mint amennyi szigorúan szükséges volna a tájékozódási pontok közötti távolságok meghatározásához. A csillagászok és a távközlési mérnökök ezt az elvet alkalmazzák, amikor zajos adatokból értelmes jeleket nyernek ki. Még az ács mondása is, miszerint „kétszer mérj, egyszer vágj”, e megközelítés bölcsességének példája.

A csapadékpéldában egyetlen számot kerestünk, amely egy egész számsokaságot reprezentál, vagy valamilyen értelemben közelít. Általánosabban fogalmazva: különféle elméleti és gyakorlati okokból gyakran keresünk egy-egy magasabb dimenziós objektumhoz alacsonyabb dimenziós közelítést. Ennek célja lehet a hibák kisimítása vagy a lényegtelen részletek figyelmen kívül hagyása – például amikor zajos adatokból jelet vagy trendet nyerünk ki –, vagy az, hogy egy nagy adattömeget kezelhetőbb mennyiségre csökkentsünk, vagy hogy egy bonyolult függvényt egyszerű közelítéssel helyettesítsünk. Nem várjuk el, hogy egy ilyen közelítés egzakt legyen – a legtöbb célra nem is szeretnénk, hogy az legyen –, mindazonáltal azt akarjuk, hogy valamennyire emlékeztessen az eredeti adatokra. A lineáris algebra terminológiájával élve azt szeretnénk, hogy egy magasabb dimenziós térből vett vektort egy alacsonyabb dimenziós altérre vetítsünk. Ennek egyik legnépszerűbb és számítási szempontból legkényelmesebb módja a legkisebb négyzetek módszere, amelyet ebben a fejezetben tárgyalunk.

Figyelmünket egyelőre a lineáris feladatokra szűkítjük, a nemlineáris legkisebb négyzeteket a 6.6. szakaszra halasztva. A 2.2. szakaszban láttuk, hogy egy négyzetes lineáris rendszer pontosan meghatározott: ugyanannyi egyenlettel és ismeretlennel mindig pontosan egy megoldás létezik, feltéve hogy a mátrix nemszinguláris. Az interpolációnál például a paraméterek és az adatpontok száma közötti egyezést kihasználva bázisfüggvények lineáris kombinációjával illesztjük pontosan az adott adatokat (lásd a 7. fejezetet). A jelen helyzetben ezzel szemben feltételezzük, hogy az adott adatok zajosak vagy lényegtelen részleteket tartalmaznak, ezért semmilyen különleges előnnyel nem jár, ha pontosan illesztjük őket. Sőt, az ilyen ingadozásokat éppen azzal simíthatjuk ki, hogy lemondunk a pontos illeszkedésről, és a szükségesnél több adatpontot vagy mérést használunk, ami egy túlhatározott rendszerhez vezet, amelyben több az egyenlet, mint az ismeretlen. A lineáris rendszert mátrix-vektor jelöléssel felírva a következőt kapjuk:

$$\boldsymbol{A}\boldsymbol{x} = \boldsymbol{b},$$

ahol $\boldsymbol{A}$ egy $m \times n$-es mátrix, amelyre $m > n$, $\boldsymbol{b}$ egy $m$-dimenziós vektor, $\boldsymbol{x}$ pedig egy $n$-dimenziós vektor. Általában, mivel az $\boldsymbol{x}$ vektorban mindössze $n$ paraméter szerepel, nem várhatjuk el, hogy az $\boldsymbol{A}$ $n$ oszlopának lineáris kombinációjaként reprodukálni tudjuk az $m$-dimenziós $\boldsymbol{b}$ vektort. Más szóval egy túlhatározott rendszernek a szokásos értelemben általában nincs megoldása. Ehelyett a bal és a jobb oldal közötti távolságot minimalizáljuk, azaz az $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ maradékvektor valamely normáját minimalizáljuk az $\boldsymbol{x}$ függvényeként. Elvileg bármelyik norma használható, de – ahogyan látni fogjuk – erős érvek szólnak az euklideszi norma (2-norma) mellett, ideértve a belső szorzattal és az ortogonalitással való kapcsolatát, a simaságát és szigorú konvexitását, valamint a számítási kényelmét. A 2-norma használata adja a legkisebb négyzetek módszerének nevét: a megoldás az az $\boldsymbol{x}$ vektor, amely a lineáris rendszer bal és jobb oldala komponenseinek különbségei négyzetösszegét minimalizálja. A pontos egyenlőség hiányát tükrözendő egy lineáris legkisebb négyzetek feladatot a következő alakban írunk fel:

$$\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b},$$

ahol a közelítést a 2-norma, illetve a legkisebb négyzetek értelmében értjük.

**3.1. Példa. Túlhatározott rendszer.** Egy földmérőnek három domb magasságát kell meghatároznia egy referenciaponthoz képest. Először a referenciapontból mérve a földmérő a dombok magasságait rendre $x_1 = 1237$ lábnak, $x_2 = 1941$ lábnak és $x_3 = 2417$ lábnak méri. Ezen kezdeti mérések megerősítésére felmászik az első domb tetejére, és azt méri, hogy a második domb $x_2 - x_1 = 711$ lábbal, a harmadik pedig $x_3 - x_1 = 1177$ lábbal magasabb az elsőnél. Végül a második domb tetejére is felmászik, és azt méri, hogy a harmadik domb $x_3 - x_2 = 475$ lábbal magasabb a másodiknál. Észrevéve a mérések közötti ellentmondásokat, a földmérő a később bemutatandó módszereket használja a

$$\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} 1237 \\ 1941 \\ 2417 \\ 711 \\ 1177 \\ 475 \end{bmatrix} = \boldsymbol{b}$$

túlhatározott lineáris rendszer legkisebb négyzetes megoldásának meghatározására, amelyből $\boldsymbol{x} = [1236,\ 1943,\ 2416]^T$ adódik. Ezek az értékek, amelyek enyhén eltérnek a három kezdeti magasságméréstől, olyan kompromisszumot képviselnek, amely (a legkisebb négyzetek értelmében) a lehető legjobban összehangolja a mérési hibákból eredő ellentmondásokat.

A legkisebb négyzetek módszerének korai fejlesztése nagyrészt Gaussnak köszönhető, aki csillagászati feladatok – különösen égitestek, például kisbolygók és üstökösök pályájának meghatározása – megoldására használta. Egy ilyen test elliptikus pályáját öt paraméter határozza meg (lásd a 3.5. számítógépes feladatot), így elvileg öt pozíciómegfigyelés elegendő lenne a teljes pálya meghatározásához. A mérési hibák miatt azonban egy csupán öt megfigyelésre alapozott pálya rendkívül megbízhatatlan volna. Ehelyett jóval több megfigyelést végeznek, és a legkisebb négyzetek módszerét alkalmazzák arra, hogy elsimítsák a hibákat, és pontosabb értékeket kapjanak a pályaparaméterekre. A legkisebb négyzetes közelítés a megfigyelések tucatjait vagy százait – amelyek egy megfelelően nagy dimenziós térben helyezkednek el – az elliptikus pályamodell ötdimenziós paramétertérévé redukálja.

**3.2. Példa. Adatillesztés.** A legkisebb négyzetek módszerének egyik leggyakoribb alkalmazási területe az *adatillesztés*, más néven a *görbeillesztés*, különösen akkor, amikor az adatokat valamilyen véletlen hiba terheli, mint a legtöbb empirikus laboratóriumi mérés vagy egyéb természeti megfigyelés esetében. Adott $(t_i, y_i)$, $i = 1, \ldots, m$ adatpontok esetén azt az $n$-dimenziós $\boldsymbol{x}$ paramétervektort keressük, amely az $f(t, \boldsymbol{x})$ *modellfüggvénnyel* – ahol $f: \mathbb{R}^{n+1} \to \mathbb{R}$ – a „legjobb illeszkedést” adja az adatokra, ahol a legjobb illeszkedést a legkisebb négyzetek értelmében értjük:

$$\min_{\boldsymbol{x}} \sum_{i=1}^{m} (y_i - f(t_i, \boldsymbol{x}))^2.$$

Egy adatillesztési feladat *lineáris*, ha az $f$ függvény lineáris az $\boldsymbol{x}$ paramétervektor komponenseiben, azaz $f$ a csak $t$-től függő $\phi_j$ függvények

$$f(t, \boldsymbol{x}) = x_1 \phi_1(t) + x_2 \phi_2(t) + \dots + x_n \phi_n(t)$$

lineáris kombinációja. Például a polinomillesztés, amelyre

$$f(t, \boldsymbol{x}) = x_1 + x_2 t + x_3 t^2 + \dots + x_n t^{n-1},$$

lineáris adatillesztési feladat, mert a polinom a $x_j$ együtthatóiban lineáris, bár a $t$ független változóban nemlineáris. Egy *nemlineáris* adatillesztési feladatra példa – amellyel a 6.6. szakaszban foglalkozunk – az exponenciálisok

$$f(t, \boldsymbol{x}) = x_1 e^{x_2 t} + \dots + x_{n-1} e^{x_n t}$$

alakú összege.

Ha definiáljuk az $a_{ij} = \phi_j(t_i)$ elemekkel rendelkező $m \times n$-es $\boldsymbol{A}$ mátrixot, valamint a $b_i = y_i$ komponensekkel rendelkező $m$-dimenziós $\boldsymbol{b}$ vektort, akkor egy lineáris legkisebb négyzetes adatillesztési feladat a

$$\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$$

alakot ölti. Például ha egy háromparaméteres másodfokú polinomot illesztünk öt $(t_1, y_1), \ldots, (t_5, y_5)$ adatpontra, akkor az $\boldsymbol{A}$ mátrix $5 \times 3$-as, és a feladat alakja:

$$\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} 1 & t_1 & t_1^2 \\ 1 & t_2 & t_2^2 \\ 1 & t_3 & t_3^2 \\ 1 & t_4 & t_4^2 \\ 1 & t_5 & t_5^2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \end{bmatrix} = \boldsymbol{b}.$$

Egy ilyen alakú mátrixot, amelynek oszlopai (vagy sorai) egy független változó egymás utáni hatványai, *Vandermonde-mátrixnak* nevezünk.

Tegyük fel, hogy az alábbi mért adatokkal rendelkezünk.

Ez a 21 adatpont, amelyet a 3.1. ábrán pontokként ábrázoltunk, láthatóan tartalmaz bizonyos véletlen zajt, de úgy tűnik, nagyjából egy parabolaív mentén helyezkednek el (vagy talán valamilyen mögöttes fizikai folyamat, például egy lövedék röppályája parabolikus modellt sugall), ezért úgy döntünk, hogy egy másodfokú polinommal illesztjük őket. Nyilvánvaló, hogy egy másodfokú polinom nem illeszkedik pontosan az adatokra, de csupán az adatok általános trendjét kívánjuk meghatározni, és amúgy sem szeretnénk utánozni a véletlen mérési zajt, így a legkisebb négyzetes közelítés megfelelőnek tűnik. Az így kapott túlhatározott $21 \times 3$-as lineáris rendszer alakja:

$$\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} 1 & 0{,}0 & 0{,}0 \\ 1 & 0{,}5 & 0{,}25 \\ 1 & 1{,}0 & 1{,}0 \\ \vdots & \vdots & \vdots \\ 1 & 10{,}0 & 100{,}0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} 2{,}9 \\ 2{,}7 \\ 4{,}8 \\ \vdots \\ 4{,}1 \end{bmatrix} = \boldsymbol{b}.$$

E rendszer megoldása – amelynek kiszámítását később ismertetjük – $\boldsymbol{x} \approx \begin{bmatrix} 2{,}18 & 2{,}67 & -0{,}238 \end{bmatrix}^T$, ami azt jelenti, hogy a közelítő polinom, amelyet a 3.1. ábrán sima görbeként ábrázoltunk, a következő:

$$p(t) = 2{,}18 + 2{,}67t - 0{,}238t^2.$$

Ez a konkrét polinom olyan értelemben a legjobban illeszkedő polinom az adott adatokra az összes másodfokú polinom közül, hogy az adatpontok és a görbe közötti függőleges távolságok négyzetösszegét minimalizálja az összes lehetséges másodfokú polinom körében.

A legkisebb négyzetek módszere fontos eszköz a statisztikában, ahol regresszióanalízis néven is ismerik. Mi csak a legkisebb négyzetes feladatok megoldására szolgáló numerikus algoritmusokkal foglalkozunk. A legkisebb négyzetes feladatok felírásával és az eredmények helyes értelmezésével kapcsolatos sok fontos statisztikai szempontért lásd a regresszióanalízis vagy a többváltozós statisztika bármelyik tankönyvét.

![](_page_4_Figure_2.jpeg)

3.1. ábra: Másodfokú polinom legkisebb négyzetes illesztése az adott adatokra.

# 3.2 Létezés és egyértelműség

A 2.1. szakaszból felidézhetjük, hogy egy $m \times n$-es $\boldsymbol{A}\boldsymbol{x} = \boldsymbol{b}$ lineáris egyenletrendszer azt kérdezi, kifejezhető-e $\boldsymbol{b}$ az $\boldsymbol{A}$ oszlopainak lineáris kombinációjaként. Négyzetes rendszerek ($m = n$) esetén a válasz nemszinguláris $\boldsymbol{A}$-ra mindig „igen”. Túlhatározott rendszerek ($m > n$) esetén ezzel szemben a válasz általában „nem”, hacsak $\boldsymbol{b}$ történetesen a $\operatorname{span}(\boldsymbol{A})$-ban fekszik, ami a legtöbb alkalmazásban igen valószínűtlen. A legkisebb négyzetek módszerénél azonban nem is várjuk el – és többnyire nem is kívánjuk –, hogy az egyenlet két oldala pontosan egyezzen, csupán a 2-norma szerinti lehető legjobb egyezést. A megoldás ezen másféle fogalmával a létezés és egyértelműség feltételei némileg eltérnek a négyzetes lineáris rendszerekéitől, ahogyan azt a továbbiakban látni fogjuk.

Először is megjegyezzük, hogy a legkisebb négyzetes megoldás létezése mindig biztosított: a $\phi(\boldsymbol{y}) = \|\boldsymbol{b} - \boldsymbol{y}\|_2$ függvény folytonos és koercív $\mathbb{R}^m$-en, így $\phi$-nek minimuma van a zárt, nem korlátos $\operatorname{span}(\boldsymbol{A})$ halmazon (lásd a 6.2. szakaszt), azaz létezik olyan $\boldsymbol{y} \in \operatorname{span}(\boldsymbol{A})$ $m$-dimenziós vektor, amely euklideszi normában a legközelebb van $\boldsymbol{b}$-hez. Emellett $\phi$ szigorúan konvex a $\operatorname{span}(\boldsymbol{A})$ konvex halmazon, így a $\boldsymbol{b}$-hez legközelebbi $\boldsymbol{y} \in \operatorname{span}(\boldsymbol{A})$ vektor egyértelmű (lásd a 6.2.1. szakaszt). Ez azonban nem jelenti azt, hogy a legkisebb négyzetes feladat $\boldsymbol{x}$ megoldása szükségképpen egyértelmű. Tegyük fel, hogy $\boldsymbol{x}_1$ és $\boldsymbol{x}_2$ ilyen megoldások, és legyen $\boldsymbol{z} = \boldsymbol{x}_2 - \boldsymbol{x}_1$. Ekkor, mivel $\boldsymbol{A}\boldsymbol{x}_1 = \boldsymbol{y} = \boldsymbol{A}\boldsymbol{x}_2$, azt kapjuk, hogy $\boldsymbol{A}\boldsymbol{z} = \boldsymbol{0}$. Márpedig ha $\boldsymbol{z} \neq \boldsymbol{0}$, azaz $\boldsymbol{x}_1 \neq \boldsymbol{x}_2$, akkor az $\boldsymbol{A}$ oszlopai lineárisan összefüggők kell, hogy legyenek (vö. négyzetes mátrix nemszingularitásának 4. feltételével a 2.2. szakaszban). Arra a következtetésre jutunk, hogy egy $m \times n$-es $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladat megoldása akkor és csak akkor egyértelmű, ha $\boldsymbol{A}$ teljes oszloprangú, azaz $\operatorname{rank}(\boldsymbol{A}) = n$ (vö. négyzetes mátrix nemszingularitásának 3. feltételével a 2.2. szakaszban). Ha $\operatorname{rank}(\boldsymbol{A}) < n$, akkor az $\boldsymbol{A}$-t *ranghiányosnak* mondjuk, és bár a megfelelő legkisebb négyzetes feladatnak ekkor is kell hogy legyen megoldása, ebben az esetben az nem lehet egyértelmű. A ranghiány következményeit később vizsgáljuk; egyelőre feltételezzük, hogy $\boldsymbol{A}$ teljes oszloprangú.

Az imént idézett létezési bizonyítás nem konstruktív, és kevés betekintést nyújt abba, miként jellemezzük vagy számítsuk ki egy lineáris legkisebb négyzetes feladat megoldását. A továbbiakban analitikus, geometriai és algebrai nézőpontokat tekintünk át, amelyek mélyebb betekintést nyújtanak a legkisebb négyzetes feladatok természetébe és a megoldásukra szolgáló különféle módszerekbe.

### 3.2.1 Normálegyenletek

Minimalizálási feladatként a legkisebb négyzetes feladat a többváltozós analízis eszközeivel kezelhető, hasonlóan ahhoz, ahogyan az egyváltozós analízisben a derivált nullával egyenlőségét írjuk elő. Az $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ maradékvektor euklideszi normájának négyzetét szeretnénk minimalizálni. Ezt a célfüggvényt $\phi: \mathbb{R}^n \to \mathbb{R}$-rel jelölve

$$\phi(\boldsymbol{x}) = \|\boldsymbol{r}\|_2^2 = \boldsymbol{r}^T\boldsymbol{r} = (\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x})^T(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}) = \boldsymbol{b}^T\boldsymbol{b} - 2\boldsymbol{x}^T\boldsymbol{A}^T\boldsymbol{b} + \boldsymbol{x}^T\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x}.$$

A minimum szükséges feltétele, hogy $\boldsymbol{x}$ kritikus pontja legyen $\phi$-nek, azaz a $\nabla \phi(\boldsymbol{x})$ gradiensvektor – amelynek $i$-edik komponensét $\partial \phi(\boldsymbol{x})/\partial x_i$ adja – nulla legyen (lásd a 6.2.2. szakaszt). Ezért teljesülnie kell, hogy

$$\boldsymbol{0} = \nabla \phi(\boldsymbol{x}) = 2\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x} - 2\boldsymbol{A}^T\boldsymbol{b},$$

tehát $\phi$ bármely $\boldsymbol{x}$ minimumhelyének ki kell elégítenie az $n \times n$-es szimmetrikus lineáris rendszert:

$$\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x} = \boldsymbol{A}^T\boldsymbol{b}.$$

Elegendő feltétel ahhoz, hogy egy ilyen $\boldsymbol{x}$ valóban minimum legyen, az, hogy a második parciális deriváltakból álló Hesse-mátrix – amely ebben az esetben éppen $2\boldsymbol{A}^T\boldsymbol{A}$ – pozitív definit (ismét lásd a 6.2.2. szakaszt). Könnyen belátható, hogy $\boldsymbol{A}^T\boldsymbol{A}$ akkor és csak akkor pozitív definit, ha az $\boldsymbol{A}$ oszlopai lineárisan függetlenek, azaz $\operatorname{rank}(\boldsymbol{A}) = n$, ami éppen az a kritérium, amelyet korábban a legkisebb négyzetes megoldás egyértelműségére vonatkozóan láttunk.

Az $\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x} = \boldsymbol{A}^T\boldsymbol{b}$ lineáris rendszert általánosan *normálegyenletek*nek nevezik. Az $\boldsymbol{A}^T\boldsymbol{A}$ mátrix $(i, j)$ elemét az $\boldsymbol{A}$ $i$-edik és $j$-edik oszlopainak belső szorzata adja; emiatt az $\boldsymbol{A}^T\boldsymbol{A}$-t olykor az $\boldsymbol{A}$ keresztszorzat-mátrixának is nevezik. Ez a négyzetes lineáris rendszer egy módszert sugall – amelyet a 3.4.1. szakaszban részletesebben megvizsgálunk – a túlhatározott legkisebb négyzetes feladatok megoldására.

**3.3. Példa. Normálegyenletek.** A 3.1. példabeli lineáris legkisebb négyzetes feladat normálegyenlet-rendszere az alábbi szimmetrikus pozitív definit rendszer:

$$\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} -651 \\ 2177 \\ 4069 \end{bmatrix} = \boldsymbol{A}^T\boldsymbol{b},$$

amelynek megoldása $\boldsymbol{x} = [1236,\ 1943,\ 2416]^T$, és a 2.21. példában kapott Cholesky-felbontással számítható ki; ez éri el a négyzetösszeg lehető legkisebb értékét, $\|\boldsymbol{r}\|_2^2 = 35$.

#### 3.2.2 Ortogonalitás és ortogonális projektorok

A legkisebb négyzetes feladatok geometriai szemléletéhez szükségünk van az ortogonalitás fogalmára. Felidézzük, hogy $\boldsymbol{v}_1, \boldsymbol{v}_2 \in \mathbb{R}^m$ vektorokra

$$\boldsymbol{v}_1^T\boldsymbol{v}_2 = \|\boldsymbol{v}_1\|_2 \cdot \|\boldsymbol{v}_2\|_2 \cdot \cos(\theta),$$

ahol $\theta$ a $\boldsymbol{v}_1$ és a $\boldsymbol{v}_2$ által bezárt szög. Ennek megfelelően a $\boldsymbol{v}_1$ és a $\boldsymbol{v}_2$ *ortogonális* (vagy *merőleges*, illetve *normális*) egymásra, ha $\boldsymbol{v}_1^T\boldsymbol{v}_2 = 0$.

Egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladatnál, ahol $m > n$, az $m$-dimenziós $\boldsymbol{b}$ vektor általában nem fekszik a legfeljebb $n$ dimenziós $\operatorname{span}(\boldsymbol{A})$ altérben. Az az $\boldsymbol{y} = \boldsymbol{A}\boldsymbol{x} \in \operatorname{span}(\boldsymbol{A})$ vektor, amely euklideszi normában a legközelebb van $\boldsymbol{b}$-hez, ott adódik, ahol az $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ maradékvektor ortogonális a $\operatorname{span}(\boldsymbol{A})$-ra (lásd a 3.2. ábrát). Ezért az $\boldsymbol{x}$ legkisebb négyzetes megoldásra az $\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}$ maradékvektornak az $\boldsymbol{A}$ minden oszlopára ortogonálisnak kell lennie, és így teljesülnie kell, hogy

$$\boldsymbol{0} = \boldsymbol{A}^T\boldsymbol{r} = \boldsymbol{A}^T(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}),$$

azaz

$$\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x} = \boldsymbol{A}^T\boldsymbol{b},$$

ami ugyanaz a normálegyenlet-rendszer, mint amelyet korábban az analízis eszközeivel vezettünk le.

![](_page_6_Picture_11.jpeg)

3.2. ábra: A lineáris legkisebb négyzetes feladat geometriai szemléltetése. A paralelogramma a $\operatorname{span}(\boldsymbol{A})$ alteret jelöli, amelyben $\boldsymbol{b}$ általában nem fekszik benne.

Az ortogonalitás iménti tárgyalásából, különösen a 3.2. ábrából intuitívan látható, hogy az a $\boldsymbol{y} = \boldsymbol{A}\boldsymbol{x} \in \operatorname{span}(\boldsymbol{A})$ vektor, amely euklideszi normában a legközelebb van $\boldsymbol{b}$-hez, nem más, mint $\boldsymbol{b}$ ortogonális projekciója a $\operatorname{span}(\boldsymbol{A})$-ra. E megfigyelés a legkisebb négyzetes megoldások algebrai jellemzéséhez vezet, amelyet most formálisabban is megvizsgálunk.

Egy $\boldsymbol{P}$ négyzetes mátrixot *projektornak* nevezünk, ha idempotens (azaz $\boldsymbol{P}^2 = \boldsymbol{P}$). Egy ilyen mátrix bármely adott vektort egy altérre – nevezetesen a $\operatorname{span}(\boldsymbol{P})$-re – vetít, viszont változatlanul hagy bármely olyan vektort, amely már eleve ebben az altérben fekszik. Ha egy $\boldsymbol{P}$ projektor ezen kívül szimmetrikus is (azaz $\boldsymbol{P}^T = \boldsymbol{P}$), akkor *ortogonális projektor*. Ha $\boldsymbol{P}$ ortogonális projektor, akkor $\boldsymbol{P}_{\perp} = \boldsymbol{I} - \boldsymbol{P}$ is ortogonális projektor a $\operatorname{span}(\boldsymbol{P})^{\perp}$-re, azaz a $\operatorname{span}(\boldsymbol{P})$ ortogonális kiegészítőjére – vagyis a $\operatorname{span}(\boldsymbol{P})$-re ortogonális összes vektor alterére. Bármely $\boldsymbol{v} \in \mathbb{R}^m$ vektor felírható

$$\boldsymbol{v} = (\boldsymbol{P} + (\boldsymbol{I} - \boldsymbol{P}))\,\boldsymbol{v} = \boldsymbol{P}\boldsymbol{v} + \boldsymbol{P}_{\perp}\boldsymbol{v}$$

alakban, kölcsönösen ortogonális vektorok összegeként, amelyek közül az egyik a $\operatorname{span}(\boldsymbol{P})$-ben, a másik a $\operatorname{span}(\boldsymbol{P})^{\perp}$-ben van.

Hogy ezeket a fogalmakat az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetes feladatra alkalmazzuk, tegyük fel, hogy $\boldsymbol{P}$ ortogonális projektor a $\operatorname{span}(\boldsymbol{A})$-ra. Ekkor

$$\begin{aligned}
\|\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}\|_2^2 &= \|\boldsymbol{P}(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}) + \boldsymbol{P}_{\perp}(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x})\|_2^2 \\
&= \|\boldsymbol{P}(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x})\|_2^2 + \|\boldsymbol{P}_{\perp}(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x})\|_2^2 \quad \text{(Pitagorasz-tétel alapján)} \\
&= \|\boldsymbol{P}\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}\|_2^2 + \|\boldsymbol{P}_{\perp}\boldsymbol{b}\|_2^2 \quad \text{(mivel } \boldsymbol{P}\boldsymbol{A} = \boldsymbol{A} \text{ és } \boldsymbol{P}_{\perp}\boldsymbol{A} = \boldsymbol{O}\text{)}.
\end{aligned}$$

A jobb oldal második tagja nem függ $\boldsymbol{x}$-től, így a maradéknorma akkor minimális, ha $\boldsymbol{x}$-et úgy választjuk, hogy az első tag nulla legyen. A legkisebb négyzetes megoldást tehát a

$$\boldsymbol{A}\boldsymbol{x} = \boldsymbol{P}\boldsymbol{b}$$

túlhatározott, de konzisztens lineáris rendszer adja meg. Ebből az egyenletből úgy juthatunk négyzetes lineáris rendszerhez, hogy mindkét oldalát balról megszorozzuk $\boldsymbol{A}^T$-vel, figyelembe véve, hogy $\boldsymbol{A}^T\boldsymbol{P} = \boldsymbol{A}^T\boldsymbol{P}^T = (\boldsymbol{P}\boldsymbol{A})^T = \boldsymbol{A}^T$, amiből

$$\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x} = \boldsymbol{A}^T\boldsymbol{b}$$

adódik, ami ismét a korábban levezetett normálegyenlet-rendszer.

Az ortogonális projektort az alábbi módon kaphatjuk meg explicit alakban: ha $\boldsymbol{A}$ teljes oszloprangú, úgyhogy $\boldsymbol{A}^T\boldsymbol{A}$ nemszinguláris, akkor

$$\boldsymbol{P} = \boldsymbol{A}(\boldsymbol{A}^T\boldsymbol{A})^{-1}\boldsymbol{A}^T$$

szimmetrikus és idempotens, és így ortogonális projektor a $\operatorname{span}(\boldsymbol{A})$-ra. Ennélfogva az a $\boldsymbol{y} \in \operatorname{span}(\boldsymbol{A})$ vektor, amely a legközelebb van $\boldsymbol{b}$-hez, a

$$\boldsymbol{y} = \boldsymbol{P}\boldsymbol{b} = \boldsymbol{A}(\boldsymbol{A}^T\boldsymbol{A})^{-1}\boldsymbol{A}^T\boldsymbol{b} = \boldsymbol{A}\boldsymbol{x}$$

ortogonális projekció, ahol $\boldsymbol{x}$ a normálegyenletek által megadott legkisebb négyzetes megoldás. Érdemes megjegyezni azt is, hogy $\boldsymbol{b}$ a

$$\boldsymbol{b} = \boldsymbol{P}\boldsymbol{b} + \boldsymbol{P}_{\perp}\boldsymbol{b} = \boldsymbol{A}\boldsymbol{x} + (\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}) = \boldsymbol{y} + \boldsymbol{r}$$

alakban felírható két kölcsönösen ortogonális vektor összegeként, ahol $\boldsymbol{y} \in \operatorname{span}(\boldsymbol{A})$ és $\boldsymbol{r} \in \operatorname{span}(\boldsymbol{A})^{\perp}$.

Egy másik lehetőség: legyen $\boldsymbol{Q}$ egy olyan $m \times n$-es mátrix, amelynek oszlopai ortonormált bázist alkotnak (azaz $\boldsymbol{Q}^T\boldsymbol{Q} = \boldsymbol{I}$) a $\operatorname{span}(\boldsymbol{A})$-ban. Ekkor $\boldsymbol{P} = \boldsymbol{Q}\boldsymbol{Q}^T$ szimmetrikus és idempotens, így ortogonális projektor a $\operatorname{span}(\boldsymbol{Q}) = \operatorname{span}(\boldsymbol{A})$-ra. Ezzel a megközelítéssel az előbbi konzisztens túlhatározott rendszerből úgy kaphatunk négyzetes rendszert, hogy mindkét oldalát balról megszorozzuk $\boldsymbol{Q}^T$-vel, és figyelembe vesszük, hogy $\boldsymbol{Q}^T\boldsymbol{P} = \boldsymbol{Q}^T\boldsymbol{Q}\boldsymbol{Q}^T = \boldsymbol{Q}^T$, amiből a

$$\boldsymbol{Q}^T\boldsymbol{A}\boldsymbol{x} = \boldsymbol{Q}^T\boldsymbol{b}$$

négyzetes rendszer adódik. Később látni fogjuk, hogyan számítható ki a $\boldsymbol{Q}$ mátrix úgy, hogy ez a rendszer felső háromszögű legyen, és ezért könnyen megoldható. A szokásos normálegyenletek felírásának ily módon való elkerülése pontosság és stabilitás szempontjából is előnyökkel jár, amint azt hamarosan látni fogjuk.

**3.4. Példa. Ortogonalitás és projekciók.** Ezeket a fogalmakat a 3.1. és 3.3. példabeli legkisebb négyzetes feladat folytatásaként szemléltetjük. Az $\boldsymbol{x} = [1236,\ 1943,\ 2416]^T$ megoldáshelyen a maradékvektor

$$\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x} = \boldsymbol{b} - \boldsymbol{y} = \begin{bmatrix} 1237 \\ 1941 \\ 2417 \\ 711 \\ 1177 \\ 475 \end{bmatrix} - \begin{bmatrix} 1236 \\ 1943 \\ 2416 \\ 707 \\ 1180 \\ 473 \end{bmatrix} = \begin{bmatrix} 1 \\ -2 \\ 1 \\ 4 \\ -3 \\ 2 \end{bmatrix}$$

ortogonális az $\boldsymbol{A}$ minden oszlopára, azaz $\boldsymbol{A}^T\boldsymbol{r} = \boldsymbol{0}$. A $\operatorname{span}(\boldsymbol{A})$-ra vetítő ortogonális projektor

$$\boldsymbol{P} = \boldsymbol{A}(\boldsymbol{A}^T\boldsymbol{A})^{-1}\boldsymbol{A}^T = \frac{1}{4}\begin{bmatrix} 2 & 1 & 1 & -1 & -1 & 0 \\ 1 & 2 & 1 & 1 & 0 & -1 \\ 1 & 1 & 2 & 0 & 1 & 1 \\ -1 & 1 & 0 & 2 & 1 & -1 \\ -1 & 0 & 1 & 1 & 2 & 1 \\ 0 & -1 & 1 & -1 & 1 & 2 \end{bmatrix},$$

a $\operatorname{span}(\boldsymbol{A})^{\perp}$-re vetítő ortogonális projektor pedig

$$\boldsymbol{P}_{\perp} = \boldsymbol{I} - \boldsymbol{P} = \frac{1}{4}\begin{bmatrix} 2 & -1 & -1 & 1 & 1 & 0 \\ -1 & 2 & -1 & -1 & 0 & 1 \\ -1 & -1 & 2 & 0 & -1 & -1 \\ 1 & -1 & 0 & 2 & -1 & 1 \\ 1 & 0 & -1 & -1 & 2 & -1 \\ 0 & 1 & -1 & 1 & -1 & 2 \end{bmatrix},$$

úgyhogy $\boldsymbol{b} = \boldsymbol{P}\boldsymbol{b} + \boldsymbol{P}_{\perp}\boldsymbol{b} = \boldsymbol{y} + \boldsymbol{r}$.

# 3.3 Érzékenység és kondicionáltság

Most rátérünk a lineáris legkisebb négyzetek feladatának érzékenységére és kondicionáltságára. Először is ki kell terjesztenünk a mátrix kondíciószámának fogalmát a téglalap alakú mátrixokra is. A négyzetes mátrixok kondíciószámának 2.3.3. szakaszban adott definíciója a mátrix inverzét használja. Egy nem négyzetes $\boldsymbol{A}$ mátrixnak a hagyományos értelemben vett inverze nincs, de definiálható egy *pszeudoinverz*, amelyet $\boldsymbol{A}^+$ jelöl, és amely sok szempontból úgy viselkedik, mint egy inverz (lásd a 3.32. feladatot). Később egy általánosabb definíciót is látni fogunk, amely tetszőleges mátrixra érvényes, de egyelőre csak olyan $\boldsymbol{A}$ mátrixokat tekintünk, amelyek oszloprangja maximális. Ebben az esetben $\boldsymbol{A}^T \boldsymbol{A}$ nemszinguláris, és az $\boldsymbol{A}$ pszeudoinverzét a következőképpen definiáljuk:

$$\boldsymbol{A}^+ = (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T.$$

Triviálisan adódik, hogy $\boldsymbol{A}^+ \boldsymbol{A} = \boldsymbol{I}$, és a 3.2.2. szakaszból tudjuk, hogy $\boldsymbol{P} = \boldsymbol{A} \boldsymbol{A}^+$ ortogonális projektor a $\operatorname{span}(\boldsymbol{A})$ altérre, úgyhogy az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladatának megoldása

$$\boldsymbol{x} = \boldsymbol{A}^+ \boldsymbol{b}.$$

Most az olyan $m \times n$-es mátrix kondíciószámát, amelyre $\operatorname{rank}(\boldsymbol{A}) = n$, a következőképpen definiáljuk:

$$\operatorname{cond}(\boldsymbol{A}) = \|\boldsymbol{A}\|_2 \cdot \|\boldsymbol{A}^+\|_2.$$

Megállapodás szerint $\operatorname{cond}(\boldsymbol{A}) = \infty$, ha $\operatorname{rank}(\boldsymbol{A}) < n$. Ahogyan egy négyzetes mátrix kondíciószáma a szingularitáshoz való közelséget méri, úgy egy téglalap alakú mátrix kondíciószáma a ranghiányhoz való közelséget jellemzi.

Míg egy négyzetes $\boldsymbol{A}\boldsymbol{x} = \boldsymbol{b}$ lineáris egyenletrendszer kondicionáltsága csak az $\boldsymbol{A}$ mátrixtól függ, addig az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat kondicionáltsága az $\boldsymbol{A}$ mátrixon kívül a $\boldsymbol{b}$ jobb oldali vektortól is függ, ezért $\operatorname{cond}(\boldsymbol{A})$ önmagában nem elegendő az érzékenység jellemzésére. Nevezetesen, ha $\boldsymbol{b}$ közel van a $\operatorname{span}(\boldsymbol{A})$ altérhez, akkor $\boldsymbol{b}$ kis perturbációja viszonylag kevéssé változtatja meg az $\boldsymbol{y} = \boldsymbol{P}\boldsymbol{b}$ vetületet. Ha viszont $\boldsymbol{b}$ közel merőleges a $\operatorname{span}(\boldsymbol{A})$ altérre, akkor maga az $\boldsymbol{y} = \boldsymbol{P}\boldsymbol{b}$ is viszonylag kicsi lesz, így $\boldsymbol{b}$ kis változása viszonylag nagy változást okozhat $\boldsymbol{y}$-ban, és ennélfogva az $\boldsymbol{x}$ legkisebb négyzetes megoldásban is. Így adott $\boldsymbol{A}$ mellett azt várjuk, hogy egy olyan $\boldsymbol{b}$-vel felírt legkisebb négyzetek feladat, amely nagy maradékot eredményez (vagyis az adatokra rossz illeszkedést ad), érzékenyebb lesz, mint egy kis maradékot (azaz jó illeszkedést) adó feladat. Annak, hogy $\boldsymbol{b}$ mennyire van közel a $\operatorname{span}(\boldsymbol{A})$ altérhez, megfelelő mérőszáma a következő arány:

$$\frac{\|\boldsymbol{A}\boldsymbol{x}\|_2}{\|\boldsymbol{b}\|_2} = \frac{\|\boldsymbol{y}\|_2}{\|\boldsymbol{b}\|_2} = \cos(\theta),$$

ahol $\theta$ a $\boldsymbol{b}$ és az $\boldsymbol{y}$ közötti szög (lásd a 3.2. ábrát). Így nagyobb érzékenységre számítunk akkor, amikor ez az arány kicsi, vagyis $\theta$ közel van a $\pi/2$ értékhez.

Most kvantitatívabban értékeljük az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat $\boldsymbol{x}$ megoldásának érzékenységét, ahol $\boldsymbol{A}$ oszloprangja maximális. Az egyszerűség kedvéért a $\boldsymbol{b}$-beli és az $\boldsymbol{A}$-beli perturbációkat külön-külön vizsgáljuk. A $\boldsymbol{b} + \Delta\boldsymbol{b}$ perturbált jobb oldali vektor esetén a perturbált megoldást a normálegyenletek adják meg:

$$\boldsymbol{A}^T \boldsymbol{A} (\boldsymbol{x} + \Delta\boldsymbol{x}) = \boldsymbol{A}^T (\boldsymbol{b} + \Delta\boldsymbol{b}).$$

Mivel $\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b}$, ezért

$$\boldsymbol{A}^T \boldsymbol{A} \, \Delta\boldsymbol{x} = \boldsymbol{A}^T \Delta\boldsymbol{b},$$

és így

$$\Delta\boldsymbol{x} = (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T \Delta\boldsymbol{b} = \boldsymbol{A}^+ \Delta\boldsymbol{b}.$$

Normát véve mindkét oldalon:

$$\|\Delta\boldsymbol{x}\|_2 \leq \|\boldsymbol{A}^+\|_2 \cdot \|\Delta\boldsymbol{b}\|_2.$$

Mindkét oldalt $\|\boldsymbol{x}\|_2$-vel elosztva a következő korlátot kapjuk:

$$\begin{aligned} \frac{\|\Delta \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} & \leq \|\boldsymbol{A}^{+}\|_{2} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{x}\|_{2}} \\ & = \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{b}\|_{2}}{\|\boldsymbol{A}\|_{2} \cdot \|\boldsymbol{x}\|_{2}} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}} \\ & \leq \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{b}\|_{2}}{\|\boldsymbol{A}\boldsymbol{x}\|_{2}} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}} \\ & = \operatorname{cond}(\boldsymbol{A}) \frac{1}{\cos(\theta)} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}}. \end{aligned}$$

Tehát a legkisebb négyzetes $\boldsymbol{x}$ megoldásnak a $\boldsymbol{b}$-beli perturbációkra vonatkozó kondíciószáma függ $\operatorname{cond}(\boldsymbol{A})$-tól és a $\boldsymbol{b}$ és az $\boldsymbol{A}\boldsymbol{x}$ közötti $\theta$ szögtől is (lásd a 3.2. ábrát). Nevezetesen, a kondíciószám közelítőleg $\operatorname{cond}(\boldsymbol{A})$, amikor a maradék kicsi, azaz $\cos(\theta) \approx 1$, de a kondíciószám tetszőlegesen rosszabb is lehet $\operatorname{cond}(\boldsymbol{A})$-nál, amikor a maradék nagy, vagyis $\cos(\theta) \approx 0$.

Az $\boldsymbol{A} + \boldsymbol{E}$ perturbált mátrix esetén a perturbált megoldást a normálegyenletek adják meg:

$$(\boldsymbol{A} + \boldsymbol{E})^T (\boldsymbol{A} + \boldsymbol{E})(\boldsymbol{x} + \Delta\boldsymbol{x}) = (\boldsymbol{A} + \boldsymbol{E})^T \boldsymbol{b}.$$

Figyelembe véve, hogy $\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b}$, elhagyva a másodrendű tagokat (azaz a kis perturbációk szorzatait), és átrendezve, azt kapjuk, hogy

$$\begin{array}{lll} \boldsymbol{A}^T\boldsymbol{A}\,\Delta\boldsymbol{x} & \approx & \boldsymbol{E}^T\boldsymbol{b} - \boldsymbol{E}^T\boldsymbol{A}\boldsymbol{x} - \boldsymbol{A}^T\boldsymbol{E}\boldsymbol{x} \\ & = & \boldsymbol{E}^T(\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}) - \boldsymbol{A}^T\boldsymbol{E}\boldsymbol{x} \\ & = & \boldsymbol{E}^T\boldsymbol{r} - \boldsymbol{A}^T\boldsymbol{E}\boldsymbol{x}, \end{array}$$

így

$$\Delta\boldsymbol{x} \approx (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{E}^T \boldsymbol{r} - (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T \boldsymbol{E} \boldsymbol{x} = (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{E}^T \boldsymbol{r} - \boldsymbol{A}^+ \boldsymbol{E} \boldsymbol{x}.$$

Normát véve:

$$\|\Delta\boldsymbol{x}\|_2 \lesssim \|(\boldsymbol{A}^T \boldsymbol{A})^{-1}\|_2 \cdot \|\boldsymbol{E}\|_2 \cdot \|\boldsymbol{r}\|_2 + \|\boldsymbol{A}^+\|_2 \cdot \|\boldsymbol{E}\|_2 \cdot \|\boldsymbol{x}\|_2.$$

Mindkét oldalt $\|\boldsymbol{x}\|_2$-vel elosztva, és felhasználva, hogy $\|\boldsymbol{A}\|_2^2 \cdot \|(\boldsymbol{A}^T \boldsymbol{A})^{-1}\|_2 = [\operatorname{cond}(\boldsymbol{A})]^2$, a következő korlátot kapjuk:

$$\begin{aligned} \frac{\|\Delta \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} & \lesssim \|(\boldsymbol{A}^{T}\boldsymbol{A})^{-1}\|_{2} \cdot \|\boldsymbol{E}\|_{2} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{x}\|_{2}} + \|\boldsymbol{A}^{+}\|_{2} \cdot \|\boldsymbol{E}\|_{2} \\ & = [\operatorname{cond}(\boldsymbol{A})]^{2} \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{A}\|_{2} \cdot \|\boldsymbol{x}\|_{2}} + \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \\ & \leq \left([\operatorname{cond}(\boldsymbol{A})]^{2} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{A}\boldsymbol{x}\|_{2}} + \operatorname{cond}(\boldsymbol{A})\right) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \\ & = \left([\operatorname{cond}(\boldsymbol{A})]^{2} \tan(\theta) + \operatorname{cond}(\boldsymbol{A})\right) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}}. \end{aligned}$$

Tehát a legkisebb négyzetes $\boldsymbol{x}$ megoldás $\boldsymbol{A}$-beli perturbációkra vonatkozó kondíciószáma is függ $\operatorname{cond}(\boldsymbol{A})$-tól, valamint a $\boldsymbol{b}$ és az $\boldsymbol{A}\boldsymbol{x}$ közötti $\theta$ szögtől (lásd a 3.2. ábrát). Nevezetesen, a kondíciószám közelítőleg $\operatorname{cond}(\boldsymbol{A})$, amikor a maradék kicsi, azaz $\tan(\theta) \approx 0$, de a kondíciószám lényegében négyzetre emelődik közepes nagyságú maradék esetén, és tetszőlegesen naggyá válik, ha a maradék ennél is nagyobb. Ezek az érzékenységi eredmények nemcsak a legkisebb négyzetes megoldások minőségének értékelését teszik majd lehetővé számunkra, hanem fontos szerepet játszanak az ilyen megoldások numerikus előállítására szolgáló különféle algoritmusok viszonylagos előnyeinek megértésében is.

**3.5. Példa. Érzékenység és kondicionáltság.** Ezeket a fogalmakat ismét a 3.1., a 3.3. és a 3.4. példák folytatásával szemléltetjük. A pszeudoinverz:

$$\boldsymbol{A}^{+} = (\boldsymbol{A}^{T}\boldsymbol{A})^{-1}\boldsymbol{A}^{T} = \frac{1}{4} \begin{bmatrix} 2 & 1 & 1 & -1 & -1 & 0 \\ 1 & 2 & 1 & 1 & 0 & -1 \\ 1 & 1 & 2 & 0 & 1 & 1 \end{bmatrix}.$$

A mátrixnormák kiszámítva:

$$\|\boldsymbol{A}\|_2 = 2, \qquad \|\boldsymbol{A}^+\|_2 = 1,$$

így

$$\operatorname{cond}(\boldsymbol{A}) = \|\boldsymbol{A}\|_2 \cdot \|\boldsymbol{A}^+\|_2 = 2.$$

Az

$$\cos(\theta) = \frac{\|\boldsymbol{A}\boldsymbol{x}\|_2}{\|\boldsymbol{b}\|_2} = \frac{\|\boldsymbol{y}\|_2}{\|\boldsymbol{b}\|_2} \approx \frac{3640{,}8761}{3640{,}8809} \approx 0{,}99999868$$

arányból azt kapjuk, hogy a $\boldsymbol{b}$ és az $\boldsymbol{y}$ közötti $\theta$ szög körülbelül $0{,}001625$, ami nagyon apró, ahogyan egy az adatokhoz nagyon szorosan illeszkedő feladat esetén várható. A kicsi kondíciószámból és a kicsi $\theta$ szögből azt a következtetést vonjuk le, hogy ez a konkrét legkisebb négyzetek feladat jól kondicionált.

**3.6. Példa. A kondíciószám négyzetre emelése.** Tekintsük a következő mátrixot és perturbációt:

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 \\ \epsilon & -\epsilon \\ 0 & 0 \end{bmatrix}, \qquad \boldsymbol{E} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ -\epsilon & \epsilon \end{bmatrix},$$

ahol $\epsilon \ll 1$, mondjuk $\epsilon$ körülbelül $\sqrt{\epsilon_{\text{mach}}}$ nagyságrendű, amelyre

$$\operatorname{cond}(\boldsymbol{A}) = 1/\epsilon, \qquad \|\boldsymbol{E}\|_2 / \|\boldsymbol{A}\|_2 = \epsilon.$$

A $\boldsymbol{b} = [1 \ 0 \ 0]^T$ jobb oldali vektor esetén $\|\Delta\boldsymbol{x}\|_2 / \|\boldsymbol{x}\|_2 = 0{,}5\epsilon$, tehát a megoldás relatív perturbációja körülbelül annyi, mint $\operatorname{cond}(\boldsymbol{A})$-szorosa az $\boldsymbol{A}$ relatív perturbációjának. Ennél a jobb oldalnál nem lép fel a kondíciószám négyzetre emelésének hatása, mert a maradék kicsi, és $\tan(\theta) \approx \epsilon$, így a perturbációs korlátban szereplő négyzetre emelt kondíciószámú tag lényegében elnyomódik.

A $\boldsymbol{b} = [1 \ 0 \ 1]^T$ jobb oldali vektor esetén viszont $\|\Delta\boldsymbol{x}\|_2 / \|\boldsymbol{x}\|_2 = 0{,}5/\epsilon$, tehát a megoldás relatív perturbációja körülbelül annyi, mint $[\operatorname{cond}(\boldsymbol{A})]^2$-szerese az $\boldsymbol{A}$ relatív perturbációjának. Ennél a jobb oldalnál a maradék normája körülbelül $1$, és $\tan(\theta) \approx 1$, így a perturbációs korlátban szereplő négyzetre emelt kondíciószámú tag nem nyomódik el, és a megoldás rendkívül érzékeny. <!-- TODO: verify original "1, say around √mach" – OCR hiányos, valószínűleg "ε ≪ 1, say around √ε_mach" -->

# 3.4 Feladat-átalakítások

Most több olyan módszert tekintünk, amellyel egy túlhatározott lineáris legkisebb négyzetek $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ feladat négyzetes (végül is háromszögű) lineáris egyenletrendszerré alakítható át, így az a 2. fejezet módszereivel megoldható.

### 3.4.1 Normálegyenletek

Ahogyan a 3.2.1. szakaszban láttuk, ha az $\boldsymbol{A}$ oszloprangja maximális, akkor az $n \times n$-es, szimmetrikus, pozitív definit

$$\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b}$$

normálegyenletek megoldása ugyanaz az $\boldsymbol{x}$, mint az $m \times n$-es $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladaté. Ezt a négyzetes rendszert úgy oldjuk meg, hogy kiszámítjuk a Cholesky-felbontást (lásd a 2.5.1. szakaszt):

$$\boldsymbol{A}^T \boldsymbol{A} = \boldsymbol{L}\boldsymbol{L}^T,$$

ahol $\boldsymbol{L}$ alsó háromszögmátrix, majd az $\boldsymbol{x}$ megoldás az $\boldsymbol{L}\boldsymbol{y} = \boldsymbol{A}^T \boldsymbol{b}$ és $\boldsymbol{L}^T \boldsymbol{x} = \boldsymbol{y}$ háromszögű rendszerek megoldásával számítható ki.

A normálegyenletek használata egy túlhatározott legkisebb négyzetek feladat megoldására annak a korábban említett általános stratégiának a példája, amelyben egy nehéz feladatot azonos megoldású, egyre könnyebb feladatokká alakítunk át. Ebben az esetben a feladat-átalakítások sorozata:

téglalap alakú $\longrightarrow$ négyzetes $\longrightarrow$ háromszögű.

Ez a módszer azonban egyúttal egy másik fontos tényre is rávilágít, nevezetesen arra, hogy egy elméletileg helyes feladat-átalakítás numerikusan nem mindig ajánlott. A normálegyenletek rendszere elméletben a lineáris legkisebb négyzetek feladat pontos megoldását adja, a gyakorlatban azonban ez a megközelítés olykor kiábrándítóan pontatlan eredményeket szolgáltat. Ennek a viselkedésnek két oka van:

- A keresztszorzat-mátrix és a jobb oldali vektor képzése során információ veszhet el. Például legyen

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 \\ \epsilon & 0 \\ 0 & \epsilon \end{bmatrix},$$

ahol $0 < \epsilon < \sqrt{\epsilon_{\text{mach}}}$ az adott lebegőpontos rendszerben. Ekkor lebegőpontos aritmetikában

$$\boldsymbol{A}^T \boldsymbol{A} = \begin{bmatrix} 1 + \epsilon^2 & 1 \\ 1 & 1 + \epsilon^2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix},$$

amely a munkapontosság erejéig szinguláris.

- A keresztszorzat-mátrix kondíciószáma – amely a normálegyenletek megoldásának érzékenységét határozza meg (lásd a 2.3. szakaszt) – az eredeti $\boldsymbol{A}$ mátrix kondíciószámának négyzete:

$$\operatorname{cond}(\boldsymbol{A}^T \boldsymbol{A}) = [\operatorname{cond}(\boldsymbol{A})]^2.$$

A 3.3. szakaszban láttuk, hogy a legkisebb négyzetes megoldások érzékenységében fellép a kondíciószám potenciális négyzetre emelésének hatása, ez azonban csak akkor lenne jelentős tényező, amikor a maradék nagy (vagyis az illeszkedés rossz). Sajnos a normálegyenletek akkor is elszenvedhetik a kondíciószám négyzetre emelésének hatását, amikor az illeszkedés jó és a maradék kicsi, így a számított megoldás érzékenyebbé válik, mint amennyit a mögöttes legkisebb négyzetek feladat önmagában indokolna. Ebben az értelemben a normálegyenletek módszere instabil.

Ezek a hiányosságok nem teszik használhatatlanná a normálegyenletek módszerét, de aggodalomra adnak okot, és indokolttá teszik, hogy numerikusan robusztusabb módszereket keressünk a lineáris legkisebb négyzetek feladataira.

### 3.4.2 Kibővített rendszer

Egy másik mód, ahogyan egy legkisebb négyzetek feladat négyzetes lineáris egyenletrendszerré alakítható, az, hogy beágyazzuk egy nagyobb rendszerbe. A $\boldsymbol{r}$ maradékvektor definíciója és az a követelmény, hogy a maradék merőleges legyen az $\boldsymbol{A}$ oszlopaira, együtt a következő két egyenletből álló rendszert adja:

$$\begin{array}{rcl} \boldsymbol{r} + \boldsymbol{A}\boldsymbol{x} &=& \boldsymbol{b}, \\ \boldsymbol{A}^T \boldsymbol{r} &=& \boldsymbol{0}, \end{array}$$

amely mátrixalakban $(m+n) \times (m+n)$-es kibővített rendszerként írható fel:

$$\begin{bmatrix} \boldsymbol{I} & \boldsymbol{A} \\ \boldsymbol{A}^T & \boldsymbol{O} \end{bmatrix} \begin{bmatrix} \boldsymbol{r} \\ \boldsymbol{x} \end{bmatrix} = \begin{bmatrix} \boldsymbol{b} \\ \boldsymbol{0} \end{bmatrix},$$

amelynek megoldása a keresett $\boldsymbol{x}$ megoldást és az ahhoz tartozó $\boldsymbol{r}$ maradékot egyszerre szolgáltatja.

Első pillantásra ez a módszer nem tűnik ígéretesnek: a kibővített rendszer szimmetrikus, de nem pozitív definit, nagyobb az eredeti rendszernél, és megköveteli, hogy az $\boldsymbol{A}$ két példányát tároljuk. Ráadásul, ha pusztán a főátló mentén választunk főelemet (ami a $2 \times 2$-es blokkrendszer blokkonkénti eliminációjával egyenértékű), akkor a normálegyenleteket kapjuk vissza, amelyek potenciális numerikus gyengeségét már megfigyeltük. Az egyetlen elért előny az, hogy most más főelemkiválasztási stratégiák is rendelkezésünkre állnak, amelyek numerikus vagy más okokból hasznosak lehetnek.

A kibővített rendszer mátrixának szimmetrikus indefinit (lásd a 2.5.2. szakaszt) vagy LU-felbontásában a főelemek megválasztása nyilvánvalóan a felső és az alsó blokksorokban szereplő elemek relatív nagyságától függ. A $\boldsymbol{r}$ és az $\boldsymbol{x}$ relatív skálái önkényesek, ezért egy $\alpha$ skálázási paramétert vezetünk be a maradékhoz, ami a következő új rendszert adja:

$$\begin{bmatrix} \alpha \boldsymbol{I} & \boldsymbol{A} \\ \boldsymbol{A}^T & \boldsymbol{O} \end{bmatrix} \begin{bmatrix} \boldsymbol{r}/\alpha \\ \boldsymbol{x} \end{bmatrix} = \begin{bmatrix} \boldsymbol{b} \\ \boldsymbol{0} \end{bmatrix}.$$

Az $\alpha$ paraméter azt szabályozza, hogyan súlyozódnak a két alrendszer elemei egymáshoz képest a főelemek kiválasztásakor. Ésszerű ökölszabályként

$$\alpha = \max_{i,j} |a_{ij}|/1000$$

használható, de a legjobb érték meghatározásához némi kísérletezésre lehet szükség.

A módszer közvetlen implementációja aránytalanul nagy számításigényű lehet ($(m+n)^3$-nal arányos), ezért gondosan ki kell használni a kibővített mátrix speciális szerkezetét. A kibővített rendszer módszerét például a MATLAB hatékonyan használja nagy, ritka lineáris legkisebb négyzetek feladatokra.

### 3.4.3 Ortogonális transzformációk

A normálegyenletek megközelítésének potenciális numerikus nehézségei miatt szükségünk van egy olyan alternatívára, amely nem igényli a keresztszorzat-mátrix és a jobb oldali vektor képzését. Ezért egy numerikusan robusztusabb típusú transzformációt keresünk, amely egy egyszerűbb feladatra vezet, amelynek megoldása ugyanaz, mint az eredeti legkisebb négyzetek feladaté, de könnyebben számítható. Ahogyan a négyzetes lineáris rendszereknél, úgy itt is azt látjuk majd, hogy a háromszögű alak megfelelő célalak a legkisebb négyzetek feladatok egyszerűsítésére. Egy mátrix háromszögűvé alakítása Gauss-eliminációval azonban ebben a kontextusban nem megfelelő, mert egy ilyen transzformáció nem őrzi meg az euklideszi normát, és ennélfogva a legkisebb négyzetes megoldást sem.

Az ortogonalitásról korábban mondottakat alapul véve most olyan típusú lineáris transzformációt definiálunk, amely *megőrzi* az euklideszi normát. Egy négyzetes valós $\boldsymbol{Q}$ mátrixot *ortogonálisnak* mondunk, ha az oszlopai ortonormáltak, azaz ha $\boldsymbol{Q}^T \boldsymbol{Q} = \boldsymbol{I}$, az egységmátrix. Egy $\boldsymbol{Q}$ ortogonális transzformáció tetszőleges $\boldsymbol{v}$ vektor euklideszi normáját megőrzi, hiszen

$$\|\boldsymbol{Q}\boldsymbol{v}\|_2^2 = (\boldsymbol{Q}\boldsymbol{v})^T \boldsymbol{Q}\boldsymbol{v} = \boldsymbol{v}^T \boldsymbol{Q}^T \boldsymbol{Q} \boldsymbol{v} = \boldsymbol{v}^T \boldsymbol{v} = \|\boldsymbol{v}\|_2^2.$$

Az ortogonális mátrixok különböző módokon – például forgatással vagy tükrözéssel – transzformálhatnak vektorokat, de egy vektor euklideszi hosszát nem változtatják meg. Ennélfogva, ha egy lineáris legkisebb négyzetek feladat mindkét oldalát megszorozzuk egy ortogonális mátrixszal, a megoldás nem változik.

Az ortogonális mátrixok a numerikus számítások számos területén rendkívül fontosak, mert normamegőrző tulajdonságuk miatt nem erősítik fel a hibát. Így például ortogonális transzformációkkal négyzetes lineáris rendszerek is megoldhatók anélkül, hogy a numerikus stabilitás érdekében főelemkiválasztást kellene alkalmaznunk. Sajnos az ortogonalizáló módszerek számítási szempontból lényegesen költségesebbek, mint a Gauss-eliminációra épülők, ezért jobb numerikus tulajdonságaikért olyan árat kell fizetni, amely a kontextustól függően megérheti, vagy sem.

### 3.4.4 Háromszögű legkisebb négyzetek feladatok

Most, hogy a birtokunkban van egy olyan transzformációcsalád, amely megőrzi a legkisebb négyzetes megoldást, a következő lépés, hogy találjunk egy megfelelő célalakot, amelyre egyszerűsítve a legkisebb négyzetek feladat könnyen megoldhatóvá válik. Ahogyan a négyzetes lineáris rendszereknél tettük, most is olyan legkisebb négyzetek feladatot tekintünk, amelyben felső háromszögmátrix szerepel. A túlhatározott esetben, azaz amikor $m > n$, egy ilyen feladat alakja

$$\begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix} \boldsymbol{x} \cong \begin{bmatrix} \boldsymbol{c}_1 \\ \boldsymbol{c}_2 \end{bmatrix},$$

ahol $\boldsymbol{R}$ egy $n \times n$-es felső háromszögmátrix, és a $\boldsymbol{c}$ jobb oldali vektort is hasonlóan particionáltuk. A legkisebb négyzetek maradéka ekkor

$$\|\boldsymbol{r}\|_2^2 = \|\boldsymbol{c}_1 - \boldsymbol{R}\boldsymbol{x}\|_2^2 + \|\boldsymbol{c}_2\|_2^2.$$

Mivel a fenti összeg második tagja, $\|\boldsymbol{c}_2\|_2^2$, független $\boldsymbol{x}$-től, így arra nincs befolyásunk, az első tag azonban nullává tehető, ha $\boldsymbol{x}$-et úgy választjuk meg, hogy kielégítse az

$$\boldsymbol{R}\boldsymbol{x} = \boldsymbol{c}_1$$

háromszögű rendszert, amely $\boldsymbol{x}$-re visszahelyettesítéssel megoldható. Ezzel megtaláltuk az $\boldsymbol{x}$ legkisebb négyzetes megoldást, és azt is leszűrhetjük, hogy a négyzetösszeg minimuma

$$\|\boldsymbol{r}\|_2^2 = \|\boldsymbol{c}_2\|_2^2.$$

## 3.4.5 QR-felbontás

A háromszögű alakra való ortogonális transzformációt a QR-felbontással valósítjuk meg, amelynek alakja egy $m \times n$-es $\boldsymbol{A}$ mátrix esetén $m > n$ mellett

$$\boldsymbol{A} = \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix},$$

ahol $\boldsymbol{Q}$ egy $m \times m$-es ortogonális mátrix, $\boldsymbol{R}$ pedig egy $n \times n$-es felső háromszögmátrix. Egy ilyen felbontás az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetek feladatot azonos megoldású háromszögű legkisebb négyzetek feladattá alakítja, hiszen

$$\|\boldsymbol{r}\|_2^2 = \|\boldsymbol{b} - \boldsymbol{A}\boldsymbol{x}\|_2^2 = \left\|\boldsymbol{b} - \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}\boldsymbol{x}\right\|_2^2 = \left\|\boldsymbol{Q}^T \boldsymbol{b} - \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}\boldsymbol{x}\right\|_2^2 = \|\boldsymbol{c}_1 - \boldsymbol{R}\boldsymbol{x}\|_2^2 + \|\boldsymbol{c}_2\|_2^2,$$

ahol a transzformált jobb oldalt

$$\boldsymbol{Q}^T \boldsymbol{b} = \begin{bmatrix} \boldsymbol{c}_1 \\ \boldsymbol{c}_2 \end{bmatrix}$$

úgy particionáltuk, hogy $\boldsymbol{c}_1$ egy $n$-dimenziós vektor. Az $\boldsymbol{x}$ megoldás ekkor kielégíti az $n \times n$-es $\boldsymbol{R}\boldsymbol{x} = \boldsymbol{c}_1$ háromszögű lineáris egyenletrendszert, a minimális maradéknorma értéke pedig $\|\boldsymbol{r}\|_2 = \|\boldsymbol{c}_2\|_2$. A következő szakaszban fogjuk látni, hogyan számítható ki a QR-felbontás.

A QR-felbontásnak a legkisebb négyzetek feladatok megoldásán kívül sok más alkalmazása is van. Ha a $\boldsymbol{Q}$-t $\boldsymbol{Q} = [\boldsymbol{Q}_1 \ \boldsymbol{Q}_2]$ alakban particionáljuk, ahol $\boldsymbol{Q}_1$ a $\boldsymbol{Q}$ első $n$ oszlopát, $\boldsymbol{Q}_2$ pedig a maradék $m - n$ oszlopot tartalmazza, akkor

$$\boldsymbol{A} = \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix} = \begin{bmatrix} \boldsymbol{Q}_1 & \boldsymbol{Q}_2 \end{bmatrix} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix} = \boldsymbol{Q}_1 \boldsymbol{R}.$$

Az olyan $\boldsymbol{A} = \boldsymbol{Q}_1 \boldsymbol{R}$ alakú felbontást, amelyben $\boldsymbol{Q}_1$ oszlopai ortonormáltak és $\boldsymbol{Q}_1$ mérete megegyezik $\boldsymbol{A}$-éval, $\boldsymbol{R}$ pedig négyzetes és felső háromszögű, olykor az $\boldsymbol{A}$ redukált, vagy „economy size" QR-felbontásának nevezik. Ha az $\boldsymbol{A}$ oszloprangja maximális, azaz $\boldsymbol{R}$ nemszinguláris, akkor a $\boldsymbol{Q}_1$ oszlopai a $\operatorname{span}(\boldsymbol{A})$ altér egy ortonormált bázisát alkotják, a $\boldsymbol{Q}_2$ oszlopai pedig a $\operatorname{span}(\boldsymbol{A})$ ortogonális komplementumának, azaz a $\operatorname{span}(\boldsymbol{A})^{\perp}$ altérnek – amely megegyezik az $\boldsymbol{A}^T$ nullterével, $\{\boldsymbol{z} \in \mathbb{R}^m : \boldsymbol{A}^T \boldsymbol{z} = \boldsymbol{0}\}$-val – egy ortonormált bázisát alkotják. Az ilyen ortonormált bázisok nemcsak a legkisebb négyzetek számításaiban hasznosak – amint azt a 3.2.2. szakasz végén láttuk –, hanem sajátérték-számításokban, optimalizálásban és számos további, a későbbiekben előkerülő feladatban is.

# 3.5 Ortogonalizációs módszerek

Egy mátrix QR-felbontásának kiszámításához hasonló megközelítést követünk, mint a Gauss-eliminációval végzett LU-felbontásnál: egymás után vezetünk be nullákat az $\boldsymbol{A}$ mátrixba, míg végül felső háromszögalakot kapunk; most azonban nem elemi eliminációs mátrixokat, hanem ortogonális transzformációkat használunk, hogy az euklideszi norma megmaradjon. Számos ilyen ortogonalizációs módszer elterjedt, többek között

- Householder-transzformációk (elemi reflektorok)
- Givens-transzformációk (síkbeli forgatások)
- Gram–Schmidt-ortogonalizáció

Elsősorban a Householder-transzformációk használatára összpontosítunk, hiszen ez a legelterjedtebb, és ebben a kontextusban általában a leghatékonyabb eljárás is, de a másik két módszert is felvázoljuk.

#### 3.5.1 Householder-transzformációk

Olyan ortogonális transzformációt keresünk, amely egy adott vektor kívánt komponenseit nullázza ki. Ennek egyik módja a *Householder-transzformáció*, más néven *elemi reflektor*, amely a

$$\boldsymbol{H} = \boldsymbol{I} - 2\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}}$$

alakú mátrix, ahol $\boldsymbol{v}$ nemnulla vektor. A definícióból azonnal látszik, hogy $\boldsymbol{H} = \boldsymbol{H}^T = \boldsymbol{H}^{-1}$, vagyis a $\boldsymbol{H}$ egyszerre ortogonális és szimmetrikus. Adott $\boldsymbol{a}$ vektor esetén a $\boldsymbol{v}$ vektort úgy szeretnénk megválasztani, hogy az $\boldsymbol{a}$ első komponensén kívül minden további komponens nullává váljon, azaz

$$\boldsymbol{H}\boldsymbol{a} = \begin{bmatrix} \alpha \\ 0 \\ \vdots \\ 0 \end{bmatrix} = \alpha \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} = \alpha \boldsymbol{e}_1.$$

A $\boldsymbol{H}$ képletét felhasználva

$$\alpha\, \boldsymbol{e}_1 = \boldsymbol{H}\boldsymbol{a} = \left(\boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}}\right)\boldsymbol{a} = \boldsymbol{a} - 2\,\boldsymbol{v}\,\frac{\boldsymbol{v}^T\boldsymbol{a}}{\boldsymbol{v}^T\boldsymbol{v}},$$

és így

$$\boldsymbol{v} = (\boldsymbol{a} - \alpha\,\boldsymbol{e}_1)\,\frac{\boldsymbol{v}^T\boldsymbol{v}}{2\boldsymbol{v}^T\boldsymbol{a}}.$$

A skaláris szorzó azonban közömbös a $\boldsymbol{v}$ meghatározása szempontjából, mert a $\boldsymbol{H}$ képletéből úgyis kiesik, ezért vehetjük, hogy

$$\boldsymbol{v} = \boldsymbol{a} - \alpha\,\boldsymbol{e}_1.$$

A norma megőrzéséhez szükségképpen $\alpha = \pm \|\boldsymbol{a}\|_2$, az előjelet pedig úgy kell megválasztani, hogy elkerüljük a számjegykioltást (azaz $\alpha = -\mathrm{sign}(a_1)\|\boldsymbol{a}\|_2$). További lehetséges numerikus nehézség, hogy a $\|\boldsymbol{a}\|_2$ kiszámítása fölösleges túlcsorduláshoz vagy alulcsorduláshoz vezethet, ha az $\boldsymbol{a}$ komponensei nagyon nagyok vagy nagyon kicsik. Ezt elkerülhetjük, ha az $\boldsymbol{a}$ vektort már az elején elosztjuk a legnagyobb abszolút értékű komponensével. Ez a skálatényező a kapott $\boldsymbol{H}$ transzformációt sem változtatja meg.

A fenti algebrai levezetés mélyebb megértése érdekében tekintsük a 3.3. ábrán szemléltetett geometriai értelmezést. Az $\boldsymbol{a}$ vektort úgy vihetjük át az első koordinátatengelyre (ahol a többi komponense nullává válik) a normáját megőrizve, hogy tükrözzük azt valamelyik hipersíkra a kettő közül (a kétdimenziós ábrákon szaggatott vonalakkal jelölt hipersíkokra), amelyek az $\boldsymbol{a}$ és az első koordinátatengely közötti két szöget megfelezik. Az így kapott transzformált vektor $\pm \|\boldsymbol{a}\|_2 \boldsymbol{e}_1$ lesz, attól függően, hogy a két hipersík közül melyiket választjuk. Egy ilyen hipersík alakja $\operatorname{span}(\boldsymbol{v})^{\perp} = \{\boldsymbol{x} : \boldsymbol{v}^T\boldsymbol{x} = 0\}$ valamilyen nemnulla $\boldsymbol{v}$ vektorra. Az ábrákból jól látszik, hogy a $\boldsymbol{v}$ párhuzamos kell, hogy legyen az $\boldsymbol{a} - \alpha \boldsymbol{e}_1$ vektorral, ahol $\alpha = \pm \|\boldsymbol{a}\|_2$ – a hipersík választásától függően. Emlékezzünk a 3.2.2. szakaszból arra, hogy a $\operatorname{span}(\boldsymbol{v})$-re vetítő ortogonális projektor $\boldsymbol{P} = \boldsymbol{v}(\boldsymbol{v}^T\boldsymbol{v})^{-1}\boldsymbol{v}^T = (\boldsymbol{v}\boldsymbol{v}^T)/(\boldsymbol{v}^T\boldsymbol{v})$, a $\operatorname{span}(\boldsymbol{v})^{\perp}$-re vetítő projektor pedig $\boldsymbol{I} - \boldsymbol{P}$. Ennélfogva $(\boldsymbol{I} - \boldsymbol{P})\boldsymbol{a} = \boldsymbol{a} - \boldsymbol{v}(\boldsymbol{v}^T\boldsymbol{a})/(\boldsymbol{v}^T\boldsymbol{v})$ adja az $\boldsymbol{a}$ vektornak a hipersíkra vett vetületét, de az első koordinátatengely eléréséhez kétszer olyan messzire kell elmennünk, azaz $\boldsymbol{a} - 2\boldsymbol{v}(\boldsymbol{v}^T\boldsymbol{a})/(\boldsymbol{v}^T\boldsymbol{v})$-ig, így a keresett transzformáció $\boldsymbol{H} = \boldsymbol{I} - 2\boldsymbol{P} = \boldsymbol{I} - 2(\boldsymbol{v}\boldsymbol{v}^T)/(\boldsymbol{v}^T\boldsymbol{v})$. Elvben bármelyik hipersík választása működik, de ahhoz, hogy véges precíziójú aritmetikában a $\boldsymbol{v}$ kiszámítása során elkerüljük a számjegykioltást, az $\alpha$-nak azt az előjelét kell választanunk, amelyhez az első koordinátatengelyen az $\boldsymbol{a}$-tól távolabbi pont tartozik. Az ábrákon szereplő példavektor esetén a pozitív előjelet kell választani (azaz a jobb oldali ábrát), mert $a_1$ negatív.

![](_page_18_Figure_2.jpeg)

3.3. ábra: A Householder-transzformáció geometriai értelmezése tükrözésként.

**3.7. Példa. Householder-transzformáció.** A most leírt konstrukció szemléltetéséhez olyan Householder-transzformációt határozunk meg, amely a

$$\boldsymbol{a} = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix}$$

vektor első komponensén kívül minden komponensét kinullázza.

Az ismertetett recept szerint a

$$\boldsymbol{v} = \boldsymbol{a} - \alpha \boldsymbol{e}_1 = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix} - \alpha \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix} - \begin{bmatrix} \alpha \\ 0 \\ 0 \end{bmatrix}$$

vektort választjuk, ahol $\alpha = \pm \|\boldsymbol{a}\|_2 = \pm 3$. Mivel $a_1$ pozitív, a számjegykioltást úgy kerülhetjük el, ha az $\alpha$-hoz a negatív előjelet választjuk. Így

$$\boldsymbol{v} = \begin{bmatrix} 2\\1\\2 \end{bmatrix} - \begin{bmatrix} -3\\0\\0 \end{bmatrix} = \begin{bmatrix} 5\\1\\2 \end{bmatrix}.$$

Annak ellenőrzésére, hogy a Householder-transzformáció a vártnak megfelelően viselkedik, kiszámoljuk, hogy

$$\boldsymbol{H}\boldsymbol{a} = \boldsymbol{a} - 2\,\frac{\boldsymbol{v}^T\boldsymbol{a}}{\boldsymbol{v}^T\boldsymbol{v}}\,\boldsymbol{v} = \begin{bmatrix} 2\\1\\2 \end{bmatrix} - 2\,\frac{15}{30}\begin{bmatrix} 5\\1\\2 \end{bmatrix} = \begin{bmatrix} -3\\0\\0 \end{bmatrix},$$

ami azt mutatja, hogy az eredmény nullamintázata helyes, és a 2-norma megmarad. Figyeljük meg, hogy a $\boldsymbol{H}$ mátrixot nem kell explicit módon felírnunk, hiszen a $\boldsymbol{H}$ bármely vektorra való alkalmazásához elegendő a $\boldsymbol{v}$ vektor ismerete.

Eddig azt mutattuk meg, hogyan konstruálhatunk Householder-transzformációt, amely egy adott vektor első komponensén kívül minden komponensét kinullázza. Általánosabban, egy adott $m$-dimenziós $\boldsymbol{a}$ vektorhoz tekintsük a

$$\boldsymbol{a} = \begin{bmatrix} \boldsymbol{a}_1 \\ \boldsymbol{a}_2 \end{bmatrix}$$

partíciót, ahol $\boldsymbol{a}_1$ egy $(k-1)$-dimenziós vektor, $1 \le k < m$. Ha a Householder-vektort a

$$\boldsymbol{v} = \begin{bmatrix} \boldsymbol{0} \\ \boldsymbol{a}_2 \end{bmatrix} - \alpha\,\boldsymbol{e}_k$$

alakban vesszük, ahol $\alpha = -\mathrm{sign}(a_k)\|\boldsymbol{a}_2\|_2$, akkor az ebből adódó Householder-transzformáció az $\boldsymbol{a}$ utolsó $m - k$ komponensét nullázza ki. Ilyen Householder-transzformációk sorozatát $k = 1, \ldots, n$ értékekre alkalmazva egy $m \times n$-es $\boldsymbol{A}$ mátrix minden főátló alatti elemét kinullázhatjuk – oszloponként haladva balról jobbra –, és így a mátrixot felső háromszögalakra hozzuk. Minden Householder-transzformációt a mátrix még redukálatlan részére kell alkalmazni, de a már redukált korábbi oszlopokat nem érinti, ezért a nullák az egymás utáni transzformációk során megmaradnak. Egy tetszőleges $\boldsymbol{u}$ vektorra alkalmazott $\boldsymbol{H}$ Householder-transzformáció esetén

$$\boldsymbol{H}\boldsymbol{u} = \left(\boldsymbol{I} - 2\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}}\right)\boldsymbol{u} = \boldsymbol{u} - \left(2\frac{\boldsymbol{v}^T\boldsymbol{u}}{\boldsymbol{v}^T\boldsymbol{v}}\right)\boldsymbol{v},$$

amelynek kiszámítása lényegesen olcsóbb, mint egy általános mátrix-vektor szorzásé, és csupán a $\boldsymbol{v}$ vektor ismeretét igényli, a $\boldsymbol{H}$ mátrix explicit felírását nem. Egy $m \times n$-es $\boldsymbol{A}$ mátrix Householder-transzformációkkal történő QR-felbontását a 3.1. algoritmus foglalja össze; benne az $\boldsymbol{A}$ mátrix $j$-edik oszlopát $\boldsymbol{a}_j$ jelöli, az egyszerűség kedvéért pedig elhagytuk azt a skálázást, amely robusztus megvalósításhoz elengedhetetlen volna. Hatékony megvalósításban kerülnénk az egyes $\boldsymbol{v}_k$ vezető nulláival végzett műveleteket. Az algoritmus végén a mátrix felső háromszögű lesz.

Vegyük észre, hogy ha valamely $k$ lépésnél $\beta_k = 0$, akkor az ebben a lépésben kinullázandó főátló alatti elemek már eleve nullák, így egyszerűen továbbléphetünk a következő oszlopra, és a QR-felbontás ettől még befejezhető. Az $\alpha_k$ előjelének választása miatt azonban $\beta_k$ csak akkor lehet nulla, ha $a_{kk}$ is nulla, ami azt jelenti, hogy az $\boldsymbol{A}$ $k$-adik oszlopa lineárisan függ az első $k-1$ oszloptól, tehát az $\boldsymbol{A}$ nem teljes oszlopú rangú. Ekkor a kapott $\boldsymbol{R}$ felső háromszögmátrixnak lesz nulla főátlóeleme, és így szinguláris lesz. Alattomosabb gond, ha a főátlóban egy nagyon kicsi, de nemnulla elem jelenik meg, ami közel ranghiányra utal. A ranghiány és a közel ranghiány következményeit a 3.5.4. szakaszban tárgyaljuk.

A most leírt folyamat egy

$$\boldsymbol{H}_n \cdots \boldsymbol{H}_1 \boldsymbol{A} = \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}$$

alakú felbontást ad,

#### 3.1. Algoritmus. Householder QR-felbontás.

```
for k = 1 to min(n, m − 1)                                { ciklus az oszlopokra }
    αk = −sign(akk) √(akk² + … + amk²)
    vk = [0 … 0  akk … amk]ᵀ − αk ek                      { Householder-vektor
                                                            kiszámítása a
                                                            jelenlegi oszlopra }
    βk = vkᵀ vk
    if βk = 0 then                                        { az aktuális oszlop
        continue with next k                                átugrása, ha az
                                                            már nulla }
    for j = k to n                                        { transzformáció
        γj = vkᵀ aj                                         alkalmazása a maradék
        aj = aj − (2γj/βk) vk                               részmátrixra }
    end
end
```

ahol $\boldsymbol{R}$ felső háromszögű. Az egymást követő Householder-transzformációk $\boldsymbol{H}_n \cdots \boldsymbol{H}_1$ szorzata maga is ortogonális mátrix. Így ha bevezetjük a

$$\boldsymbol{Q}^T = \boldsymbol{H}_n \cdots \boldsymbol{H}_1,$$

vagy ezzel ekvivalens módon a $\boldsymbol{Q} = \boldsymbol{H}_1 \cdots \boldsymbol{H}_n$ jelölést, akkor

$$\boldsymbol{A} = \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}.$$

Ezzel tehát valóban kiszámítottuk az $\boldsymbol{A}$ mátrix QR-felbontását, amellyel a lineáris legkisebb négyzetek feladata most már megoldható. A megoldás megőrzéséhez azonban ugyanezen Householder-transzformációk sorozatával a $\boldsymbol{b}$ jobb oldali vektort is transzformálnunk kell. Ezek után az ezzel ekvivalens, háromszögű legkisebb négyzetes feladatot oldjuk meg:

$$\begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix} \boldsymbol{x} \cong \boldsymbol{Q}^T \boldsymbol{b} = \begin{bmatrix} \boldsymbol{c}_1 \\ \boldsymbol{c}_2 \end{bmatrix}.$$

A lineáris legkisebb négyzetek feladatának megoldásához a Householder-transzformációk $\boldsymbol{Q}$ szorzatát nem szükséges explicit módon felírni. Az erre a feladatra készült szoftverek többségében a $\boldsymbol{R}$-t az eredetileg az $\boldsymbol{A}$-t tartalmazó tömb felső háromszögében tárolják, a Householder-transzformációk felírásához szükséges $\boldsymbol{v}_k$ Householder-vektorok nemnulla részeit pedig az $\boldsymbol{A}$ (most nullákká vált) alsó háromszögű részében helyezik el. (Szigorúan véve ehhez még egy $n$-dimenziós vektornyi memóriára van szükség, mivel minden Householder-vektornak eggyel több nemnulla komponense van, mint ahányat az $\boldsymbol{A}$ megfelelő oszlopának főátló alatti része el tud tárolni.) Amint már láttuk, a Householder-transzformációkat amúgy is legegyszerűbben ebben az alakban alkalmazzuk (nem pedig explicit mátrix-vektor szorzással), így a $\boldsymbol{v}_k$ vektorok elegendőek mind az eredeti legkisebb négyzetes feladat, mind minden további, ugyanolyan mátrixú, de más jobb oldali vektort tartalmazó feladat megoldásához. Ha azonban a $\boldsymbol{Q}$-ra valamilyen más okból explicit alakban volna szükségünk, úgy az kiszámítható az egyes Householder-transzformációk egymás utáni szorzataként, kiindulásként az $\boldsymbol{I}$ egységmátrixszal – ehhez viszont további memória szükséges.

**3.8. Példa. Householder QR-felbontás.** A Householder QR-felbontást a 3.1. példában szereplő legkisebb négyzetes feladat megoldásával szemléltetjük. Az $\boldsymbol{A}$ első oszlopa főátló alatti elemeinek kinullázásához a $\boldsymbol{v}_1$ Householder-vektor

$$\boldsymbol{v}_1 = \boldsymbol{a}_1 - \alpha\,\boldsymbol{e}_1 = \begin{bmatrix} 1\\0\\0\\-1\\-1\\0 \end{bmatrix} - \begin{bmatrix} -1{,}7321\\0\\0\\0\\0\\0 \end{bmatrix} = \begin{bmatrix} 2{,}7321\\0\\0\\-1\\-1\\0 \end{bmatrix}.$$

Az ebből adódó $\boldsymbol{H}_1$ Householder-transzformáció alkalmazásával

$$\boldsymbol{H}_1 \boldsymbol{A} = \begin{bmatrix} -1{,}7321 & 0{,}5774 & 0{,}5774 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0{,}7887 & -0{,}2113 \\ 0 & -0{,}2113 & 0{,}7887 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \boldsymbol{H}_1 \boldsymbol{b} = \begin{bmatrix} 376 \\ 1941 \\ 2417 \\ 1026 \\ 1492 \\ 475 \end{bmatrix}.$$

A $\boldsymbol{H}_1 \boldsymbol{A}$ második oszlopa főátló alatti elemeinek kinullázásához a $\boldsymbol{v}_2$ Householder-vektor

$$\boldsymbol{v}_2 = \begin{bmatrix} 0\\1\\0\\0{,}7887\\-0{,}2113\\-1 \end{bmatrix} - \begin{bmatrix} 0\\-1{,}6330\\0\\0\\0\\0 \end{bmatrix} = \begin{bmatrix} 0\\2{,}6330\\0\\0{,}7887\\-0{,}2113\\-1 \end{bmatrix}.$$

Az ebből adódó $\boldsymbol{H}_2$ Householder-transzformáció alkalmazásával

$$\boldsymbol{H}_2 \boldsymbol{H}_1 \boldsymbol{A} = \begin{bmatrix} -1{,}7321 & 0{,}5774 & 0{,}5774 \\ 0 & -1{,}6330 & 0{,}8165 \\ 0 & 0 & 1 \\ 0 & 0 & 0{,}0332 \\ 0 & 0 & 0{,}7231 \\ 0 & 0 & 0{,}6899 \end{bmatrix}, \qquad \boldsymbol{H}_2 \boldsymbol{H}_1 \boldsymbol{b} = \begin{bmatrix} 376 \\ -1200 \\ 2417 \\ 85 \\ 1744 \\ 1668 \end{bmatrix}.$$

A $\boldsymbol{H}_2 \boldsymbol{H}_1 \boldsymbol{A}$ harmadik oszlopa főátló alatti elemeinek kinullázásához a $\boldsymbol{v}_3$ Householder-vektor

$$\boldsymbol{v}_3 = \begin{bmatrix} 0\\0\\1\\0{,}0332\\0{,}7231\\0{,}6899 \end{bmatrix} - \begin{bmatrix} 0\\0\\-1{,}4142\\0\\0\\0 \end{bmatrix} = \begin{bmatrix} 0\\0\\2{,}4142\\0{,}0332\\0{,}7231\\0{,}6899 \end{bmatrix}.$$

Az ebből adódó $\boldsymbol{H}_3$ Householder-transzformáció alkalmazásával

$$\boldsymbol{H}_3 \boldsymbol{H}_2 \boldsymbol{H}_1 \boldsymbol{A} = \begin{bmatrix} -1{,}7321 & 0{,}5774 & 0{,}5774 \\ 0 & -1{,}6330 & 0{,}8165 \\ 0 & 0 & -1{,}4142 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}$$

és

$$\boldsymbol{H}_3 \boldsymbol{H}_2 \boldsymbol{H}_1 \boldsymbol{b} = \begin{bmatrix} 376 \\ -1200 \\ -3417 \\ 5 \\ 3 \\ 1 \end{bmatrix} = \boldsymbol{Q}^T \boldsymbol{b} = \begin{bmatrix} \boldsymbol{c}_1 \\ \boldsymbol{c}_2 \end{bmatrix}.$$

Az $\boldsymbol{R}\boldsymbol{x} = \boldsymbol{c}_1$ felső háromszögű rendszert mostantól visszahelyettesítéssel oldhatjuk meg, és az $\boldsymbol{x} = [1236, 1943, 2416]^T$ megoldást kapjuk. Mind a megoldás, mind a minimális maradék négyzetösszege – $\|\boldsymbol{r}\|_2^2 = \|\boldsymbol{c}_2\|_2^2 = 35$ – megegyezik a 3.3. példában kapott értékekkel.

#### 3.5.2 Givens-forgatások

A Householder-transzformációk egyszerre sok nullát vezetnek be egy oszlopba. Bár hatékonyság szempontjából ez általában előnyös, a megközelítés túlságosan „durva" is lehet, ha nagyobb szelektivitásra van szükségünk a nullák bevezetésekor. Ezért bizonyos esetekben érdemesebb Givens-forgatásokat használni, amelyek egyszerre egy-egy nullát vezetnek be.

Olyan ortogonális mátrixot keresünk, amely egy adott vektor egyetlen komponensét nullázza ki. Ennek egyik módja a *síkbeli forgatás*, amelyet a QR-felbontás kontextusában gyakran *Givens-forgatásnak* neveznek; alakja

$$\boldsymbol{G} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix},$$

ahol $c$ és $s$ a forgatási szög koszinusza és szinusza. Az ortogonalitás megköveteli, hogy $c^2 + s^2 = 1$ teljesüljön, ami természetesen bármely szög koszinuszára és szinuszára igaz. Itt egy adott $\boldsymbol{a} = \begin{bmatrix} a_1 & a_2 \end{bmatrix}^T$ 2-dimenziós vektorra úgy szeretnénk megválasztani $c$-t és $s$-t, hogy

$$\boldsymbol{G}\boldsymbol{a} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \end{bmatrix}.$$

Azaz: ha az $\boldsymbol{a}$ vektort úgy forgatjuk el, hogy az első koordinátatengellyel párhuzamos legyen, akkor a második komponense nullává válik. A fenti egyenlet átírható a következő alakba:

$$\begin{bmatrix} a_1 & a_2 \\ a_2 & -a_1 \end{bmatrix} \begin{bmatrix} c \\ s \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \end{bmatrix}.$$

Erre a rendszerre Gauss-eliminációt végrehajtva a

$$\begin{bmatrix} a_1 & a_2 \\ 0 & -a_1 - a_2^2/a_1 \end{bmatrix} \begin{bmatrix} c \\ s \end{bmatrix} = \begin{bmatrix} \alpha \\ -\alpha a_2/a_1 \end{bmatrix}$$

háromszögű rendszert kapjuk. Visszahelyettesítéssel ezután

$$s = \frac{\alpha a_2}{a_1^2 + a_2^2}, \qquad c = \frac{\alpha a_1}{a_1^2 + a_2^2}.$$

Végül a $c^2 + s^2 = 1$ követelmény, amelyből $\alpha = \sqrt{a_1^2 + a_2^2}$, azt adja, hogy

$$c = \frac{a_1}{\sqrt{a_1^2 + a_2^2}}, \qquad s = \frac{a_2}{\sqrt{a_1^2 + a_2^2}}.$$

A Householder-transzformációkhoz hasonlóan a fölösleges túlcsordulás vagy alulcsordulás megfelelő skálázással elkerülhető. Ha $|a_1| > |a_2|$, akkor dolgozhatunk a forgatási szög tangensével, $t = s/c = a_2/a_1$, így a koszinuszt és a szinuszt a

$$c = 1/\sqrt{1 + t^2}, \qquad s = c \cdot t$$

képletek adják. Ha viszont $|a_2| > |a_1|$, akkor a $\tau = c/s = a_1/a_2$ kotangenssel analóg képleteket használhatjuk, így

$$s = 1/\sqrt{1 + \tau^2}, \qquad c = s \cdot \tau.$$

Mindkét esetben elkerüljük, hogy 1-nél nagyobb abszolút értékű számot négyzetre emeljünk. A forgatási szöget nem szükséges explicit módon meghatározni, csak a szinuszára és a koszinuszára van szükségünk.

**3.9. Példa. Givens-forgatás.** A most leírt konstrukciót úgy szemléltetjük, hogy meghatározunk egy olyan Givens-forgatást, amely az

$$\boldsymbol{a} = \begin{bmatrix} 4 \\ 3 \end{bmatrix}$$

vektor második komponensét nullázza ki.

Ennél a feladatnál a koszinuszt és a szinuszt biztonságosan közvetlenül is kiszámíthatjuk:

$$c = \frac{a_1}{\sqrt{a_1^2 + a_2^2}} = \frac{4}{5} = 0{,}8, \qquad s = \frac{a_2}{\sqrt{a_1^2 + a_2^2}} = \frac{3}{5} = 0{,}6,$$

vagy ezzel ekvivalens módon használhatjuk a $t = a_2/a_1 = 3/4 = 0{,}75$ tangenst is:

$$c = \frac{1}{\sqrt{1 + (0{,}75)^2}} = \frac{1}{1{,}25} = 0{,}8, \qquad s = c \cdot t = (0{,}8)(0{,}75) = 0{,}6.$$

Így a forgatást a

$$\boldsymbol{G} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} = \begin{bmatrix} 0{,}8 & 0{,}6 \\ -0{,}6 & 0{,}8 \end{bmatrix}$$

mátrix adja. Annak ellenőrzésére, hogy a forgatás a vártnak megfelelően viselkedik, kiszámoljuk, hogy

$$\boldsymbol{G}\boldsymbol{a} = \begin{bmatrix} 0{,}8 & 0{,}6 \\ -0{,}6 & 0{,}8 \end{bmatrix} \begin{bmatrix} 4 \\ 3 \end{bmatrix} = \begin{bmatrix} 5 \\ 0 \end{bmatrix},$$

ami azt mutatja, hogy az eredmény nullamintázata helyes, és a 2-norma megmarad. A forgatási szög értéke – ebben az esetben körülbelül $36{,}87$ fok – közvetlenül nem szerepel a számításban, és nem is szükséges explicit módon meghatározni.

Láttuk, hogyan tervezhetünk síkbeli forgatást egy 2-dimenziós vektor egyik komponensének kinullázására. Egy $m$-dimenziós vektor bármely kívánt komponensének kinullázásához ugyanezt a technikát alkalmazhatjuk: a célkomponenst – legyen ez a $j$-edik – egy másik komponenssel – mondjuk az $i$-edikkel – együtt forgatjuk. A vektor e két kiválasztott komponense a fentiek szerint határozza meg a megfelelő $2 \times 2$-es forgatási mátrixot, amelyet azután $2 \times 2$-es részmátrixként beágyazunk az $m$-dimenziós $\boldsymbol{I}_m$ egységmátrix $i$-edik és $j$-edik sorába, illetve oszlopába – ahogy az alábbiakban bemutatjuk az $m = 5$, $i = 2$, $j = 4$ esetben:

$$\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & c & 0 & s & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & -s & 0 & c & 0 \\ 0 & 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ a_4 \\ a_5 \end{bmatrix} = \begin{bmatrix} a_1 \\ \alpha \\ a_3 \\ 0 \\ a_5 \end{bmatrix}.$$

Ilyen Givens-forgatások sorozatával az $\boldsymbol{A}$ mátrix egyes elemeit egymás után kinullázhatjuk, míg végül a mátrixot felső háromszögalakra nem hozzuk. Az egyetlen megszorítás az elemek kinullázásának sorrendjére az, hogy ne vezessünk vissza nemnulla értékeket olyan mátrixelemekbe, amelyeket korábban már kinulláztunk; ez azonban sokféle sorrenddel megvalósítható. Itt is a forgatások szorzata egy olyan ortogonális mátrix, amely megadja a keresett QR-felbontást.

Az általános lineáris legkisebb négyzetes feladatok megoldására szolgáló Givens-módszer egyszerű megvalósítása körülbelül 50 százalékkal több munkát igényel, mint a Householder-módszer. Több memóriát is igényel, mivel minden forgatást két szám – $c$ és $s$ – határoz meg (így a kinullázott $a_{ij}$ elem nem elegendő a forgatás tárolására). Ezek a munkával és a memóriával kapcsolatos hátrányok leküzdhetők annyira, hogy a Givens-módszer versenyképes legyen a Householder-módszerrel, de ennek ára a bonyolultabb megvalósítás. A Givens-módszert ezért általában azokra a helyzetekre tartjuk fenn, amelyekben a nagyobb szelektivitás kiemelt jelentőségű – például amikor a mátrix ritka, vagy amikor a meglévő nullák valamilyen adott mintázatát meg kell őriznünk.

A Householder-transzformációkhoz hasonlóan a $\boldsymbol{Q}$ mátrixot nem szükséges explicit módon felírni, mivel az egymást követő forgatásokkal való szorzás ugyanazt az eredményt adja, mint a $\boldsymbol{Q}$-val való szorzás. Ha azonban a $\boldsymbol{Q}$-ra valamilyen más okból explicit alakban volna szükségünk, úgy az kiszámítható az egyes forgatások egymás utáni szorzataként, kiindulásként az $\boldsymbol{I}$ egységmátrixszal.

**3.10. Példa. Givens QR-felbontás.** A Givens QR-felbontást a 3.1. példában szereplő legkisebb négyzetes feladat megoldásával szemléltetjük. Ennek a feladatnak a mátrixában a főátló alatt mindössze hat nemnulla elem van, amelyek Givens-forgatásokkal egyenként, szelektíven kinullázhatók (a Householder-módszer az ilyen ritkaságot nem tudja könnyen kihasználni, mivel egyszerre egy egész oszlopot nulláz ki).

Az első oszlopban alulról felfelé haladva, az $\boldsymbol{A}$ első nemnulla eleme az $(5,1)$ pozícióban van; ez kinullázható egy olyan Givens-forgatással, amely az $\boldsymbol{A}$ első oszlopának első és ötödik elemére épül. Egy megfelelő forgatást a $c = 1/\sqrt{2}$, $s = -1/\sqrt{2}$ értékek adnak, amelyet a $6 \times 6$-os egységmátrixba beágyazva

$$\boldsymbol{G}_1 = \begin{bmatrix} 0{,}7071 & 0 & 0 & 0 & -0{,}7071 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0{,}7071 & 0 & 0 & 0 & 0{,}7071 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}.$$

Ezt a forgatást az $\boldsymbol{A}$-ra és a $\boldsymbol{b}$-re alkalmazva

$$\boldsymbol{G}_1 \boldsymbol{A} = \begin{bmatrix} 1{,}4142 & 0 & -0{,}7071 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \\ 0 & 0 & 0{,}7071 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \boldsymbol{G}_1 \boldsymbol{b} = \begin{bmatrix} 42 \\ 1941 \\ 2417 \\ 711 \\ 1707 \\ 475 \end{bmatrix}.$$

Ezek után a $(4,1)$ elemet nullázzuk ki egy olyan Givens-forgatással, amely az első oszlop első és negyedik elemére épül. Egy megfelelő forgatást a $c = \sqrt{2}/\sqrt{3}$, $s = -1/\sqrt{3}$ értékek adnak, amelyet az egységmátrixba beágyazva

$$\boldsymbol{G}_2 = \begin{bmatrix} 0{,}8165 & 0 & 0 & -0{,}5774 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0{,}5774 & 0 & 0 & 0{,}8165 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}.$$

Ezt a forgatást alkalmazva

$$\boldsymbol{G}_2 \boldsymbol{G}_1 \boldsymbol{A} = \begin{bmatrix} 1{,}7321 & -0{,}5744 & -0{,}5744 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0{,}8165 & -0{,}4082 \\ 0 & 0 & 0{,}7071 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \boldsymbol{G}_2 \boldsymbol{G}_1 \boldsymbol{b} = \begin{bmatrix} -376 \\ 1941 \\ 2417 \\ 605 \\ 1707 \\ 475 \end{bmatrix}.$$

Ezzel az első oszlop készen van, így ezután a második oszlopra lépnénk tovább, és hasonló módon egyenként kinulláznánk a főátló alatti nemnulla elemeit, majd végül ugyanígy járnánk el a harmadik oszloppal is, míg a végén megkapnánk a felső háromszögű mátrixot és a transzformált jobb oldalt:

$$\boldsymbol{Q}^T \boldsymbol{A} = \begin{bmatrix} 1{,}7321 & -0{,}5774 & -0{,}5774 \\ 0 & 1{,}6330 & -0{,}8165 \\ 0 & 0 & 1{,}4142 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \qquad \boldsymbol{Q}^T \boldsymbol{b} = \begin{bmatrix} -376 \\ 1200 \\ 3417 \\ 5{,}66 \\ -1{,}63 \\ -0{,}56 \end{bmatrix},$$

ahol $\boldsymbol{Q}^T$ az összes felhasznált Givens-forgatás szorzata. A felső háromszögű rendszert mostantól visszahelyettesítéssel oldhatjuk meg, és az $\boldsymbol{x} = [1236, 1943, 2416]^T$ megoldást kapjuk.### 3.5.3 Gram–Schmidt-ortogonalizáció

A QR-felbontás kiszámításának egy másik módszere a Gram–Schmidt-ortogonalizáció. Adott két lineárisan független $m$-dimenziós vektor, $\boldsymbol{a}_1$ és $\boldsymbol{a}_2$; célunk két olyan ortonormált $m$-dimenziós $\boldsymbol{q}_1$ és $\boldsymbol{q}_2$ vektor meghatározása, amelyek ugyanazt az alteret feszítik ki, mint $\boldsymbol{a}_1$ és $\boldsymbol{a}_2$. Először $\boldsymbol{a}_1$-et normáljuk, és így megkapjuk $\boldsymbol{q}_1 = \boldsymbol{a}_1/\|\boldsymbol{a}_1\|_2$-t. Ezután $\boldsymbol{a}_2$-ből le szeretnénk vonni annak $\boldsymbol{q}_1$ irányú összetevőjét, amit úgy érhetünk el, hogy $\boldsymbol{a}_2$-t ortogonálisan levetítjük a span($\boldsymbol{q}_1$) altérre; lásd a 3.4. ábrát. Ez utóbbi ekvivalens az alábbi $m \times 1$ méretű legkisebb négyzetek feladattal:

$$\boldsymbol{q}_1 \gamma \cong \boldsymbol{a}_2,$$

amelynek megoldása a normálegyenleten keresztül

$$\gamma = \left(\boldsymbol{q}_1^T \boldsymbol{q}_1\right)^{-1} \left(\boldsymbol{q}_1^T \boldsymbol{a}_2\right) = \boldsymbol{q}_1^T \boldsymbol{a}_2.$$

A kívánt $\boldsymbol{q}_2$ vektort tehát úgy kapjuk meg, hogy normáljuk az $\boldsymbol{r} = \boldsymbol{a}_2 - (\boldsymbol{q}_1^T \boldsymbol{a}_2) \boldsymbol{q}_1$ maradékvektort ehhez az $m \times 1$ méretű legkisebb négyzetek feladathoz.

![](_page_26_Figure_11.jpeg)

3.4. ábra: A Gram–Schmidt-ortogonalizáció egyetlen lépése.

Az imént leírt folyamat tetszőleges számú $\boldsymbol{a}_1, \ldots, \boldsymbol{a}_k$, $1 \leq k \leq m$ vektorra kiterjeszthető úgy, hogy minden egyes új vektort ortogonalizálunk az összes megelőző vektorhoz képest; ezt nevezzük a *klasszikus* Gram–Schmidt-ortogonalizációs eljárásnak, amelyet a 3.2. algoritmus mutat be. Ha az $\boldsymbol{a}_k$ vektorok az $m \times n$-es $\boldsymbol{A}$ mátrix oszlopai, akkor a keletkező $\boldsymbol{q}_k$ vektorok az $m \times n$-es $\boldsymbol{Q}_1$ mátrix oszlopai lesznek, az $r_{jk}$ értékek pedig

#### 3.2. Algoritmus. Klasszikus Gram–Schmidt-ortogonalizáció

```
for k = 1 to n
    qk = ak
    for j = 1 to k − 1
        rjk = qj^T * ak
        qk = qk − rjk * qj
    end
    rkk = ||qk||2
    if rkk = 0 then stop
    qk = qk / rkk
end
                                  { oszlopokon futó ciklus }
                                  { a jelenlegi oszlopból levonjuk
                                      az őt megelőző oszlopok
                                      irányú komponenseit }
                                  { megállás, ha lineárisan összefüggő }
                                  { a jelenlegi oszlop normálása }
```

az $\boldsymbol{A}$ redukált QR-felbontásában szereplő $n \times n$-es felső háromszögű $\boldsymbol{R}$ mátrix elemei (lásd a 3.4.5. szakaszt).

Sajnos a klasszikus Gram–Schmidt-eljárás véges pontosságú aritmetikával megvalósítva nem kielégítő, mert a kiszámított $\boldsymbol{q}_k$ vektorok ortogonalitása a kerekítési hibák miatt hajlamos elveszni. Ráadásul a klasszikus Gram–Schmidt-eljárás külön memóriát igényel az $\boldsymbol{A}$ és a $\boldsymbol{Q}_1$ (valamint az $\boldsymbol{R}$) számára, mert az eredeti $\boldsymbol{a}_k$-t a belső ciklusban is használjuk, ezért a belső ciklusban frissülő $\boldsymbol{q}_k$ nem írhatja felül. Mindkét hiányosság egyszerűen orvosolható, ha a belső ciklusban $\boldsymbol{a}_k$ helyett $\boldsymbol{q}_k$-t használjuk; ez egy olyan Gram–Schmidt-változatot ad, amely továbbra is oszloponként állítja elő az $\boldsymbol{R}$-t. A számítás alaposabb átrendezése azonban további előnnyel is jár.

Mégpedig, amint kiszámítottuk az új $\boldsymbol{q}_k$ vektort, rögtön ortogonalizáljuk hozzá az összes hátralévő vektort, így az $\boldsymbol{R}$-t nem oszloponként, hanem soronként állítjuk elő. Ez az átrendezés a módosított Gram–Schmidt-ortogonalizációs eljárást adja, amelyet a 3.3. algoritmus mutat be; ez matematikailag ekvivalens a klasszikus Gram–Schmidttel, de numerikusan jobb nála. A Gram–Schmidt mindkét változatában, ha valamelyik $k$ lépésnél $r_{kk}=0$, akkor az $\boldsymbol{A}$ $k$-adik oszlopa szükségképpen lineárisan függ az első $k-1$ oszloptól, ezért $\boldsymbol{A}$ nem teljes oszlopranggal rendelkezik. Az itt közölt formában egyik algoritmus sem folytatható ebben a helyzetben. Az oszloponkénti Gram–Schmidt-eljárásokkal ellentétben azonban a soronkénti módosított Gram–Schmidt-eljárás lehetővé teszi az oszloponkénti főelemkiválasztás használatát az $\boldsymbol{A}$ oszlopai közül egy maximális lineárisan független részhalmaz kiválasztására (lásd a 3.5.4. szakaszt). Alattomosabb probléma, ha $r_{kk}$ értéke nagyon kicsi, de nem nulla: ez a közeli ranghiányt jelzi, és szintén elegánsan kezelhető oszloponkénti főelemkiválasztással, a soronkénti módosított Gram–Schmidt-eljárással együtt.

A 3.3. algoritmusban a világosság kedvéért továbbra is külön írtuk $\boldsymbol{a}_k$-t és $\boldsymbol{q}_k$-t, de valójában most már közös memóriát használhatnak (egy programozó eleve így is fogalmazta volna meg az algoritmust). Sajnos a $\boldsymbol{Q}_1$ és az $\boldsymbol{R}$ továbbra is külön memóriát igényel, ami hátrány a Householder-módszerhez képest, ahol az $\boldsymbol{R}$ és a $\boldsymbol{Q}$ implicit reprezentációja osztozhat az $\boldsymbol{A}$ által korábban elfoglalt területen. Másrészt a Gram–Schmidt explicit reprezentációt ad a $\boldsymbol{Q}_1$-re,

#### 3.3. Algoritmus. Módosított Gram–Schmidt-ortogonalizáció

```
for k = 1 to n
    rkk = ||ak||2
    if rkk = 0 then stop
    qk = ak / rkk
    for j = k+1 to n
        rkj = qk^T * aj
        aj = aj − rkj * qk
    end
end
                                  { oszlopokon futó ciklus }
                                  { megállás, ha lineárisan összefüggő }
                                  { a jelenlegi oszlop normálása }
                                  { a rákövetkező oszlopokból
                                      levonjuk a jelenlegi oszlop
                                      irányú komponenseiket }
```

amit a Householder-módszer esetén – ha szükséges – többlet-memória árán kapnánk meg.

Még a módosított Gram–Schmidt-eljárás esetén is előfordulhat számjegykioltás, amikor egyik vektorból egy másik irányú komponenst vonunk le, és ez a $\boldsymbol{Q}_1$ oszlopainak ortogonalitásában jelentős veszteséghez vezethet, ha $\boldsymbol{A}$ rosszul kondicionált, bár a veszteség jóval enyhébb, mint a klasszikus Gram–Schmidtnél. Ezért, ha a módosított Gram–Schmidtet az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetek feladat megoldására használjuk, nem tanácsos a kiszámított $\boldsymbol{Q}_1$-et explicit módon felhasználni a transzformált jobb oldal $\boldsymbol{c}_1 = \boldsymbol{Q}_1^T \boldsymbol{b}$ kiszámításához. Numerikusan jobb, ha a $\boldsymbol{b}$ jobb oldali vektort $(n+1)$-edik oszlopként kezeljük, és a módosított Gram–Schmidtet használjuk az így kapott $m \times (n+1)$-es kibővített mátrix redukált QR-felbontásának kiszámítására:

$$\left[ \begin{array}{cc} \boldsymbol{A} & \boldsymbol{b} \end{array} \right] = \left[ \begin{array}{cc} \boldsymbol{Q}_1 & \boldsymbol{q}_{n+1} \end{array} \right] \left[ \begin{array}{cc} \boldsymbol{R} & \boldsymbol{c}_1 \\ \boldsymbol{0}^T & \rho \end{array} \right],$$

ezután a legkisebb négyzetek feladat $\boldsymbol{x}$ megoldását az $\boldsymbol{R}\boldsymbol{x} = \boldsymbol{c}_1$ $n \times n$-es háromszögű lineáris egyenletrendszer megoldása adja.

A Gram–Schmidt-eljárás bármelyik változatával a kapott $\boldsymbol{Q}_1$ mátrix ortogonalitása jelentősen javítható reortogonalizációval: egyszerűen ismételjük meg az eljárást $\boldsymbol{Q}_1$-en. Ilyen reortogonalizáció ismételten is végezhető, iteratív finomítás gyanánt, de tipikusan már egyetlen reortogonalizáció is kielégítő eredményt ad.

**3.11. Példa. Gram–Schmidt QR-felbontás.** A módosított Gram–Schmidt-ortogonalizációt a 3.1. példa legkisebb négyzetek feladatának megoldásával szemléltetjük. Az $\boldsymbol{A}$ első oszlopát normálva kapjuk:

$$r_{1,1} = \|\boldsymbol{a}_1\|_2 = 1{,}7321, \qquad \boldsymbol{q}_1 = \boldsymbol{a}_1/r_{1,1} = \begin{bmatrix} 0{,}5774\\0\\0\\-0{,}5774\\-0{,}5774\\0 \end{bmatrix}.$$

Az első oszlopot ortogonalizálva a rákövetkező oszlopokhoz képest, a következőt kapjuk:

$$r_{1,2} = \boldsymbol{q}_1^T \boldsymbol{a}_2 = -0{,}5774, \qquad r_{1,3} = \boldsymbol{q}_1^T \boldsymbol{a}_3 = -0{,}5774.$$

Levonva $\boldsymbol{q}_1$ ezen többszöröseit a második, illetve a harmadik oszlopból, és $\boldsymbol{q}_1$-et az első oszlop helyére írva, a transzformált mátrix:

$$\begin{bmatrix} 0{,}5774 & 0{,}3333 & 0{,}3333 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ -0{,}5774 & 0{,}6667 & -0{,}3333 \\ -0{,}5774 & -0{,}3333 & 0{,}6667 \\ 0 & -1 & 1 \end{bmatrix}.$$

A második oszlopot normálva kapjuk:

$$r_{2,2} = \|\boldsymbol{a}_2\|_2 = 1{,}6330, \qquad \boldsymbol{q}_2 = \boldsymbol{a}_2/r_{2,2} = \begin{bmatrix} 0{,}2041 \\ 0{,}6124 \\ 0 \\ 0{,}4082 \\ -0{,}2041 \\ -0{,}6124 \end{bmatrix}.$$

A második oszlopot a harmadik oszlophoz képest ortogonalizálva:

$$r_{2,3} = \boldsymbol{q}_2^T \boldsymbol{a}_3 = -0{,}8165.$$

$\boldsymbol{q}_2$ e többszörösét levonva a harmadik oszlopból, és $\boldsymbol{q}_2$-t a második oszlop helyére írva, a transzformált mátrix:

$$\begin{bmatrix} 0{,}5774 & 0{,}2041 & 0{,}5 \\ 0 & 0{,}6124 & 0{,}5 \\ 0 & 0 & 1 \\ -0{,}5774 & 0{,}4082 & 0 \\ -0{,}5774 & -0{,}2041 & 0{,}5 \\ 0 & -0{,}6124 & 0{,}5 \end{bmatrix}.$$

Végül normáljuk a harmadik oszlopot:

$$r_{3,3} = \|\boldsymbol{a}_3\|_2 = 1{,}4142, \qquad \boldsymbol{q}_3 = \boldsymbol{a}_3/r_{3,3} = \begin{bmatrix} 0{,}3536\\0{,}3536\\0{,}7071\\0\\0{,}3536\\0{,}3536 \end{bmatrix}.$$

A harmadik oszlopot $\boldsymbol{q}_3$-mal helyettesítve megkapjuk a redukált QR-felbontást:

$$\boldsymbol{A} = \begin{bmatrix} 0{,}5774 & 0{,}2041 & 0{,}3536 \\ 0 & 0{,}6124 & 0{,}3536 \\ 0 & 0 & 0{,}7071 \\ -0{,}5774 & 0{,}4082 & 0 \\ -0{,}5774 & -0{,}2041 & 0{,}3536 \\ 0 & -0{,}6124 & 0{,}3536 \end{bmatrix} \begin{bmatrix} 1{,}7321 & -0{,}5774 & -0{,}5774 \\ 0 & 1{,}6330 & -0{,}8165 \\ 0 & 0 & 1{,}4142 \end{bmatrix} = \boldsymbol{Q}_1 \boldsymbol{R}.$$

Mivel a feladat jól kondicionált, a transzformált jobb oldalt biztonsággal kiszámíthatjuk explicit módon:

$$\boldsymbol{Q}_1^T \boldsymbol{b} = \begin{bmatrix} -376 \\ 1200 \\ 3417 \end{bmatrix} = \boldsymbol{c}_1.$$

Az $\boldsymbol{R}\boldsymbol{x} = \boldsymbol{c}_1$ felső háromszögű rendszert visszahelyettesítéssel megoldva $\boldsymbol{x} = [1236, 1943, 2416]^T$ adódik.

### 3.5.4 Ranghiány

Eddig feltettük, hogy $\boldsymbol{A}$ teljes oszloprangú, azaz $\operatorname{rank}(\boldsymbol{A}) = n$. Ha ez nem teljesül, azaz ha $\boldsymbol{A}$-nak lineárisan összefüggő oszlopai vannak, akkor a QR-felbontás még mindig létezik, de a felső háromszögű $\boldsymbol{R}$ faktor szinguláris (akárcsak az $\boldsymbol{A}^T \boldsymbol{A}$ mátrix). Így sok $\boldsymbol{x}$ vektor adja ugyanazt a minimális maradéknormát, és a legkisebb négyzetek megoldás nem egyértelmű. Ez a helyzet rendszerint rosszul megtervezett kísérlet, hiányos adatok, vagy nem megfelelő, illetve redundáns modell következménye. Ezért a feladatot valószínűleg át kell fogalmazni vagy újra kell gondolni.

Ha mégis ragaszkodunk a továbblépéshez, bevett eljárás a minimális maradékot adó megoldások közül a legkisebb euklideszi normájú $\boldsymbol{x}$ kiválasztása. Ez kiszámítható oszloponkénti főelemkiválasztással végzett QR-felbontással, amit alább tárgyalunk, vagy szingulárisérték-felbontással (SVD), amit a 3.6. szakaszban fogunk tárgyalni. Megjegyezzük, hogy a ranghiány ilyen kezelése lehetővé teszi az alulhatározott – $m < n$ – feladatok kezelését is, mert ebben az esetben $\boldsymbol{A}$ oszlopai szükségképpen lineárisan összefüggők.

**3.12. Példa. Ranghiány.** Tegyük fel, hogy a 3.1. példában szereplő földmérő csak az egyes dombpárok egymáshoz viszonyított relatív magasságát mérte meg, de egyik domb magasságát sem mérte meg közvetlenül a referenciaponthoz képest, így a $3 \times 3$-as lineáris egyenletrendszerünk:

$$\boldsymbol{A}\boldsymbol{x} = \begin{bmatrix} -1 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} 711 \\ 1177 \\ 475 \end{bmatrix} = \boldsymbol{b}.$$

Elég információ áll-e még rendelkezésre a három domb magasságának meghatározásához? E kérdés megválaszolásához kiszámítjuk a QR-felbontást:

$$\boldsymbol{A} = \begin{bmatrix} -0{,}7071 & 0{,}4082 & 0{,}5774 \\ -0{,}7071 & -0{,}4082 & -0{,}5774 \\ 0 & -0{,}8165 & 0{,}5774 \end{bmatrix} \begin{bmatrix} 1{,}4142 & -0{,}7071 & -0{,}7071 \\ 0 & 1{,}2247 & -1{,}2247 \\ 0 & 0 & 0 \end{bmatrix} = \boldsymbol{Q}\boldsymbol{R},$$

ami mutatja, hogy $\boldsymbol{R}$ szinguláris, és ezért $\boldsymbol{A}$ ranghiányos. Ebben az egyszerű példában ezt közvetlenül is láthattuk volna abból, hogy $\boldsymbol{A}$ minden sorösszege nulla (azaz $\boldsymbol{A}\boldsymbol{e} = \boldsymbol{0}$), a gyakorlatban azonban a ranghiány ritkán ennyire nyilvánvaló.

A gyakorlatban egy mátrix rangja gyakran nem egyértelmű. Így a legkisebb négyzetek feladatok közeli ranghiányának kimutatására relatív tolerancia szolgál, pontosan úgy, mint a négyzetes lineáris egyenletrendszerek közeli szingularitásának kimutatására. Ha egy legkisebb négyzetek feladat majdnem ranghiányos, akkor a megoldás érzékeny lesz a bemeneti adatok perturbációira. Ezeket a kérdéseket pontosabban meg tudjuk majd vizsgálni, amikor a 3.6. szakaszban bevezetjük egy mátrix szingulárisérték-felbontását. A QR-felbontás keretein belül a ranghiány kimutatására és kezelésére egy megbízható módszer az oszloponkénti főelemkiválasztás, amit alább tárgyalunk.

**3.13. Példa. Közeli ranghiány.** Tekintsük a következő $3 \times 2$-es mátrixot:

$$\boldsymbol{A} = \begin{bmatrix} 0{,}913 & 0{,}659 \\ 0{,}780 & 0{,}563 \\ 0{,}457 & 0{,}330 \end{bmatrix}.$$

Ha kiszámítjuk az $\boldsymbol{A}$ QR-felbontását, azt találjuk, hogy

$$\boldsymbol{R} = \begin{bmatrix} -1{,}28484 & -0{,}92744 \\ 0 & 0{,}00013 \end{bmatrix}.$$

Tehát $\boldsymbol{R}$ rendkívül közel áll ahhoz, hogy szinguláris legyen, és ha $\boldsymbol{R}$-et használjuk egy legkisebb négyzetek feladat megoldására, az eredmény ennek megfelelően érzékeny lesz a feladat adatainak perturbációira. Gyakorlati célokra az $\boldsymbol{A}$ rangja csak egy, nem pedig kettő, hiszen az oszlopai közel lineárisan összefüggők.

Az $\boldsymbol{A}$ mátrix oszlopait tekinthetjük vektorok rendezetlen halmazának, amelyből egy maximális lineárisan független részhalmazt szeretnénk kiválasztani. A QR-felbontás kiszámításakor ahelyett, hogy az oszlopokat a természetes sorrendjükben dolgoznánk fel, minden lépésben a hátralévő, még redukálatlan részmátrix maximális euklideszi normájú oszlopát választjuk ki redukálásra. Ezt az oszlopot (explicit módon vagy implicit módon) felcseréljük a természetes sorrendben következő oszloppal, majd az átló alatti részét a szokásos módon lenullázzuk. Az ehhez szükséges transzformációt ezután alkalmazni kell a hátralévő redukálatlan oszlopokra, majd az eljárást megismételjük. Az imént leírt folyamat neve az *oszloponkénti főelemkiválasztással végzett QR-felbontás*. Megjegyezzük, hogy az oszloponkénti főelemkiválasztás működésének feltétele, hogy a QR-felbontási folyamat minden lépésében a hátralévő oszlopoknak ne legyen komponensük a már feldolgozott oszlopok irányában. Ez igaz a Householder-, a Givens- és a soronkénti módosított Gram–Schmidt-algoritmusra, de nem igaz az oszloponkénti Gram–Schmidt-algoritmusokra (sem a klasszikusra, sem a módosítottra), ezért ez utóbbiak nem használhatók oszloponkénti főelemkiválasztással.

Ha $\operatorname{rank}(\boldsymbol{A}) = k < n$, akkor az oszloponkénti főelemkiválasztással végzett QR-felbontás $k$ lépése után a hátralévő redukálatlan oszlopok normái a $k$-adik sor alatt nullák (vagy véges pontosságú aritmetikában „elhanyagolhatóak”) lesznek. Így a következő alakú ortogonális felbontást állítottuk elő:

$$\boldsymbol{Q}^T \boldsymbol{A} \boldsymbol{P} = \begin{bmatrix} \boldsymbol{R} & \boldsymbol{S} \\ \boldsymbol{O} & \boldsymbol{O} \end{bmatrix},$$

ahol $\boldsymbol{R}$ $k \times k$-as felső háromszögű és nemszinguláris, $\boldsymbol{P}$ pedig az oszlopcseréket végrehajtó permutációs mátrix. Ezen a ponton az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat egy bázismegoldása (azaz egy legfeljebb $k$ darab nem nulla komponenssel rendelkező megoldás) kiszámítható úgy, hogy megoldjuk az $\boldsymbol{R}\boldsymbol{z} = \boldsymbol{c}_1$ háromszögű rendszert, ahol $\boldsymbol{c}_1$ a $\boldsymbol{Q}^T \boldsymbol{b}$ vektor első $k$ komponenséből álló vektor, majd vesszük

$$\boldsymbol{x} = \boldsymbol{P} \begin{bmatrix} \boldsymbol{z} \\ \boldsymbol{0} \end{bmatrix}.$$

Az adatillesztés szempontjából ez az eljárás azt jelenti, hogy figyelmen kívül hagyjuk a modell azon komponenseit, amelyek redundánsak vagy rosszul meghatározottak. Ha azonban a *minimális normájú megoldásra* van szükségünk, ez is kiszámítható, további ortogonális transzformációk költségén, amelyeket jobbról alkalmazunk, hogy $\boldsymbol{S}$-et is nullázzuk.

**3.14. Példa. Bázis- és minimális normájú megoldás.** A 3.12. példát folytatva egy bázismegoldás az egyik dombhoz nulla magasságot rendel (hogy melyik dombot választjuk, az a QR-felbontásban szereplő $\boldsymbol{P}$ oszlop-permutációtól függ), ami ezután lehetővé teszi a másik két domb magasságának meghatározását ehhez képest egy kisebb rendszer megoldásával. Ebben a példában a harmadik dombnak nulla magasságot rendelve a $\boldsymbol{x}^T = [-1180, -472, 0]$ bázismegoldást kapjuk (a negatív magasságok egyszerűen azt jelentik, hogy az első két domb a nulla magasságúnak választott domb alatt van). Megjegyezzük, hogy ez a megoldás nem elégíti ki egzaktul a lineáris rendszert (tükrözve azt, hogy a rendszer inkonzisztens, ami négyzetes rendszernél csak ranghiány esetén lehetséges), de ez egy (nem egyértelmű) legkisebb négyzetek megoldás. Ennek a ranghiányos feladatnak a minimális normájú megoldása $\boldsymbol{x}^T = [-629, 79, 551]$ (lásd a 3.16. példát).

A gyakorlatban $\boldsymbol{A}$ rangja általában ismeretlen, ezért az oszloponkénti főelemkiválasztási folyamatot a rang felderítésére használjuk: a hátralévő redukálatlan oszlopok normáit figyeljük, és a felbontást akkor állítjuk le, amikor a maximális érték egy relatív tolerancia alá esik. QR-felbontáson alapuló, kifinomultabb rangfelderítő technikák is léteznek, valamint a szingulárisérték-felbontás, amely a rang numerikus meghatározásának legmegbízhatóbb (de legköltségesebb) módja (lásd a 3.6.1. szakaszt).

## 3.6 Szingulárisérték-felbontás

Akárcsak a négyzetes lineáris egyenletrendszereknél, egy diagonális lineáris legkisebb négyzetek feladat még könnyebben megoldható, mint egy háromszögű. Idézzük fel a háromszögű LU-felbontás és a négyzetes mátrix Gauss–Jordan-eliminációval kapott diagonális felbontása közötti összefüggést (lásd a 2.4.8. szakaszt). Bizonyos mértékig hasonló módon a háromszögű QR-felbontáson túl is el lehet jutni: téglalap alakú mátrix diagonális felbontását is meg lehet kapni ortogonális transzformációkkal.

Egy $m \times n$-es $\boldsymbol{A}$ mátrix szingulárisérték-felbontása (SVD) a következő alakú:

$$\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T,$$

ahol az $\boldsymbol{U}$ egy $m \times m$-es ortogonális mátrix, a $\boldsymbol{V}$ egy $n \times n$-es ortogonális mátrix, a $\boldsymbol{\Sigma}$ pedig egy $m \times n$-es diagonális mátrix, amelyre

$$\sigma_{ij} = \begin{cases} 0 & \text{ha } i \neq j, \\ \sigma_i \ge 0 & \text{ha } i = j. \end{cases}$$

A $\sigma_i$ diagonális elemeket az $\boldsymbol{A}$ mátrix szinguláris értékeinek nevezzük, és rendszerint úgy rendezzük őket, hogy $\sigma_{i-1} \ge \sigma_i$, $i = 2, \ldots, \min\{m, n\}$. Az $\boldsymbol{U}$ $\boldsymbol{u}_i$ oszlopai, illetve a $\boldsymbol{V}$ $\boldsymbol{v}_i$ oszlopai az ezeknek megfelelő bal és jobb oldali szinguláris vektorok. Mivel az SVD kiszámítása szorosan kapcsolódik a sajátértékek kiszámításának algoritmusaihoz, az SVD kiszámításának tárgyalását a 4.7. szakaszra halasztjuk; az SVD alkalmazásait viszont itt tárgyaljuk, mivel a legkisebb négyzetek és kapcsolódó feladatok megoldásában fontos szerepet játszik.

**3.15. Példa. Szingulárisérték-felbontás.** Az

$$\boldsymbol{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \\ 10 & 11 & 12 \end{bmatrix}$$

mátrix szingulárisérték-felbontása $\boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T =$

$$\begin{bmatrix} 0{,}141 & 0{,}825 & -0{,}420 & -0{,}351 \\ 0{,}344 & 0{,}426 & 0{,}298 & 0{,}782 \\ 0{,}547 & 0{,}028 & 0{,}664 & -0{,}509 \\ 0{,}750 & -0{,}371 & -0{,}542 & 0{,}079 \end{bmatrix} \begin{bmatrix} 25{,}5 & 0 & 0 \\ 0 & 1{,}29 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0{,}504 & 0{,}574 & 0{,}644 \\ -0{,}761 & -0{,}057 & 0{,}646 \\ 0{,}408 & -0{,}816 & 0{,}408 \end{bmatrix}.$$

Tehát $\sigma_1 = 25{,}5$, $\sigma_2 = 1{,}29$ és $\sigma_3 = 0$. Egy nullával egyenlő szinguláris érték azt jelzi, hogy a mátrix ranghiányos; általánosabban egy mátrix rangja egyenlő a nem nulla szinguláris értékek számával, ami ebben a példában kettő.

Az SVD különösen rugalmas módszert nyújt tetszőleges alakú és rangú lineáris legkisebb négyzetek feladatok megoldására. Tekintsük először a túlhatározott, teljes rangú esetet. Ha $\boldsymbol{A}$ egy $m \times n$-es mátrix $\operatorname{rank}(\boldsymbol{A}) = n$ esetén, akkor

$$\boldsymbol{A} = \boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^T = \begin{bmatrix} \boldsymbol{U}_1 & \boldsymbol{U}_2 \end{bmatrix} \begin{bmatrix} \boldsymbol{\Sigma}_1 \\ \boldsymbol{O} \end{bmatrix} \boldsymbol{V}^T = \boldsymbol{U}_1 \boldsymbol{\Sigma}_1 \boldsymbol{V}^T,$$

ahol az $\boldsymbol{U}_1$ egy $m \times n$-es, a $\boldsymbol{\Sigma}_1$ pedig egy $n \times n$-es, nemszinguláris mátrix; ez az $\boldsymbol{A}$ redukált, „takarékos méretű” SVD-je. Az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat megoldását ekkor a

$$\boldsymbol{x} = \boldsymbol{V} \boldsymbol{\Sigma}_1^{-1} \boldsymbol{U}_1^T \boldsymbol{b}$$

összefüggés adja, amint az $\boldsymbol{A}$ redukált SVD-jét a normálegyenletbe behelyettesítve könnyen ellenőrizhető. Általánosabban, tetszőleges alakú és rangú $\boldsymbol{A}$ esetén az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat minimális euklideszi normájú megoldását a

$$\boldsymbol{x} = \sum_{\sigma_i \neq 0} \frac{\boldsymbol{u}_i^T \boldsymbol{b}}{\sigma_i} \, \boldsymbol{v}_i$$

összefüggés adja. Az SVD különösen hasznos rosszul kondicionált vagy közel ranghiányos feladatoknál, mert az összegzésből tetszőleges, relatív értelemben kicsi szinguláris értékek elhagyhatók, és így a megoldás jóval kevésbé érzékeny az adatok perturbációira.

**3.16. Példa. Minimális normájú megoldás.** A 3.12. példában szereplő $\boldsymbol{A}$ mátrix SVD-je $\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T =$

$$\begin{bmatrix} -0{,}707 & 0{,}408 & 0{,}577 \\ -0{,}707 & -0{,}408 & -0{,}577 \\ 0 & -0{,}816 & 0{,}577 \end{bmatrix} \begin{bmatrix} 1{,}732 & 0 & 0 \\ 0 & 1{,}732 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0{,}816 & -0{,}408 & -0{,}408 \\ 0 & 0{,}707 & -0{,}707 \\ -0{,}577 & -0{,}577 & -0{,}577 \end{bmatrix},$$

így a minimális euklideszi normájú legkisebb négyzetek megoldás:

$$\boldsymbol{x} = \frac{\boldsymbol{u}_1^T \boldsymbol{b}}{\sigma_1} \, \boldsymbol{v}_1 + \frac{\boldsymbol{u}_2^T \boldsymbol{b}}{\sigma_2} \, \boldsymbol{v}_2 = \frac{-1335}{1{,}732} \begin{bmatrix} 0{,}816 \\ -0{,}408 \\ -0{,}408 \end{bmatrix} + \frac{-578}{1{,}732} \begin{bmatrix} 0 \\ 0{,}707 \\ -0{,}707 \end{bmatrix} = \begin{bmatrix} -629 \\ 79 \\ 551 \end{bmatrix}.$$

### 3.6.1 Az SVD további alkalmazásai

Az $\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T$ szingulárisérték-felbontásnak számos más fontos alkalmazása is van, köztük az alábbiak:

*Euklideszi mátrixnorma.* Az euklideszi vektornorma által indukált mátrixnormát a mátrix legnagyobb szinguláris értéke adja:

$$\|\boldsymbol{A}\|_2 = \max_{\boldsymbol{x} \neq \boldsymbol{0}} \frac{\|\boldsymbol{A}\boldsymbol{x}\|_2}{\|\boldsymbol{x}\|_2} = \sigma_{\max}.$$

Még nem áll módunkban belátni, miért igaz ez, mert sajátértékek (4. fejezet) és optimalizálás (6. fejezet) ismeretét igényli.

*Euklideszi kondíciószám.* Egy tetszőleges $\boldsymbol{A}$ mátrix euklideszi normában vett kondíciószámát a

$$\operatorname{cond}_2(\boldsymbol{A}) = \sigma_{\max}/\sigma_{\min}$$

hányados adja. Ez a definíció egybeesik a $\operatorname{cond}(\boldsymbol{A})$ 2.3.3. szakaszban adott, négyzetes mátrixra vonatkozó – euklideszi normát használó – definíciójával, valamint a 3.3. szakaszban megadott, teljes oszloprangú túlhatározott mátrix kondíciószámával is. Ez mindkettőt általánosítja tetszőleges alakú és rangú téglalap alakú mátrixra. Figyeljük meg, hogy ezzel a definícióval, akárcsak korábban, $\operatorname{cond}_2(\boldsymbol{A}) = \infty$ ha $\operatorname{rank}(\boldsymbol{A}) < \min(m,n)$, mert ebben az esetben $\sigma_{\min} = 0$. Ahogyan egy négyzetes mátrix kondíciószáma a szingularitáshoz való közelséget méri, úgy egy téglalap alakú mátrix kondíciószáma a ranghiányhoz való közelséget méri.

**3.17. Példa. Euklideszi mátrixnorma és kondíciószám.** A 2.4. és 2.5. példában szereplő $\boldsymbol{A}$ mátrix SVD-je $\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T =$

$$\begin{bmatrix} 0{,}392 & -0{,}920 & -0{,}021 \\ 0{,}240 & 0{,}081 & 0{,}967 \\ 0{,}888 & 0{,}384 & -0{,}253 \end{bmatrix} \begin{bmatrix} 5{,}723 & 0 & 0 \\ 0 & 1{,}068 & 0 \\ 0 & 0 & 0{,}327 \end{bmatrix} \begin{bmatrix} 0{,}645 & -0{,}224 & 0{,}731 \\ -0{,}567 & 0{,}501 & 0{,}653 \\ 0{,}513 & 0{,}836 & -0{,}196 \end{bmatrix},$$

így

$$\|\boldsymbol{A}\|_2 = 5{,}723, \quad \operatorname{cond}_2(\boldsymbol{A}) = 5{,}723/0{,}327 = 17{,}5.$$

*Rang meghatározása.* Egy mátrix rangja egyenlő a nem nulla szinguláris értékeinek számával (lásd a 3.15. és 3.16. példát). A gyakorlatban azonban a rang nem feltétlenül egyértelmű, mert egyes szinguláris értékek nagyon kicsik lehetnek, de nem nullák. Sok célra célszerűbb elhanyagolhatónak tekinteni azokat a szinguláris értékeket, amelyek (a legnagyobb szinguláris értékhez viszonyítva) egy bizonyos küszöb alá esnek, és így határozni meg a mátrix „numerikus rangját”. Ennek egyik értelmezése, hogy az adott mátrix nagyon közel van (azaz az adott küszöbön belül) ahhoz a mátrixhoz, amelynek rangját így határoztuk meg. Az SVD használata a numerikus rang meghatározására megbízhatóbb (bár drágább), mint az oszloponkénti főelemkiválasztással végzett QR-felbontás használata (lásd a 3.5.4. szakaszt).

**3.18. Példa. Rang meghatározása.** A 3.13. példában szereplő $\boldsymbol{A}$ mátrix SVD-je $\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T =$

$$\begin{bmatrix} 0{,}71058 & -0{,}26631 & -0{,}65127 \\ 0{,}60707 & -0{,}23592 & 0{,}75882 \\ 0{,}35573 & 0{,}93457 & 0{,}00597 \end{bmatrix} \begin{bmatrix} 1{,}58460 & 0 \\ 0 & 0{,}00011 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 0{,}81083 & 0{,}58528 \\ -0{,}58528 & 0{,}81083 \end{bmatrix}.$$

Tehát körülbelül $10^{-4}$ vagy nagyobb küszöb mellett a rangot egynek nyilvánítanánk, nem pedig kettőnek.

*Pszeudoinverz.* Egy $\sigma$ skalár pszeudoinverzét $1/\sigma$-ként definiáljuk, ha $\sigma \neq 0$, egyébként nullaként. Egy (esetleg téglalap alakú) diagonális mátrix pszeudoinverzét a mátrix transzponálásával, majd minden elem skaláris pszeudoinverzének vételével definiáljuk. Ekkor egy általános $m \times n$-es $\boldsymbol{A}$ mátrix pszeudoinverzét a

$$\boldsymbol{A}^+ = \boldsymbol{V} \boldsymbol{\Sigma}^+ \boldsymbol{U}^T$$

összefüggés adja. Figyeljük meg, hogy a pszeudoinverz mindig létezik, függetlenül attól, hogy a mátrix négyzetes-e, vagy teljes rangú-e. Ha $\boldsymbol{A}$ négyzetes és nemszinguláris, akkor a pszeudoinverz megegyezik a szokásos $\boldsymbol{A}^{-1}$ mátrixinverzzel. Ha $\boldsymbol{A}$ teljes oszloprangú, akkor ez a definíció egybeesik a 3.3. szakaszban adottal (lásd a 3.33. feladatot). Minden esetben az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat minimális euklideszi normájú megoldását $\boldsymbol{A}^+\boldsymbol{b}$ adja.

**3.19. Példa. Pszeudoinverz.** A 3.16. példában látott SVD-ből azt látjuk, hogy a 3.12. példában szereplő $\boldsymbol{A}$ mátrix pszeudoinverze:

$$\boldsymbol{A}^{+} = \frac{1}{3} \begin{bmatrix} -1 & -1 & 0\\ 1 & 0 & -1\\ 0 & 1 & 1 \end{bmatrix},$$

így az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ legkisebb négyzetek feladat minimális euklideszi normájú megoldása:

$$\boldsymbol{x} = \boldsymbol{A}^{+}\boldsymbol{b} = \frac{1}{3} \begin{bmatrix} -1 & -1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 711 \\ 1177 \\ 475 \end{bmatrix} = \begin{bmatrix} -629 \\ 79 \\ 551 \end{bmatrix}.$$

*Ortonormált bázisok.* Ha $\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T$, akkor az $\boldsymbol{U}$ nem nulla szinguláris értékekhez tartozó oszlopai ortonormált bázist alkotnak a span($\boldsymbol{A}$) altérben, az $\boldsymbol{U}$ többi oszlopa pedig annak ortogonális kiegészítőjében, azaz a span($\boldsymbol{A}$)$^{\perp}$ altérben. Hasonlóképpen, a $\boldsymbol{V}$ nulla szinguláris értékekhez tartozó oszlopai ortonormált bázist alkotnak az $\boldsymbol{A}$ nullterében, azaz az $\{\boldsymbol{x} \in \mathbb{R}^n : \boldsymbol{A}\boldsymbol{x} = \boldsymbol{0}\}$ altérben, a $\boldsymbol{V}$ többi oszlopa pedig a nulltér ortogonális kiegészítőjében.

*Alacsonyabb rangú közelítés.* Az SVD egy másik írásmódja:

$$\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T = \sigma_1\boldsymbol{E}_1 + \sigma_2\boldsymbol{E}_2 + \dots + \sigma_n\boldsymbol{E}_n,$$

ahol $\boldsymbol{E}_i = \boldsymbol{u}_i\boldsymbol{v}_i^T$. Minden $\boldsymbol{E}_i$ egyrangú, és tárolása csupán $m+n$ memóriahelyet igényel. Ráadásul a $\boldsymbol{E}_i\boldsymbol{x}$ szorzat csupán $m+n$ szorzással képezhető. Így az $\boldsymbol{A}$ egy hasznos, tömörített közelítését kaphatjuk meg, ha a fenti összegzésből elhagyjuk a kisebb szinguláris értékekhez tartozó tagokat, hiszen azok az összeghez viszonylag keveset tesznek hozzá. Megmutatható, hogy a $k$ legnagyobb szinguláris értékkel kapott közelítés a Frobenius-normában az $\boldsymbol{A}$-hoz legközelebbi $k$ rangú mátrix. (Egy $m \times n$-es mátrix Frobenius-normája a mátrix $\mathbb{R}^{mn}$-beli vektornak tekintett euklideszi normája.) Ez a közelítés hasznos a képfeldolgozásban, az adattömörítésben, az információ-visszakeresésben, a kriptográfiában és számos más alkalmazásban.

**3.20. Példa. Alacsonyabb rangú közelítés.** A 3.13. példában megadott $\boldsymbol{A}$ mátrix 3.18. példában látott SVD-jéből azt látjuk, hogy az

$$\sigma_1 \boldsymbol{E}_1 = \sigma_1 \boldsymbol{u}_1 \boldsymbol{v}_1^T = 1{,}58460 \begin{bmatrix} 0{,}71058 \\ 0{,}60707 \\ 0{,}35573 \end{bmatrix} \begin{bmatrix} 0{,}81083 & 0{,}58528 \end{bmatrix} = \begin{bmatrix} 0{,}91298 & 0{,}65902 \\ 0{,}77999 & 0{,}56302 \\ 0{,}45706 & 0{,}32992 \end{bmatrix}$$

egyrangú mátrix rendkívül közeli közelítése az eredeti $\boldsymbol{A}$ mátrixnak, mert $\sigma_2$ olyan kicsi, hogy a hozzá tartozó tag szinte semmit sem tesz hozzá az összeghez.

*Teljes legkisebb négyzetek.* Egy közönséges $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetek feladatban implicit módon feltesszük, hogy az $\boldsymbol{A}$ elemei pontosan ismertek, míg a $\boldsymbol{b}$ elemei véletlen hibával terheltek, és ez indokolja az adatpontok és a görbe közötti függőleges távolságok minimalizálását. Amikor azonban az összes változó mérési hibával vagy egyéb bizonytalansággal terhelt, értelmesebb lehet az adatpontok és a görbe közötti ortogonális távolságok minimalizálása; ez a *teljes legkisebb négyzetek* feladatmegoldást adja. Idézzük fel, hogy a közönséges legkisebb négyzetek esetén az $\|\boldsymbol{b} - \boldsymbol{y}\|_2$-t szeretnénk minimalizálni az $\boldsymbol{y} \in \operatorname{span}(\boldsymbol{A})$ feltétel mellett, azaz a legközelebbi kompatibilis rendszert keressük, és csak a jobb oldalt engedjük változni. A teljes legkisebb négyzetek esetén is a legközelebbi kompatibilis rendszert keressük, de most a mátrix és a jobb oldal is változhat. Ahogy az előző bekezdésben láttuk, az ilyen mátrixközelítési feladat a szingulárisérték-felbontással megoldható. Nevezetesen, tekintsük az $m \times (n+1)$-es $[\boldsymbol{A} \ \boldsymbol{b}] = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T$ SVD-jét. Ahhoz, hogy a közelítő $[\hat{\boldsymbol{A}} \ \boldsymbol{y}]$ rendszer kompatibilis legyen, azaz $\boldsymbol{y} \in \operatorname{span}(\hat{\boldsymbol{A}})$ teljesüljön, a rangjának legfeljebb $n$-nek kell lennie. Ahogy láttuk, a legközelebbi $n$ rangú közelítő mátrixot úgy kapjuk meg, hogy az első $n$ szinguláris értéket tartjuk meg, és $\sigma_{n+1}$-et elhagyjuk. A keletkező kompatibilis rendszer $\boldsymbol{x}$ megoldásának ki kell elégítenie a

$$[\hat{\boldsymbol{A}} \ \boldsymbol{y}] \begin{bmatrix} \boldsymbol{x} \\ -1 \end{bmatrix} = \boldsymbol{0}$$

egyenletet, amiből látszik, hogy $[\boldsymbol{x}^T \ -1]^T$-nek a $[\hat{\boldsymbol{A}} \ \boldsymbol{y}]$ nullterében kell lennie, ami viszont azt jelenti, hogy $[\boldsymbol{x}^T \ -1]^T$ arányos $\boldsymbol{v}_{n+1}$-gyel, azaz a $\sigma_{n+1}$-nek megfelelő jobb oldali szinguláris vektorral. Így a megoldás megszerzéséhez csupán annyit kell tennünk, hogy $\boldsymbol{v}_{n+1}$-et úgy skálázzuk, hogy az utolsó komponense $-1$ legyen. Arra a következtetésre jutunk tehát, hogy amennyiben $\sigma_{n+1} < \sigma_n$ és $v_{n+1,n+1} \neq 0$, a teljes legkisebb négyzetek megoldását az

$$\boldsymbol{x} = -\frac{1}{v_{n+1,n+1}} \begin{bmatrix} v_{1,n+1} \\ \vdots \\ v_{n,n+1} \end{bmatrix}$$

összefüggés adja. Általánosabb feladatok – például több jobb oldallal, vagy ha a változók egy része pontosan ismert – hasonló módon kezelhetők, de lényegesen bonyolultabbak (a részletekhez lásd [478]-at).

**3.21. Példa. Teljes legkisebb négyzetek.** Tekintsük az

$$f(t,x) = x t$$

modellfüggvény (azaz egy origón átmenő, meghatározandó $x$ meredekségű egyenes) illesztését a következő adatpontokhoz:

$$\begin{array}{c|ccc} t & -2 & -1 & 3 \\ y & -1 & 3 & -2 \end{array}$$

Az $y$ értékeknek $t$ függvényeként való illesztése akkor célszerű, ha az $y$ adatok hibával terheltek, a $t$-re vonatkozó adatok viszont pontosak. Az így kapott közönséges legkisebb négyzetek illesztés, amely a 3.5(a). ábrán látható, az egyenes és az adatpontok közötti függőleges távolságok négyzetösszegét minimalizálja, ami $x = -0{,}5$ meredekséget ad. Ha azonban a $t$-re vonatkozó adatok éppúgy hibával terheltek, akár meg is fordíthattuk volna a szerepeket, és $t$-t illeszthettük volna $y$ függvényében. Az így kapott közönséges legkisebb négyzetek illesztés, amely a 3.5(b). ábrán látható, az egyenes és az adatpontok közötti vízszintes távolságok négyzetösszegét minimalizálja, ami $x = -2$ meredekséget ad. Ilyen helyzetben mindkettőnél jobb stratégia a teljes legkisebb négyzetek, amely minden adatot egyenrangúan kezel. Az így kapott illesztés, amely a 3.5(c). ábrán látható, az egyenes és az adatpontok közötti legrövidebb (azaz merőleges) távolságok négyzetösszegét minimalizálja, ami $x = -1$ meredekséget ad. Ahhoz, hogy ezt az utóbbi illesztést hogyan kaptuk, észrevesszük, hogy ennek a feladatnak az $\boldsymbol{A}$ mátrixa csak egyetlen oszlopot tartalmaz, ezért kiszámítjuk az

$$[\boldsymbol{A} \ \boldsymbol{b}] = [\boldsymbol{t} \ \boldsymbol{y}] = \begin{bmatrix} -2 & -1 \\ -1 & 3 \\ 3 & -2 \end{bmatrix} =$$

$$\begin{bmatrix} -0{,}154 & 0{,}802 & 0{,}577 \\ -0{,}617 & -0{,}535 & 0{,}577 \\ 0{,}772 & -0{,}267 & 0{,}577 \end{bmatrix} \begin{bmatrix} 4{,}583 & 0 \\ 0 & 2{,}646 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 0{,}707 & -0{,}707 \\ -0{,}707 & -0{,}707 \end{bmatrix} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T$$

SVD-t, így

$$\boldsymbol{x} = -(1/v_{2,2})\,v_{1,2} = -(1/(-0{,}707))\,(-0{,}707) = -1.$$

![](_page_38_Figure_4.jpeg)

3.5. ábra: Egyenes közönséges és teljes legkisebb négyzetes illesztése adott adatokra.

## 3.7 Módszerek összehasonlítása

Eddig több módszert is láttunk legkisebb négyzetek feladatok megoldására. Hogy közülük melyiket választjuk, az a konkrét megoldandó feladattól függ, és a hatékonyság, a pontosság és a megbízhatóság közötti átváltásokkal jár.

A normálegyenletek módszere könnyen megvalósítható: csupán mátrixszorzást és Cholesky-felbontást igényel. Ráadásul rendkívül vonzó, hogy $m \gg n$ esetén a feladatot egy $n \times n$-es rendszerre redukálja. Ha kihasználjuk a szimmetriáját, az $\boldsymbol{A}^T \boldsymbol{A}$ keresztszorzat-mátrix előállítása körülbelül $mn^2/2$ szorzást és hasonló számú összeadást igényel. A keletkező lineáris egyenletrendszer megoldása Cholesky-felbontással körülbelül $n^3/6$ szorzást és hasonló számú összeadást igényel. Sajnos a normálegyenletek módszere olyan megoldást ad, amelynek relatív hibája $[\operatorname{cond}(\boldsymbol{A})]^2$-tel arányos, a szükséges Cholesky-felbontás pedig $\operatorname{cond}(\boldsymbol{A}) \approx 1/\sqrt{\epsilon_{\text{mach}}}$ vagy rosszabb esetén várhatóan meghiúsul.

Sűrű lineáris legkisebb négyzetek feladatok megoldására a Householder-módszer általában a leghatékonyabb és legpontosabb az ortogonalizációs módszerek közül. Körülbelül $mn^2 - n^3/3$ szorzást és hasonló számú összeadást igényel. Megmutatható, hogy a Householder-módszer olyan megoldást ad, amelynek relatív hibája $\operatorname{cond}(\boldsymbol{A}) + \|\boldsymbol{r}\|_2[\operatorname{cond}(\boldsymbol{A})]^2$-tel arányos, ami a lehető legjobb, mivel ez a legkisebb négyzetek feladat megoldásának belső érzékenysége (idézzük fel a 3.3. szakaszt). Ráadásul a Householder-módszer (a visszahelyettesítési fázisban) csak akkor várhatóan hiúsul meg, ha $\operatorname{cond}(\boldsymbol{A}) \approx 1/\epsilon_{\text{mach}}$ vagy rosszabb.

Majdnem négyzetes feladatokra, $m \approx n$ esetén a normálegyenletek módszere és a Householder-módszer körülbelül ugyanannyi munkát igényel. Erősen túlhatározott feladatokra azonban, $m \gg n$, a Householder-módszer körülbelül kétszer annyi munkát igényel, mint a normálegyenletek módszere. Másrészt a Householder-módszer pontosabb és szélesebb körben alkalmazható, mint a normálegyenletek módszere. Ezek az előnyök azonban nem feltétlenül érik meg a többletköltséget, ha a feladat elég jól kondicionált ahhoz, hogy a normálegyenletek módszere kellően pontos eredményt szolgáltasson. Ranghiányos vagy közel ranghiányos feladatokra természetesen az oszloponkénti főelemkiválasztással végzett Householder-módszer használható eredményt adhat ott is, ahol a normálegyenletek módszere egyenesen meghiúsulna.

Végül az SVD a legköltségesebb módszer: költsége $mn^2 + n^3$-tel arányos, az arányossági állandó pedig $4$-től $10$-ig vagy annál is tovább terjedhet, az alkalmazott konkrét algoritmustól függően (lásd a 4.7. szakaszt). Így az SVD kiemelkedő robusztusságának és megbízhatóságának magas az ára, amit mindazonáltal különösen kritikus vagy kényes helyzetekben érdemes lehet megfizetni.

# 3.8 Szoftverek lineáris legkisebb négyzetek feladatokhoz

A 3.1. táblázat a lineáris legkisebb négyzetek feladatok megoldására alkalmas rutinok listáját tartalmazza, mind teljes rangú, mind ranghiányos esetre. A felsorolt rutinok többsége QR-felbontáson alapul. Sok csomag SVD-hez is tartalmaz szoftvert, amely – nagyobb számítási költséggel – szintén használható legkisebb négyzetek feladatok megoldására. Az SVD különösen megbízható módszert ad a numerikus rang meghatározására és a lehetséges ranghiány kezelésére (lásd a 3.6. szakaszt). Mivel az SVD kiszámításának módszerei szorosan kapcsolódnak a sajátérték-számítás módszereihez (lásd a 4.7. szakaszt), az SVD kiszámítására szolgáló szoftvereket a sajátértékekre és sajátvektorokra vonatkozó szoftverekkel együtt a 4.2. táblázat sorolja fel. A teljes legkisebb négyzetek feladatok megoldására – ahol az összes változó véletlen hibával terhelt – a `dtls` rutin elérhető a Netlibről.

Az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ lineáris legkisebb négyzetek feladatok megoldására szolgáló hagyományos szoftver olykor egyetlen rutinként van megvalósítva, de felosztható két rutinra is: az egyik a felbontás kiszámítására, a másik a keletkező háromszögű rendszer megoldására szolgál. A tipikusan megkövetelt bemenet a következőket tartalmazza: egy kétdimenziós tömb az $\boldsymbol{A}$ mátrixszal, egy egydimenziós tömb a $\boldsymbol{b}$ jobb oldali vektorral (vagy egy kétdimenziós tömb több jobb oldali vektorra), a mátrix $m$ sorainak és $n$ oszlopainak száma, az $\boldsymbol{A}$-t tartalmazó tömb vezető dimenziója (hogy a szubrutin helyesen tudja értelmezni a tömbindexeket), valamint esetenként némi munkaterület és egy zászló az elvégzendő konkrét feladat jelzésére.

| Forrás             | Felbontás          | Megoldás                       | Ranghiányos          |
| ------------------ | ------------------ | ------------------------------ | -------------------- |
| FMM [152]          | `svd`              |                                | `svd`                |
| GSL                | `gsl_linalg_QR_decomp` | `gsl_linalg_QR_solve`      | `gsl_linalg_QRPT_decomp` |
| IMSL               | `lqrrr`            | `lqrsl`                        | `lsqrr`              |
| KMN [262]          | `sqrls`            | `sqrls`                        | `ssvdc`              |
| LAPACK [9]         | `sgeqrf`           | `sormqr` / `strtrs`            | `sgeqpf` / `stzrqf`  |
| Lawson & Hanson [299] | `hft`           | `hs1`                          | `hfti`               |
| LINPACK [116]      | `sqrdc`            | `sqrsl`                        | `sqrst`              |
| MATLAB             | `qr`               | `\`                            | `svd`                |
| NAG                | `f08aef`           | `f08agf` / `f07tef`            | `f04jgf`             |
| NAPACK [220]       | `qr`               | `over`                         | `sing` / `rsolve`    |
| NR [377]           | `qrdcmp`ᵃ          | `qrsolv`                       | `svdcmp` / `svbksb`  |
| NUMAL [297]        | `lsqortdec`        | `lsqsol`                       | `solovr`             |
| SciPy              | `linalg.qr`        | `linalg.solve_triangular`      | `linalg.qr`          |
| SLATEC             | `sqrdc`            | `sqrsl`                        | `llsia` / `sglss` / `minfit` |
| SOL [509]          | `hredl`            | `qrvslv`                       | `mnlnls`             |

ᵃA megjelent formájában a `qrdcmp` és a `qrsolv` csak négyzetes mátrixokat kezel, de könnyen módosíthatók téglalap alakú mátrixok kezelésére.

3.1. táblázat: Szoftverek lineáris legkisebb négyzetek feladatokhoz.

A felhasználónak adott esetben egy toleranciát is meg kell adnia, ha oszloponkénti főelemkiválasztás vagy más rang-meghatározási módszer alkalmazására kerül sor. Visszatéréskor az $\boldsymbol{x}$ megoldás rendszerint felülírja a $\boldsymbol{b}$ memóriáját, a felbontás pedig az $\boldsymbol{A}$ memóriáját.

A MATLAB-ban a négyzetes lineáris egyenletrendszerek megoldására használt bal oldali osztás operátor téglalap alakú rendszerekre is kiterjesztésre került. Így az $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ túlhatározott rendszer legkisebb négyzetek megoldását az `x = A \ b` utasítás adja. A megoldást belsőleg QR-felbontással számítja, de a felhasználónak erről nem kell tudnia. A QR-felbontás kifejezetten is kiszámítható, ha szükséges, a MATLAB `qr` függvényével: `[Q, R] = qr(A)`. A szingulárisérték-felbontást kiszámító MATLAB-függvény alakja `[U, S, V] = svd(A)`.

A táblázatban felsoroltakhoz hasonló matematikai szoftverkönyvtárakon kívül számos statisztikai csomag terjedelmes szoftverrel rendelkezik a legkisebb négyzetek feladatok különféle kontextusban történő megoldására, és ezek gyakran számos diagnosztikai lehetőséget is tartalmaznak az eredmények minőségének értékelésére. Ebbe a kategóriába tartozó ismert csomagok a BMDP, a JMP, a Minitab, az R, az S, a SAS, az SPSS, a Stata és a Statistica. Elérhető egy statisztikai eszköztár (*toolbox*) MATLAB-hoz, valamint könyvtárak a Pythonhoz, például a pandas és a statsmodels. További szoftver is rendelkezésre áll olyan adatillesztéshez, amely nem a legkisebb négyzetek, hanem más kritériumok alapján történik – különösen az 1-norma és a $\infty$-norma alapján –, amelyek bizonyos kontextusokban kedvezőbbek.

# 3.9 Történeti jegyzetek és további olvasnivaló

A legkisebb négyzetek módszerét, amely a normálegyenleteken alapul, Gauss fogalmazta meg és használta 1795-ben, először azonban Legendre publikálta 1805-ben, ami elsőbbségi vitához vezetett (lásd [374]-et). A Gram–Schmidt-ortogonalizációt Gram fogalmazta meg 1883-ban, majd modern algoritmikus formában Schmidt adta meg 1907-ben. A Gram–Schmidt „módosított” változata valójában idősebb a „klasszikus” változatnál: Laplace vezette le 1816-ban, numerikus fölényét azonban csak 1966-ban ismerte fel Rice. A QR-felbontás kiszámításának Householder-féle módszerét 1958-ban publikálták, bár elemi reflektorokat (amelyeket ma Householder-transzformációknak nevezünk) Turnbull és Aitken már 1932-ben használt, egy másik célból. A QR-felbontás kiszámításának Givens-féle módszerét szintén 1958-ban publikálták, bár síkbeli forgatásokat Jacobi már egy évszázaddal korábban használt sajátértékek kiszámítására (lásd a 4.5.8. szakaszt). A QR-felbontás – és különösen a Householder-módszer – legkisebb négyzetek feladatok megoldására való felhasználását Golub tette népszerűvé 1965-ben [194]. A legkisebb négyzetek feladat számításainak átfogó kézikönyvei közé tartoznak [39, 136, 229, 299]. A 2.8. szakaszban hivatkozott, mátrixszámításokkal foglalkozó könyvek szintén tárgyalják részletesen a lineáris legkisebb négyzetek feladatokat. A ranghiány kezelésére szolgáló technikák tárgya [226, 228]. A teljes legkisebb négyzetek alapos tárgyalása – amely akkor megfelelő, ha minden változó véletlen hibával terhelt – megtalálható [477, 478]-ban. A legkisebb négyzetek feladatok számításainak statisztikai nézőpontú tárgyalásához lásd [178, 179, 273, 335, 452]-t.

A legkisebb négyzetek feladatok legegyszerűbb típusával foglalkoztunk, amelyben a modellfüggvény lineáris és minden adatpont egyenlő súllyal szerepel. A nemlineáris legkisebb négyzetek feladatokat a 6.6. szakaszban tárgyaljuk. Az adatpontok változó súlyainak vagy a változók közötti általánosabb keresztkorrelációknak a figyelembevétele a tárgyalt keretben viszonylag egyszerű. Az adatpontok változó súlyainak engedélyezése például mindössze annyit jelent, hogy a legkisebb négyzetek rendszer mindkét oldalát megszorozzuk egy megfelelő diagonális mátrixszal.

A szingulárisérték-felbontást egymástól függetlenül Beltrami fogalmazta meg 1873-ban és Jordan 1874-ben, mindketten kvadratikus alakok kapcsán. Az SVD mátrixokra vonatkozó definícióját az 1930-as években Eckart és Young dolgozta ki, akik a 3.6.1. szakaszban idézett alacsonyabb rangú közelítési tételt is bizonyították. A szingulárisérték-felbontás részletes történetéhez lásd [427]-et. A szingulárisérték-felbontásnak a törzsanyagban tárgyaltakon kívül az alkalmazások széles köre ismert, köztük a képfeldolgozás [11], a jelfeldolgozás [470], az irányítás [336], a geofizika [250], az információ-visszakeresés [36] és a kriptográfia [332]. A pszeudoinverzt – az itt adott definícióban – Moore fogalmazta meg 1920-ban, majd Penrose tette népszerűvé 1955-ben, hatalmas szakirodalmat indítva útjára.

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
- **3.18.** (a) Használható-e a főelemkiválasztással végzett Gauss-elimináció arra, hogy egy téglalap alakú $m \times n$-es $\boldsymbol{A}$ mátrix $\boldsymbol{L}\boldsymbol{U}$-felbontását kiszámítsuk, ahol $\boldsymbol{L}$ egy $m \times k$-s mátrix, amelynek a főátló feletti összes eleme nulla, $\boldsymbol{U}$ egy $k \times n$-es mátrix, amelynek a főátló alatti összes eleme nulla, és $k = \min\{m, n\}$? (b) Ha ez lehetséges volna, megoldási módot adna-e egy $\boldsymbol{A}\boldsymbol{x} \cong \boldsymbol{b}$ túlhatározott legkisebb négyzetes feladatra, ahol $m > n$? Miért?
- **3.19.** (a) Mit jelent az, hogy két $\boldsymbol{x}$ és $\boldsymbol{y}$ vektor ortogonális egymásra? (b) Bizonyítsd be, hogy ha két nem nulla vektor ortogonális egymásra, akkor szükségképpen lineárisan függetlenek is. (c) Adj példát $\mathbb{R}^2$-ben két olyan nem nulla vektorra, amelyek ortogonálisak egymásra. (d) Adj példát $\mathbb{R}^2$-ben két olyan nem nulla vektorra, amelyek nem ortogonálisak egymásra. (e) Sorolj fel két módot, ahogyan az ortogonalitás fontos a lineáris legkisebb négyzetes feladatok kontextusában.
- **3.20.** Az euklideszi $n$-dimenziós térben tranzitív reláció-e az ortogonalitás? Azaz ha $\boldsymbol{x}$ ortogonális $\boldsymbol{y}$-ra, és $\boldsymbol{y}$ ortogonális $\boldsymbol{z}$-re, akkor $\boldsymbol{x}$ szükségképpen ortogonális-e $\boldsymbol{z}$-re?
- **3.21.** Mit értünk ortogonális projektor alatt? Miért releváns ez a fogalom a lineáris legkisebb négyzetek szempontjából?
- **3.22.** (a) Miért használnak gyakran ortogonális transzformációkat – például Householder- vagy Givens-típusúakat – a legkisebb négyzetes feladatok megoldására? (b) Miért nem használják gyakran az ilyen módszereket négyzetes lineáris egyenletrendszerek megoldására? (c) Van-e valamilyen előnye az ortogonális transzformációknak a Gauss-eliminációval szemben a négyzetes lineáris egyenletrendszerek megoldásában? Ha igen, nevezz meg egyet.
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
- **3.33.** Az $\boldsymbol{A}$ mátrixot tartalmazó – felülírható – bemeneti tömbön túl mennyi további kisegítő tömbmemória szükséges az alábbiak kiszámításához és tárolásához? (a) $\boldsymbol{A}$ LU-felbontása részleges főelemkiválasztással végzett Gauss-eliminációval, ahol $\boldsymbol{A}$ egy $n \times n$-es mátrix. (b) $\boldsymbol{A}$ QR-felbontása Householder-transzformációkkal, ahol $\boldsymbol{A}$ egy $m \times n$-es mátrix.
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
