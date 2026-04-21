# Jelölések

A könyvben használt jelölésrendszer meglehetősen szabványos, és kevés magyarázatra szorul. Szabadon használunk vektor- és mátrixjelölést: mátrixokat általában nagybetűs félkövér szedéssel, vektorokat kisbetűs félkövér szedéssel, skalárokat pedig normál szedéssel jelölünk. Az iterációs és komponensindexeket alsó indexszel jelöljük, általában $i$-től $n$-ig. Például egy $\boldsymbol{x}$ vektornak és egy $\boldsymbol{A}$ mátrixnak rendre $x_i$ és $a_{ij}$ elemei vannak. Azokban a ritkább esetekben, amikor iterációs index és komponensindex egyaránt szükséges, az iterációt zárójeles felső index jelzi, például $x_i^{(k)}$ egy sorozat $k$-adik vektorának $i$-edik komponensét jelenti. Egyébként $x_i$ az $\boldsymbol{x}$ vektor $i$-edik komponensét jelöli, míg $\boldsymbol{x}_k$ egy sorozat $k$-adik vektorát.

Az egyszerűség kedvéért elsősorban valós vektorokkal és mátrixokkal foglalkozunk, noha az általunk tárgyalt elmélet és algoritmusok nagy része kevés változtatással (vagy akár változtatás nélkül) átvihető a komplex esetre. A valós számok halmazát $\mathbb{R}$ jelöli, az $n$-dimenziós valós euklideszi teret $\mathbb{R}^n$, a valós $m \times n$ mátrixok halmazát pedig $\mathbb{R}^{m \times n}$. A megfelelő komplex megfelelők jelölése rendre $\mathbb{C}$, $\mathbb{C}^n$ és $\mathbb{C}^{m \times n}$.

Egy vektor vagy mátrix transzponáltját felső $T$ index jelzi, konjugált transzponáltját pedig felső $H$ index (a Hermitian transpose rövidítése). Hacsak másként nem jelezzük, minden vektort oszlopvektornak tekintünk; egy sorvektort egy oszlopvektor explicit transzponálásával adunk meg. A tördelési kényelem kedvéért egy oszlopvektor komponenseit néha a megfelelő sorvektor transzponáltjaként jelöljük, például $\mathbf{x} = \begin{bmatrix} x_1 & x_2 \end{bmatrix}^T$. Két $n$-dimenziós $\mathbf{x}$ és $\mathbf{y}$ vektor belső szorzata (más néven skaláris szorzat) a mátrixszorzás speciális eseteként áll elő, ezért $\mathbf{x}^T\mathbf{y}$-nal jelöljük (vagy $\mathbf{x}^H\mathbf{y}$-nal a komplex esetben). Hasonlóképpen két $n$-dimenziós $\mathbf{x}$ és $\mathbf{y}$ vektor külső szorzata, amely egy $n \times n$-es mátrix, $\mathbf{x}\mathbf{y}^T$ alakban írható. Az $n$-edrendű egységmátrixot $\mathbf{I}_n$ jelöli (vagy csak $\mathbf{I}$, ha az $n$ dimenzió a szövegkörnyezetből egyértelmű), $i$-edik oszlopát pedig $\mathbf{e}_i$. A zérusmátrixot $\mathbf{O}$, a zérusvektort $\mathbf{0}$, a zérusskalárt pedig $0$ jelöli. A $d_1, \ldots, d_n$ átlóbeli elemekkel rendelkező diagonális mátrixot $\operatorname{diag}(d_1, \ldots, d_n)$ jelöli. Vektorok vagy mátrixok közötti egyenlőtlenségek elemenként értelmezendők. Az $m \times n$-es $\mathbf{A}$ mátrix oszlopai által kifeszített alteret $\mathbb{R}^m$-ben, azaz $\{\mathbf{A}\mathbf{x}: \mathbf{x} \in \mathbb{R}^n\}$-t, $\operatorname{span}(\mathbf{A})$ jelöli.

Egyváltozós $f(t)$ függvény közönséges deriváltját $df/dt$ vagy $f'(t)$ jelöli. Több változóban értelmezett függvény — például $u(x,y)$ — parciális deriváltjait $\partial u/\partial x$ alakban, vagy egyes szövegkörnyezetekben alsó indexszel, például $u_x$ alakban jelöljük. A gradiensvektorok, a Jacobi-mátrixok és a Hesse-mátrixok jelölését szükség szerint vezetjük be. Minden logaritmus természetes alapú (alap $e \approx 2.718$), hacsak más alapot kifejezetten nem jelölünk. A $\approx$ szimbólumot hagyományos értelemben vett közelítő egyenlőségre, a $\cong$ szimbólumot pedig kifejezetten legkisebb négyzetes közelítésekre tartjuk fenn.

A numerikus algoritmusok számítási költségét, avagy számítási komplexitását általában a szükséges aritmetikai műveletek számával mérjük. Hagyományosan a numerikus analízisben csak a szorzásokat számolták (esetleg az osztásokat és négyzetgyökvonásokat is), mert a szorzás általában lényegesen drágább volt az összeadásnál vagy kivonásnál, és mert a legtöbb algoritmusban a szorzások jellemzően hasonló számú összeadással párosulnak (például két vektor belső szorzatának számításánál). Újabban az összeadás és a szorzás közötti költségkülönbség nagyrészt eltűnt (sőt, sok modern mikroprocesszor egyetlen szorzás-összeadás utasítással el tudja végezni a kapcsolt szorzást és összeadást). A számítógépgyártók és -felhasználók szeretik a legmagasabb lehetséges teljesítményt hirdetni, ezért egyre gyakoribb, hogy minden egyes aritmetikai műveletet számolnak. Mivel azonban egyes műveletszámok nagyon jól ismertek a hagyományos gyakorlat szerint, ebben a könyvben rendszerint csak a szorzásokat számoljuk. Az értelem egyértelművé tétele végett hozzátesszük a „és hasonló számú összeadás” fordulatot, vagy külön jelezzük, ha mindkét műveletet számoljuk.

A műveletszám és a közelítések pontosságának számszerűsítéséhez gyakran a „nagy O” jelölést használjuk egy függvény nagyságrendjének, illetve domináns tagjának megadására. Műveletszám esetén arra vagyunk kíváncsiak, hogyan viselkedik a függvény, ha a feladat mérete — mondjuk $n$ — nagy lesz. Azt mondjuk, hogy

$$f(n) = \mathcal{O}(g(n))$$

(„$f$ nagy O-ja $g$-nek”, vagy „$f$ $g$ nagyságrendű”), ha létezik olyan $C$ pozitív állandó, amelyre

$$|f(n)| \le C|g(n)|$$

minden elég nagy $n$-re teljesül. Például

$$2n^3 + 3n^2 + n = \mathcal{O}(n^3),$$

mert ahogy $n$ nagy lesz, az $n^3$-nál kisebb rendű tagok relatíve jelentéktelenné válnak. Pontossági becslésnél egy olyan $h$ mennyiség (például egy lépésköz vagy rácstávolság) kicsivé válását vizsgáljuk. Azt mondjuk, hogy

$$f(h) = \mathcal{O}(g(h)),$$

ha létezik olyan $C$ pozitív állandó, amelyre

$$|f(h)| \leq C|g(h)|$$

minden elég kicsi $h$-ra teljesül. Például

$$\frac{1}{1-h} = 1 + h + h^2 + h^3 + \dots = 1 + h + \mathcal{O}(h^2),$$

mert ahogy $h$ kicsi lesz, a $h^2$-en túli elhagyott tagok relatíve jelentéktelenné válnak. Vegyük észre, hogy a két definíció ekvivalens, ha $h = 1/n$.
