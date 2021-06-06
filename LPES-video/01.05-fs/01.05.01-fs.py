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
	{ 'title': [ "#01.5", "Struktura", "drzewa katalogów", "" ] },
	
	{ 'comment': 'Struktura systemu plików' },
	{
		'image': [
			[0.0, eduMovie.convertFile("katalogi1.tex", negate=True)]
		],
		'text' : [
			'Warto powiedzieć kilka słów na temat katalogów. <m>'
			'Jak już mówiliśmy systemy uniksowe posiadają drzewiastą <m> strukturę katalogów, zaczynającą się od ukośnika. <m>'
			'Nie mamy tutaj pojęcia osobnych dysków na których są pliki, <m> natomiast poszczególne zasoby dyskowe, systemy plików <m> są montowane, <m> czyli podłączane do drzewa, <m> w katalogach tej struktury. <m>'
			'Oczywiście główny katalog, oznaczany ukośnikiem, <m> też jest zamontowany z jakiegoś systemu plików na jakimś urządzeniu. <m>'

			'Struktura ta jest też trochę ustandaryzowana i na przykład w głównym katalogu, <m> mamy katalogi bin i <sbin>[S bin], które zawierają programy wykonywalne. <m>'
			'W bin są to programy ogólnego użytkowania <m> a w <sbin>[S bin] są to programy przeznaczone raczej dla administratora systemu. <m>'
			'Mamy katalog lib, lub nawet kilka podobnych katalogów, <m> które zawierają biblioteki. <m>'
			
			'Trochę analogiczne drzewo mamy w katalogu <usr>[U S R], <m> gdzie również mamy bin, <sbin>[S bin], lib i kilka innych katalogów. <m>'
			'Klasyczny podział jest taki że tych katalogach bezpośrednio <m> w katalogu głównym znajdują się programy i biblioteki <m> niezbędne do uruchomienia systemu. <m>'
			'Natomiast w <usr>[U S R] są programy i narzędzia oraz biblioteki <m> niebędące niezbędnymi do uruchomienia systemu, <m>'
			'dzięki czemu katalog <usr>[U S R] może być montowany po uruchomieniu systemu <m> i wtedy one stają się dostępne. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("dysk-pdp.svg", margins=0)]
		],
		'text' : [
			'Idea ta wynikała z tego że dawniej, kiedy przestrzeń dyskowa była droga to <m> katalog <usr>[U S R] często był współdzielony przez wiele komputerów. <m>'
			'Z ważniejszych podkatalogów <usr>[U S R] należy wspomnieć o share, <m> przeznaczonym na dane programów nie będące bibliotekami <m> (takie jak dokumentacja, czcionki, ikony, itp.) <m>'
			'oraz local, przeznaczony na programy, biblioteki, i tak dalej <m> instalowane lokalnie, czyli nie pochodzące z repozytoriów danej dystrybucji. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("unixv5.svg", margins=0)]
		],
		'text' : [
	
			'Innym takim podkatalogiem <usr>[U S R] jest include <m> przeznaczony na pliki nagłówkowe C i C++.'
			'Język C jest dość mocno związany z unixami i unixy z C, <m> więc będzie się to nam trochę przenikało. <m>'
			'Język C ma też spore znaczenie systemowe w unixach, <m> czego objawem są na przykład właśnie dedykowane jemu katalogi <m> na dość wysokim poziomie struktury. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("katalogi2.tex", negate=True)]
		],
		'text' : [
			'Wracając do katalogu głównego mamy tam też katalog <etc>[E Te Ce] <m> zawierający ogólnosystemowe pliki konfiguracyjne. <m>'
			'W katalogu var mamy dane programów i usług takie jak na przykład <m> kolejka poczty, harmonogramy, bazy danych <itd.>[i te de] <m>'
				'– rzeczy które nie są danymi użytkownika, a raczej danymi <m> jakiejś aplikacji na przykład bazy danych. <m>'
			'W katalogu home mamy katalogi domowe użytkowników, <m> wyjątkiem tutaj typowo jest root, <m> który ma katalog domowy na poziomie korzenia systemu plików. <m>'
			'Wynika to również z tego względu żeby był on dostępny <m> nawet jeżeli home nie jest zamontowany, <m> ponieważ katalog home często jest trzymany na innym systemie plików <m>'
				'albo nawet montowany zdalnie z innej maszyny, <m> po to aby zapewnić wspólny katalog domowy na wielu różnych komputerach. <m>'
			
			'Mamy także katalog <tmp>[T M P] zawierające pliki tymczasowe, <m> niekiedy jest on nawet na <tmpfs>[T M P FS], czyli nie jest umieszczony <m> na dysku twardym a w pamięci operacyjnej. <m>'
			"W Linux'ach podobne przeznaczenie ma katalog run, przechowujący także <m> dane tymczasowe, ale są to dane działających usług <m> takie jak numery identyfikujące procesy, pliki blokad i tym podobne rzeczy. <m>"
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("katalogi3.tex", negate=True)]
		],
		'text' : [
			'Katalog dev zawiera pliki reprezentujące urządzenia, <m> w Linuxie podobną funkcję pełni też po części katalog sys, <m> który zawiera informacje i ustawienia dotyczące urządzeń. <m>'
			'Zasadnicza różnica jest taka że w dev znajdują sie pliki urządzeń <m> używane w operacjach na nich, a w sys pliki reprezentujące konfigurację tych urządzeń. <m>'
			'Innym katalogiem który zawiera ustawienia konfiguracyjne <m> w przypadku Linuxa jest katalog proc, który oprócz tego <m> (tak jak na każdym systemie uniksowym) <m>'
			'zawiera też podkatalogi o numerycznych nazwach <m> związane z działającymi w systemie procesami. <m>'
		]
	},
]
