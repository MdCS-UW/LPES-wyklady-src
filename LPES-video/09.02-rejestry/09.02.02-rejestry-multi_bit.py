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
	{ 'comment': 'rejestry' },
	{
		'image': [
			[0.0, ""],
			["rejestr1", eduMovie.circuitjs("rejestr1", 0, 1)],
			["rejestr1run", eduMovie.circuitjs("rejestr1", 2, 22, [
				("switch", 380, 50), ("wait", 1.0),
				("switch", 380, 170), ("switch", 380, 170), ("wait", 1.0),
				("switch", 380, 410), ("wait", 2.0),
				("switch", 380, 480), ("wait", 1.0), ("switch", 380, 480), ("wait", 1.0), ("switch", 380, 480), ("wait", 1.0), # CLK ‾‾\_/‾\__
				("switch", 380, 290), ("switch", 380, 410)
			])],
		],
		'text' : [
			'Kolejnym poziomem złożoności układu pamięciowego jest możliwość <m> zapamiętania większych ilości bitów, bo poznane do tej pory układy <m> są w stanie przechować tylko 1 bit. <m>'
			
			'Układy takie złożone są po prostu z większej ilości przerzutników <m> lub zatrzasków i określamy je mianem rejestrów. <m>'
			'Rejestr n bitowy to zespół n przerzutników, rzadziej zatrzasków, <m> aczkolwiek można się spotkać z rejestrami opartymi na zatrzaskach. <m>'
			
			'Często ma on wspólne dla wszystkich wchodzących w jego skład przerzutników, <m> sygnały sterujące typu clock, set, reset i tym podobne. <m>'
			'Wynika to z faktu że jeżeli chcemy zapamiętać n bitów informacji to na ogół <m> chcemy zapamiętać taką n bitową liczbę w jednej, danej chwili, <m>'
				'więc nie ma potrzeby stosowania osobnych sygnałów zegara i tym podobnych. <mark name="rejestr1" />'
			
			'Podstawową formą rejestrów są rejestry równoległe, <m> które działają tak jak na przedstawionej tutaj symulacji. <m>'
			'Całość układu przerzutnika, który oglądaliśmy na wcześniejszej symulacji <m> została zastąpiona pojedynczym symbolem przerzutnika D, <m>'
				'w którym widzimy wejście D, wejście zegarowe <m> (które często oznaczone jest takim trójkącikiem) i dwa wyjścia q i nie q. <mark name="rejestr1run" />'
			
			'Jak widać bez względu na to jak się zmieniają sygnały na wejściach <m> w czasie gdy zegar jest w stanie wysokim lub niskim, wyjście nie zmienia się. <m>'
			'Stan wyjść odzwierciedla stan wejść w momencie <m> przejścia sygnału zegarowego ze stanu niskiego na wysoki. <m>'
			'Czyli tym razem mamy rejestry reagujące na zbocze narastające, <m> a nie na opadające jak poprzednio. <m>'
			'W rzeczywistości występują oba te rodzaje rejestrów, <m> a nawet rejestry reagujące na oba zbocza. <m>'
			'Informację o tym na które zbocze reaguje dany rejestr <m> znaleźć można w jego dokumentacji. <m>'
			
			'W prezentowanym przykładzie przejście sygnału zegara ze stanu niskiego <m> do stanu wysokiego powoduje zapamiętanie czterech bitów informacji. <m>'
			'Jest to rejestr równoległy ponieważ poszczególne przerzutniki są połączone <m> tak jakby równolegle i każdy otrzymuje bezpośrednio swój bit wejściowy <m> i wystawia jego zapamiętany stan jako swój bit wyjściowy. <m>'
			'Ten typ rejestru jest także nazywane parallel input - parallel output <m> – wejście równoległe i wyjście równoległe. <m>'
			'Mamy tutaj tyle samo bitów wejścia, wyjścia i zapamiętanej informacji, <m> które odpowiadają sobie jeden do jednego. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("rejestr2", 2, 50, [
				("switch", 110, 60), ("wait", 0.5), # in = H
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 60), ("wait", 0.5), # in = L
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("wait", 2.0),
				("switch", 110, 60), ("wait", 0.5), # in = H
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 60), ("wait", 0.5), # in = L
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 60), ("wait", 0.5), # in = H
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 60), ("wait", 0.5), # in = L
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 60), ("wait", 0.5), # in = H
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
				("switch", 110, 60), ("wait", 0.5), # in = L
				("switch", 110, 480), ("wait", 0.5), ("switch", 110, 480), ("wait", 0.5),  # CLK __/‾\__
			])],
		],
		'text' : [
			'Innym typem rejestrów są rejestry szeregowe, <m> na przykład z wejściem szeregowym i wyjściem równoległym, <m> czyli serial input paraller output, tak jak widzimy to na symulacji. <m>'
			'Rejestr ten z każdym cyklem zegara wczytuje bit z swojego wejścia <m> i zapamiętuje go równocześnie przesuwając wszystkie wcześniej zapamiętane bity, <m> najdawniej zapamiętany bit jest tracony. <m>'
			
			'Na symulacji widzimy że w chwili narastającego zbocza zegara <m> stan znajdujący się w rejestrze zostaje przesunięty, <m> tak aby zrobić miejsce dla nowo wczytanego bitu. <m>'
			
			'Aby wczytać całą zawartość n bitowego rejestru potrzebujemy <m> n taktów zegara, podczas których podawane będą kolejne bity <m> wartości która ma znaleźć się w rejestrze. <m>'
			'Stąd też nazwa tego typu rejestrów <m> – dane przesyłane są do nich szeregowo, bit za bitem. <m>'
			
			'Pozwala to na zaoszczędzenie na liniach przesyłających dane <m> – w pokazanym przykładzie <4>[cztery] bity przesyłamy dwoma liniami, <m>'
				'a rozbudowując ten rejestr tymi samymi liniami (tylko trochę wolniej) <m> możemy przesłać 8, 10, 16 i więcej bitów. <m>'
			'Oczywiście oszczędność ta odbywa się kosztem większej liczby cykli zegara <m> potrzebnych do wprowadzenia danych do takiego rejestru. <m>'
			
			'Rejestr ten w pokazanym wariancie ma pewną wadę, <m> która w wielu sytuacjach może być istotna <m> – w trakcie wczytywania nowej wartości poszczególne wyjścia <m> przyjmują na pewien czas niewłaściwe wartości. <m>'
			'Jeżeli rejestr ten steruje np. jakimiś lampkami kontrolnymi to przy odpowiedniej <m> szybkości może to być niezauważalne dla człowieka i jest akceptowalne. <m>'
			'Natomiast jeżeli pod któreś wyjście mamy podpięte jakieś układy wykonawcze <m> (na przykład sygnał odpalenia rakiety z głowicą jądrową) to <m>'
				'nie chcemy aby stan takiego wyjścia przybrał na chwilę <m> wartość oznaczającą odpalenie, tylko z tego względu że na przykład <m> sąsiednie wyjście od jakiejś kontrolki miało taki stan. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("rejestr3", 2, 30, [
				("switch", 145, 50), ("wait", 0.5), # in = H
				("switch", 145, 440), ("wait", 0.5), ("switch", 145, 440), ("wait", 0.5),  # CLK __/‾\__
				("switch", 145, 440), ("wait", 0.5), ("switch", 145, 440), ("wait", 0.5),  # CLK __/‾\__
				("switch", 145, 50), ("wait", 0.5), # in = L
				("switch", 145, 440), ("wait", 0.5), ("switch", 145, 440), ("wait", 0.5),  # CLK __/‾\__
				("wait", 0.5), ("switch", 145, 490), ("wait", 0.5), ("switch", 145, 490), ("wait", 1.0),  # STROBE __/‾\__
				
				("switch", 145, 50), ("wait", 0.5), # in = H
				("switch", 145, 440), ("wait", 0.5), ("switch", 145, 440), ("wait", 0.5),  # CLK __/‾\__
				("switch", 145, 50), ("wait", 0.5), # in = L
				("switch", 145, 440), ("wait", 0.5), ("switch", 145, 440), ("wait", 0.5),  # CLK __/‾\__
			])],
		],
		'text' : [
			'Problem ten rozwiązuje się przez dodanie na wyjściu takiego układu <m> rejestru równoległego sterowanego osobnym sygnałem zegara, <m>'
				'który informuje że dane zapisane w rejestrze szeregowym <m> należy wystawić na wyjścia. <m>'
			
			'Symulację takiego układu widzimy obecnie na ekranie <m> – mamy tutaj jak poprzednio wejście danych, wejście zegara danych <m> (czyli tego który wyznacza nam chwilę odczytu kolejnych bitów) <m>'
				'oraz wejście zegara wyjść określanego też niekiedy jako strobe, <m> czyli tego sygnału który powoduje wystawienie danych na wyjście. <m>'
			
			'Układy takie często mają wyprowadzony także sygnał z ostatniego <m> rejestru szeregowego nie zasłonięty rejestrem wyjściowym. <m>'
			'Pozwala to na dołączenie w tym miejscu kolejnego rejestru szeregowego, <m> celem zwiększenia ilości bitów, które możemy zapisać. <m>'
			
			'Można zauważyć że w warstwie wyjściowej możemy zamiast przerzutników użyć <m> zatrzasków i wprowadzanie danych wykonywać gdy wystawiają one zapamiętany stan, <m>'
				'a stan przeźroczysty zatrzasku wykorzystywać tylko <m> gdy informacja w rejestrze szeregowym nie jest modyfikowana. <m>',
			
			'Oprócz pokazanych rejestrów szeregowych typu serial input - parallel output <m> możemy mieć również rejestry szeregowe typu parallel input - serial output, <m>'
				'czyli takie które posiadają wejścia równoległe i wyjście szeregowe. <m>'
			'Umożliwiają one na przykład zczytanie ośmiu bitów przy pomocy dwóch lub trzech przewodów. <m>'
			
			'Układami podobnymi trochę do rejestrów są liczniki, <m> czyli układy które potrafią zliczać jakieś impulsy. <m>'
			'Można nawet powiedzieć że są to rejestry, tym bardziej że często mają <m> też wejścia pozwalające na ich załadowanie jakąś wartością, <m>'
				'które zostały wyposażone w dodatkowe wejście <m> powodujące zwiększenie zapisanej w nich wartości o jeden. <m>'
		]
	},
]
