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

eduMovie.runCommandString(r"cp intro.c /tmp/plik.c")

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#06.1", "", "Podstawy C", "" ] },
	
	{ 'comment': 'C C++ intro' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"cat plik.c", cwd="/tmp")],
		],
		'text' : [
			'C oraz C++ są to najpopularniejsze języki kompilowane do kodu maszynowego. <m>'
			'Jeżeli do potraktować je łącznie, <m> aczkolwiek pomimo dużych podobieństw są to niezależne języki, <m> to byłyby najpopularniejszymi językami programowania w ogóle. <m>'
			'Pozwalają na stosowanie nisko poziomowych mechanizmów łącznie ze <m> wstawkami asemblera danej maszyny na którą ma być kompilowany kod. <m>'
			'W związku z tym są też bardzo użyteczne do programowania samego sprzętu <m> nawet bez warstwy systemu operacyjnego, <m> czy też właśnie tworzenia systemów operacyjnych. <m>'
			
			'Języki te są kompilowane. <m>'
			'To znaczy źródła muszą być przetworzone na plik wykonywalny <m> w postaci kodu maszynowego danej maszyny, na której ma być uruchomiony program, <m> czyli bezpośrednio do instrukcji danego procesora. <m>'
			'Nie mamy tutaj żadnej warstwy pośredniej <m> jak na przykład w przypadku kompilacji plików Pythona. <m>'
			
			'C jest językiem wysokopoziomowym, w znaczeniu że używa instrukcji i konstrukcji, <m> które zamieniane są na wiele niskopoziomowych instrukcji procesora. <m>'
			'W przeciwieństwie do asemblera, gdzie zasadniczo poszczególne <m> używane mnemoniki odpowiadają jeden do jednego instrukcjom procesora. <m>'
			
			'C określany bywa mianem przenośnego asemblera, wywodzi się to z tego że <m> głównym założeniem C było umożliwienie łatwego przenoszenia programów <m> pomiędzy różnymi maszynami, o różnych architekturach. <m>'
			'I w porównaniu z językami takimi jak na przykład Python <m> język C pozostaje językiem stosunkowo niskopoziomowym. <m>',
			
			'Kompilacja kodu C lub C++ przebiega kilku etapowo, <m> w pierwszej kolejności uruchamiany jest pre-procesor, <m>'
			'który odpowiedzialny jest za przetworzenie poleceń zaczynających <m> się od hasza (takich jak include, define, ifdef). <m>'
			'Przetwarzanie to polega tak naprawdę na modyfikowaniu pliku tekstowego, <m> czyli jeżeli mamy napisane hash include <m> to w tym miejscu pre-procesor wklej podany plik, <m>'
			'tak jakby tekst tego pliku znajdował się dokładnie w tym miejscu. <m>'
			'Specyficzną dyrektywą jest dyrektywa pragma, która nie modyfikuje tekstu <m> stanowiącego kod źródłowy a wpływa na zachowanie kompilatora, <m>'
			'pozwala na ustawianie opcji danego kompilatora <m> i bardziej zależy od używanego kompilatora niż od języka i jego wersji. <m>'
			
			'Kompilator troszczy się także o umieszczanie zmiennych na stosie <m> (czyli w obszarze pamięci przeznaczonym między innymi na <m> argumenty funkcji i zmienne automatyczne) oraz o usuwanie ich z stamtąd. <m>'
			'Pamięć poza stosem programista może alokować z użyciem <m> biblioteki standardowej C (na przykład funkcją malloc), <m> jednak wtedy to programista odpowiada za jej zwolnienie. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["gcc", eduMovie.runCommandString(r"gcc -std=c99 plik.c", cwd="/tmp")],
			["clang", eduMovie.runCommandString(r"clang -std=c99 plik.c", cwd="/tmp")],
			["run", eduMovie.runCommandString(r"./a.out", cwd="/tmp")],
			["etapy",       eduMovie.runCommandString(r"# kompilacja - utworzy plik .o z kodem maszynowym", cwd="/tmp")],
			["etapy + 0.2", eduMovie.runCommandString(r"gcc -std=c99 -c plik.c", cwd="/tmp")],
			["etapy + 4.7", eduMovie.runCommandString(r"# linkowanie - tu można podać wiele plików .o", cwd="/tmp")],
			["etapy + 4.9", eduMovie.runCommandString(r"gcc -std=c99 plik.o", cwd="/tmp")],
			["etapy + 9.1", eduMovie.runCommandString(r"./a.out", cwd="/tmp")],
		],
		'text' : [
			'C i C++ nie są bardzo jednorodnymi językami programowania <m> – istnieje wiele historycznie nawarstwionych, <m> czy też kolejno powstających standardów tych języków. <m>'
			'Kod który będziemy omawiali w ramach wykładu zakłada używanie C w wersji <m> co najmniej 99, czyli z roku <1999>[tysiąc dziewięćset dziewięćdziesiątego dziewiątego] '
				'i C++ z roku <2011>[dwa tysiące jedenastego] w wersji C++ 11. <mark name="gcc" />'
			
			'Na temat C++ pomówimy sobie później, najpierw zaczniemy od samego C. <m>'
			'Aby skompilować kod C wydajemy polecenie <gcc>[gie ce ce] <m> (możemy podać dodatkowo opcje, na przykład takie które określa nam standard) <m> i podajemy mu ścieżkę do pliku z kodem źródłowym. <mark name="clang" />'
			
			'Zamiast <gcc>[gie ce ce] możemy użyć także innego kompilatora – na przykład <clang>[ce lang]. <mark name="run" />'
			
			'W obu wypadkach jako że nie podaliśmy nazwy pliku wynikowego <m> to skompilowany program został zapisany do pliku <a.out>[a kropka out] w bieżącym katalogu. <m>'
			'Tak jak mówiliśmy na wcześniejszych zajęciach <./>[kropka ukośnik] jest konieczny żeby <m> uruchomić plik wykonywalny znajdujący się w bieżącym katalogu, <m>'
				'ponieważ jeżeli byśmy napisali a.out <m> to bash chciałby znaleźć taki program <m> w ścieżce wyszukiwania, bądź znaleźć taką komendę wbudowaną, itd. <m>',
			
			'Proces utworzenia pliku binarnego w oparciu o źródła składa się z kilku etapów. <mark name="etapy" />'
			'Warto tutaj powiedzieć o rozdzieleniu kompilacji, <m> czyli zamiany kodu w postaci tekstu na kod maszynowy <m> oraz linkowania, czyli połączenia wielu takich plików binarnych <m> w plik wykonywalny lub bibliotekę. <m>'
			'Pozwala to na łatwy podział źródeł na wiele plików, <m> ich niezależną (nawet równoległą) kompilację, <m> a następnie złączenie w jeden program. <m>'
			'W procesie linkowania przetwarzane są także odwołania do bibliotek, <m> w tym przypadku do biblioteki standardowej C dostarczającej funkcję puts. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"cat plik.c", cwd="/tmp")],
		],
		'text' : [
			'Wykonywanie każdego programu musi zacząć się od jakiegoś miejsca. <m>'
			'Do tej pory używaliśmy języków skryptowych, <m> dla których miejscem tym był po prostu początek pliku z danym skryptem. <m>'
			'Tak wygląda to w zdecydowanej większości języków interpretowanych. <m>'
			'Natomiast w przypadku języków poddawanych <m> większym przekształceniom przed uruchomieniem, <m> takim jak kompilacja do kodu maszynowego, sprawa nie jest już tak oczywista. <m>'
			
			'W przypadku C i C++ wykonywanie się kodu rozpocznie się od funkcji main. <m>'
			'Oczywiście wcześniej nastąpią jakieś działania techniczne związane <m> na przykład z tworzeniem nowego procesu, czy ładowaniem bibliotek, <m> ale nie jest to nic nadzwyczajnego. <m>'
			'Gdy uruchamialiśmy skrypty w Pythonie lub bashu to najpierw też <m> uruchamiany był interpreter, który ustawiał wartości niektórych zmiennych itd., <m> a dopiero potem rozpoczynał przetwarzanie naszego skryptu. <m>'
			
			'Z punktu widzenia kodu C, czy C++ nie jest ważne <m> gdzie zostanie umieszczona funkcja main. <m>'
			'Natomiast jeżeli chcemy skompilować nasz kod do postaci <m> wykonywalnego programu to powinna ona gdzieś być zdefiniowana. <m>'
			
			'W widocznym na ekranie kodzie źródłowym programu, <m> który przed chwilą skompilowaliśmy i uruchomiliśmy widzimy właśnie funkcję main. <m>'
			
			'Oprócz niej mamy włączenie pliku nagłówkowego związanego z biblioteką <m> standardową C i obsługą wejścia wyjścia w ramach niej. <m>'
			'W ramach funkcji main wywołujemy funkcję puts, przekazując do niej <m> ciąg znaków, a następnie kończymy działanie main zwracając zero. <m>'
			'Ta wartość zwracana z funkcji main to jest właśnie kod powrotu programu <m> o którym mówiliśmy tak dużo na wcześniejszych zajęciach. <m>'
			'Każdą instrukcję kończymy średnikiem – C nie wymaga wcięć <m> ani znaków nowej linii, wymaga za to klamerek i średników. <m>'

			'Funkcja puts po prostu wypisuje na ekran podany ciąg znaków <m> dodając do niego znak nowej linii, <m> czyli jest to taki odpowiednik funkcji print z Pythona, <m>'
			'tyle że o znacznie mniejszych możliwościach <m> – potrafi tylko i wyłącznie wypisać ciąg znaków, <m> czyli nie możemy tutaj podać mu na przykład do wypisania liczby całkowitej. <m>'
		]
	},
]
