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
	{ 'title': [ "#04.2", "Język AWK", "", "" ] },
	
	{ 'comment': 'napisy' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"""head /etc/passwd > /tmp/passwd""")],
			[0.7, eduMovie.runCommandString(r"""cut -f5 -d: /tmp/passwd""")],
			["awk1", eduMovie.runCommandString(r"""awk -F: '{print $5}' /tmp/passwd""")],
		],
		'text' : [
			'Pliki o układzie kolumnowym, o których mówiliśmy wcześniej, <m> często stanowią tekstowe bazy danych - linia odpowiada rekordowi, <m>'
				'a kolejne kolumny (oddzielane jakimś separatorem) <m> stanowią pola w takim rekordzie (czyli komórki tabeli). <m>'
			'Pamiętamy że do wypisania danej kolumny z takiej tekstowej <m> bazy danych mogliśmy użyć polecenia cut. <m>'
			
			'Bardzo wszechstronnym narzędziem do przetwarzania tego typu plików, <m> czy też plików tekstowych w ogóle jest <AWK>[awuka]. <m>'
			'<AWK>[awuka] to zasadniczo interpreter prostego, skryptowego <m> języka programowania o składni podobnej do składni C. <mark name="awk1" />'
			
			'Na ekranie widzimy przykład realizacji <m> funkcjonalności polecenia cut z użyciem AWK. <m>'
			'Opcja <-F>[minus F duże] służy do ustalenia separatora pola <m> (który w odróżnieniu od cut może być wieloznakowym napisem a nawet wyrażeniem regularnym). <m>'
			'Następnie podany jest kod programu i plik na którym operujemy. <m>'
			
			'Program <awk-owy>[awkowy] składa się z bloków instrukcji ujętych w klamerki, <m> każdy z nich może być poprzedzony warunkiem. <m>'
			'Dla każdej linii pliku wejściowego wykonywane są kolejno <m> wszystkie bloki których warunek jest dla niej spełniony. <m>'
			
			'W prezentowanym przykładzie mamy jeden blok, <m> z pustym warunkiem, czyli takim, który pasuje do każdej linii. <m>'
			'Zatem dla każdej linii pliku wejściowego zostanie wykonana instrukcja <m> <print $5>[print dolar pięć], która wypisze nam wartość piątego pola. <m>'
			
			'Dzieje się tak dlatego że <awk>[afk] rozbija linię na pola <m> z użyciem wskazanego separatora i pozwala się do nich odwoływać <m> przy pomocy zmiennych postaci dolar numer pola. <m>'
			'Dolar zero pozwala na dostęp do zawartości całej linii. <m>'
			'<AWK>[awuka] obsługuje zmienne i odwołujemy się do nich po prostu używając ich nazwy <m> – tak samo jak np. w Pythonie. <m>'
			'Natomiast dolar jest operatorem odwołania do danego pola, a nie do zmiennej. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"""awk -F: '/r..t/ {print $0}' /tmp/passwd""")],
			["awk3", eduMovie.runCommandString(r"""awk -F: '$3%2 != 0 {print $5}' /tmp/passwd""")],
			["awk4 + 1.7", eduMovie.runCommandString(r"""awk -F: '$7 ~ "/.*sh[^/]*$" {print $5}' /tmp/passwd""")],
		],
		'text' : [
			'<AWK>[awuka] może zastąpić także polecenie grep. <m>'
			'W przykładzie widocznym na ekranie blok instrukcji <m> (złożony z jednej instrukcji – print dolar zero) <m> wykonywany jest tylko dla linii pasujących do podanego wyrażenia regularnego. <mark name="awk3" />'
			
			'Połączenie tych dwóch cech pozwala na wykonywanie operacji <m> trudnych do uzyskania stosując indywidualne komendy takie jak grep, cut, itp. <m>'
			'Na przykład możemy wypisywać kolumnę piątą <m> gdy kolumna trzecia spełnia podane kryterium. <m>'
			'Może to być na przykład kryterium numeryczne – tak jak w widocznym <m> na ekranie przykładzie, gdzie wymagamy aby jej wartość była nie parzysta. <mark name="awk4" />'
			
			'Może to być dopasowanie do wyrażenia regularnego, porównanie napisów itd. <m>'
			'Operatory nierówności mają postać standardową, <m> porównanie to dwa znaki równości. <m>'
			'Operator tylda oznacza pasowanie do wyrażenia regularnego, <m> a wykrzyknik tylda nie pasowanie do tego wyrażenia. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"""awk 'NR <3 {print $0}' /tmp/passwd""")],
			["awk6", eduMovie.runCommandString(r"""awk '{print NR " : " $0}' /tmp/passwd""")],
			["awkif1", eduMovie.runCommandString(r"""awk '{if (NR <3) print $0}' /tmp/passwd""")],
			["awkif2", eduMovie.runCommandString(r"""awk '{if (NR <3) {print "AAA"; print $0;}}' /tmp/passwd""")],
			["awkbegin1", eduMovie.runCommandString(r"""awk 'BEGIN {print "ABC"} NR<3 {print NR " : " $0}' /tmp/passwd""")],
			["awkbegin2", eduMovie.runCommandString(r"""awk 'BEGIN{FS=":"} {print $5}' /tmp/passwd""")],
		],
		'text' : [
			'<AWK>[awuka] może zastąpić nam też polecenia takie jak head i tail, <m> czyli wypisywać tylko linie o odpowiednich numerach. <m>'
			'Możliwe jest to dzięki zmiennej <NR>[eN eR] w której <AWK>[awuka] przechowuje <m> numer aktualnego rekordu (czyli standardowo linii). <mark name="awk6" />'
			'Możemy tej zmiennej użyć także do wypisania pliku z ponumerowanymi liniami. <m>'
			
			'<AWK>[awuka] pozwala także na stosowanie w ramach bloku kodu <m> instrukcji warunkowych i pętli. <mark name="awkif1" />'
			
			'Możemy zmodyfikować przykład z wypisywaniem linii <m> o odpowiednich numerach tak żeby zamiast <m> warunku przed blokiem użyć warunku if w środku bloku. <mark name="awkif2" />'
			
			'Podobnie jak w C jeżeli blok instrukcji związany z <m> warunkiem lub pętlą ma obejmować więcej niż jedną instrukcję <m> to powinniśmy umieścić je w klamerkach. <m>'
			'Kolejne instrukcje możemy oddzielać przy pomocy średnika <m> lub (gdy piszemy kod w pliku) znaków nowej linii. <mark name="awkbegin1" />'
			
			'Przed klamerkami możemy podać także specjalne słowa kluczowe. <m>'
			'Jednym z nich jest begin i jak widzimy <AWK>[awuka] wykonał ten blok instrukcji <m> przed przetworzeniem pierwszej linii danych wejściowych (pliku). <mark name="awkbegin2" />'
			
			'Begin często wykorzystywane jest do inicjalizacji jakiś zmiennych, <m> wliczając w to znienne FS i RS czyli separator pola i separator rekordu. <m>'
			'Mamy także warunek end, którego blok kodu <m> wykonuje się po przetworzeniu całego pliku. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"""echo '1 3' | awk 'function f(x) {return 2*x} {print f($1+$2)}'""")],
			["cut2", eduMovie.runCommandString(r"""cut -f4- -d: /tmp/passwd""")],
			["awkcut1", eduMovie.runCommandString(r"""awk -F: '{for (i=4;i<NF;++i) printf("%s%s",$i, FS); printf("%s%s", $NF, RS);}' /tmp/passwd""")],
			["awkcut2", eduMovie.runCommandString(r"""awk -F: '{for (i=4;i<NF;++i) printf($i FS); printf($NF RS);}' /tmp/passwd""")],
			["awkcut3", eduMovie.runCommandString(r"""awk -F: '{x=$0; for (i=1;i<4;++i) { x=substr(x, length($i)+1); sub("^"FS, "", x) } print(x)}' /tmp/passwd""")],
		],
		'text' : [
			'W podobny sposób możemy też definiować funkcje <m> – w tym celu używamy słowa kluczowego function <m> następnie nazwy funkcji z nawiasami okrągłymi, <m>'
			'w których możemy podać argumenty <m> i w klamerkach związanych z tym blokiem podajemy kod danej funkcji. <mark name="cut2" />'
			
			'Pamiętamy że cut pozwalał w łatwy sposób na wypisanie <m> wszystkich kolumn od podanej do końca linii. <mark name="awkcut1" />'
			'W <AWK>[awuka] uzyskanie takiego efektu jest zaskakująco trudne, <m> zwłaszcza jak na prostotę tego języka. <m>'
			
			'Możemy uzyskać go stosując pętlę for, <m> w taki sposób jak widzimy na ekranie. <m>'
			'Pętla ta będzie przechodziła po wszystkich polach od wskazanego <m> aż do przed ostatniego pola w danej linii. <m>'
			'Korzystamy tutaj ze zmiennej NF, która przechowuje liczbę pól <m> w bieżącym rekordzie, czyli zarazem numer ostatniego pola. <m>'
			'W ramach pętli wypisujemy zawartość pola i separator. <m>'
			'Po pętli wypisujemy wartość ostatniego pola i separator rekordów <m> (w tym wypadku domyślny, czyli nową linię). <mark name="awkcut2" />'
			
			'Dzięki bez operatorowemu łączeniu napisów w <AWK>[awuka] możemy ten kod nieco uprościć <m> do postaci widocznej teraz na ekranie. <m>'
			'Rozwiązanie to nie sprawdzi się jednak gdy separatorem pola <m> jest jakieś wyrażenie regularne, a chcemy zachować jego oryginalną wartość. <mark name="awkcut3" />'
			
			'W takiej sytuacji możemy użyć pętli, która przechodzi po <m> niechcianych początkowych polach i usuwa je z użyciem <m> np. funkcji związanych z przetwarzaniem napisów. <m>'
			'W prezentowanym przykładzie do zmiennej x <m> przypisujemy wartość całej linii. <m>'
			'Następnie w kolejnych obiegach pętli przy pomocy funkcji <m> <substr>[sub STR] podstawiamy fragment nie zawierający bieżącego pola. <m>'
			'Warto zwrócić uwagę na lenght plus jeden, co wynika z tego iż <m> <substr>[sub STR] w <AWK>[awuka] indeksuje napisy od jeden a nie od zera. <m>'
			'Następnie przy pomocy funkcji sub usuwamy separator pola, <m> który znajduje się teraz na początku zmodyfikowanego x. <m>'
			'Po zakończeniu pętli wypisujemy zmienną x, <m> w której mamy linię z obciętymi polami o wskazanych numerach. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"""/bin/echo -e 'a z\na z\nb y\na z\nc y\nb y\nd q\na x' > /tmp/abc""")],
			[0.8, eduMovie.runCommandString(r"""cat /tmp/abc""")],
			["awktab1", eduMovie.runCommandString(r"""awk 'x[$0]<1 {x[$0]=1; print $0}' /tmp/abc""")],
			["awktab2", eduMovie.runCommandString(r"""awk 'BEGIN {RS="[ \t\n]+"} {x[$0]++} END {for (s in x) printf("%s: %s\n", s, x[s])}' /tmp/abc""")],
		],
		'text' : [
			'<AWK>[awuka] pozwala też na korzystanie z tablic i są to tablice asocjacyjne, <m> czyli podobnie jak w przypadku pythonowych słowników <m> indeksem może być dowolna wartość np. napis. <m>'
			'Operatorem odwołania się do elementu tablicy jest nawias kwadratowy. <m>'
			'Odwołanie się do nieistniejącego elementu <m> (podobnie jak nie istniejącej zmiennej) <m> nie jest traktowane jako błąd i w przypadku odwołań <m> numerycznych daje wartość zero, a tekstowych napisu pustego. <mark name="awktab1" />'
			
			'Pozwala nam to na przykład na prostą realizację wypisywania <m> tylko pierwszego wystąpienia danej linii w pliku, <m> bez konieczności sortowania go jak wymagała komenda uniq. <m>'
			'Dla każdej linii sprawdzamy czy wartość w tablicy x indeksowana <m> treścią tej linii jest mniejsza od jeden, i jeżeli jest <m>'
				'(a tak się dzieje gdy odwołujemy się do nieistniejącego elementu tablicy) <m> to ustawiamy ją na jeden i wypisujemy tą linię. <mark name="awktab2" />'
			
			'Przy pomocy pętli for w stylu znanym z pythona, <m> czyli "foreach" możemy iterować po całej tablicy. <m>'
			'Pozwala nam to na przerobienie poprzedniego kodu na licznik słów. <m>'
			'W tym celu  zmieniamy ustawienia separatora rekordów, <m> tak aby rekordowi odpowiadało pojedyncze słowo <m>'
				'(możemy je, w tym przykładzie, rozdzielać <m> spacjami, tabulatorami, lub znakami nowej linii). <m>'
			'W bloku wykonywanym dla każdego rekordu zwiększamy wartość tablicy o jeden, <m>'
				'a w bloku wykonywanym na końcu przetwarzania wypisujemy <m> wszystkie klucze wraz z odpowiadającymi wartościami z tablicy x. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
		],
		'text' : [
			'Kod programu tworzonego w <AWK>[awuka] możemy też zapisać w pliku <m> i przekazać go do komendy <AWK>[awuka] w opcji <-f>[minus f małe]. <m>'
			'W takim wypadku możemy sobie pozwolić między innymi na ładne formatowanie kodu. <m>'
			
			'<AWK>[awuka] jest językiem programowania dedykowanym właśnie do plików tekstowych. <m>'
			'Można w nim tworzyć programy nie związane z przetwarzaniem tekstów, <m> jednak ze względu na brak bibliotek może to być trudne. <m>'
			
			'Wszystko to, co można zrobić przy pomocy <AWK>[awuka] <m> można zrobić także przy pomocy na przykład Pythona, <m>'
				'natomiast nie zawsze ten kod pythonowy będzie <m> prostszy i bardziej zwięzły od kodu <AWK>[awuka]. <m>'
			'Dodatkowo dostępność polecenia <AWK>[awuka] jest gwarantowana przez standard <POSIX>[poz\'iks], a Python nie. <m>'
			'Nieważne z jakim systemem uniksowym będziemy mieli do czynienia, <m> standard gwarantuje tam obecność w nim podstawowej wersji <AWK>[awuka]. <m>'
			
			'<AWK>[awuka] którego używamy na tych zajęciach to tak naprawdę <GAWK>[gawk], <m> czyli GNU <AWK>[awuka], w którym są pewne rozszerzenia wykraczające poza standard, <m>'
				'więc jeżeli chcemy napisać komendę przenośną na inne Unixy, <m> to warto się zapoznać z dokumentacją man, <m> gdzie są szczegółowo opisane również te niekompatybilności. <m>'
		]
	},
]
