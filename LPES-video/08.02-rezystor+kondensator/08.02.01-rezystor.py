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
	{ 'title': [ "#08.2", "Rezystor i ", "kondensator", "" ] },
	
	{ 'comment': 'rezystor' },
	{
		'image': [
			[0.0, eduMovie.convertFile("rezystor.sch", negate=True)],
		],
		'text' : [
			'Mianem elementów biernych określamy takie elementy dla których <m> spełnione jest prawo Ohma, bądź jego uogólnienia dla prądów przemiennych, <m> oczywiście z granicą stałości temperaturowej parametrów danego elementu. <m>'
			
			'Podstawowym takim elementem jest opornik, zwany też rezystorem, <m> jest to taki element który w najlepszym stopniu ze wszystkich innych elementów <m> spełnia nam prawo Ohma, <m>'
				'ponieważ jego ideą jest reprezentować właśnie tą oporność w obwodzie. <m>'
			'Rezystor wprowadzony w obwód wprowadza do niego jakąś rezystancję, <m> inaczej opór, związany ze swoją wartością nominalną. <m>'
			'Wartość oporu wyrażamy w omach - najczęściej są to setki omów lub kilo omy. <m>'
			
			'Na ekranie widzimy też symbol rezystora w obu notacjach, <m> czyli tak zwanej europejskiej i amerykańskiej. <m>'
			'Należy zaznaczyć że ten amerykański zygzaczek nie może być zaokrąglony, <m> musi mieć ostre zęby, bo inaczej zacząłby przypominać symbol innego elementu. <m>'
			
			'Rezystor często służy do ograniczenia wartości prądu <m> przepływającego w obwodzie, bo jak wprowadzamy większy opór <m>'
				'to przy stałym napięciu maleje nam prąd płynący w takim obwodzie, <m> co wynika z prawa Ohma. <m>'
			
			'Na ogół większość układów elektronicznych rozważamy właśnie <m> z punktu widzenia napięciowego (a rzadziej prądowego), <m>'
				'czyli to wartość napięcia ma charakter pierwotny, <m> a prąd jest wynikowym tej wartości i wartości elementów w układzie. <m>'
			'W takich przypadkach rezystor ogranicza prąd <m> – im większa rezystancja tym mniejszy prąd. <m>'
			
			'Są jednak układy w których to wartość prądu jest pierwotna, <m> a napięcia wynikają z niej i wartości elementów. <m>'
			'W tych przypadkach rezystor służy do uzyskania <m> spadku napięcia proporcjonalnego do płynącego prądu. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('moc.tex', margins=12, dpi=260, viaCairo=True)],
		],
		'text' : [
			'Jako że potencjały tożsame są z pracą <m> związaną z przenoszeniem ładunku do nieskończoności, <m> to ze spadkiem napięcia związana jest pewna różnica energetyczna. <m>'
			'Jako że mamy prawo zachowania energii, to ta energia gdzieś musi się podziać. <m>'
			'W związku z czym taki rezystor zamienia nam tą energię prądu elektrycznego <m> na ciepło zgodnie z zależnością, że moc to jest napięcie razy prąd. <m>'
			
			'Możemy też powiedzieć że to jest <m> napięcie w kwadracie podzielone przez rezystancję takiego rezystora <m> lub prąd w kwadracie pomnożony przez oporność takiego rezystora. <m>'
			'Warto zauważyć że o ile przy stałym napięciu jeżeli zwiększamy rezystancję <m> to moc wydzielona na takim rezystorze będzie malała, <m>'
				'to przy stałym prądzie jeżeli zwiększamy rezystancję <m> to moc wydzielana będzie rosła. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('rezystory.svg', margins=0)],
		],
		'text' : [
			'Rzeczywisty rezystor oprócz samej rezystancji posiada też inne parametry. <m>'
			'Jednym z nich jest maksymalna moc, która może się na tym elemencie wydzielić. <m>'
			'Na przykład jeżeli mamy mały rezystorek, stosowany powszechnie <m> w układach elektronicznych, to nie jesteśmy w stanie wydzielić na nim <m> kilowatów energii elektrycznej, ponieważ on się po prostu spali. <m>'
			
			'Na ogół dla takich powszechnie używanych rezystorów <m> maksymalna moc wydzielana jest poniżej połówki wata. <m>'
			'Bardzo często są to rezystory <0,25>[jedna czwarta] wata, niekiedy <0,5>[jedna druga] lub <0,75>[trzy czwarte] wata. <m>'
			'Zasadniczo powyżej jednego, czy nawet pół wata mówimy o rezystorach dużej mocy <m> i wtedy na schemacie oprócz rezystancji danego elementu często podaje się to <m>'
				'jaka powinna być maksymalna moc która może się na nim wydzielić, <m> gdyż wymaga to zastosowania elementu niestandardowego. <m>',
			
			'Kolejnym parametrem jest dokładność, czyli to jak bardzo <m> opór konkretnego elementu może odbiegać od wartości nominalnej. <m>'
			'Jeżeli mówimy że rezystor ma na przykład 1000 Omów, <m> to rzeczywiście wyprodukowane elementy nie będą miały dokładnie 1000 Omów, <m> tylko będą bliskie tej wartości <m>'
				'i dokładność mówi nam jak bliskie tej wartości powinny być. <m>'
			'Na ogół jest to około pięciu procent, jeżeli wymagamy większej dokładności <m> to również takie rzeczy oznaczane są na schemacie albo w wykazie elementów. <m>',
			
			'Innym aspektem również powiązanym poniekąd z dokładnością danego elementu <m> jest stabilność oporu w funkcji temperatury oraz w funkcji przyłożonego napięcia. <m>'
			'Typowo chcemy aby opór nie zależał znacznie od tych parametrów. <m>'
			'Niekiedy jednak w elektronice stosuje się elementy, <m> których rezystancja celowo zależy od temperatury. <m>'
			'Mają one dobrze określoną charakterystykę oporu w funkcji temperatury <m> i to może być zarówno charakterystyka rosnąca, malejąca, jak też nie liniowa, <m>'
				'czyli opór danego elementu może rosnąć wraz z temperaturą, może maleć <m> albo może zmienić się dość gwałtownie <m> przy przekroczeniu pewnej krytycznej temperatury. <m>'
			'Są to różnego rodzaju termistory. <m>'
			
			'Takie o charakterystyce liniowej służą często do pomiaru temperatury. <m>'
			'Natomiast elementy których opór rośnie, a powyżej pewnej temperatury bardzo <m> gwałtownie osiąga duże wartości mogą być używane jako bezpieczniki termiczne, <m>'
				'gdyż taki element wraz z przepływem dużego prądu nagrzewa się, <m> co powoduje wzrost oporu i ograniczenie tego prądu <m> lub całkowite wyłączenie gdy temperatura wzrośnie powyżej granicznej. <m>'
			'Po ostygnięciu zaczyna przewodzić ponownie.  <m>'
			'Stosuje się także elementy których opór zmienia się <m> (i to dość gwałtownie) z napięciem do nich przyłożonym. <m>'
			'Są to warystory, używane niekiedy jako zabezpieczenia przepięciowe. <m>',
			
			'Produkowane i stosowane są także rezystory o nastawnej rezystancji, <m> nazywane potencjometrami lub rezystorami nastawnymi. <m>'
			'Są one wykorzystywane do ustawiania jakiś wartości <m> w procesie kalibracji urządzenia lub do wprowadzania analogowej <m> wartości przez użytkownika w trakcie działania urządzenia. <m>'
			'Na przykład w ten sposób odbywa się odczyt wychylenia joystików, <m> czy też kierownic używanych w grach komputerowych. <m>'
		]
	},
	{
		'image': [
			[0.0,        eduMovie.circuitjs("dzielnik", 0, 6)],
			["out3v",    eduMovie.circuitjs("dzielnik", 4, 6,  [("setSlider", 2, 1)])],
			["load1k",   eduMovie.circuitjs("dzielnik", 4, 6,  [("switch", 510, 300)])],
			["load100",  eduMovie.circuitjs("dzielnik", 4, 6,  [("switch", 600, 300)])],
			["proporcj", eduMovie.circuitjs("dzielnik", 4, 10, preActions = [("setSlider", 2, 1), ("setSlider", 1, 0)], actions = [
					("setSlider", 1, 0.1), ("wait", 0.7), ("setSlider", 1, 0.2), ("wait", 0.7), ("setSlider", 1, 0.4), ("wait", 0.7), ("setSlider", 1, 0.7), ("wait", 0.7), ("setSlider", 1, 1.0)
			])],
		],
		'text' : [
			'Jednym z najistotniejszych układów złożonych z samych rezystorów <m> jest rezystancyjny dzielnik napięcia. <m>'
			'Są to dwa rezystory połączone ze sobą w szereg <m> i podłączone typowo do jakiegoś źródła napięcia. <m>'
			'Czyli tak jak widzimy w lewej gałęzi symulacji pokazanej na ekranie. <m>'
			'W efekcie między tymi rezystorami mamy napięcie <m> związane ze stosunkiem ich rezystancji. <m>'
			'W pokazanym przykładzie są one równe sobie, <m> zatem mamy tam połowę napięcia zasilania, czyli 6 woltów. <mark name="out3v" />'
			
			'Jeżeli wartość górnego zmienimy na przykład na 1500, <m> to będziemy mieli podział napięcia zasilania w proporcjach <1/4>[jedna czwarta] do <3/4>[trzech czwartych]. <m>'
			'Czyli napięcie wyjściowe wyniesie 3 wolty. <m>'
			'Dzieje się tak dlatego że prąd płynący przez oba rezystory jest taki sam <m>'
				'(i równy prądowi jaki płynąłby przez opornik o rezystancji równej sumie ich rezystancji), <m> a przy stałym prądzie większe napięcie odkłada się na większej rezystancji. <m>'
			'Czyli na górnym, większym rezystorze mamy spadek dziewięciu woltów. <m>'
			
			'W dzielniku suma rezystancji określa prąd płynący w takiej gałęzi, <m> a poszczególne rezystancje określają nam spadki napięcia na sobie. <m>'
			'Oczywiście suma tych spadków musi być równa napięciu przyłożonemu do dzielnika, <m>'
				'w efekcie napięcie wyjściowe na dzielniku zależy tylko od <m> stosunku rezystancji i napięcia wejściowego, <m> a nie zależy od łącznej rezystancji tego dzielnika. <mark name="load1k" />'
			
			'Układ taki może być używany jako źródło jakiegoś napięcia. <m>'
			'Wadą takiego źródła napięcia, jest to, że <m> napięcie wyjściowe mocno zależy od obciążenia. <m>'
			'Jeżeli na przykład ten dzielnik obciążymy rezystorem jedno kiloomowym, <m> to napięcie na wyjściu spadło do 4.8 wolta, <m> a jest to rezystancja porównywalna z rezystancją naszego dzielnika. <mark name="load100" />'
			
			'Jeżeli obciąży my ten dzielnik jeszcze mniejszym oporem, <m> na przykład 100 omów to napięcie spada już poniżej dwóch woltów. <m>'
			
			'Czyli dzielnik jest dosyć dobry jako źródło napięcia, <m> ale nie możemy z niego pobierać dużego prądu i dlatego nie jest on stosowany <m> w układach zasilania bezpośrednio jako źródło napięcia. <m>'
			'Natomiast dość często stosowany jest do proporcjonalnego podziału napięcia, <m> obniżenia jakiegoś napięcia którego wielkości nie znamy. <mark name="proporcj" />'
			
			'Na przykład zakładamy że napięcie może być od zera do 24 woltów, <m> a my chcemy mieć napięcie które jest do niego proporcjonalne, <m>'
				'ale w zakresie od zera do sześciu woltów <m> (np. aby je mierzyć miernikiem o takim zakresie). <m>'
			'Dobierając odpowiednio wartości rezystorów tworzących dzielnik <m> możemy to napięcie obniżyć zachowując proporcjonalność do napięcia wejściowego. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("pullup", 0, 1)],
			["pullup", eduMovie.circuitjs("pullup", 1, 7,  [
				("longClick", 340, 360, 1.5), ("wait", 0.7), ("longClick", 340, 360, 1.5),
			])],
			["pulldown", eduMovie.circuitjs("pullup", 1, 4,  [
				("longClick", 610, 260, 1.5)
			])],
		],
		'text' : [
			'Rezystor jest też często używany w celu wymuszenia <m> domyślnego poziomu napięcia na jakiejś linii. <m>'
			'Jest to zasadniczo forma dzielnika, w którym jeden z rezystorów <m> został zastąpiony jakiegoś rodzaju przełącznikiem, <m>'
				'czyli czymś co w zależności od swojego stanu ma <m> prawie zerową albo prawie nieskończoną rezystancję. <m>'
			
			'Ma to zastosowanie głównie na jakiś liniach sygnalizacyjnych, <m> z których nie jest pobierany żaden większy prąd. <mark name="pullup" />'
			'W efekcie w układzie takim jeżeli styk jest rozwarty to prąd nie płynie, <m> zatem spadek na rezystorze wynosi zero i na wyjściu mamy napięcie zasilania. <m>'
			'Jeżeli styk zostanie zwarty prąd płynie, ale ze względu na małą rezystancję <m> styku praktycznie całe napięcie odkłada się na rezystorze <m> i na wyjściu mamy zero voltów. <m>'
			
			'Układ taki pozwala na przykład stosowanie zwykłego styku zwiernego <m> zamiast przełączalnego i jest bardzo często spotykany. <mark name="pulldown" />'
			'Oczywiście możemy zamienić rezystor z przełącznikiem miejscami <m> i wtedy domyślnym stanem (przy rozwartym styku) będzie zero woltów. <m>'
			
			'Wadą takiego rozwiązania jest ograniczenie prądu który może być pobierany <m> z wyjścia i spadek napięcia wraz ze wzrostem tego prądu oraz straty energii. <m>'
		]
	},
]
