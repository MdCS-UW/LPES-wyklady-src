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
	{ 'title': [ "#08.5", "", "Tranzystory", "" ] },
	
	{ 'comment': 'bipolarne' },
	{
		'image': [
			[0.0, ""],
			["symbole", eduMovie.convertFile("bipolarne_symbole.sch", negate=True)],
			["wzory", eduMovie.convertFile("wzór.tex", margins=12, viaCairo=True, negate=True)],
		],
		'text' : [
			'Kolejnym elementem półprzewodnikowym, <m> który także nie spełnia prawa Ohma, jest tranzystor. <m>'
			'Jest to element o regulowanym elektrycznie przewodzeniu prądu. <m>'
			'Czyli można powiedzieć że opór tego elementu możemy regulować elektrycznie <m> przy pomocy przyłożenia pomiędzy dwoma jego wyprowadzeniami jakiegoś napięcia, <m> bądź przepuszczenia tamtędy prądu. <m>'
			'Często wykorzystywany jest do wzmacniania sygnałów <m> lub jako przełącznik elektroniczny, nazywany też kluczem tranzystorowym. <m>'
			
			'Klucz jest układem przełączającym wykorzystującym dwa <m> skrajne tryby pracy tranzystora, <m>'
				'czyli stan zatkania (tranzystor praktycznie nie przewodzi) <m> i nasycenia (tranzystor przewodzi z minimalnymi ograniczeniami, <m> minimalnym spadkiem napięcia na nim). <m>'
			
			'Istnieje wiele rodzajów tranzystorów i dużo dużo więcej konkretnych modeli, <m> różniących się poszczególnymi parametrami. <mark name="symbole" />'
			
			'Na początek powiemy o tranzystorach <bipolarnych>[bi-polarnych], <m> które występują w dwóch odmianach – NPN i PNP. <m>'
			'Symbole tych tranzystorów przedstawione są na ekranie. <m>'
			'Każdy z nich ma 3 wyprowadzenia – emiter, bazę i kolektor, <m> oznaczone tutaj dodatkowo literami E, B i C. <m>'
			'Wyprowadzenie rysowane jako prostopadłe do innych to baza, <m> wyprowadzenie oznaczone strzałką to emiter, <m> a to trzecie to kolektor. <m>'
			'Kierunek strzałki pokazuje kierunek przepływu prądu przez emiter <m> i jednocześnie oznacza typ tranzystora – w NPN prąd wypływa emiterem, <m> w PNP prąd wpływa emiterem. <mark name="wzory" />'
			
			'W przypadku tranzystorów <bipolarnych>[bi-polarnych] (NPN lub PNP) <m> prąd kolektora jest funkcją prądu bazy. <m>'
			'To właśnie przy pomocy ustawienia wartości prądu bazy <m> możemy regulować przewodzenie takiego tranzystora. <m>'
			'Prąd kolektora jest beta razy większy od prądu bazy. <m>'
			'Współczynnik beta, często oznaczany jest jako HFE <m> i jest cechą charakterystyczną dla danego tranzystora. <m>'
			'W przypadku tranzystora NPN prąd bazy wpływa bazą a wypływa emiterem, <m> natomiast w przypadku tranzystora PNP wpływa emiterem i wypływa bazą. <m>'
			'Prąd emitera jest sumą prądów kolektora i bazy. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("npn_pnp.sch")],
		],
		'text' : [
			'Tranzystor zarówno w funkcji klucza jak i w pracy liniowej <m> (wzmacniania sygnału) współpracuje z jakimś obciążeniem, <m> oznaczonym na widocznych schematach jako rezystor R load. <m>'
			'W przypadku tranzystorów NPN typowo jest ono dołączane <m> pomiędzy biegun dodatni zasilania a kolektor, <m> natomiast w przypadku PNP pomiędzy kolektor a biegun ujemny zasilania. <m>'
			'Nie są to jedyne możliwe układy pracy tranzystora, ale najczęściej stosowane. <m>'
			
			'W takim układzie spadek napięcia na tranzystorze jest wynikową <m> rezystancji obciążenia, napięcia zasilania i właśnie wartości prądu kolektora, <m> który jest jednocześnie prądem obciążenia. <m>'
			'Obliczyć go możemy obliczając najpierw prąd kolektora <m> (w oparciu o prąd bazy i wartość bety), <m>'
				'następnie spadek napięcia na obciążeniu <m> (w oparciu o jego rezystancję i prąd kolektora) <m> i odejmując go od wartości napięcia zasilania. <m>'
			'Wartość tego spadku napięcia nie może być mniejsza niż 0.2 wolta. <m>'
			'Jeżeli w wyniku obliczeń uzyskalibyśmy spadek na takim lub niższym poziomie <m> oznacza to że tranzystor pracuje w stanie nasycenia <m> i wtedy spadek ten wynosi właśnie 0.2 wolta. <m>'
			
			'Jeżeli zależy nam aby tranzystor pracował w stanie nasycenia <m> to dobieramy taką wartość prądu bazy, <m>'
				'aby obliczony w oparciu o niego prąd kolektora znacznie przekraczał <m> prąd obciążenia podłączonego bezpośrednio do zasilania. <m>'
			
			'Jeżeli chcemy żeby tranzystor NPN pracował w stanie zatkania <m> to na jego bazę należy podać potencjał emitera lub mniejszy od niego, <m> tak żeby prąd bazy nie płynął. <m>'
			'W ten sposób prąd kolektora też wynosi 0 i tranzystor nie przewodzi. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("npn", 0, 6)],
			["npn_zatk - 4", eduMovie.circuitjs("npn", 4, 6, [("switch", 360, 340)])],
			["npn_bez_rezystora1 - 3", eduMovie.circuitjs("npn", 3, 2, [("switch", 460, 410)], [("switch", 360, 340)])],
			["npn_bez_rezystora2 - 1.5", eduMovie.circuitjs("npn", 3, 2, [("switch", 460, 410)])],
		],
		'text' : [
			'Na ekranie widzimy symulację układu z tranzystorem NPN. <m>'
			'Aktualnie tranzystor jest w stanie nasycenia – mamy na nim <m> spadek niecałych dwóch dziesiątych wolta, <m> a płynący prąd wynika z napięcia zasilania i wielkości rezystora obciążenia. <m>'
			'Nie jest regulowany przez tranzystor, <m> który przy takich parametrach mógłby przepuścić znacznie więcej prądu. <mark name="npn_zatk" />'
			
			'Jeżeli podamy na bazę 0 woltów <m> to wprowadzimy tranzystor stan zatkania <m> – prąd prawie nie płynie, mamy tu jakieś ułamki piko ampera. <m>'
			
			'Należy zwrócić uwagę że zastosowanie rezystora <m> podłączonego do bazy jest tutaj konieczne. <m>'
			'Wynika to z tych samych przyczyn, <m> z których konieczne stosowanie było rezystora przy diodach. <m>'
			'Można powiedzieć że pomiędzy bazą a emiterem mamy <m> diodę w kierunku przewodzenia (złącze p-n) i ta dioda w stanie przewodzenia <m> chce mieć spadek około 0.6 wolta, <m>'
				'więc nie możemy przyłożyć bezpośrednio trzech woltów. <mark name="npn_bez_rezystora1" />'
			
			'Możemy przyłożyć bezpośrednio masę, bo wtedy prąd nie płynie. <mark name="npn_bez_rezystora2" />'
			
			'Ale jeżeli przyłożyli byśmy tutaj bezpośrednio jakiś potencjał większy <m>, to wtedy jak widzimy prądy nam rosną katastrofalnie <m>'
				'<–>[.] w symulacji doszliśmy do jakichś milionów zeta amperów, <m> po czym symulator się zatrzymał. <m>'
			'Oczywiście w rzeczywistym układzie tyle nie osiągniemy, <m> ponieważ źródło ma jakąś skończoną wydajność prądową, <m>'
				'a tranzystor uległby zniszczeniu już przy znacznie mniejszych wartościach. <m>'
			'Jednak dobrze obrazuje to że takie podłączenie nie jest dobrym pomysłem. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("npn", 0, 9, [
				("setSlider", 3, 0.2), ("wait", 1.3), ("setSlider", 3, 0.4), ("wait", 1.3), ("setSlider", 3, 0.6), ("wait", 1.3), ("setSlider", 3, 0.8)
			])],
			["npn_wzmac", eduMovie.circuitjs("npn", 2, 26, [
				("setSlider", 1, 0.3), ("wait", 0.7), ("setSlider", 1, 0.25), ("wait", 0.7), ("setSlider", 1, 0.2), ("wait", 0.7), ("setSlider", 1, 0.15), ("wait", 1.7),
				# zwiększamy ...
				("setSlider", 3, 0.2), ("wait", 1.3), ("setSlider", 3, 0.3), ("wait", 1.3), ("setSlider", 3, 0.4), ("wait", 1.3), ("setSlider", 3, 0.5),
				("setSlider", 3, 0.6), ("wait", 1.3), ("setSlider", 3, 0.7), ("wait", 1.3), ("setSlider", 3, 0.8), ("wait", 1.3), ("setSlider", 3, 0.9),
				# i w drógą stronę ...
				("wait", 1.3), ("setSlider", 3, 0.8), ("wait", 1.3), ("setSlider", 3, 0.7), ("wait", 1.3), ("setSlider", 3, 0.6), ("wait", 1.3), ("setSlider", 3, 0.5)
			])],
		],
		'text' : [
			'Jeżeli jesteśmy w stanie nasycenia to zmiana wartości prądu bazy, <m> dopóki nie spowoduje wyjścia z tego trybu, <m> nie wpływa na prąd kolektora, czyli prąd płynący przez nasze obciążenie. <m>'
			
			'Oczywiście napięcie podawane na bazę nie musi być niższe od napięcia <m> zasilającego obciążenie, ale może być, co jest często wykorzystywane. <m>'
			'Tranzystorem NPN możemy przełączać wyższe napięcia, <m> niż te na których operuje układ sterujący. <mark name="npn_wzmac" />'
			
			'Jeżeli zmniejszymy rezystancję obciążenia to widzimy, <m> że od pewnego momentu (od około 26 miliamper) jej dalsze zmniejszenie <m> nie wpływa na prąd płynący przez tranzystor. <m>'
			'Wyszliśmy z zakresu nasycenia i teraz modyfikując prąd bazy możemy zmieniać <m> prąd obciążenia i widzimy że jest on stu krotnie większy od prądu bazy, <m> gdyż beta symulowanego tranzystora wynosi 100. <m>'
			
			'Układ ten działa teraz jako wzmacniacz, <m> czyli prąd kolektora jest wzmocnionym prądem bazy. <m>'
			'Stosowanie tego układu w roli wzmacniacza jest możliwe, <m> natomiast jest praktycznie nie stosowane, ze względu na to, <m> iż wzmocnienie wyznacza tutaj parametr beta. <m>'
			'Unika się takiego rozwiązania gdyż parametr beta po pierwsze posiada <m> gigantyczny rozrzut pomiędzy egzemplarzami tranzystorów konkretnego modelu, <m> dodatkowo nie jest zbytnio stabilny w funkcji temperatury i tak dalej. <m>'
			'Ogólnie beta potrafi się zmieniać i nie należy opierać się na założeniu <m> że wynosi ona dokładnie ileś, tylko że zawiera się <m> w dość szerokim przedziale (np. od stu do sześciuset). <m>'
			
			'W związku z tym tego typu układy z jednym rezystorem bazy używane są <m> niemal wyłącznie w trybie pracy klucza, <m> który korzysta jedynie ze stanów nasycenia i zatkania. <m>'
			'Na potrzeby takiej pracy wartość rezystora bazy dobierana jest w ten sposób, <m> żeby na pewno operować w zakresach nasycenia i zatkania, <m>'
				'bez względu na rozrzut produkcyjny oraz niestabilność temperaturową bety <m> oraz ewentualne wahania rezystancji obciążenia. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("pnp", 0, 6)],
			["pnp_nasycenie - 16", eduMovie.circuitjs("pnp", 13, 6, [("switch", 340, 250)])],
			["pnp_rezystor", eduMovie.circuitjs("pnp", 3, 6, [("switch", 460, 310), ("wait", 3.0), ("switch", 340, 250)])],
			["pnp_wzmac - 1.1", eduMovie.circuitjs("pnp", 3, 16, preActions=[("switch", 340, 250)], actions=[
				("setSlider", 2, 0.0), ("wait", 1.3),
				("setSlider", 3, 0.2), ("wait", 1.3), ("setSlider", 3, 0.3), ("wait", 1.3), ("setSlider", 3, 0.4), ("wait", 1.3), ("setSlider", 3, 0.5),
				("setSlider", 3, 0.6), ("wait", 1.3), ("setSlider", 3, 0.7), ("wait", 1.3), ("setSlider", 3, 0.8), ("wait", 1.3), ("setSlider", 3, 0.98)
			])],
		],
		'text' : [
			'Drugim typem tranzystorów <bipolarnych>[bi-polarnych] jest tranzystor PNP, <m> który jest poniekąd takim trochę lustrzanym odbiciem, <m> czy też symetrycznym partnerem dla tranzystora NPN. <m>'
			
			'W tranzystorze NPN prąd wpływał bazą a wypływał emiterem, w PNP prąd wypływa bazą i jest podkradany z prądu emitera. <m>'
			'W obu wypadkach prąd emitera to jest suma prądu bazy i prądu kolektora. <m>'
			
			'Jeżeli chcemy zatkać tranzystor PNP to należy podać mu na bazę <m> napięcie zasilania lub wyższe – wtedy prąd bazy nie płynie, <m> więc nie płynie też prąd kolektora. <m>'
			'Tak jak widzimy to obecnie na symulacji. <m>'
			'Jeżeli chcemy go wprowadzić do przewodzenia to podajemy mu napięcie niższe, <mark name="pnp_nasycenie" /> oczywiście z użyciem jakiegoś rezystora w celu ograniczenia prądu bazy. <m>'
			
			'Potencjał bazy wprowadzający tranzystor w stan przewodzenia <m> musi być jedynie o niecały wolt niższy od potencjału emitera <m> (w tranzystorze NPN musiał być wyższy) <m>'
				'i nie ma przeszkód aby tym napięciem było zero woltów czyli masa. <mark name="pnp_rezystor" />'
			
			'W tym układzie bazę możemy podłączyć bezpośrednio do napięcia zasilania <m> (celem zatkania tranzystora), <m> ale jeżeli chcemy ją podłączyć do napięć niższych konieczny jest rezystor. <mark name="pnp_wzmac" />'
			
			'Analogicznie jak w przypadku tranzystora NPN jeżeli zmodyfikujemy wartość <m> rezystancji obciążenia lub rezystora bazy możemy przejść w zakres pracy liniowej <m>'
				'i widzimy że także tutaj prąd kolektora jest funkcją prądu bazy <m> i jest stu krotnie większy, czyli beta tego tranzystora również wynosi 100. <m>'
		]
	},
]
