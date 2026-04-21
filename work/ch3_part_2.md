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

$$\begin{split} \frac{\|\Delta \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} & \leq \|\boldsymbol{A}^{+}\|_{2} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{x}\|_{2}} \\ & = \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{b}\|_{2}}{\|\boldsymbol{A}\|_{2} \cdot \|\boldsymbol{x}\|_{2}} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}} \\ & \leq \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{b}\|_{2}}{\|\boldsymbol{A}\boldsymbol{x}\|_{2}} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}} \\ & = \operatorname{cond}(\boldsymbol{A}) \frac{1}{\cos(\theta)} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}}. \end{split}$$

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

$$\begin{split} \frac{\|\Delta \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} & \lesssim \|(\boldsymbol{A}^{T}\boldsymbol{A})^{-1}\|_{2} \cdot \|\boldsymbol{E}\|_{2} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{x}\|_{2}} + \|\boldsymbol{A}^{+}\|_{2} \cdot \|\boldsymbol{E}\|_{2} \\ & = [\operatorname{cond}(\boldsymbol{A})]^{2} \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{A}\|_{2} \cdot \|\boldsymbol{x}\|_{2}} + \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \\ & \leq \left([\operatorname{cond}(\boldsymbol{A})]^{2} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{A}\boldsymbol{x}\|_{2}} + \operatorname{cond}(\boldsymbol{A})\right) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \\ & = \left([\operatorname{cond}(\boldsymbol{A})]^{2} \tan(\theta) + \operatorname{cond}(\boldsymbol{A})\right) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}}. \end{split}$$

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

A $\boldsymbol{b} = [1 \ 0 \ 1]^T$ jobb oldali vektor esetén viszont $\|\Delta\boldsymbol{x}\|_2 / \|\boldsymbol{x}\|_2 = 0{,}5/\epsilon$, tehát a megoldás relatív perturbációja körülbelül annyi, mint $[\operatorname{cond}(\boldsymbol{A})]^2$-szerese az $\boldsymbol{A}$ relatív perturbációjának. Ennél a jobb oldalnál a maradék normája körülbelül $1$, és $\tan(\theta) \approx 1$, így a perturbációs korlátban szereplő négyzetre emelt kondíciószámú tag nem nyomódik el, és a megoldás rendkívül érzékeny. <!-- TODO: verify original "1, say around √mach" — OCR hiányos, valószínűleg "ε ≪ 1, say around √ε_mach" -->

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

Első pillantásra ez a módszer nem tűnik ígéretesnek: a kibővített rendszer szimmetrikus, de nem pozitív definit, nagyobb az eredeti rendszernél, és megköveteli, hogy az $\boldsymbol{A}$ két példányát tároljuk. Ráadásul, ha pusztán a főátló mentén választunk főelemet (ami a $2 \times 2$-es blokkrendszer blokkonkénti kiküszöbölésével egyenértékű), akkor a normálegyenleteket kapjuk vissza, amelyek potenciális numerikus gyengeségét már megfigyeltük. Az egyetlen elért előny az, hogy most más főelemkiválasztási stratégiák is rendelkezésünkre állnak, amelyek numerikus vagy más okokból hasznosak lehetnek.

A kibővített rendszer mátrixának szimmetrikus indefinit (lásd a 2.5.2. szakaszt) vagy LU-felbontásában a főelemek megválasztása nyilvánvalóan a felső és az alsó blokksorokban szereplő elemek relatív nagyságától függ. A $\boldsymbol{r}$ és az $\boldsymbol{x}$ relatív skálái önkényesek, ezért egy $\alpha$ skálázási paramétert vezetünk be a maradékhoz, ami a következő új rendszert adja:

$$\begin{bmatrix} \alpha \boldsymbol{I} & \boldsymbol{A} \\ \boldsymbol{A}^T & \boldsymbol{O} \end{bmatrix} \begin{bmatrix} \boldsymbol{r}/\alpha \\ \boldsymbol{x} \end{bmatrix} = \begin{bmatrix} \boldsymbol{b} \\ \boldsymbol{0} \end{bmatrix}.$$

Az $\alpha$ paraméter azt szabályozza, hogyan súlyozódnak a két alrendszer elemei egymáshoz képest a főelemek kiválasztásakor. Ésszerű ökölszabályként

$$\alpha = \max_{i,j} |a_{ij}|/1000$$

használható, de a legjobb érték meghatározásához némi kísérletezésre lehet szükség.

A módszer közvetlen implementációja aránytalanul nagy számításigényű lehet ($(m+n)^3$-nal arányos), ezért gondosan ki kell használni a kibővített mátrix speciális szerkezetét. A kibővített rendszer módszerét például a MATLAB hatékonyan használja nagy, ritka lineáris legkisebb négyzetek feladatokra.

### 3.4.3 Ortogonális transzformációk

A normálegyenletek megközelítésének potenciális numerikus nehézségei miatt szükségünk van egy olyan alternatívára, amely nem igényli a keresztszorzat-mátrix és a jobb oldali vektor képzését. Ezért egy numerikusan robusztusabb típusú transzformációt keresünk, amely egy egyszerűbb feladatra vezet, amelynek megoldása ugyanaz, mint az eredeti legkisebb négyzetek feladaté, de könnyebben számítható. Ahogyan a négyzetes lineáris rendszereknél, úgy itt is azt látjuk majd, hogy a háromszögű alak megfelelő célalak a legkisebb négyzetek feladatok egyszerűsítésére. Egy mátrix háromszögűvé alakítása Gauss-kiküszöböléssel azonban ebben a kontextusban nem megfelelő, mert egy ilyen transzformáció nem őrzi meg az euklideszi normát, és ennélfogva a legkisebb négyzetes megoldást sem.

Az ortogonalitásról korábban mondottakat alapul véve most olyan típusú lineáris transzformációt definiálunk, amely *megőrzi* az euklideszi normát. Egy négyzetes valós $\boldsymbol{Q}$ mátrixot *ortogonálisnak* mondunk, ha az oszlopai ortonormáltak, azaz ha $\boldsymbol{Q}^T \boldsymbol{Q} = \boldsymbol{I}$, az egységmátrix. Egy $\boldsymbol{Q}$ ortogonális transzformáció tetszőleges $\boldsymbol{v}$ vektor euklideszi normáját megőrzi, hiszen

$$\|\boldsymbol{Q}\boldsymbol{v}\|_2^2 = (\boldsymbol{Q}\boldsymbol{v})^T \boldsymbol{Q}\boldsymbol{v} = \boldsymbol{v}^T \boldsymbol{Q}^T \boldsymbol{Q} \boldsymbol{v} = \boldsymbol{v}^T \boldsymbol{v} = \|\boldsymbol{v}\|_2^2.$$

Az ortogonális mátrixok különböző módokon – például forgatással vagy tükrözéssel – transzformálhatnak vektorokat, de egy vektor euklideszi hosszát nem változtatják meg. Ennélfogva, ha egy lineáris legkisebb négyzetek feladat mindkét oldalát megszorozzuk egy ortogonális mátrixszal, a megoldás nem változik.

Az ortogonális mátrixok a numerikus számítások számos területén rendkívül fontosak, mert normamegőrző tulajdonságuk miatt nem erősítik fel a hibát. Így például ortogonális transzformációkkal négyzetes lineáris rendszerek is megoldhatók anélkül, hogy a numerikus stabilitás érdekében főelemkiválasztást kellene alkalmaznunk. Sajnos az ortogonalizáló módszerek számítási szempontból lényegesen költségesebbek, mint a Gauss-kiküszöbölésre épülők, ezért jobb numerikus tulajdonságaikért olyan árat kell fizetni, amely a kontextustól függően megérheti, vagy sem.

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
