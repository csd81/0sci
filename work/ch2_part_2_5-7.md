## 2.5 Lineáris egyenletrendszerek speciális típusai

Eddig azt feltételeztük, hogy a lineáris rendszer mátrixa általános és *sűrű*, azaz a mátrix bejegyzéseinek lényegében mindegyike nemnulla. Ha a mátrix rendelkezik valamilyen speciális tulajdonsággal, akkor a lineáris rendszer megoldásakor gyakran műveletet és tárhelyet lehet megtakarítani. A kihasználható speciális tulajdonságokra néhány példa a következő:

- Szimmetrikus: $\mathbf{A} = \mathbf{A}^T$, azaz $a_{ij} = a_{ji}$ minden $i, j$ esetén.
- Pozitív definit: $\mathbf{x}^T \mathbf{A} \mathbf{x} > 0$ minden $\mathbf{x} \neq \mathbf{0}$ vektorra.
- Sávos: $a_{ij} = 0$ minden $|i - j| > \beta$ esetén, ahol $\beta$ az $\boldsymbol{A}$ mátrix sávszélessége. Fontos speciális eset a tridiagonális mátrix, amelyre $\beta = 1$.
- Ritka: az $A$ bejegyzéseinek többsége nulla.

A szimmetrikus és sávos rendszerek kezelésének technikái a sűrű rendszerekre alkalmazott Gauss-kiküszöbölés viszonylag egyszerű változatai. Az általánosabb nemnulla-mintázatú ritka lineáris rendszerek ezzel szemben olyan kifinomultabb algoritmusokat és adatszerkezeteket igényelnek, amelyek elkerülik a mátrixban lévő nullák tárolását és a velük végzett műveleteket (lásd a 11.4.1. szakaszt).

A valós mátrixokra az imént definiált tulajdonságoknak komplex mátrixok esetén is megvannak a megfelelőik, de a komplex esetben a szokásos mátrixtranszponált helyébe a konjugált transzponált lép, amelyet $H$ felső indexszel jelölünk. Ha $z = \alpha + i\beta$ komplex szám, ahol $\alpha$ és $\beta$ valós számok és $i = \sqrt{-1}$, akkor a komplex konjugáltját a $\bar{z} = \alpha - i\beta$ definíció adja (lásd az 1.3.11. szakaszt). Egy $\boldsymbol{A}$ mátrix konjugált transzponáltját ezek után az $\{\boldsymbol{A}^H\}_{ij} = \bar{a}_{ji}$ képlet adja meg. Természetesen egy valós $\boldsymbol{A}$ mátrixra $\boldsymbol{A}^H = \boldsymbol{A}^T$. Egy komplex mátrix *hermitikus*, ha $\boldsymbol{A} = \boldsymbol{A}^H$, és pozitív definit, ha $\boldsymbol{x}^H \boldsymbol{A} \boldsymbol{x} > 0$ minden $\boldsymbol{x} \neq \boldsymbol{0}$ komplex vektorra.

### 2.5.1 Szimmetrikus pozitív definit rendszerek

Ha az $\boldsymbol{A}$ mátrix szimmetrikus és pozitív definit, akkor az LU-felbontás úgy is elrendezhető, hogy $\boldsymbol{U} = \boldsymbol{L}^T$ legyen, azaz $\boldsymbol{A} = \boldsymbol{L}\boldsymbol{L}^T$, ahol $\boldsymbol{L}$ alsó háromszögmátrix pozitív diagonális bejegyzésekkel (de általában nem egységdiagonálissal). Ezt nevezik az $\boldsymbol{A}$ Cholesky-felbontásának, és egy algoritmus a kiszámítására abból kapható, ha az $\boldsymbol{A}$ és a $\boldsymbol{L}\boldsymbol{L}^T$ megfelelő bejegyzéseit egyenlővé tesszük, majd az $\boldsymbol{L}$ bejegyzéseit a helyes sorrendben állítjuk elő. Például a $2 \times 2$-es esetben

$$\begin{bmatrix} a_{11} & a_{21} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} \ell_{11} & 0 \\ \ell_{21} & \ell_{22} \end{bmatrix} \begin{bmatrix} \ell_{11} & \ell_{21} \\ 0 & \ell_{22} \end{bmatrix},$$

amiből adódik, hogy

$$\ell_{11} = \sqrt{a_{11}}, \quad \ell_{21} = a_{21}/\ell_{11}, \quad \ell_{22} = \sqrt{a_{22} - \ell_{21}^2}.$$

Az ezáltal nyert általános eljárás egyik lehetséges megszervezése a 2.7. algoritmus, amelyben a Cholesky-faktor $\boldsymbol{L}$ felülírja az eredeti $\boldsymbol{A}$ mátrixot.

A Cholesky-felbontási algoritmusnak számos olyan tulajdonsága van, amely nagyon vonzóvá és népszerűvé teszi szimmetrikus pozitív definit mátrixok esetén:

- A szükséges $n$ négyzetgyökvonás mindegyike pozitív számra történik, így az algoritmus jól definiált.
- Numerikus stabilitás céljából nincs szükség főelemkiválasztásra.

**2.7. Algoritmus. Cholesky-felbontás.**

```
for k = 1 to n
    akk =
          √
            akk
    for i = k + 1 to n
        aik = aik/akk
    end
    for j = k + 1 to n
        for i = j to n
            aij = aij − aik · ajk
        end
    end
end
                                        { ciklus az oszlopokon }
                                        { az aktuális oszlop skálázása }
                                        { minden hátralévő oszlopból
                                             kivonjuk az aktuális oszlop
                                             egy megfelelő többszörösét }
```

- Csak az $A$ alsó háromszöge kerül elérésre, ezért a szigorú felső háromszög-részét nem kell tárolni.
- Csak körülbelül $n^3/6$ szorzásra és hozzávetőleg ugyanennyi összeadásra van szükség.

Így a Cholesky-felbontás csak körülbelül feleannyi műveletet és feleannyi tárhelyet igényel, mint egy általános mátrix Gauss-kiküszöböléssel való LU-felbontása. Sajnos ahhoz, hogy a tárhelynek ezt a megtakarítását ki is használjuk, rendszerint szükség van arra, hogy a szimmetrikus mátrix egyik háromszögét egy egydimenziós tömbbe csomagoljuk, ami kényelmetlenebb, mint a mátrixok szokásos kétdimenziós tárolása. Ezért a lineáris algebrai szoftvercsomagok szimmetrikus mátrixokra általában mind a csomagolt tárolású, mind a szabványos kétdimenziós tömbtárolású változatot felkínálják, hogy a felhasználó a kényelem és a tárhelytakarékosság között választhasson.

Bizonyos körülmények között előnyös lehet a Cholesky-felbontást $\boldsymbol{A} = \boldsymbol{L}\boldsymbol{D}\boldsymbol{L}^T$ alakban felírni, ahol $\boldsymbol{L}$ egységdiagonálisú alsó háromszögmátrix, $\boldsymbol{D}$ pedig pozitív diagonális bejegyzésű diagonális mátrix. Egy ilyen felbontás a szabványos Cholesky-algoritmus egy egyszerű változatával számítható ki, és megvan az az előnye, hogy nem igényel négyzetgyökvonást. A $\boldsymbol{L}\boldsymbol{D}\boldsymbol{L}^T$-felbontásban a $\boldsymbol{D}$ diagonális bejegyzései egyszerűen a $\boldsymbol{L}\boldsymbol{L}^T$-felbontásban szereplő $\boldsymbol{L}$ diagonális bejegyzéseinek négyzetei.

**2.21. Példa. Cholesky-felbontás.** Az algoritmus szemléltetésére kiszámítjuk a szimmetrikus pozitív definit

$$\mathbf{A} = \begin{bmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{bmatrix}$$

mátrix Cholesky-felbontását. Mivel az algoritmus csak a mátrix alsó háromszögét érinti, a mátrix alsó háromszögének egymást követő transzformációit mutatjuk be. Az első oszlopot a diagonális bejegyzésének négyzetgyökével, $\sqrt{3} \approx 1{,}7321$-gyel elosztva

$$\begin{bmatrix} 1{,}7321 \\ -0{,}5774 & 3 \\ -0{,}5774 & -1 & 3 \end{bmatrix}$$

adódik. A második oszlopot úgy módosítjuk, hogy kivonjuk belőle a $(2, 1)$ bejegyzésnek, $-0{,}5774$-nek, az első oszlop megfelelő részével vett szorzatát, a harmadik oszlopot pedig úgy, hogy kivonjuk belőle a $(3, 1)$ bejegyzésnek, szintén $-0{,}5774$-nek, az első oszlop megfelelő részével vett szorzatát, ami

$$\begin{bmatrix} 1{,}7321 \\ -0{,}5774 & 2{,}6667 \\ -0{,}5774 & -1{,}3333 & 2{,}6667 \end{bmatrix}$$

eredményre vezet. A második oszlopot ezután elosztjuk a diagonális bejegyzésének négyzetgyökével, $\sqrt{2{,}6667} \approx 1{,}6330$-cal, amivel

$$\begin{bmatrix} 1{,}7321 \\ -0{,}5774 & 1{,}6330 \\ -0{,}5774 & -0{,}8165 & 2{,}6667 \end{bmatrix}$$

adódik. A harmadik oszlopot úgy módosítjuk, hogy kivonjuk belőle a $(3, 2)$ bejegyzésnek, $-0{,}8165$-nek, a második oszlop megfelelő részével vett szorzatát, ami

$$\begin{bmatrix} 1{,}7321 \\ -0{,}5774 & 1{,}6330 \\ -0{,}5774 & -0{,}8165 & 2{,}0000 \end{bmatrix}$$

eredményre vezet. A harmadik diagonális bejegyzés négyzetgyökét véve a végeredmény

$$\mathbf{L} = \begin{bmatrix} 1{,}7321 \\ -0{,}5774 & 1{,}6330 \\ -0{,}5774 & -0{,}8165 & 1{,}4142 \end{bmatrix}.$$

### 2.5.2 Szimmetrikus indefinit rendszerek

Ha az $A$ mátrix szimmetrikus, de indefinit (azaz $x^T A x$ $x$-től függően pozitív és negatív értékeket is felvehet), akkor a Cholesky-felbontás nem alkalmazható, és a numerikus stabilitáshoz általában valamilyen főelemkiválasztásra van szükség. Nyilvánvaló, hogy ha meg akarjuk őrizni a mátrix szimmetriáját, a főelemkiválasztásnak szimmetrikusnak kell lennie, azaz $P A P^T$ alakúnak, ahol $P$ permutációs mátrix.

Szeretnénk olyan $P A P^T = L D L^T$ alakú felbontást kapni, ahol $L$ egységdiagonálisú alsó háromszögmátrix és $D$ diagonális. Sajnos diagonális $D$-vel ilyen felbontás nem feltétlenül létezik, és létezése esetén is általában nem számítható ki stabilan pusztán szimmetrikus főelemkiválasztással. A legjobb, amit tehetünk, hogy $D$-t vagy tridiagonálisnak, vagy $1 \times 1$-es és $2 \times 2$-es diagonális blokkokkal rendelkező blokkdiagonálisnak választjuk. (Blokkmátrixnak nevezünk egy olyan mátrixot, amelynek bejegyzéseit kompatibilis méretű részmátrixokra, azaz „blokkokra” osztjuk. Egy blokkdiagonális mátrixban ezek közül a részmátrixok közül mindegyik nulla, kivéve a fő blokkdiagonálisban lévőket.)

Hatékony algoritmusokat dolgozott ki Aasen a tridiagonális felbontásra, valamint Bunch és Parlett (Bunch és Kaufman, illetve mások későbbi továbbfejlesztéseivel a főelemkiválasztási eljárásban) a blokkdiagonális felbontásra (lásd [198]). Mindkét esetben a főelemkiválasztási eljárás olyan stabil felbontást ad, amely csak körülbelül $n^3/6$ szorzást és hozzávetőleg ugyanennyi összeadást igényel. Mindkét esetben a rákövetkező megoldási szakasznak is csak $\mathcal{O}(n^2)$ munkára van szüksége. Így a szimmetrikus indefinit rendszerek megoldásának költsége hasonló a pozitív definit rendszerek Cholesky-felbontással való megoldásának költségéhez, és csak körülbelül a fele a nemszimmetrikus rendszerek Gauss-kiküszöböléssel való megoldásának költségének.

### 2.5.3 Sávos rendszerek

A Gauss-kiküszöbölés sávmátrixokra alig különbözik az általános esettől: az egyedüli algoritmikus változtatások a ciklusok tartományaiban vannak. Természetesen olyan adatszerkezetet érdemes használni a sávmátrixhoz, amely elkerüli a sávon kívüli nulla bejegyzések tárolását. Gyakori választás, amikor a sáv sűrű, hogy a mátrixot kétdimenziós tömbben, diagonálisonként tároljuk. Ha numerikus stabilitáshoz szükség van főelemkiválasztásra, akkor az algoritmus kissé bonyolultabbá válik annyiban, hogy a sávszélesség növekedhet (de legfeljebb a kétszeresére). Így egy tetszőleges sávszélességű sávos rendszereket kezelő általános célú megoldó igen hasonló egy általános mátrixokra szolgáló Gauss-kiküszöbölési kódhoz.

Rögzített kis sávszélesség esetén azonban egy sávos rendszermegoldó rendkívül egyszerű lehet, különösen ha a stabilitáshoz nincs szükség főelemkiválasztásra. Tekintsük például a tridiagonális

$$\mathbf{A} = \begin{bmatrix} b_1 & c_1 & 0 & \cdots & 0 \\ a_2 & b_2 & c_2 & \ddots & \vdots \\ 0 & \ddots & \ddots & \ddots & 0 \\ \vdots & \ddots & a_{n-1} & b_{n-1} & c_{n-1} \\ 0 & \cdots & 0 & a_n & b_n \end{bmatrix}$$

mátrixot. Ha a stabilitáshoz nincs szükség főelemkiválasztásra — ami a gyakorlatban előforduló tridiagonális rendszerek esetén gyakran teljesül (például ha a mátrix diagonálisan domináns vagy pozitív definit) —, akkor a Gauss-kiküszöbölés a 2.8. algoritmusra redukálódik, és az $\boldsymbol{A}$ mátrix keletkező háromszögű faktorait a következő képletek adják:

$$\boldsymbol{L} = \begin{bmatrix} 1 & 0 & \cdots & \cdots & 0 \\ m_2 & 1 & \ddots & \ddots & \vdots \\ 0 & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & m_{n-1} & 1 & 0 \\ 0 & \cdots & 0 & m_n & 1 \end{bmatrix}, \quad \boldsymbol{U} = \begin{bmatrix} d_1 & c_1 & 0 & \cdots & 0 \\ 0 & d_2 & c_2 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & 0 \\ \vdots & \ddots & \ddots & \ddots & 0 \\ \vdots & \ddots & \ddots & d_{n-1} & c_{n-1} \\ 0 & \cdots & \cdots & 0 & d_n \end{bmatrix}.$$

Általában egy $\beta$ sávszélességű sávos rendszer csak $\mathcal{O}(\beta n)$ tárhelyet igényel, a felbontás pedig csak $\mathcal{O}(\beta^2 n)$ munkát; mindkettő jelentős megtakarítást jelent a telt rendszerekhez képest, ha $\beta \ll n$.

**2.8. Algoritmus. Tridiagonális LU-felbontás főelemkiválasztás nélkül.**

```
d1 = b1
for i = 2 to n
    mi = ai/di−1
    di = bi − mici−1
end
                                 { ciklus az oszlopokon }
                                 { szorzó kiszámítása }
                                 { transzformáció alkalmazása }
```

## 2.6 Iterációs módszerek lineáris egyenletrendszerekhez

A Gauss-kiküszöbölés egy példa a lineáris rendszerek megoldására szolgáló direkt módszerre, azaz olyan módszerre, amely (pontos aritmetikát feltételezve) egy lineáris rendszer pontos megoldását véges számú lépésben állítja elő. Az iterációs módszerek ezzel szemben a megoldás egy kezdeti becsléséből indulnak ki, és azt egymást követően javítják, amíg a megoldás olyan pontos nem lesz, amilyet kívánunk. Elméletben végtelen sok iterációra lehet szükség ahhoz, hogy a pontos megoldáshoz konvergáljon, a gyakorlatban azonban az iterációkat akkor állítjuk le, amikor a $\|b - Ax\|$ maradék — vagy a hiba valamilyen más mérőszáma — olyan kicsi, amilyet kívánunk. Egyes feladattípusok esetén az iterációs módszereknek jelentős előnyeik lehetnek a direkt módszerekkel szemben. A lineáris egyenletrendszerek iterációs módszereinek tárgyalását a 11. fejezetre halasztjuk, ahol a parciális differenciálegyenletek numerikus megoldását tekintjük, ami olyan ritka lineáris rendszerekre vezet, amelyeket gyakran iterációs módszerekkel lehet a legjobban megoldani.

## 2.7 Szoftverek lineáris egyenletrendszerekhez

Szinte minden tudományos számítási szoftverkönyvtár tartalmaz különféle típusú lineáris rendszerek megoldására szolgáló rutinokat. A 2.1. táblázat valós, általános, sűrű lineáris rendszerek megoldására, valamint a kondíciószám becslésére szolgáló megfelelő rutinok listáját tartalmazza néhány széles körben elérhető szoftvergyűjteményből. Egyes csomagok a rutinnevekben különböző elő- vagy utótagokat használnak az adattípus jelölésére, tipikusan az `s` az egyszeres pontosságú valós, `d` a dupla pontosságú valós, `c` az egyszeres pontosságú komplex és `z` a dupla pontosságú komplex változatra utal; itt csak az egyszeres pontosságú valós változatokat soroljuk fel. A legtöbb ilyen szubrutinkönyvtárban speciálisabb rutinok is rendelkezésre állnak a lineáris rendszerek bizonyos típusaira, mint a szimmetrikus, pozitív definit, sávos rendszerek vagy ezek kombinációi. Ezek közül a rutinok közül néhányat a 2.2. táblázat sorol fel; más rutinok is rendelkezésre állhatnak, amelyek tárhelytakarékosabbak, vagy egyéb speciális feladatokra készültek.

Az $A\boldsymbol{x} = \boldsymbol{b}$ lineáris rendszerek megoldására szolgáló hagyományos szoftver olykor egyetlen rutinként van megvalósítva, de felosztható két rutinra is: az egyik a felbontás kiszámítására, a másik a keletkező háromszögű rendszer megoldására. Mindkét esetben a felbontás megismétlésére nincs szükség, ha ugyanazzal a mátrixszal, de más jobb oldalakkal szeretnénk további megoldásokat. A tipikusan megkövetelt bemenet a következőket tartalmazza: egy kétdimenziós tömb az $A$ mátrixszal, egy egydimenziós tömb a $\boldsymbol{b}$ jobb oldali vektorral (vagy egy kétdimenziós tömb több jobb oldali vektorra), a rendszer egész $n$ rendje, az $A$-t tartalmazó tömb vezető dimenziója (hogy a szubrutin helyesen tudja értelmezni a tömbindexeket), valamint esetenként némi munkaterület és egy zászló az elvégzendő konkrét feladat jelzésére. Visszatéréskor az $\boldsymbol{x}$ megoldás rendszerint felülírja a $\boldsymbol{b}$ tárhelyét, a felbontás pedig az $A$ tárhelyét. További kimenetként szerepelhet egy állapotjelző zászló a hibák vagy figyelmeztetések jelzésére, valamint a mátrix kondíciószámának egy becslése (vagy olykor a kondíciószám reciproka). A kondíciószám becslésének többletköltsége miatt ez a szolgáltatás általában opcionális.

| Forrás           | Felbontás      | Megoldás       | Kondíció­becslés |
|------------------|----------------|----------------|--------------------|
| [152]<br>FMM     | decomp         | solve          |                    |
| GSL              | gsl<br>linalg  | gsl<br>linalg  |                    |
|                  | LU<br>decomp   | LU<br>solve    |                    |
| HSL              | ma21           | ma21           |                    |
| IMSL             | lftrg          | lfsrg          | lfcrg              |
| [262]<br>KMN     | sgefs          | sgefs          | sgefs              |
| [9]<br>LAPACK    | sgetrf         | sgetrs         | sgecon             |
| [116]<br>LINPACK | sgefa          | sgesl          | sgeco              |
| MATLAB           | lu             | \              | rcond/condest      |
| NAG              | f07adf         | f07aef         | f07agf             |
| [220]<br>NAPACK  | fact           | solve          | con                |
| [377]<br>NR      | ludcmp         | lubksb         |                    |
| [297]<br>NUMAL   | dec            | sol            |                    |
| SciPy            | linalg.        | linalg.        | numpy.linalg.      |
|                  | lu<br>factor   | lu<br>solve    | cond               |
| SLATEC           | sgefa          | sgesl          | sgeco              |

2.1. táblázat: Szoftverek általános lineáris rendszerek megoldására

Lineáris rendszerek megoldása interaktív környezetben, például MATLAB-ban egyszerűbb, mint hagyományos szoftverrel, mert a csomag belsőleg nyilvántartja az olyan részleteket, mint a vektorok és mátrixok méretei, és sok mátrixművelet be van építve a nyelv szintaxisába és szemantikájába. Például az $A\boldsymbol{x} = \boldsymbol{b}$ lineáris rendszer megoldását MATLAB-ban a „bal oldali osztás” operátor adja, amelyet fordított törtvonal jelöl, tehát `x = A \ b`. A megoldást belsőleg LU-felbontással, majd előre- és visszahelyettesítéssel számítja a rendszer, de a felhasználónak erről nem kell tudnia. Az LU-felbontás kifejezetten is kiszámítható, ha szükséges, a MATLAB `lu` függvényével: `[L, U] = lu(A)`, illetve ha a mátrix szimmetrikus és pozitív definit, akkor a Cholesky-felbontását az `L = chol(A)` adja.

### 2.7.1 LINPACK és LAPACK

A LINPACK átfogó szoftvercsomag sokféle lineáris egyenletrendszer megoldására, az általános sűrű rendszereken kívül olyanokat is beleértve, amelyeknek különféle speciális tulajdonságaik vannak, például szimmetrikusak vagy sávosak. A lineáris rendszerek megoldása annyira alapvető fontosságú a tudományos számításokban, hogy a LINPACK a számítógépek teljesítményének összehasonlítására szolgáló szabványos benchmarkká vált. A LINPACK kézikönyv [116] hasznos forrás gyakorlati tanácsokhoz a lineáris egyenletrendszerek megoldásához.

|                  | Szimmetrikus       | Szimmetrikus        | Általános       |
|------------------|--------------------|---------------------|-----------------|
| Forrás           | pozitív definit    | indefinit           | sávos           |
| GSL              | gsl<br>linalg      | gsl<br>linalg       |                 |
|                  | cholesky<br>decomp | mcholesky<br>decomp |                 |
| HSL              | ma22               | ma29                | ma35            |
| IMSL             | lftds/lfsds        | lftsf/lfssf         | lftrb/lfsrb     |
| [9]<br>LAPACK    | spotrf/spotrs      | ssytrf/ssytrs       | sgbtrf/sgbtrs   |
| [116]<br>LINPACK | spofa/sposl        | ssifa/ssisl         | sgbfa/sgbsl     |
| NAG              | f07fdf/f07fef      | f07mdf/f07mef       | f07bdf/f07bef   |
| [220]<br>NAPACK  | sfact/ssolve       | ifact/isolve        | bfact/bsolve    |
| [377]<br>NR      | choldc/cholsl      |                     | bandec/banbks   |
| [297]<br>NUMAL   | chldec2/chlsol2    | decsym2/solsym2     | decbnd/solbnd   |
| SciPy            | linalg.            | linalg.             | linalg.         |
|                  | cholesky           | ldl                 | solve<br>banded |
| SLATEC           | spofa/sposl        | ssifa/ssisl         | sgbfa/sgbsl     |

2.2. táblázat: Szoftverek speciális lineáris rendszerek megoldására

A LAPACK nevű utódcsomag a teljes LINPACK-gyűjteményt frissíti, nagyobb teljesítményt nyújtva a modern számítógép-architektúrákon, egyes párhuzamos számítógépeket is beleértve. A LAPACK újabb algoritmusai sok esetben nagyobb pontosságot, robusztusságot és funkcionalitást is elérnek, mint a LINPACK-beli elődeik. A LAPACK a lineáris algebra összes jelentős számítási feladatához egyaránt tartalmaz egyszerű és szakértői meghajtókat, valamint a különféle felbontásokhoz, a háromszögű rendszerek megoldásához, a normabecsléshez, a skálázáshoz és az iteratív finomításhoz szükséges sokféle számítási és kiegészítő rutint. Mind a LINPACK, mind a LAPACK elérhető a Netlibről, és számos egyéb könyvtár és csomag lineáris rendszermegoldóit közvetlenül ezekre építik.

### 2.7.2 Basic Linear Algebra Subprograms (BLAS)

A LINPACK és a LAPACK magas szintű rutinjai az alacsonyabb szintű Basic Linear Algebra Subprograms (BLAS) csomagon alapulnak. A BLAS-t eredetileg arra tervezték, hogy egységbe zárja a vektorokon végzett alapvető műveleteket, hogy azok egy adott számítógép-architektúrára optimalizálhatók legyenek, miközben a magasabb szintű, őket hívó rutinok hordozhatók maradnak. Az újabb számítógép-architektúrák arra ösztönöztek, hogy magasabb szintű BLAS-t fejlesszenek ki, amely a mátrix-vektor és a mátrix-mátrix műveleteket zárja egységbe a hierarchikus memóriának — például a gyorsítótárnak, a vektorregisztereknek és a lapozásos virtuális memóriának — a jobb kihasználása érdekében. A 2.3. táblázat felsorolja az egyes szintek néhány legfontosabb BLAS-rutinját.

A jó teljesítmény kulcsa az adat-újrafelhasználás, azaz az, hogy egy adott adaton minél több aritmetikai műveletet végezzünk, miközben az a memóriahierarchia leggyorsabban elérhető részében van tárolva. A 3. szintű BLAS-nak nagyobb lehetősége van az adat-újrafelhasználásra, mert $\mathcal{O}(n^3)$ műveletet végez $\mathcal{O}(n^2)$ adaton, míg az alacsonyabb szintű BLAS esetén a műveletek száma az adatok számával arányos. A BLAS általános változatai elérhetők a Netlibről, és számos számítógépgyártó kínál egyedi változatokat, amelyek a saját rendszerükön a legjobb teljesítményre vannak optimalizálva.

| Szint | TOMS<br># | Munka         | Példák | Funkció                          |  |
|-------|-----------|---------------|----------|---------------------------------|--|
| 1     | 539       | O(n)          | saxpy    | Skalár · vektor plusz vektor    |  |
|       |           |               | sdot     | Két vektor belső szorzata       |  |
|       |           |               | snrm2    | Vektor euklideszi normája       |  |
| 2     | 656       | 2<br>O(n<br>) | sgemv    | Mátrix-vektor szorzás           |  |
|       |           |               | strsv    | Háromszögű megoldás             |  |
|       |           |               | sger     | Elsőrendű frissítés             |  |
| 3     | 679       | 3<br>O(n<br>) | sgemm    | Mátrix-mátrix szorzás           |  |
|       |           |               | strsm    | Többszörös háromszögű megoldás  |  |
|       |           |               | ssyrk    | $k$-adrendű frissítés           |  |

2.3. táblázat: Példák az alapvető lineáris algebrai szubrutinokra (BLAS)
