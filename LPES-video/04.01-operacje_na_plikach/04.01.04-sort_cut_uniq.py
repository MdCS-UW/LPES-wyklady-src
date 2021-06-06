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
	{ 'comment': 'sort cut paste join comm uniq' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"head /etc/passwd > /tmp/passwd;  head /etc/group > /tmp/group")],
			[1.0, eduMovie.runCommandString(r"sort /tmp/passwd")],
			
			["stdin",   eduMovie.runCommandString(r"du -s /lib/[s-x]* | sort")],
			["numeric", eduMovie.runCommandString(r"du -s /lib/[s-x]* | sort -n")],
			
			["kolumny",  eduMovie.runCommandString(r"sort -k4 -t: /tmp/passwd")],
			["kolumny2", eduMovie.runCommandString(r"sort -k4 -t: -n /tmp/passwd")],
		],
		'text' : [
			'Polecenie sort pozwala nam na sortowanie plików, <m> a dokładniej linii w plikach. <m>'
			'Jeżeli nie podamy żadnej opcji to linie w pliku <m> zostaną posortowane alfabetycznie. <mark name="stdin" />'
			'Jeżeli nie podamy pliku sortowane będzie standardowe wejście. <mark name="numeric" />'
			'Dodanie opcji <-n>[minus n] spowoduje sortowanie po wartościach liczbowych, <m> czyli 1000 zostanie umieszczone po 99. <mark name="kolumny" />'
			
			'Możemy także określić że sortowanie ma się odbywać po konkretnej <m> kolumnie z użyciem opcji <-k>[minus k], jeżeli chcemy sortować po kolumnie <m> to zazwyczaj też określamy jakiś separator kolumn z użyciem opcji <-t>[minus t]. <m>'
			'Na ekranie widzimy przykład sortowania po czwartej kolumnie, <m> gdzie separatorem kolumn jest dwukropek. <mark name="kolumny2" /> Jako że wartości w tej kolumnie są liczbami możemy dodać opcję <-n>[minus n]. <m>'
			
			'Możemy też przy sortowaniu ignorować wielkość liter przy pomocy <-i>[minus i]. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["cut",  eduMovie.runCommandString(r"cut -f6 -d: /tmp/passwd")],
			["cut2", eduMovie.runCommandString(r"cut -f1,2-4 -d: /tmp/passwd")],
			["cut3", eduMovie.runCommandString(r"cut -f4- -d: /tmp/passwd")],
		],
		'text' : [
			'Jeżeli wspomnieliśmy już o kolumnach w pliku <m> to możemy chcieć wypisać tylko wybrane kolumny takiego pliku. <m>'
			'Do tego służy komenda cut, która przyjmuje opcje określające <m> kolumny do wypisania oraz separator. <mark name="cut" />'
			'Niestety nazwy tych opcji są inne niż w wypadku polecenia sort <m> i kolumnę określamy przy pomocy opcji <-f>[minus f] <m> a separator przy pomocy opcji <-d>[minus d]. <mark name="cut2" />'
			
			'Polecenie cut pozwala na podanie zakresu kolumn przy pomocy myślnika, <m> lub zbioru kolumn z użyciem przecinka. <mark name="cut3" />'
			'Jeżeli chcemy wypisać wszystkie kolumny od podanej do końca, <m> nie określamy prawej strony przedziału, <m> zostawiając ją pustą, tak jak widzimy to na ekranie. <m>'
			
			'Wadą polecenia cut jest to iż separator <m> ograniczony jest do pojedynczego znaku, a dokładniej nawet pojedynczego bajtu <m> (czyli nie mogą nim być znaki z poza podstawowego zakresu ASCII). <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"paste -d '@' /etc/networks /tmp/passwd ")],
			["join", eduMovie.runCommandString(r"join -t: -1 4 -2 3 /tmp/passwd /tmp/group")],
		],
		'text' : [
			'Kolejnym poleceniem o którym warto wspomnieć <m> w kontekście plików o strukturze kolumnowej jest komenda paste, <m>'
				'umożliwiająca połączenie linii o takich samych numerach z dwóch plików, <m> w jedną linię z użyciem jakiegoś separatora. <mark name="join" />'
			
			'Możemy również łączyć pliki pod względem pasującego pola <m> przy pomocy komendy join, która działa trochę tak jak join w bazach SQL. <m>'
			'Opcja <-t>[minus t] określa separator pól, opcja <-1>[minus jeden] określa <m> pole z pierwszego pliku, <-2>[minus dwa] pole z drugiego pliku. <m>'
			'Polecenie wypisze złączone linii z obu plików <m> dla których podane pola są równe. <m>'
			
			'W przykładzie widocznym na ekranie uzyskaliśmy połączenie <m> (skróconych na potrzeby tego przykładu) <m> plików <passwd>[pass wu de] i group w oparciu o numer grupy. <m>'
			'Widzimy też że join wypisał komunikat o nie posortowaniu <m> pliku wejściowego – dla poprawnego działania pliki wejściowe <m> powinny być posortowane wg pola używanego do operacji join. <m>'
			
			'Domyślnie join nie wypisze linii do których nie znalazł dopasowania <m> w drugim pliku, można to zmienić odpowiednimi opcjami. <m> Szczegóły w dokumentacji man. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.runCommandString(r"/bin/echo -e 'a\nb\nd' > /tmp/a")],
			[0.0, eduMovie.runCommandString(r"/bin/echo -e 'a\nc\nd' > /tmp/b")],
			[0.5, eduMovie.runCommandString(r"cat /tmp/a")],
			[1.0, eduMovie.runCommandString(r"cat /tmp/b")],
			[2.5, eduMovie.runCommandString(r"comm /tmp/a /tmp/b")],
			
			["uniq - 0.5", eduMovie.runCommandString(r"/bin/echo -e 'a\na\nb\nc\nc\nd' > /tmp/c")],
			["uniq",  eduMovie.runCommandString(r"cat /tmp/c")],
			["uniq + 1.5",  eduMovie.runCommandString(r"uniq /tmp/c")],
			["uniq2", eduMovie.runCommandString(r"uniq -c /tmp/c")],
		],
		'text' : [
			'Podobną komendą jest comm, która porówna dwa posortowane <m> pliki pod względem unikalności linii. <m>'
			'Jak widzimy na ekranie standardowo wypisuje 3 kolumny <m> – w pierwszej linie występujące tylko w pierwszym pliku, <m> w drugiej tylko w drugim a w trzeciej w obu. <m>'
			'To które informacje będą wypisywane można zmieniać odpowiednimi opcjami. <mark name="uniq" />'
			
			'Mamy także komendę uniq, która po prostu wypisuje linie z jakiegoś <m> posortowanego pliku pomijając ich powtórzenia, <m>'
			'czyli jeżeli kilkakrotnie po sobie <m> napotka taką samą linię wypisze ją tylko jeden raz. <mark name="uniq2" />'
			'Przy pomocy odpowiednich opcji może ona zliczać powtórzenia, <m> wypisywać tylko to co się powtarzało, albo to co się nie powtarzało. <m>'
		]
	},
]

if not 'is not sorted' in eduMovie.runCommandString(r"join -t: -1 4 -2 3 /tmp/passwd /tmp/group"):
	logInfo("  Warning: brak komunikatu o nieposortowaniu w join", red)
