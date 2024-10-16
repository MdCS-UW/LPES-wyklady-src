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

code_w_zmiennej = r"""
a="echo -e abc\ndef ..."
$a ABC
"""

code_eval_A = r"""
A='tekst do wypisania, $SHELL, `ls -d`'
B="A"

C=$( eval "echo \$$B" )
echo $C

echo ${!B}
"""

code_eval_B = r"""
A='tekst do wypisania, $SHELL, `ls -d`'
B="A"

C=$( eval eval "echo \$$B" )
echo $C
"""

code_eval_C = r"""
LISTA_WYBORU="a) echo AA;; b) echo BB;;"
INNE="e|f"

ff() {
	eval "case $1 in
		$LISTA_WYBORU
		c) echo "CCC";;
		$INNE) echo inne;;
	esac"
}

ff a
ff e
ff c
"""

code_envsubst = r"""
x=12
A='tekst, ${x}, $SHELL, $x, `ls -d`'

C=`export x; echo $A | envsubst`
echo $C
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'bash - uzupełnienia' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
			["wzmiennej", eduMovie.clear + eduMovie.code2console(code_w_zmiennej, "sh")],
			["evalA", eduMovie.clear + eduMovie.code2console(code_eval_A, "sh")],
			["evalB", eduMovie.clear + eduMovie.code2console(code_eval_B, "sh")],
			["evalC", eduMovie.clear + eduMovie.code2console(code_eval_C, "sh")],
			["envsubst", eduMovie.clear + eduMovie.code2console(code_envsubst, "sh")],
		],
		'consoleDown': [
			[0.0, ""],
			["wzmiennej", eduMovie.runCode(code_w_zmiennej, [], cmd="bash")],
			["evalA", eduMovie.runCode(code_eval_A, [], cmd="bash")],
			["evalB", eduMovie.runCode(code_eval_B, [], cmd="bash")],
			["evalC", eduMovie.runCode(code_eval_C, [], cmd="bash")],
			["envsubst", eduMovie.runCode(code_envsubst, [], cmd="bash")],
		],
		'text' : [
			'Omawiając Pythona wspomnieliśmy sobie o funkcji exec <m> wykonującej kod podany do niej w formie napisu <m>'
				'oraz o funkcjach z rodziny exec znajdujących się w module os <m> umożliwiających zastąpienie pythona innym programem. <m>'
			'W przypadku basha instrukcja exec działa tak jak te funkcje z modułu os, <m> czyli jeżeli napiszemy exec <python3>[python 3] to uruchomimy interpreter pythona, <m>'
				'ale nie jako proces potomny, a jako proces zastępujący naszego basha. <mark name="wzmiennej" />'
			
			'Bash pozwala jednak także na wykonywanie kodu z napisu go zawierającego. <m>'
			'Najprostszym przypadkiem jest wykonanie polecenia, <m> które mamy zapisane w zmiennej. <m>'
			'Wystarczy uruchomić zmienną, tak jak jest to pokazane na ekranie. <m>'
			'Jak widzimy w tej samej zmiennej możemy mieć nawet <m> opcje i argumenty dla uruchamianego polecenia. <m>'
			
			'Metoda ta nie pozwala jednak na podstawianie <m> wartości zmiennych podanych w napisie w momencie uruchamiania go, <itp.>[i te pe.] <m>'
			
			'Bash oferuje także instrukcję eval, <m> która pozwala na uruchamianie bardziej złożonych fragmentów kodu. <m>'
			'Zapewnia ona podstawienie występujących w tym napisie zmiennych, itd. <mark name="evalA" />'
			
			'Jednym z prostszych przypadków użycia eval <m> jest pobranie wartości zmiennej, której nazwa jest w innej zmiennej. <m>'
			'W przykładzie widocznym na ekranie chcemy pobrać wartość zmiennej "A", <m> w oparciu o jej nazwę w zmiennej B. <m>'
			'Można to też uzyskać poprzez odwołanie klamerkowe z wykrzyknikiem, <m> ale nie jest ono ujęte w standardzie <sh>[SH] <m> i może być nie wspierane na innych powłokach niż bash. <mark name="evalB" />'
			
			'Jeżeli chcielibyśmy aby kod znajdujący się w zmiennej "A" <m> także został przetworzony, czyli podstawiona wartość zmiennej <m> oraz output komendy ls, to możemy użyć eval dwukrotnie,<m>'
				'tak jak pokazuje to przykład widoczny na ekranie. <mark name="evalC" />'
			
			'Z pomocą instrukcji eval możemy także budować kod bashowy <m> (np. fragmenty konstrukcji case) w oparciu o zawartość zmiennych, <m> tak jak pokazuje to kolejny przykład na ekranie. <m>'
			'Używając eval należy zachować podobną ostrożność jak <m> wczytując pliki z użyciem kropki lub wykonując pythonowy exec. <mark name="envsubst" />'
			
			'Innym poleceniem umożliwiającym podstawienie wartości <m> zmiennych występujących w jakimś napisie jest <envsubst>[enw subst]. <m>'
			'W odróżnieniu od eval nie wykonuje on podanego kodu, <m> a jedynie przetwarza napis podstawiając wartości zmiennych <m>'
				'(zatem jest bezpieczniejszy przy przetwarzaniu <m> danych niewiadomego pochodzenia). <m>'
			'Jako że jest to zewnętrzny program to używane zmienne <m> muszą być dla niego dostępne, czyli muszą być wyeksportowane. <m>',
			
			'Należy też wspomnieć o ograniczeniach dotyczących <m> maksymalnej długości listy argumentów <m> (zarówno całej jak i pojedynczego argumentu). <m>'
			'Mogą one okazać się problemem na przykład, <m> gdy korzystamy ze znaków uogólniających powłoki <m> i dopasowanych zostanie zbyt wiele plików dopasowanych. <m>'
			'Lub Gdy wykorzystujemy przechwycenie <m> standardowego wyjścia jakiegoś polecenia, <m> aby użyć go jako argumentów innego polecenia. <m>'
			'W takich sytuacjach warto skorzystać na przykład <m> z pętli while-read działającej na standardowym wyjściu <m> polecenia zwracającego te dane. <m>'
			'W przypadku listy plików może to być ls bez argumentów lub (gdy potrzebujemy wybrać tylko niektóre pliki) find. <m>'
		]
	},
]

code_cateof = r"""
cat > plik << EOF
wieloliniowa
treść zapisywana
do wskazanego pliku
EOF

echo ------
cat plik
"""

code_tee = r"""
echo abc | tee plik

echo ------
cat plik
"""

code_echoerr = r"""
echo "Bardzo ważny komunikat o błędzie!" > /dev/stderr
"""

code_filestream = r"""
diff <(cat /etc/passwd) <(cat /etc/passwd-)
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
			["cateof", eduMovie.clear + eduMovie.code2console(code_cateof, "sh")],
			["tee", eduMovie.clear + eduMovie.code2console(code_tee, "sh")],
			
			["echoerr", eduMovie.clear + eduMovie.code2console(code_echoerr, "sh")],
			["filestream", eduMovie.clear + eduMovie.code2console(code_filestream, "sh")],
		],
		'consoleDown': [
			[0.0, ""],
			["cateof", eduMovie.runCode(code_cateof, [], cmd="bash")],
			["tee", eduMovie.runCode(code_tee, [], cmd="bash")],
			
			["devstd", eduMovie.runCommandString(r"ls -l /dev/std*")],
			["echoerr", eduMovie.runCode(code_echoerr, [], cmd="bash")],
			["filestream", eduMovie.runCode(code_filestream, [], cmd="bash")],
		],
		'text' : [
			'Kilkukrotnie mówiliśmy już o przekierowaniach <m> strumieni i używaliśmy ich w różnych zastosowaniach. <m>'
			'Należy jednak wspomnieć jeszcze o kilku <m> istotnych aspektach takich przekierowań. <mark name="cateof" />'
			
			'Konstrukcja widoczna na ekranie bardzo często używana <m> jest do tworzenia zewnętrznych plików z poziomu kodu skryptu bashowego. <m>'
			
			'Widzimy wywołanie komendy cat (z którą mieliśmy już do czynienia, <m> np. gdy mówiliśmy o kopiowaniu plików poprzez <ssh>[S S H]). <m>'
			'Polecenie to wywołane z argumentami będącymi nazwami plików <m> wypisze te pliki na standardowe wyjście. <m>'
			'Wywołane bez argumentów przeczyta swoje standardowe wejście <m> i wypisze je na standardowe wyjście. <m>'
			
			'W tym wypadku polecenie cat wykonane jest bez nazwy pliku <m> a jego wyjście przekierowane jest do pliku, <m> czyli do tego pliku zapisze to co przeczyta na swoim standardowym wejściu. <m>'
			'Zwraca tutaj jednak uwagę inny operator - dwa znaki mniejszości. <m>'
			'Powoduje on że tekst podawany w kolejnych liniach będzie kierowany <m> na standardowe wejście komendy po której wystąpił, <m>'
				'aż do momentu napotkania linii <m> zawierającej jedynie ciąg znaków podany po nim. <m>'
			'Ciąg ten może być dowolnym napisem, także zawierającym spacje <m> (jeżeli ujmiemy go w cudzysłów), <m> ale bardzo często jest to widoczny w przykładzie EOF. <mark name="tee" />'
			
			'Innym poleceniem przydatnym przy manipulacji strumieniami jest tee. <m>'
			'Podobnie jak cat kopiuje on swoje standardowe wejście na standardowe wyjście. <m>'
			'Natomiast jeżeli poda mu się ścieżkę do pliku to będzie on <m> zapisywał te dane także do wskazanego pliku. <mark name="devstd" />'
			
			'Wiele programów jeżeli w miejscu w którym oczekuje ścieżki do pliku <m> otrzyma myślnik zinterpretuje to jako użycie w tym miejscu standardowego wejścia / wyjścia. <m>'
			'Nawet jeżeli program nie wspiera tej konwencji to możemy użyć <m> specjalnych urządzeń znajdujących się w dev reprezentujących te strumienie. <mark name="echoerr" />'
			
			'Możemy ich także użyć aby wypisać coś na przykład <m> na standardowym wyjściu błędu z użyciem echo. <mark name="filestream" />'
			
			'Bash pozwala także na podstawienie standardowego wyjścia różnych komend <m> w miejsce kilku plików bez potrzeby jawnego tworzenia plików tymczasowych, <m> tak jak widzimy to na ekranie. <m>'
			'W tym przykładzie diff oba pliki do porównania <m> otrzymuje jako output innych poleceń. <m>'
			'Oczywiście zaprezentowane zastosowanie tego mechanizmu z użyciem <m> poleceń cat jest całkowicie bezsensowne (prościej podać ścieżki do plików), <m>'
				'ale gdyby występował tam już np. jakiś grep mogłoby to być użyteczne. <m>'
			'Jest to rozszerzenie bashowe nie występujące w czystym <sh>[SH]. <m>'
		]
	},
]

code_trap = r"""
trap '{ echo "to koniec"; }' EXIT;

set -e;    # to spowoduje przerwanie skryptu gdy jakieś polecenie
           # zwróci nieobsłużony niezerowy kod powrotu

echo "aa"
false      # tu zostanie przerwane wykonywanie skryptu
echo "bb"
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_trap, "sh")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_trap, [], cmd="bash")],
		],
		'text' : [
			'Jak wiemy działający program może zostać zakończony <m> w sposób niespodziewany, np. na skutek działania sygnałów. <m>'
			'Dotyczy to również basha wykonującego jakiś skrypt powłoki. <m>'
			'Możemy nawet samodzielnie zażądać przerwania wykonywania skryptu <m> przy pierwszym błędzie wydając polecenie <set -e>[set minus e]. <m>'
			'W efekcie działanie skryptu zakończy się przy pierwszym poleceniu, <m> które zwróciło nieobsłużony (np. w warunku if), niezerowy kod powrotu.<m>'
			
			'Możliwe jest zaplanowanie działań które mają być wykonywane na zakończenie. <m>'
			'Służy do tego instrukcja trap, która pozwala na zdefiniowanie procedury <m> obsługi sygnałów (oczywiście tych które mamy prawo obsłużyć) i innych zdarzeń. <m>'
			
			'W przykładzie widocznym na ekranie widzimy ustawienie instrukcji, <m> które mają być wykonane gdy skrypt zostanie zakończony <m> oraz włączenie automatycznego przerwania gdy napotkamy błąd. <m>'
			'Następnie pomiędzy dwoma wypisaniami wywołujemy taki błąd. <m>'
			'W efekcie nie widzimy wypisania <bb>[be be], za to widzimy wypisanie "to koniec". <m>'
			
			'Instrukcje zdefiniowane w trap dla exit wykonają się także gdy przerwiemy <m> działanie skryptu z użyciem Control C lub innego przechwytywalnego sygnału. <m>'
		]
	},
]
