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
	{ 'section': 'archiwizacja \n i kopiowanie zdalne' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"tar -cf /tmp/abc.tgz  /etc/passwd /etc/group /bin/ls")],
			[5.0, eduMovie.runCommandString(r"cd /tmp; tar -xvf abc.tgz")],
		],
		'text' : [
			'Niekiedy zachodzi potrzeba zawarcia wielu plików w ramach pojedynczego <m> pliku, czyli utworzenia archiwum. <m>'
			'Najpopularniejszą komendą która na to pozwala jest tar. <m>'
			'Polecenie to przyjmuje opcje określające działania, <m> które mają być wykonane na archiwum, <m>'
			'takie jak <-c>[minus c] utworzenie bądź nadpisanie archiwum, <m> <-x>[minus x] wypakowanie z archiwum. <m>'
			'Ścieżkę do archiwum podaje się jako argument opcji <-f>[minus f], <m> a jako argumenty programu podaje się pliki do umieszczenia w archiwum. <m>'
			
			'Standardowo archiwa tworzone przez tar nie są skompresowane, <m> możemy to włączyć odpowiednimi opcjami na przykład: <m> <-z>[minus Zet] (kompresja <gzip>[G ZIP]), <-j>[minus j] (kompresja <bzip>[B ZIP]). <m>'
		]
	},
	{
		'console': [
			[0.06145, "o", eduMovie.prompt()],
			[0.878152, "o", "z"],
			[1.295432, "o", "\u0007"],
			[1.447413, "o", "\r\nzap         zcmp        zeisstopnm  zgrep       zless       \r\nzbarcam     zdiff       zenity      zipdetails  zmore       \r\n"],
			[1.447831, "o", "zbarimg     zdump       zfgrep      zipgrep     znew        \r\nzcat        zegrep      zforce      zipinfo     \r\n" + eduMovie.prompt() + "z"],
			[3.02899, "o", "\b\u001b[K"],
			[3.757187, "o", "b"],
			[4.389197, "o", "z"],
			[4.799194, "o", "\u0007"],
			[4.935097, "o", "\r\nbzcat         bzegrep       bzgrep        bzless        bzr.bzr\r\n"],
			[4.935388, "o", "bzcmp         bzexe         bzip2         bzmore        \r\nbzdiff        bzfgrep       bzip2recover  bzr           \r\n" + eduMovie.prompt() + "bz"],
			[5.973232, "o", "\b\u001b[K"],
			[6.132996, "o", "\b\u001b[K"],
			[6.92533, "o", "x"],
			[7.18123, "o", "z"],
			[7.629814, "o", "\u0007"],
			[7.783058, "o", "\r\nxz       xzcmp    xzegrep  xzgrep   xzmore   \r\n"],
			[7.783363, "o", "xzcat    xzdiff   xzfgrep  xzless   \r\n" + eduMovie.prompt() + "xz"],
		],
		'text' : [
			# Ekran: tab tab na z  bz  xz ...
			"Kompresji możemy też używać niezależnie <m> przy pomocy programów takich jak gzip, <bzip2>[B ZIP dwa], <xz>[X Zet]. <m>"
			"W systemie często są dostępne polecenia pozwalające operować bezpośrednio <m> na skmpresowanych plikach takie jak na przykład <zless>[Zet LESS] <m> uruchamiający less'a na zawartości pliku skompresowanego <gzip'em>[G Zipem], <m>"
			'<bzgrep>[B Zet grep] uruchamiający grepa na pliku <m> skompresowanym <bzip2>[B ZIP dwa], i tak dalej. <m>'
		]
	},
	{
		'console': [
			[0.0, "x", eduMovie.clear + eduMovie.prompt() + "scp  sciezka/do/pliku.lokalnego  użytkownik@serwer.zdalny:sciezka/na/serwerze/do.pliku\r\n"],
		],
		'text' : [
			'Kopiowanie plików możemy wykonywać nie tylko lokalnie, <m> ale także poprzez sieć komputerową. <m>'
			'Do zdalnego kopiowania służy komenda <scp>[SCP], <m> która działa podobnie jak zwykłe <cp>[CP], <m>'
			'tyle że jako jeden z argumentów przyjmuje coś w postaci: <user@host:scieżka>[user małpa host dwukropek ścieżka] <m> i przy pomocy dostępu <SSH>[eses H] do tego hosta wykonuje kopiowanie. <m>'
			'Nazwa użytkownika oczywiście tak jak w <SSH>[eses H] jest opcjonalna <m> – wystarczy <host:scieżka>[host dwukropek ścieżka]. <m>'
			'Podobnie opcjonalna jest ścieżka na systemie zdalnym <m> – jeżeli ją pominiemy plik zostanie zapisany do katalogu domowego <m> wskazanego użytkownika na systemie zdalnym. <m>'
			
			'Bardzo ważny jest natomiast dwukropek, <m> który mówi nam że ścieżka po jego prawej stronie znajduje się <m> na maszynie określonej po jego lewej stronie, <m>'
			'czyli że jest to ścieżka na zdalnym systemie. <m> Jeżeli o nim zapomnimy <scp>[SCP] będzie działał lokalnie <m> i utworzy nam na przykład plik o nazwie <user@host>[user małpa host]. <m>'
			
			'Podobnie jak w <cp>[CP] w <scp>[SCP] żeby kopiować katalogi <m> również musimy podać opcję <-r>[minus r] <m>'
			'W odróżnieniu od <ssh>[S S H] do określenia numeru portu na którym mamy się <m> połączyć z serweram służy opcja <-P>[minus p duże], gdyż opcja p małe działa jak w <cp>[CP]. <m>'
		]
	},
	{
		'console': [
			[0.0, "x", eduMovie.prompt() + "rsync -rtu źródło cel\r\n"],
		],
		'text' : [
			'Użytecznym narzędziem do synchronizacji plików i drzewa katalogów, <m> czyli tworzenia ich kopii i jej utrzymywania <m> (ale w taki sposób aby nie kopiować wielokrotnie tego <m> co nie uległo zmianie) jest <rsync>[R synk]. <m>'
			'Polecenia <rsync>[R synk] możemy używać zarówno lokalnie, <m> jak też możemy go wykorzystać do kopiowania przez sieć <m> – podając ścieżkę zawierającą dwukropek, w taki sposób jak przy poleceniu <scp>[SCP].  <m>'
			
			'Żeby <rsync>[R synk] działał rekurencyjnie, czyli kopiował katalogi wraz <m> z ich zawartością wymagana jest opcja <-r>[minus r], <m> a żeby zachowywał czas modyfikacji <-t>[minus t]. <m>'
			
			'<rsync>[R synk] może identyfikować pliki, które należy przekopiować ze źródła <m> do celu w oparciu o różne kryteria, takie jak: <m>'
			'czas modyfikacji (opcja <-u>[minus u], <m> kopiowane będą tylko pliki nowsze niż znajdujące się na celu), <m> sumy kontrolne (opcja <-c>[minus c], <m> kopiowane będą pliki mające inną sumę kontrolną), i tak dalej. <m>'
			
			'<rsync>[R synk] standardowo nie kasuje plików które są w docelowym katalogu <m> a nie ma ich w źródłowym, można to włączyć przy pomocy opcji <--delete>[minus minus delete]. <m>'
		]
	},
	{
		'console': [
			[0.0, "x", eduMovie.prompt() + "tar -cf - pliki* | ssh user@host 'cat > plik.tar'\r\n"],
			["spakujrozpakuj", "x", eduMovie.prompt() + "tar -cf - pliki* | ssh user@host 'tar -xf - -C /tmp'\r\n"],
			["kompresja", "x", eduMovie.prompt() + "tar -czf - pliki* | ssh user@host 'ssh -xzf - -C /tmp'\r\n"],
		],
		'text' : [
			"W przypadku kopiowania (zwłaszcza przez sieć) wielu małych plików <m> przydatne może być użycie do tego tar'a <m> czyli poznanego już archiwizera umieszczającego wiele plików w jednym strumieniu. <m>"
			'W tym celu w opcji <-f>[minus f] podajemy myślnik oznaczający użycie <m> standardowego wejścia / wyjścia zamiast pliku <m> i wyjście takie przekierowujemy do polecenia <ssh>[S S H]. <m>'
			'W <ssh>[S S H] po stronie zdalnej możemy uruchomić na przykład <m> polecenie cat aby zapisało nam te dane do pliku archiwum <mark name="spakujrozpakuj" />'
			'lub polecenia tar, które od razu wypakuje takie pliki. <m>'
			'Korzystając z opcji <-C>[minus c duże] możemy wskazać katalog <m> do którego mają zostać wypakowane. <mark name="kompresja" />'
			
			'Możemy też dodać kompresje przesyłanych danych <m> dodając do obu wywołań tar na przykład opcję <-z>[minus Zet]. <m>'
			
			'Takie kopiowanie, w odróżnieniu od kopiowania przy pomocy <scp>[SCP], <m> będzie dużo bardziej wydajne w przypadku dużej ilości małych plików, <m>'
			'gdyż <scp>[SCP] wydajnie kopiuje pojedyncze duże pliki, <m> natomiast jest dość powolny w przypadku kopiowania małych plików. <m>'
		]
	},
]
