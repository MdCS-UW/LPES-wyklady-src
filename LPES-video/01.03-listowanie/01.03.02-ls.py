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
	{ 'section': 'polecenie ls' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"ls -l", cwd='demo')],
			["ls2 + 0.215054", "o", eduMovie.prompt()],
			["ls2 + 2.91065", "o", "l"],
			["ls2 + 3.102497", "o", "s"],
			["ls2 + 3.286457", "o", " "],
			["ls2 + 3.478536", "o", "-"],
			["ls2 + 3.830568", "o", "l"],
			["ls2 + 4.206473", "o", " "],
			["ls2 + 4.398544", "o", "a"],
			["ls2 + 4.750546", "o", "\r\n"],
			["ls2 + 4.755546", "o", "-rw-r--r-- 1 rrp users 4  2021-01-02 18:15:22  a\r\n"],
			["ls2 + 4.756477", "o", eduMovie.prompt()],
			["ls2a", "o", eduMovie.editBegin(1) + "" + eduMovie.markBegin + "-" + eduMovie.markEnd + "rw-r--r-- 1 rrp users 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2b", "o", eduMovie.editBegin(1) + "-" + eduMovie.markBegin + "rw-" + eduMovie.markEnd + "r--r-- 1 rrp users 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2c", "o", eduMovie.editBegin(1) + "-rw-" + eduMovie.markBegin + "r--" + eduMovie.markEnd + "r-- 1 rrp users 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2d", "o", eduMovie.editBegin(1) + "-rw-r--" + eduMovie.markBegin + "r--" + eduMovie.markEnd + " 1 rrp users 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2e", "o", eduMovie.editBegin(1) + "-rw-r--r-- 1 " + eduMovie.markBegin + "rrp" + eduMovie.markEnd + " users 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2f", "o", eduMovie.editBegin(1) + "-rw-r--r-- 1 rrp " + eduMovie.markBegin + "users" + eduMovie.markEnd + " 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2g", "o", eduMovie.editBegin(1) + "-rw-r--r-- 1 rrp users " + eduMovie.markBegin + "4" + eduMovie.markEnd + "  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
			["ls2h", "o", eduMovie.editBegin(1) + "-rw-r--r-- 1 rrp users 4 " + eduMovie.markBegin + "2021-01-02 18:15:22" + eduMovie.markEnd + "   a" + eduMovie.editEnd(1)],
			["ls2i", "o", eduMovie.editBegin(1) + "-rw-r--r-- 1 rrp users 4  2021-01-02 18:15:22  a" + eduMovie.editEnd(1)],
		],
		'text' : [
			'Listowanie plików jest operacją na tyle istotną i użyteczną <m> że oczywiście nie używamy do niego na ogół komendy echo <m>'
			'tylko dedykowanej komendy <ls>[LS] <m> która pozwala <m> na znacznie więcej niż echo i znaki uogólniające. <mark name="ls2" />'
			'Dzięki niej możemy na przykład listować szczegóły na temat <m> danych plików, takich jak informacje na temat '
			'<mark name="ls2a" /> typu pliku (myślnik oznacza zwykły plik, <d>[de] oznacza katalog i tak dalej), <mark name="ls2b" /> uprawnień właściciela, <mark name="ls2c" /> grupy właścicielskiej,<mark name="ls2d" /> pozostałych użytkowników, '
			'<mark name="ls2e" /> nazwę właściciela, <mark name="ls2f" /> grupy właścicielskiej, <mark name="ls2g" /> rozmiaru tego pliku oraz <mark name="ls2h" /> daty jego modyfikacji. <mark name="ls2i" /> <m>'
			
			'Uprawnienia dla każdego z 3 poziomów (właściciela, grupy i pozostałych) <m> składają się z 3 liter – obecność danej litery <m> oznacza posiadanie danego prawa,<m> a myślnik jego brak. <m>'
			'Są to <r>[er] – <m>odczyt, <w>[wu] – <m>zapis i x – <m>wykonywanie. <m> Prawa odczytu i zapisu są dość oczywiste. <m>'
			'Warto wspomnieć że brak prawa zapisu do pliku nie oznacza <m> braku możliwości jego skasowania i utworzenia nowego pliku o <m> takiej samej nazwie, jeżeli mamy prawo zapisu w katalogu. <m>'
			
			'Wykonywanie dla plików oznacza prawo uruchomienia kodu z tego pliku. <m>'
			'Przy czym brak prawa wykonywalności nie oznacza że kodu z pliku <m> nie da się wykonać – aby wykonać plik,<m> wystarczy móc przeczytać jego kod, <m> zarówno w przypadku kodu interpretowanego, jak też w przypadku kodu binarnego. <m>'
			'Dla katalogów prawo wykonywalności oznacza prawo wejścia w głąb katalogu, <m> czyli dostępu do plików i podkatalogów znajdujących się wewnątrz niego. <m>'
			'Natomiast prawo odczytu oznacza prawo wylistowania plików (i podkatalogów) się w nim znajdujących. <m>'
			'Czyli jeżeli mamy prawo wykonywalności katalogu, <m> ale nie prawo czytania katalogu, to mamy dostęp do danych <m> w tym katalogu pod warunkiem że znamy ścieżkę pliku w którym są. <m>'
			'Jeżeli jej nie znamy to ze względu na brak <m> prawa listowania katalogu nie możemy jej poznać, a co najwyżej możemy ją zgadnąć. <m>'
		]
	},
	{
		'console': [
			[1.0, eduMovie.runCommandString(r"ls -lh", cwd='demo')],
			["ukryte", eduMovie.runCommandString(r"ls -la", cwd='demo')],
			["liniowo1+2.0", eduMovie.runCommandString(r"ls -1", cwd='demo')],
			["liniowo2", eduMovie.runCommandString(r"ls | less", cwd='demo')],
		],
		'text' : [
			'Komenda <ls>[LS] jest jednym z tych poleceń <m> w których opcja <-h>[minus h] oznacza wypisanie w formacie czytelnym dla człowieka, <m> a nie wypisanie tekstu pomocy. <m>'
			'Jak widzimy na ekranie jej użycie zmienia sposób wypisywania <m> rozmiarów plików w taki sposób, że zamiast dokładnego rozmiaru w bajtach <m>'
			'wypisywany jest zaokrąglony rozmiar z użyciem <m> przedrostków typu kilo, mega, giga, i tak dalej. <mark name="ukryte" />'
			
			'Przełącznik <-a>[minus a] powoduje wyświetlanie plików ukrytych, <m> czyli takich których nazwa zaczyna się od kropki <m> (poza tym niczym innym nie różnią się one od pozostałych plików). <m>'
			'Warto zauważyć iż wyświetlona zostanie wtedy też <m> kropka oznaczająca katalog bieżący <m> i dwie kropki oznaczające katalog nadrzędny. <mark name="liniowo1" />'
			
			'Opcja <-1>[minus jeden] powoduje wypisywanie jednego pliku <m> w linii, jest ona automatycznie dodawana <mark name="liniowo2" /> gdy wyjście <ls>[LS] jest przekierowane do innego polecenia lub do pliku.'
		]
	},
	{
		'console': [
			[0.0, ""],
			["data", eduMovie.runCommandString(r"ls -lt", cwd='demo')],
			["rozmiar", eduMovie.runCommandString(r"ls -lS", cwd='demo')],
			["reverse", eduMovie.runCommandString(r"ls -ltr", cwd='demo')],
		],
		'text' : [
			'<ls>[LS] pozwala również na sortowanie,<m> na przykład według <mark name="data" /> daty modyfikacji z użyciem opcji <-t>[minus t], <mark name="rozmiar" /> według rozmiaru z użyciem opcji <-S>[minus s duże]. <mark name="reverse" />'
			'Przydatna jest też opcja <-r>[minus r] odwracająca kolejność sortowania, <m>'
			"dzięki czemu chcąc zobaczyć najnowsze pliki możemy napisać <ls -tr>[L S minus T R] <m> i zostaną one wylistowane na dole i nie będziemy musieli przewijać terminala <m> lub przekierowywać wyjścia tego polecenia np. do less'a. <m>"
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"ls a*", cwd='demo')],
			[2.0, eduMovie.runCommandString(r"ls -l .", cwd='demo')],
			[4.0, eduMovie.runCommandString(r"ls -ld .", cwd='demo')],
		],
		'text' : [
			'Przydatną opcją jest <-d>[minus d], która powoduje iż <ls>[LS] <m> nie listuje zawartości podanych w linii poleceń katalogów <m> a wypisuje informacje na ich temat. <m>'
			
			'Jest to szczególności przydatne jeżeli korzystamy <m> ze znaków uogólniających do wyboru obiektów o których chcemy uzyskać informacje. <m>'
			'Jeżeli na skutek dopasowania np. do gwiazdki <ls>[LS] otrzyma katalogi <m> to bez opcji <-d>[minus d] wypisze ich zawartość <m> a nie informacje o nich samych, czego na przykład oczekiwaliśmy. <m>'
		]
	},
]

