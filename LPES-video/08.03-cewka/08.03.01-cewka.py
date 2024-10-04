# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#08.3", "", "Cewka", "" ] },
	
	{ 'comment': 'cewka' },
	{
		'image': [
			[0.0, ""],
			["stab_cap",   eduMovie.circuitjs("cap_cewka", 4, 26, [
				("switch", 350, 170), ("wait", 2), ("switch", 350, 170),  # stab_cap
				("wait", 14),
				("switch", 740, 170), ("wait", 2), ("switch", 740, 170)   # stab_cewka na tej samej symulacji żeby zachować ciągłość wykreu
			])],
		],
		'text' : [
			'Trzecim i ostatnim z podstawowych elementów biernych jest cewka. <m>'
			'Działa ona trochę podobnie jak kondensator, tyle że nie dla napięcia a dla prądu. <mark name="stab_cap" />'
			'Kondensator magazynował energię w polu elektrycznym <m> i działał stabilizująco na napięcie <m> (można powiedzieć że przeciwstawiał się zmianom napięcia, opóźniał, łagodził je). <m>'
			'Widzimy to w pokazanej na ekranie symulacji - krótkie obniżenie napięcia <m> zasilającego jest wyraźnie łagodzone przez kondensator. <mark name="stab_cewka" />'
			'Cewka magazynuje energię w polu magnetycznym i działa stabilizująco na prąd <m> (można powiedzieć że przeciwstawia się zmianom prądu <m> przez nią płynącego, opóźnia, łagodzi je). <m>'
			'Widzimy to także w pokazanej na ekranie symulacji <m> – spadek prądu w obwodzie spowodowany krótkotrwałym obniżeniem <m> napięcia zasilającego jest wyraźnie łagodzony przez cewkę. <m>'
			
			'Jeżeli naładowany kondensator po prostu odetniemy <m> od obwodu to na nim ten ładunek pozostanie. <m>'
			'Analogicznie jeżeli wypniemy naładowaną cewkę to można powiedzieć <m> że prąd w niej pozostanie – będzie nadal chciał płynąć, <m> co objawi się wzrostem napięcia na cewce. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("cewka.sch", negate=True)],
			["wzor", eduMovie.convertFile('cewka_wzory_1.tex', viaCairo=True, margins=12)],
			["foto1", eduMovie.convertFile('cewki.svg', margins=0)],
		],
		'text' : [
			'Cewkę na schematach przedstawiamy za pomocą symbolu widocznego na ekranie <m> i jej podstawowym parametrem jest indukcyjność. <m>'
			'Indukcyjność wyrażamy w henrach, najczęściej będą to mikro lub mili henry. <m>'
			
			'Samodzielnie występująca jest używana właśnie w celu stabilizacji prądu <m> (w takim sensie w jakim kondensator służy do stabilizacji napięcia). <mark name="wzor" />'
			
			'Podobnie jak w przypadku kondensatora, dla cewki również mamy stałą czasową <m> związaną ze zmianą prądu przez nią płynącego <m> – odpowiednia zależność widoczna jest na ekranie. <mark name="foto1" />'
			
			'Rzeczywiste cewki (tak jak i wcześniej poznane elementy) <m> charakteryzują się pewnymi wielkościami granicznymi oraz pasożytniczymi. <m>'
			'Głównym parametrem dodatkowym dla cewki jest <m> maksymalny prąd jaki może ona przewodzić. <m>'
			'Cewka jest zasadniczo kawałkiem drutu i jeżeli przez nawet zwykły kawałek <m> drutu będziemy chcieli przepuścić za duży prąd to ten drut nam się przepali, <m> tak samo cewka przy za dużym prądzie ulegnie przepaleniu. <m>'
			'Wiele cewek nawijanych jest dosyć cienkim drutem, <m> w związku z tym prądy które mogą one przewodzić niekoniecznie są duże. <m>'
			'Innym istotnym niekiedy parametrem jest rezystancja cewki, <m> związana z rezystancją drutu z którego jest nawinięta, w zależności <m> od danego przypadku ten element pasożytniczy może być pożądany lub szkodliwy. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('przekaźniki.svg', margins=0)],
			["trafo", eduMovie.convertFile('trafo.svg', margins=0)],
		],
		'text' : [
			'Cewki możemy spotkać w urządzeniach bardziej złożonych, <m> takich jak przekaźniki czy styczniki. <m>'
			'Tak naprawdę pod względem idei działania przekaźnik i stycznik to jest to samo <m> urządzenie oparte o elektromagnes który przełącza jakiś styk. <m>'
			'Natomiast przyjęło się rozróżnianie tych elementów na zasadzie <m> że stycznik używany jest przy większych prądach, a przekaźnik przy mniejszych. <m>'
			'Mogą ale nie muszą iść za tym zmiany konstrukcyjne, <m> związane najczęściej z samymi stykami i zagadnieniem gaszenia łuku. <m>'
			
			'Wspomniany elektromagnes to właśnie cewka <m> (która jak wiemy wytwarza pole magnetyczne) wyposażona w odpowiedni rdzeń. <m>'
			'Służy on do fizycznego przemieszczania jakiegoś elementu łączeniowego, styku. <mark name="trafo" />'
			
			'Innymi urządzeniami opartymi o cewki są transformatory, <m> które wykorzystują kilka cewek na wspólnym rdzeniu <m> do przekazywania energii przez pole magnetyczne. <m>'
			'W najprostszym, jednofazowym wariancie jedna z cewek, <m> dzięki przepływowi zmiennego prądu elektrycznego, <m> wytwarza zmienne pole magnetyczne w innej cewce. <m>'
			'Dzięki temu zmiennemu polu magnetycznemu druga cewka <m> wytwarza zmienny prąd elektryczny. <m>'
			'Transformator typowo służy do zmiany wartości napięcia <m> – zarówno jego obniżenia jak i jego podwyższenia. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('siec_energetyczna.svg')],
			["trafo_separacja", ""], # TODO obrazek / filmik to ilustrujący (?)
		],
		'text' : [
			'Na przykład przy elektrowniach mamy transformatory podwyższające napięcie, <m>'
				'gdyż generator w elektrowniach pracuje na ogół na napięciu <m> rzędu kilku kilowoltów (na przykład <6 kV>[sześciu]), a sieci przesyłowe <m> pracują na napięciu kilkuset kilowoltów (na przykład na <220 kV>[dwustu dwudziestu]). <m>'
			'Następnie im bardziej zbliżamy się do odbiorcy energii elektrycznej, <m>'
				'to mamy kolejne transformatory, tym razem obniżające napięcie najpierw do <m> kilkunastu kilowoltów, a potem do 230 woltów, czyli takiego jakie mamy w domach. <mark name="trafo_separacja" />'
			
			'Oprócz tego transformator może służyć do separacji galwanicznej obwodów, <m> czyli rozdzielenia obwodu pierwotnego od obwodu wtórnego, <m> w taki sposób aby prąd pomiędzy nimi nie mógł przepływać bezpośrednio. <m>'
			'Wykonuje się to nawet pracując na tym samym napięciu, czyli istnieją <m> i są stosowane również transformatory o przekładni jeden do jednego. <m>'
			
			'Separacja taka opiera się na tym, że jeżeli nie zewrzemy w jakiś sposób <m> jednego bieguna strony pierwotnej z jednym biegunem strony wtórnej, <m>'
				'to napięcie wyjściowe (które jest pomiędzy biegunami strony wtórnej), <m> nie ma żadnego odniesienia do napięć strony pierwotnej. <m>'
			'Można zaobserwować że napięcia te pływają względem siebie. <m>'
			
			'Typowo takie połączenie strony pierwotnej i wtórnej realizowane <m> jest poprzez uziemienie jednego z wyprowadzeń każdej ze stron. <m>'
			'W przypadku sieci elektroenergetycznych, które wykorzystują prąd trójfazowy, <m> typowo łączony z potencjałem Ziemi jest punkt neutralny transformatora. <m>'
			'W efekcie w większości naszych domowych gniazdek mamy <m> przewód neutralny (połączony z potencjałem Ziemi) <m> i fazowy (na którym jest napięcie w stosunku co do Ziemi). <m>'
			'Zatem jeżeli chcemy żeby nasze napięcia za transformatorem odnosiły się do <m> potencjału Ziemi to jeden z biegunów również uziemiamy, <m> a jeżeli chcemy żeby transformator był separujący to tego nie robimy. <m>'
			'Pierwsze podejście stosowane jest w większości (prawidłowo zasilonych) <m> komputerów stacjonarnych, a drugie w wielu laptopach. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("cewka", 4, 6, [("switch", 400, 120)])],
			["przep_res_10k", eduMovie.circuitjs("cewka_res", 4, 6, [("switch", 400, 120)])],
			["przep_res_100", eduMovie.circuitjs("cewka_res", 4, 6, [("switch", 400, 120)], preActions = [("setSlider", 2, 0)])],
			["przep_dioda", eduMovie.circuitjs("cewka_dioda", 4, 6, [("switch", 400, 120)])],
		],
		'text' : [
			'Z cewką związane jest zjawisko występujące w momencie przerywania obwodu <m> w którym ta cewka występuje, polegające na wzroście napięcia <m> na niej do bardzo dużych wartości. <m>'
			'Wynika to z wspomnianej już chęci cewki do zachowania przepływu prądu, <m> co stało się niemożliwe z powodu wprowadzonej do obwodu przerwy. <m>'
			
			'Obrazuje to widoczna na ekranie symulacja. <m>'
			'Oprócz cewki dodany jest także rezystor i kondensator <m> (powiedzmy że obrazujące pasożytniczą rezystancję i pojemność cewki) <m> oraz rezystancja wewnętrzna źródła napięcia. <m>'
			'Bez nich symulator nie byłby wstanie dobrze zobrazować tego zjawiska. <m>'
			
			'Widzimy że po przerwaniu obwodu napięcie w naszym symulowanym układzie, <m> zasilanym z 5 woltów, osiąga kilowolty. <m>'
			'Zjawisko to bywa wykorzystywane w przetwornicach impulsowych. <m>'
			'Jednak w wielu układach (np. załączających przekaźniki) <m> jest ono bardzo niepożądane i może prowadzić do przebić <m> i uszkodzeń elementów sterujących cewką. <m>'
			'Dlatego stosuje się układy zapobiegające temu. <mark name="przep_res_10k" />'
			
			'W tym celu możemy na przykład dołączyć do cewki jakiś opornik. <m>'
			'W tej chwili tracimy trochę energii na prąd płynący przez ten rezystor, <m> ale skok napięcia przy rozwarciu obwodu został <m> ograniczony do kilkuset woltów. <m>'
			'Nadal może to być więcej niż byśmy chcieli. <m>'
			'Wynika to z faktu, iż użyliśmy rezystora o dużej wartości oporu, <m> więc wymaga on dużego napięcia aby zachować prąd płynący przez cewkę. <mark name="przep_res_100" />'
			
			'Jeżeli zamienimy ten rezystor na 100 omów to uzyskamy ograniczenie <m> wartości przepięcia do kilku woltów, co może być już akceptowalne. <m>'
			'Jednak nasz układ stał się mało wydajny energetycznie. <m>'
			'Prąd płynący przez rezystor jest porównywalny z prądem płynącym przez cewkę, <m> zatem sporo energii tracimy na rezystorze w trakcie <m> normalnej pracy obwodu (przewodzenia przez cewkę). <m>'
			
			'Po dodaniu rezystora łatwiej zauważyć że po rozłączeniu obwodu <m> napięcie na cewce zmienia znak – przy normalnej pracy mamy tam spadek napięcia, <m> '
				'ale po rozłączeniu obwodu cewka aby wymusić prąd w tym samym kierunku <m> indukuje napięcie w przeciwną stronę <m> (tak aby na niej był wzrost a nie spadek napięcia). <m>'
			'Powoduje to że prąd płynący przez rezystor po rozłączeniu cewki <m> ma inny kierunek niż prąd płynący w trakcie normalnej pracy. <m>'
			'Normalnie na naszej symulacji płynął z góry do dołu, <m> po rozłączeniu przez rezystor płynie z dołu do góry. <m>'
			
			'Jeżeli zamiast rezystora moglibyśmy użyć elementu, <m> który przewodziłby tylko w jednym kierunku <m> to moglibyśmy wyeliminować problem strat. <mark name="przep_dioda" />'
			'Takim elementem jest dioda. <m>'
			'I w rzeczywistości jest powszechnie używana w celu eliminacji przepięć <m> związanych z rozłączaniem cewek przekaźników <itp.>[i tym podobnych] <m>'
			'Aby zabezpieczenie to było skuteczne dioda musi być podłączona <m> anty-równolegle z cewką, czyli do tych samych punktów obwodu co cewka, <m> ale w taki sposób aby podczas gdy cewka jest zasilana nie przewodzić prądu. <m>'
			'Tak jak widzimy to na symulacji. <m>'
		]
	},
]
