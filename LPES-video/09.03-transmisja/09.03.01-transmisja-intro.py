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
	{ 'title': [ "#09.3", "Transmisja", "danych", "" ] },
	
	{ 'comment': 'transmisja - intro' },
	{
		'image': [
			[0.0, eduMovie.convertFile('enkoder.svg', negate=True)],
			["dekoder", eduMovie.convertFile('dekoder.svg', negate=True)],
			["matrix", eduMovie.circuitjs("matrix", 1, 36, [
				("longClick", 430, 100, 1.5), ("wait", 1), ("longClick", 560, 100, 1.5), ("wait", 1), ("longClick", 690, 100, 1.5), ("wait", 1), # pierwszy rząd
				("longClick", 430, 235, 1.5), ("wait", 1), ("longClick", 560, 235, 1.5), ("wait", 1), # trzeci rząd
				("click", 160, 330), ("wait", 1), ("click", 190, 330), ("wait", 1), ("click", 160, 330), ("wait", 1), # aktywacja różnych rzędów ... kończymy na trzecim
				("longClick", 430, 235, 1.5), ("wait", 1), ("longClick", 560, 235, 1.5), ("wait", 1), ("longClick", 690, 235, 1.5)
			])],
		],
		'text' : [
			'Rejestry szeregowe nie są jedynymi układami, <m> które pozwalają na redukcję ilości linii. <m>'
			'Innym przykładem tego typu układów są enkodery i dekodery. <m>'
			'Stosowane są one w sytuacji kiedy z jakiś względów zakładamy, że spośród n <m> jakiś linii tylko jedna w danym momencie ma prawo, powinna być aktywna. <m>'
			
			'Enkoder <n>[eN] do <m>[eM] posiada <n>[eN] wejść i m-bitowe wyjście. <m>'
			'Na wyjściu tym wystawia zakodowany binarnie numer wejścia które jest aktywne, <m> czyli w enkoderach aktywowanych stanem wysokim ma stan wysoki, <m> a w aktywowanych stanem niskim, z wejściami zanegowanymi, ma stan niski. <m>'
			'Typowo są to układy priorytetowe, czyli jeżeli mimo wszystko kilka wejść <m> będzie aktywnych to wystawiony zostanie numer jednego z nich <m> – w zależności od użytego układu tego z najniższym lub najwyższym numerem. <m>'
			'Układ taki często posiada dodatkowe wyjście sygnalizujące, <m> że żadne z wejść nie jest w stanie aktywnym lub reprezentowane jest to <m> jakąś wartością w wystawianym kodzie binarnym. <m>'
			
			'Numer aktywnego wejścia na ogół podawany jest w NKB, <m> w niektórych układach mogą jednak być użyte inne kodowania. <mark name="dekoder" /> <m>'
			
			'Odwrotne działanie realizuje dekoder <m>[eM] do <n>[eN]. <m>'
			'Posiada on m-bitowe wejście i <n>[eN] wyjść. <m>'
			'Aktywuje tylko jedno z tych wyjść - to którego numer znajduje się na wejściu. <m>'
			'Aktywacja może oznaczać podanie na tym wyjściu stanu wysokiego, <m> podczas gdy pozostałe mają stan niski <m>'
				'lub (w przypadku dekoderów z zanegowanym wyjściem) podanie stanu niskiego, <m> gdy wszystkie pozostałe są w stanie wysokim. <m>'
			'Dekodery często posiadają dodatkowy sygnał wejściowy <m> zezwalający na aktywację wyjść. <mark name="matrix" />'
			
			'Jednym z zastosowań dla takich układów może być obsługa matrycy przycisków. <m>'
			'Przykład takiej matrycy opartej na dekoderze i enkoderze widoczny jest na symulacji. <m>'
			'Pozwala ona na odczyt 12 przycisków z użyciem jedynie 4 linii <m>'
				'– dwóch wyjściowych (wybierających który rząd przycisków jest czytany) <m> oraz dwóch wejściowych (informujących o tym który z przycisków <m> w wybranym rzędzie został wciśnięty). <m>'
			'Wadą takiej matrycy jest brak możliwości detekcji <m> równoczesnego naciśnięcia kilku przycisków. <m>'
			'W przedstawionym schemacie na wyjściu dekodera dodane zostały rezystory <m> zabezpieczające go przed uszkodzeniem w przypadku <m> równoczesnego wciśnięcia przycisków z kilku linii. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("mux.sch", negate=True)],
			["mux", eduMovie.circuitjs("mux", 1, 10, [
				("switch", 460, 70), ("wait", 0.5), ("switch", 460, 70), ("wait", 0.5), ("switch", 460, 70), # przełączanie linii 1
				("wait", 1), ("switch", 255, 460), ("wait", 1), # przełączenie na 3 linię
				("switch", 460, 70), ("wait", 0.5), ("switch", 460, 70)  # przełączanie linii 1
			])],
			["demux", eduMovie.convertFile("mux.sch", negate=True)],
			["analog_mux", eduMovie.convertFile("mux_analog.sch", negate=True)],
		],
		'text' : [
			'Trochę podobne działanie mają multipleksery i demultipleksery cyfrowe. <m>'
			
			'Multiplekser posiada <n>[eN] wejść, m-bitowe wejście sterujące i jedno wyjście. <m>'
			'Wejście sterujące pełni funkcję analogiczną jak w dekoderze <m> - podajemy na nim numer linii, tyle że nie jest to linia która ma być aktywowana, <m> a linia której stan ma być odzwierciedlony na wyjściu. <mark name="mux" />'
			
			'Tak jak pokazano na ekranie multiplekser można by skonstruować <m> podłączając do każdego wyjścia dekodera bramkę AND z sygnałem wejściowym <m> i łącząc wyjścia tych bramek do jednej bramki OR. <m>'
			'Dekoder wybiera która z bramek jest aktywna i ta bramka (zawsze tylko jedna) <m> przepuszcza swój sygnał na wyjście. <mark name="demux" />'
			
			'Demultiplekser ma działanie odwrotne do multipleksera, <m> czyli stan pojedynczej linii wystawia na wyjście o wskazanym numerze. <m>'
			'Można zauważyć że to prawie to samo co dekoder <m> – on aktywował wyjście o danym numerze, zatem jakby dekoderowi zabronić aktywacji <m> wyjścia gdy linia jest w stanie niskim to uzyskalibyśmy demultiplekser. <m>'
			'I tak się właśnie robi podłączając linie danych do wejścia zezwalającego <m> na aktywację wyjść, które posiada większość dekoderów. <m>'
			'Gdy chcemy używać ich jako dekoderów a nie demultiplekserów wejście to <m> podłączamy do stanu wysokiego. <m>'
			'Z tego względu nie warto szukać osobno układów <m> demultiplekserów cyfrowych i dekoderów. <mark name="analog_mux" />'
			
			'Mamy również multipleksery analogowe, których działanie polega na <m> elektrycznym zwarciu odpowiedniego wejścia z wyjściem, <m>'
				'z wykorzystaniem odpowiedniego układu tranzystorów, <m> w postaci bramek transmisyjnych, o których jeszcze powiemy. <m>'
			
			'W związku z tym ten sam układ może być używany w roli <m> multipleksera jak i demultipleksera, <m> ponieważ przewodzenie sygnału w jego wypadku jest dwukierunkowe. <m>'
			'W odróżnieniu od multipleksera cyfrowego, <m> który zawsze wymusza silny poziom logiczny swojego wyjścia, <m> multiplekser analogowy jest też w stanie przekazać poziom wysokiej impedancji. <m>'
			'Generalnie na multiplekser analogowy należy patrzeć jak na <m> zespół przełączników przełączających nam kable naszej magistrali.  <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("bufory.sch", negate=True)],
			["tristate", eduMovie.convertFile("bramka_transmisyjna.sch", negate=True)],
		],
		'text' : [
			'Oprócz układów kompresujących i dekompresujących ilość linii mamy też <m> bardziej standardowe układy służące sterowaniu linii nazywane buforami. <m>'
			
			'Bufory oznaczamy w postaci trójkąta, takiego jak pokazano na ekranie. <m>'
			'Trójkąt ten wskazuje kierunek przepływu sygnału przez bufor. <m>'
			'Bufory pełnią różne funkcje – mogą służyć do zwiększenia wydajności prądowej <m> wyjścia, do regeneracji sygnału lub wymuszenia kierunku jego podawania. <m>'
			
			'Regeneracja sygnału może być potrzebna w związku z występowaniem <m> zjawisk pasożytniczych nawet na zwykłym kawałku przewodnika <m>'
				'– na przykład kablu (czyli głównie rezystancją i pojemnością tego kabla), <m> które prowadzą do degradacji sygnału zarówno pod względem swojej wielkości, <m> jak i ostrości narastania zboczy. <m>'
			'Warto tutaj zwrócić uwagę iż nawet zwykła bramka NOT będzie regenerować sygnał, <m> gdyż sygnał z wejścia nie przepływa bezpośrednio na wyjście, <m> tylko jest odtwarzany z poziomu zasilania i masy, czyli regenerowany. <m>'
			'Ponadto taka bramka zapewnia też brak możliwości przeniesienia sygnału <m> z wyjścia na wejście ze względu na izolowaną bramkę. <m>'
			'I najprostsze bufory nie odwracające to właśnie <m> dwie połączone szeregowo bramki NOT. <m>'
			
			'Bufory mogą być także stosowane w celu zamiany linii <m> na linię typu open collector lub 3 stanową. <mark name="tristate" />'
			
			'Bufor trójstanowy decyduje o przepuszczeniu lub nie sygnału, <m> podstawą jego działania jest bramka transmisyjna, <m> której schemat widoczny teraz na ekranie. <m>'
			'Jest to zasadniczo jedyna bramka która ma charakter symetryczny <m> – przewodzi sygnał w obie strony i możemy zamienić wejście z wyjściem. <m>'
			'Samodzielnie używana jest w multiplekserach analogowych, <m> a w buforach trójstanowych występuje w kombinacji <m> (np. z jednym lub dwoma bramkami not), <m>'
				'aby zapewnić regenerację sygnału i uniemożliwć przekazywanie go w drugą stronę. <m>'
			
			'Warto zwrócić uwagę że użyte do jej konstrukcji tranzystory mają 4 wyprowadzenia. <m>'
			'Tak naprawdę w technologii MOSFET przewodzenie jest regulowane <m> napięciem pomiędzy bramką tranzystora a podłożem. <m>'
			'Jednak w większości tranzystorów podłoże zwarte jest wewnętrznie <m> do źródła i dlatego mówimy o napięciu bramka źródło. <m>'
			'W tym wypadku jednak aby uzyskać skuteczne dwukierunkowe przewodzenie <m> używamy dwóch tranzystorów przewodzących w różnych kierunkach <m>'
				'i dodatkowo polaryzujemy podłoże z potencjałem <m> napięć zasilających a nie potencjałem sygnału. <m>'
		]
	},
]
