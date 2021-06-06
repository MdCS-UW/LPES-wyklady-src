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
	{ 'section': 'system plików \n i katalog roboczy' },
	{
		'console': [
			[0.0, ""],
			["korzen", eduMovie.prompt() + "/"],
			["dir", eduMovie.prompt() + "/etc"],
			["dir + 2.3", eduMovie.prompt() + "/etc/terminfo"],
			["dir + 4.1", eduMovie.prompt() + "/etc/terminfo/README"],
		],
		'text' : [
			'Struktura katalogów i plików  w systemach unixowych ma postać drzewiastą, <m> zaczynającą się od katalogu najwyższego poziomu, <mark name="korzen" /> nazywanego korzeniem i oznaczanego przy pomocy ukośnika. <mark name="dir" />'
			'Wchodząc w jego podkatalogi, ich podkatalogi i tak dalej, <m> możemy dojść do dowolnego pliku w systemie. <m>'
			'Zapisując nazwy katalogów przez które przechodziliśmy <m> i rozdzielając je od siebie oraz od nazwy pliku <m> przy pomocy ukośników tworzymy bezwzględną ścieżkę do danego pliku, <m>'
			'czyli taką która właśnie rozpoczyna się od tego korzenia. <m>'
			
			'Możliwe jest podawanie wszystkich ścieżek jako bezwzględnych, <m> czyli rozpoczynających się od korzenia, <m> jednak w codziennym użytkowaniu systemu niekoniecznie byłoby to wygodne. <m>'
			'W wielu wypadkach chcemy móc wyrazić ścieżkę względem <m> jakiegoś katalogu i w tym celu stosuje się ścieżki względne. <m>'
			
			'Katalogiem względem którego wyrażana jest ścieżka względna <m> może być katalog, w którym znajduje się obiekt ją zawierający <m>'
			'lub znacznie częściej jest to tak zwany <m> bieżący katalog roboczy programu korzystającego z tej ścieżki. <m>'
			'Powłoka przechowuje informacje na temat ścieżki, <m> w której się aktualnie znajduje, <m> czyli względem której mają być interpretowane ścieżki względne <m> i udostępnia ją uruchamianym programom. <m>'
			'Informację tą możemy wypisać przy pomocy polecenia <pwd>[Pe Wu De], <m> często jest podawana także przed znakiem zachęty, <m> a modyfikowana może ona być przy pomocy polecenia <cd>[Ce De]. <m>'
		]
	},
	{
		'console': [
			[0.068947, "o", eduMovie.clear + eduMovie.prompt()],
			[1.315111, "o", "c"],
			[1.402979, "o", "d"],
			[1.62692, "o", " "],
			[1.755069, "o", "/"],
			[2.162973, "o", "u"],
			[2.706992, "o", "s"],
			[4.300704, "o", "r/"],
			[4.634957, "o", "b"],
			[5.050915, "o", "i"],
			[5.34105, "o", "n/"],
			[5.906948, "o", "\r\n"],
			[5.90802, "o", eduMovie.prompt("/usr/bin")],
			[6.666993, "o", "p"],
			[6.882877, "o", "w"],
			[7.106868, "o", "d"],
			[7.722933, "o", "\r\n"],
			[7.723305, "o", "/usr/bin\r\n"],
			[7.723777, "o", eduMovie.prompt("/usr/bin")],
			[10.082957, "o", "c"],
			[10.178861, "o", "d"],
			[10.394925, "o", " "],
			[11.066935, "o", "."],
			[11.250735, "o", "."],
			[11.474758, "o", "/"],
			[12.010871, "o", "l"],
			[12.266774, "o", "o"],
			[12.468549, "o", "cal/"],
			[13.218902, "o", "s"],
			[13.474884, "o", "b"],
			[13.700372, "o", "in/"],
			[14.354853, "o", "\r\n"],
			[14.355998, "o", eduMovie.prompt("/usr/local/sbin")],
			[15.33892, "o", "p"],
			[15.530802, "o", "w"],
			[15.786796, "o", "d"],
			[16.033748, "o", "\r\n"],
			[16.034748, "o", "/usr/bin/sbin\r\n"],
			[16.035731, "o", eduMovie.prompt("/usr/local/sbin")],
			[17.082857, "o", "c"],
			[17.178768, "o", "d"],
			[17.402814, "o", " "],
			[17.650857, "o", "/"],
			[18.474837, "o", "e"],
			[18.754726, "o", "t"],
			[19.074752, "o", "c"],
			[19.722815, "o", "\r\n"],
			[19.723913, "o", eduMovie.prompt("/etc")],
			[20.674843, "o", "p"],
			[20.858746, "o", "w"],
			[21.08273, "o", "d"],
			[21.274696, "o", "\r\n"],
			[21.275005, "o", "/etc\r\n"],
			[21.275593, "o", eduMovie.prompt("/etc")],
			[23.082957, "o", "c"],
			[23.178861, "o", "d"],
			[23.394925, "o", " "],
			[24.066935, "o", "/"],
			[24.250735, "o", "u"],
			[24.474758, "o", "s"],
			[26.010871, "o", "r"],
			[26.266774, "o", "o"],
			[26.468549, "o", eduMovie.prompt("/usr")],
			[27.082857, "o", "c"],
			[27.178768, "o", "d"],
			[27.402814, "o", " "],
			[27.650857, "o", "."],
			[28.474837, "o", "/"],
			[28.754726, "o", "b"],
			[29.074752, "o", "i"],
			[29.574752, "o", "n"],
			[29.922815, "o", "\r\n"],
			[29.922815, "o", eduMovie.prompt("/usr/bin")],
		],
		'text' : [
			# Ekran: kilka cd pwd
			'Ważnym elementem składowym ścieżek względnych są dwie kropki <m> oznaczające katalog nadrzędny. <m>'
			'Pozwalają one nam z dowolnego katalogu wrócić ścieżką względną <m> nawet aż do korzenia, a zatem dojść także do dowolnego innego pliku w naszym drzewie. <m>'
			'Pojedyncza kropka oznacza aktualny katalog w ścieżce, <m> czyli jeżeli jest na początku ścieżki to oznacza katalog względem <m> którego jest interpretowana ścieżka względna (na przykład bieżący katalog roboczy). <m>'

			'Sama nazwa pliku lub katalogu również stanowi ścieżkę względną <m> (względem katalogu w którym się on znajduje), <m>'
			'niekiedy jednak stosowany jest zapis kropka ukośnik nazwa pliku, <m> który pozwala na bardziej jednoznaczne zasugerowanie iż mamy na myśli ścieżkę a nie jakąś nazwę. <m>'
			'Dotyczy to zwłaszcza uruchamiania programów <m> znajdujących się w bieżącym katalogu, gdyż w tym wypadku nazwa polecenia <m> nie zawierająca ukośnika nie jest traktowana jako ścieżka. <m>'
		]
	},
	{
		'console': [
			[0.0, "cd /usr/local/./bin/../sbin/"],
			[1.7, "\r\n"],
			[1.701315, "o", eduMovie.prompt("/usr/local/sbin")],
		],
		'text' : [
			'Dwie kropki jak i pojedyncza kropka mogą wystąpić także wewnątrz <m> ścieżki i odnoszą się one wtedy do katalogu określonego <m> ścieżką opisaną po ich lewej stronie. <m>'
			'W prezentowanym na ekranie przykładzie kropka w ścieżce oznacza <m> katalog local, a dwie kropki oznaczą katalog nadrzędny <m> w stosunku co do bin. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"realpath /usr/local/./bin/../sbin/")]
		],
		'text' : [
			'Zapis taki jest nadmiarowy i może zostać uproszczony <m> na przykład z użyciem polecenia realpath, <m> jednak jest dopuszczalny i potrafi ułatwiać tworzenie ścieżek. <m>'
		]
	},
	{
		'console': [
			[1.137858, "o", "c"],
			[1.265743, "o", "d"],
			[1.705785, "o", "\r\n"],
			[1.706639, "o", eduMovie.prompt("~")],
			[2.433828, "o", "c"],
			[2.497789, "o", "d"],
			[2.721774, "o", " "],
			[2.937837, "o", "/"],
			[3.257798, "o", "\r\n"],
			[3.25881, "o", eduMovie.prompt("/")],
			[4.081833, "o", "c"],
			[4.209738, "o", "d"],
			[4.401658, "o", " "],
			[4.873895, "o", "~"],
			[5.225705, "o", "\r\n"],
			[5.226465, "o", eduMovie.prompt("~")],
		],
		'text' : [
			# Ekran: cd; cd /; cd ~
			'Polecenie <cd>[Ce De] wywołane bez argumentów ustawi bieżący katalog roboczy <m> na katalog domowy bieżącego użytkownika oznaczany także tyldą, <m> a zatem <cd>[Ce De] tylda zadziała identycznie. <m>'
			'Stosując zapis tylda nazwa użytkownika <m> możemy się odwołać do katalogu domowego wskazanego użytkownika. <m>'
		]
	},
	{
		'console': [
			[1.0, eduMovie.runCommandString(r'echo "Ala ma kota" > "xYą→€t∞.龍;&.>?.t"', cwd="/tmp")],
			[4.0, eduMovie.runCommandString(r'ls xY*', cwd="/tmp")],
			[9.0, eduMovie.runCommandString(r'cat "xYą→€t∞.龍;&.>?.t"', cwd="/tmp")],
		],
		'text' : [
			# Ekran: utworzenie i wypisanie plików z dziwnymi znaczkami w nazwie (polskie, chińskie, pytajnik gwizdka, apaersand, wieloma kropkami, etc)
			'Nazwy plików i katalogów mogą zawierać dowolne znaki z wyjątkiem ukośnika. <m>'
			'Przy odwołaniach do plików w nazwach których są znaki pełniące inne funkcje <m> (takie jak np. spacja, średnik, znaki większości, itd.) <m>'
			'powinny one być zabezpieczone przed interpretacją <m> ich w sposób standardowy (np. poprzez ujęcie ich w cudzysłów). <m>'
			'W nazwach rozróżniane są małe i wielkie litery. <m>'
			
			'Pliki mogą, ale nie muszą mieć rozszerzeń określających ich typ, <m> a kropka może występować wielokrotnie w nazwie pliku lub katalogu. <m>'
			'Znaki z poza podstawowego zestawu ASCII <m>'
			'(obejmującego 95 znaków drukowanych, na które składają się małe <m> i wielkie litery alfabetu łacińskiego, cyfry i znaki specjalne takie jak spacja, <m> nawiasy, kropki, przecinki, etc.) <m>'
			'kodowane są na ogół z użyciem UTF-8, <m> co pozwala na stosowanie dowolnych znaków z innych alfabetów <m> (np. polskich ogonków, chińskich krzaczków itd.). <m>'
			
			'Pliki i katalogi, których nazwa zaczyna się od kropki, <m> traktowane są jako pliki ukryte i przez wiele programów <m> nie będą domyślnie pokazywane. <m>'
		]
	},
]
