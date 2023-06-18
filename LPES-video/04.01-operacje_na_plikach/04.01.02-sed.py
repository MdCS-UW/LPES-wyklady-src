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
	{ 'section': 'zautomatyzowana\nedycja plików\n(sed)' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"sed -e '' /etc/networks")],
			["minusn", eduMovie.runCommandString(r"sed -n -e '' /etc/networks")],
			
			["linie", eduMovie.runCommandString(r"sed -n -e '1p' /etc/networks")],
			["linie + 2.3", eduMovie.runCommandString(r"sed -n -e '/lo..b/p' /etc/networks")],
			
			["linie2", eduMovie.runCommandString(r"sed -n -e '0,/lo..b/p' /etc/networks")],
			["linie2 + 2.7", eduMovie.runCommandString(r"sed -n -e '/lo..b/,+2p' /etc/networks")],
		],
		'text' : [
			"Kolejną komendą wykonującą operacje na plikach jest sed. <m>"
			"""Jest to kolejny edytor tekstu który poznamy, <m> jest on raczej mniej "przyjazny" od vim'a, mimo to jest bardzo użyteczny. <m>"""
			'Sed umożliwia edytowanie plików z bezpośrednio linii komend, <m> w ramach opcji <-e>[minus E małe] przyjmuje polecenia które ma wykonać na treści pliku. <m>'
			"Ścieżka do pliku może zostać podana w linii poleceń <m> lub jego treść może zostać przekazana na standardowe wejście sed'a. <m>"
			"Sed zmodyfikowany plik domyślnie wypisuje na standardowe wyjście. <m>"
			'Na ekranie widzimy domyślne zachowanie seda wywołanego <m> z pustym zbiorem komend, czyli wypisanie podanego pliku bez zmian. <mark name="minusn" />'
			
			'Dodając opcję  <-n>[minus n] możemy wyłączyć domyślne wypisywanie, <m> co spowoduje że wypisane zostaną jedynie linie dla których wykonamy komendę p. <mark name="linie" />'
			
			"Z użyciem sed'a możemy także wykonywać operacje na wskazanych liniach. <m>"
			'Do ich określenia możemy użyć na przykład numerów linii <m> lub opisać wyrażeniami regularnymi, podawanymi w ukośnikach. <mark name="linie2" />'
			'Z użyciem przecinka możliwe jest podawanie zakresów, <m> także używając do tego wyrażenia regularnego. <m>'
			
			'Dla pojedynczego wskazania zakresu linii możemy wykonać wiele <m> poleceń grupując je w nawiasach klamrowych i rozdzielając średnikami. <m>'
			'W ten sposób sed pozwala także na symulowanie zakresów wstecz <m> (<np.>[na przykład] <5>[pięć] ostatnich linii lub linia przed pasującą do wyrażenia regularnego) <m> jednak składnia jest dość egzotyczna. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"sed -e 's@def@DEF@g' /etc/networks")],
			["sedy", eduMovie.runCommandString(r"sed -e 'y@la@XY@' /etc/networks")],
			["ERE", eduMovie.runCommandString(r"sed -E -e 's@lo(..)@-\1-@g' /etc/networks")],
		],
		'text' : [
			"Jedną z bardziej użytecznych i częściej stosowanych komend sed'a <m> jest poznana już wcześniej komenda wyszukaj i zastąp. <m>"
			"Omawialiśmy ją w przypadku edytora vi oraz pythonowych wyrażeń regularnych. <m>"
			"Komenda ta ma identyczną składnie jak w <vim'ie>[wimie]: <m> po s podajemy dowolnie wybrany separator (np. małpa, krzyżyk, ukośnik) <m> i wyrażenie regularne określające ciąg który ma zostać wyszukany i zastąpiony. <m>"
			"Następnie ponownie ten sam separator <m> i ciąg którym wyszukany tekst ma zostać zastąpiony. <m>"
			"Polecenie kończymy podaniem po raz trzeci tego samego separatora <m> i opcjonalnie flag tej komendy - takich jak g, <m> które powoduje zastąpienie wszystkich wystąpień w linii. <m>"
			'W odróżnieniu od vima nie musimy podawać zakresu, <m> jeżeli zamiany chcemy wykonać w całym pliku, <m> gdyż w sed jeżeli nie podano zakresu linii to <m> polecenie stosowane jest do wszystkich linii. <mark name="sedy" />'
			
			"Inną przydatną komendą sed'a jest komenda <y>[ygrek] <m> która powoduje mapowanie znaków z pierwszego zbioru <m> na znaki z drugiego zbioru według kolejności. <m>"
			'Czyli pierwszy znak z pierwszego zbioru <m> zostanie zastąpiony pierwszym znakiem z drugiego, <m> drugi drugim, i tak dalej. <mark name="ERE" />'
			
			'Sed domyślnie używa podstawowych wyrażeń regularnych <m> i żeby używał on rozszerzonych podajemy opcję <-E>[minus E duże]. <m>'
			'Na ekranie widzimy przykład zastosowania <m> referencji wstecznych w poleceniu wyszukaj i zastąp. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["minusi - 2.0", eduMovie.runCommandString(r"cp /etc/networks /tmp/networks")],
			["minusi", eduMovie.runCommandString(r"sed -E -e 's@lo(..)@-\1-@g' -i /tmp/networks")],
			["minusi + 1", eduMovie.runCommandString(r"cat /tmp/networks")],
		],
		'text' : [
			"Polecenia sed'owe zamiast być podawane w linii poleceń w opcji <-e>[minus e] <m> mogą być wczytane z pliku przy pomocy opcji <-f>[minus f], <m> co może być wygodne przy dłuższych bardziej rozbudowanych skryptach sed'owych. <m>"
			'Tak jak na wstępie zauważyliśmy sed zmodyfikowaną wersję pliku <m> wypisuje na ekran, ale jeżeli chcielibyśmy żeby modyfikował <mark name="minusi" /> plik w miejscu, czyli zmienił zawartość pliku wskazanego do edycji <m>'
				'to możemy skorzystać z opcji <-i>[minus I]. <m>'
			"Na przykład połączenie sed'a z opcją <-i>[minus I] oraz działającego <m> rekurencyjnie grep'a umożliwia łatwe stworzenie polecenia, <m> które wyszukuje dany tekst we wszystkich plikach i zamienia go na inny. <m>"
		]
	},
]
