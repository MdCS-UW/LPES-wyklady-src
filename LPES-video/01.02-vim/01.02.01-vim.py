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
	{ 'title': [ "#01.2", "Edytor", "vi i vim", "" ] },
	
	{ 'comment': 'vim' },
	{
		'console': [
			[0.0, eduMovie.prompt()],
		],
		'text' : [
			"Nauczyliśmy się już oglądać pliki przy pomocy na przykład less'a <m> ale oprócz oglądania plików przydatna jest też umiejętność <m> ich edycji czyli możliwość modyfikacji zawartości takiego pliku. <m>"
			
			"Najbardziej zaawansowanym edytorem którego obecność gwarantuje nam <m> standard POSIX (określający właśnie czym jest uniksowy system operacyjny, <m> jakie wymagania powinien spełniać, itd.) jest vi. <m>"
			"Pomimo że jest to najbardziej zaawansowany edytor którego obecność <m> gwarantuję standard nie jest on bardzo wygodnym edytorem <m> dlatego dużo częściej używa się jego rozbudowanego klonu pod nazwą vim. <m>"
			"Na wielu systemach również sam vi odpala vim'a <m> niekiedy w trybie kompatybilności z vi, a niekiedy nie. <m>"
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('edytory.svg')],
		],
		'text' : [
			"Oczywiście oprócz vim'a często mamy wiele innych edytorów <m> – zarówno prostszych, o mniejszych możliwościach <m> ale bardziej przyjaznych użytkownikowi, <m>"
			'jak też podobnie zaawansowanych i skomplikowanych, zarówno <m> pracujących w trybie tekstowym (w terminalu) <m> jak i pracujących w środowisku graficznym. <m>'
			'Jednak jako że vi jest standardem warto opanować przynajmniej jego podstawy. <m>'
		]
	},
	{
		'console': [
			[0.0, "o", eduMovie.prompt()],
			[1.55463, "o", "v"],
			[1.77041, "o", "i"],
			[2.02641, "o", " "],
			[2.282273, "o", "/"],
			[2.466388, "o", "e"],
			[2.754359, "o", "t"],
			[2.869216, "o", "c/"],
			[3.610322, "o", "i"],
			[3.802428, "o", "s"],
			[3.962426, "o", "s"],
			[4.168136, "o", "\u0007ue"],
			[4.596491, "o", "\r\n"],
			[4.618182, "o", "\u001b[?1000h\u001b[?2004h\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\u001b[?2004h\u001b[1;23r\u001b[?12h\u001b[?12l\u001b[22;2t\u001b[22;1t"],
			[4.618551, "o", "\u001b[27m\u001b[23m\u001b[29m\u001b[m\u001b[H\u001b[2J\u001b[?25l\u001b[23;1H\"/etc/issue\" [readonly] 2L, 27C"],
			[4.620299, "o", "\u001b[2;1H▽\u001b[6n\u001b[2;1H  \u001b[1;1H\u001b[>c\u001b]10;?\u0007\u001b]11;?\u0007"],
			[4.620663, "o", "\u001b[1;1H\u001b[1m\u001b[33m  1 \u001b[mDebian GNU/Linux 10 \\n \\l\r\n\u001b[1m\u001b[33m  2 \u001b[m\r\n\u001b[312m~                                                                               \u001b[4;1H~                                                                               \u001b[5;1H~                                                                               \u001b[6;1H~                                                                               \u001b[7;1H~                                                                               \u001b[8;1H~                                                                               \u001b[9;1H~                                                                               \u001b[10;1H~                                                                               \u001b[11;1H~                                                                               \u001b[12;1H~                                                                               \u001b[13;1H~                                                                               \u001b[14;1H"],
			[4.620762, "o", "~                                                                               \u001b[15;1H~                                                                               \u001b[16;1H~                                                                               \u001b[17;1H~                                                                               \u001b[18;1H~                                                                               \u001b[19;1H~                                                                               \u001b[20;1H~                                                                               \u001b[21;1H~                                                                               \u001b[m\u001b[22;1H\u001b[1m\u001b[7m/etc/issue [RO]                                               1,24           All\u001b]2;issue (/etc)\u0007\u001b[1;28H\u001b[?25h"],
			[6.555314, "o", "\u001b[?25l\u001b[22;63H2,0-1\u001b[2;5H\u001b[?25h"],
			["wstawianie + 0.274755", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[1m-- INSERT --\u001b[m\u001b[23;14H\u001b[K\u001b[23;14H\u001b[1m\u001b[31mW10: Warning: Changing a readonly file\u001b[?1000l\u001b[?2004l"],
			["wstawianie + 1.275016", "o", "\u001b[?1000h\u001b[?2004h"],
			["wstawianie + 1.276471", "o", "\u001b[m\u001b[2;5Ha\u001b[22;13H\u001b[1m\u001b[7m+][RO]\u001b[46C2   \u001b]2;issue + (/etc)\u0007\u001b[2;6H\u001b[?25h"],
			["wstawianie + 1.515227", "o", "\u001b[?25l\u001b[mb\u001b[22;65H\u001b[1m\u001b[7m3 \u001b[2;7H\u001b[?25h"],
			["wstawianie + 1.923669", "o", "\u001b[?25l\u001b[mc\u001b[22;65H\u001b[1m\u001b[7m4 \u001b[2;8H\u001b[?25h"],
			["wstawianie + 2.211535", "o", "\u001b[?25l\u001b[md\u001b[22;65H\u001b[1m\u001b[7m5 \u001b[2;9H\u001b[?25h"],
			["wstawianie + 3.347779", "o", "\u001b[?25l\u001b[22;65H6 \u001b[2;10H\u001b[?25h"],
			["wstawianie + 3.923733", "o", "\u001b[?25l\u001b[me\u001b[22;65H\u001b[1m\u001b[7m7 \u001b[2;11H\u001b[?25h"],
			["wstawianie + 4.267683", "o", "\u001b[?25l\u001b[mf\u001b[22;65H\u001b[1m\u001b[7m8 \u001b[2;12H\u001b[?25h"],
			["wstawianie + 4.555644", "o", "\u001b[?25l\u001b[mg\u001b[22;65H\u001b[1m\u001b[7m9 \u001b[2;13H\u001b[?25h"],
			["wstawianie + 4.835589", "o", "\u001b[?25l\u001b[mh\u001b[22;65H\u001b[1m\u001b[7m10\u001b[2;14H\u001b[?25h"],
			["zastepowanie + 0.143776", "o", "\u001b[m\u001b[23;1H\u001b[K\u001b[2;13H"],
			["zastepowanie + 0.445009", "o", "\u001b[?25l"],
			["zastepowanie + 0.445655", "o", "\u001b[22;65H\u001b[1m\u001b[7m9  \u001b[2;13H\u001b[?25h"],
			["zastepowanie + 1.395391", "o", "\u001b[?25l\u001b[22;65H8 \u001b[2;12H\u001b[?25h"],
			["zastepowanie + 2.79545", "o", "\u001b[?25l\u001b[22;63H1,\u001b[1;12H\u001b[?25h"],
			["zastepowanie + 3.1379013", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[1m-- INSERT --\u001b[1;12H\u001b[?25h"],
			["zastepowanie + 3.138984", "o", "\u001b[?25l\u001b[23;4HREPLACE --\u001b[1;12H\u001b[?25h"],
			["zastepowanie + 3.443782", "o", "\u001b[?25l\u001b[mX\u001b[22;65H\u001b[1m\u001b[7m9 \u001b[1;13H\u001b[?25h"],
			["zastepowanie + 3.947817", "o", "\u001b[?25l\u001b[mX\u001b[22;65H\u001b[1m\u001b[7m10\u001b[1;14H\u001b[?25h"],
			["zastepowanie + 4.427865", "o", "\u001b[?25l\u001b[mX\u001b[22;66H\u001b[1m\u001b[7m1 \u001b[1;15H\u001b[?25h"],
			["zastepowanie + 5.835132", "o", "\u001b[?25l\u001b[22;66H2 \u001b[1;16H\u001b[?25h"],
			["zastepowanie + 5.843227", "o", "\u001b[?25l\u001b[my\u001b[22;66H\u001b[1m\u001b[7m3 \u001b[1;17H\u001b[?25h"],
			["zastepowanie + 6.355841", "o", "\u001b[?25l\u001b[my\u001b[22;66H\u001b[1m\u001b[7m4 \u001b[1;18H\u001b[?25h"],
			["zastepowanie + 6.923826", "o", "\u001b[?25l\u001b[my\u001b[22;66H\u001b[1m\u001b[7m5 \u001b[1;19H\u001b[?25h"],
			["zastepowanie + 7.459781", "o", "\u001b[?25l\u001b[my\u001b[22;66H\u001b[1m\u001b[7m6 \u001b[1;20H\u001b[?25h"],
			["zastepowanie + 8.059741", "o", "\u001b[?25l\u001b[my\u001b[22;66H\u001b[1m\u001b[7m7 \u001b[1;21H\u001b[?25h"],
			["zastepowanie + 9.667834", "o", "\u001b[m\u001b[23;1H\u001b[K\u001b[1;20H"],
			["zastepowanie + 10.669055", "o", "\u001b[?25l"],
			["zastepowanie + 10.669652", "o", "\u001b[22;66H\u001b[1m\u001b[7m6 \u001b[1;20H\u001b[?25h"],
			["wizualny + 0.011458", "o", "\u001b[?25l\u001b[22;66H7 \u001b[1;21H\u001b[?25h"],
			["wizualny + 0.483034", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[1m-- VISUAL --\u001b[1;21H\u001b[?25h"],
			["wizualny + 1.211577", "o", "\u001b[?25l\u001b[m\u001b[7m \u001b[m\u001b[22;66H\u001b[1m\u001b[7m6 \u001b[1;20H\u001b[?25h"],
			["wizualny + 1.871225", "o", "\u001b[?25l\u001b[m\u001b[7my\u001b[m\u001b[22;66H\u001b[1m\u001b[7m5 \u001b[1;19H\u001b[?25h"],
			["wizualny + 2.067403", "o", "\u001b[?25l\u001b[m\u001b[7my\u001b[m\u001b[22;66H\u001b[1m\u001b[7m4 \u001b[1;18H\u001b[?25h"],
			["wizualny + 2.251349", "o", "\u001b[?25l\u001b[m\u001b[7my\u001b[m\u001b[22;66H\u001b[1m\u001b[7m3 \u001b[1;17H\u001b[?25h"],
			["wizualny + 2.411421", "o", "\u001b[?25l\u001b[m\u001b[7my\u001b[m\u001b[22;66H\u001b[1m\u001b[7m2 \u001b[1;16H\u001b[?25h"],
			["wizualny + 2.571398", "o", "\u001b[?25l\u001b[m\u001b[7my\u001b[m\u001b[22;66H\u001b[1m\u001b[7m1 \u001b[1;15H\u001b[?25h"],
			["wizualny + 2.73147", "o", "\u001b[?25l\u001b[m\u001b[7m/\u001b[m\u001b[22;66H\u001b[1m\u001b[7m0 \u001b[1;14H\u001b[?25h"],
			["wizualny + 2.92337", "o", "\u001b[?25l\u001b[m\u001b[7mX\u001b[m\u001b[22;65H\u001b[1m\u001b[7m9  \u001b[1;13H\u001b[?25h"],
			["wizualny + 3.107348", "o", "\u001b[?25l\u001b[m\u001b[7mX\u001b[m\u001b[22;65H\u001b[1m\u001b[7m8 \u001b[1;12H\u001b[?25h"],
			["wizualny + 5.3879", "o", "\u001b[?25l\u001b[m10 \\n \\l\u001b[1;20H\u001b[K\u001b[23;1H\u001b[K\u001b[1;12H\u001b[?25h"],
			["wklejanie + 0.0299555", "o", "\u001b[?25l\u001b[22;63H\u001b[1m\u001b[7m2,\u001b[2;12H\u001b[?25h"],
			["wklejanie + 0.692075", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[1m-- INSERT --\u001b[m\u001b[3;1H\u001b[1m\u001b[33m  3 \u001b[m\u001b[3;5H\u001b[K\u001b[22;63H\u001b[1m\u001b[7m3,1 \u001b[3;5H\u001b[?25h"],
			["wklejanie + 1.291993", "o", "\u001b[m\u001b[23;1H\u001b[K\u001b[3;5H"],
			["wklejanie + 2.293211", "o", "\u001b[?25l"],
			["wklejanie + 2.293639", "o", "\u001b[22;65H\u001b[1m\u001b[7m0-1\u001b[3;5H\u001b[?25h"],
			["wklejanie + 2.883951", "o", "\u001b[?25l\u001b[mXXX/yyyyy\u001b[22;65H\u001b[1m\u001b[7m10  \u001b[3;14H\u001b[?25h"],
			["wklejanie + 5.131935", "o", "\u001b[?25l\u001b[mXXX/yyyyy\u001b[22;66H\u001b[1m\u001b[7m9 \u001b[3;23H\u001b[?25h"],
		],
		'text' : [
			"Typowo po uruchomieniu vim'a znajdujemy się w jednym <m> z trzech trybów pracy nazywanym trybem komend. <m>"
			'Służy on do wydawania różnego rodzaju poleceń – mogą to być polecenia <m> wprowadzane bezpośrednio, stanowiące odpowiednik skrótów klawiszowych, <m>'
			'albo polecenia rozpoczynające się od dwukropka <m> – wprowadzane w ramach linii poleceń edytora. <mark name="wstawianie" />'
			
			"Jeżeli chcemy móc wprowadzać jakiś tekst do pliku musimy <m> przejść do innego trybu, nazywanego trybem edycji, <m> poprzez naciśnięcie na przykład klawisza <i>[I], <m>"
			"w efekcie czego uruchomiony zostaje tryb edycji <m> w którym możemy wpisywać dowolny tekst w treści pliku. <m>"
			"W większości przypadków, będziemy mogli także poruszać się <m> po tekście z użyciem klawiszy strzałek bez opuszczania trybu edycji. <m>"
			"W trybie komend po tekście możemy poruszać się strzałkami lub klawiszami h j k l. <m>",
			
			'Aby powrócić z każdego trybu do trybu komend korzystamy z przycisku Escape. <mark name="zastepowanie" />'
			
			"Pod-trybem trybu edycji jest tryb zastępowania, <m> który działa w ten sposób że wprowadzamy dane, tak jak w trybie edycji, <m>"
			"ale wprowadzamy je na miejsce istniejących danych, <m> czyli zastępujemy to co znajdowało się pod kursorem wprowadzanymi danymi. <m>"
			'Przy pomocy klawisza insert możemy przełączać się pomiędzy <m> trybem wprowadzania a trybem nadpisywania. <mark name="wizualny" />'
			
			'Kolejnym trybem pracy edytora vim jest tryb wizualny, <m> który pozwala nam na wizualne zaznaczanie jakiegoś fragmentu tekstu <m> i wykonanie na nim operacji na przykład jego usunięcia. <mark name="wklejanie" />'
			
			"Usuwanie, kopiowanie i tego typu operacji wykonywane są w trybie komend <m> (lub po zaznaczeniu fragmentu w trybie wizualnym) <m> i służą do tego odpowiednie skróty klawiszowe. <m>"
			"x - kasuje znak pod kursorem lub zaznaczony fragment, <m> bardziej uniwersalny jest d, <m> który wymaga określenia po nim kierunku kasowania <m> przy pomocy klawiszy strzałek lub klawiszy h j k l. <m>"
			'Na przykład <dl>[De L] lub <d>[De] <break time="100ms"/> strzałka w prawo działa jak x, kasując <m> jeden znak pod kursorem, a <dh>[De Ha] lub <d>[De] <break time="100ms"/> strzałka w lewo kasuje znak przed kursorem. <m>'
			
			"Zarówno x, d jak i inne tego typu polecenia (np. kopiujące, wklejające, etc.) <m> mogą być poprzedzone liczbą określającą krotność operacji. <m>"
			"Na przykład <4dl>[4 De L] skasuje 4 znaki w prawo rozpoczynając <m> od znaku na którym znajduje się kursor. <m>"
			
			"Kasowane ciągi znaków zapisywane są do schowka, <m> którego zawartość możemy wklejać za pomocą p lub shift p. <m>"
			"Małe p wkleja po znaku na którym znajduje się kursor, <m> natomiast shift p, czyli duże p wkleja przed tym znakiem. <m>"
			"Oczywiście aby umieścić coś w tym schowku nie musimy tego kasować <m> – możemy w tym celu użyć klawisza y, działającego analogicznie jak d. <m>"
			"Podwójne użycie klawiszy d lub y skasuje lub skopiuje bieżącą linię, <m> a jeżeli jest poprzedzone liczbą to skasuje lub skopiuje taką <m> liczbę linii poczynając od bieżącej. <m>"
			
			"Należy mieć na uwadze iż komendy te nie są nigdzie <m> wyświetlane podczas ich wprowadzania."
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear],
			[1.575636, "o", "\u001b[?1000h\u001b[?2004h\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\u001b[?2004h\u001b[1;23r\u001b[?12h\u001b[?12l\u001b[22;2t\u001b[22;1t"],
			[1.576059, "o", "\u001b[27m\u001b[23m\u001b[29m\u001b[m\u001b[H\u001b[2J\u001b[?25l\u001b[23;1H\"/etc/passwd\" [readonly] 36L, 1878C"],
			[1.57725, "o", "\u001b[2;1H▽\u001b[6n\u001b[2;1H  \u001b[1;1H\u001b[>c\u001b]10;?\u0007\u001b]11;?\u0007"],
			[1.578141, "o", "\u001b[1;1H\u001b[1m\u001b[33m  1 \u001b[m\u001b[1m\u001b[36mroot\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m0\u001b[m:\u001b[1m\u001b[35m0\u001b[m:\u001b[1m\u001b[36mroot\u001b[m:\u001b[1m\u001b[32m/root\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\r\n\u001b[1m\u001b[33m  2 \u001b[m\u001b[1m\u001b[36mdaemon\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1\u001b[m:\u001b[1m\u001b[35m1\u001b[m:\u001b[1m\u001b[36mdaemon\u001b[m:\u001b[1m\u001b[32m/usr/sbin\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m  3 \u001b[m\u001b[1m\u001b[36mbin\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m2\u001b[m:\u001b[1m\u001b[35m2\u001b[m:\u001b[1m\u001b[36mbin\u001b[m:\u001b[1m\u001b[32m/bin\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m  4 \u001b[m\u001b[1m\u001b[36msys\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m3\u001b[m:\u001b[1m\u001b[35m3\u001b[m:\u001b[1m\u001b[36msys\u001b[m:\u001b[1m\u001b[32m/dev\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m  5 \u001b[m\u001b[1m\u001b[36msync\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m4\u001b[m:\u001b[1m\u001b[35m65534\u001b[m:\u001b[1m\u001b[36msync\u001b[m:\u001b[1m\u001b[32m/bin\u001b[m:\u001b[1m\u001b[33m/bin/sync\u001b[m\r\n\u001b[1m\u001b[33m  6 \u001b[m\u001b[1m\u001b[36mgames\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m5\u001b[m:\u001b[1m\u001b[35m60\u001b[m:\u001b[1m\u001b[36mgames\u001b[m:\u001b[1m\u001b[32m/usr/games\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m  7 \u001b[m\u001b[1m\u001b[36mman\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m6\u001b[m:\u001b[1m\u001b[35m12\u001b[m:\u001b[1m\u001b[36mman\u001b[m:\u001b[1m\u001b[32m/var/cache/man\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m  8 \u001b[m\u001b[1m\u001b[36ml"],
			[1.578283, "o", "p\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m7\u001b[m:\u001b[1m\u001b[35m7\u001b[m:\u001b[1m\u001b[36mlp\u001b[m:\u001b[1m\u001b[32m/var/spool/lpd\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m  9 \u001b[m\u001b[1m\u001b[36mmail\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m8\u001b[m:\u001b[1m\u001b[35m8\u001b[m:\u001b[1m\u001b[36mmail\u001b[m:\u001b[1m\u001b[32m/var/mail\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 10 \u001b[m\u001b[1m\u001b[36mnews\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m9\u001b[m:\u001b[1m\u001b[35m9\u001b[m:\u001b[1m\u001b[36mnews\u001b[m:\u001b[1m\u001b[32m/var/spool/news\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 11 \u001b[m\u001b[1m\u001b[36muucp\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m10\u001b[m:\u001b[1m\u001b[35m10\u001b[m:\u001b[1m\u001b[36muucp\u001b[m:\u001b[1m\u001b[32m/var/spool/uucp\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 12 \u001b[m\u001b[1m\u001b[36mproxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m13\u001b[m:\u001b[1m\u001b[35m13\u001b[m:\u001b[1m\u001b[36mproxy\u001b[m:\u001b[1m\u001b[32m/bin\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 13 \u001b[m\u001b[1m\u001b[36mwww-data\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m33\u001b[m:\u001b[1m\u001b[35m33\u001b[m:\u001b[1m\u001b[36mwww-data\u001b[m:\u001b[1m\u001b[32m/var/www\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 14 \u001b[m\u001b[1m\u001b[36mbackup\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m34\u001b[m:\u001b[1m\u001b[35m34\u001b[m:\u001b[1m\u001b[36mbackup\u001b[m:\u001b[1m\u001b[32m/var/backups\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin"],
			[1.578632, "o", "\u001b[m\r\n\u001b[1m\u001b[33m 15 \u001b[m\u001b[1m\u001b[36mlist\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m38\u001b[m:\u001b[1m\u001b[35m38\u001b[m:\u001b[1m\u001b[36mMailing List Manager\u001b[m:\u001b[1m\u001b[32m/var/list\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 16 \u001b[m\u001b[1m\u001b[36mirc\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m39\u001b[m:\u001b[1m\u001b[35m39\u001b[m:\u001b[1m\u001b[36mircd\u001b[m:\u001b[1m\u001b[32m/var/run/ircd\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 17 \u001b[m\u001b[1m\u001b[36mgnats\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m41\u001b[m:\u001b[1m\u001b[35m41\u001b[m:\u001b[1m\u001b[36mGnats Bug-Reporting System (admin)\u001b[m:\u001b[1m\u001b[32m/var/lib/gnats\u001b[m:\u001b[1m\u001b[33m/usr/sbin/noo\u001b[m\u001b[18;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33mlogin\u001b[m\r\n\u001b[1m\u001b[33m 18 \u001b[m\u001b[1m\u001b[36mnobody\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m65534\u001b[m:\u001b[1m\u001b[35m65534\u001b[m:\u001b[1m\u001b[36mnobody\u001b[m:\u001b[1m\u001b[32m/nonexistent\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 19 \u001b[m\u001b[1m\u001b[36mrrp\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1000\u001b[m:\u001b[1m\u001b[35m1000\u001b[m:\u001b[1m\u001b[36mRobert Paciorek,,,\u001b[m:\u001b[1m\u001b[32m/rrp\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\r\n\u001b[1m\u001b[33m 20 \u001b[m\u001b[1m\u001b[36mmessagebus\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m101\u001b[m:\u001b[1m\u001b[35m104\u001b[m::\u001b[1m\u001b[32m/var/run/dbus\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\r\n\u001b[1m\u001b[7m/etc/passwd [RO]                "],
			[1.578833, "o", "                              1,1            Top\u001b]2;passwd (/etc)\u0007\u001b[1;5H\u001b[?25h"],
			
			["wyszukiwanie + 0.274785", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H/\u001b[?2004h\u001b[?25h"],
			["wyszukiwanie + 0.786587", "o", "i\u001b[?25l\u001b[?25h"],
			["wyszukiwanie + 1.29069", "o", "s\u001b[?25l\u001b[?25h"],
			["wyszukiwanie + 1.770655", "o", "t\u001b[?25l\u001b[?25h"],
			["wyszukiwanie + 4.082716", "o", "\r"],
			["wyszukiwanie + 4.083121", "o", "\u001b[?25l"],
			["wyszukiwanie + 4.085369", "o", "\u001b[22;64H\u001b[1m\u001b[7m5,2\u001b[15;6H\u001b[?25h"],
			["wyszukiwanie + 6.578686", "o", "\u001b[?25l\u001b[23;1H"],
			["wyszukiwanie + 6.579355", "o", "\u001b[22;67H3\u001b[15;27H\u001b[?25h"],
			["wyszukiwanie + 8.194731", "o", "\u001b[?25l\u001b[23;1H"],
			["wyszukiwanie + 8.195373", "o", "\u001b[22;66H41 \u001b[15;45H\u001b[?25h"],
			["wyszukiwanie + 9.714829", "o", "\u001b[?25l\u001b[23;1H"],
			["wyszukiwanie + 9.715491", "o", "\u001b[22;64H8,35 \u001b[19;39H\u001b[?25h"],
			["wyszukiwanie + 10.042697", "o", "\u001b[?25l\u001b[m\u001b[23;1H?\b"],
			["wyszukiwanie + 11.04316", "o", "\u001b[22;64H\u001b[1m\u001b[7m5,41 \u001b[15;45H\u001b[?25h"],
			["wyszukiwanie + 11.530809", "o", "\u001b[?25l\u001b[23;1H"],
			["wyszukiwanie + 11.531508", "o", "\u001b[22;66H23 \u001b[15;27H\u001b[?25h"],
			["wyszukiwanie + 15.235675", "o", "\u001b[?25l\u001b[22;64H4,\u001b[14;27H\u001b[?25h"],
			["wyszukiwanie + 15.587533", "o", "\u001b[?25l\u001b[22;64H3,\u001b[13;27H\u001b[?25h"],
			
			["zastepowanieA + 0.83515", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			["zastepowanieA + 0.835562", "o", "\u001b[?25h"],
			["zastepowanieA + 2.579055", "o", "s\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 4.131241", "o", "#\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 4.923158", "o", "w\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 5.171058", "o", "w\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 5.363024", "o", "w\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 6.475229", "o", "#\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 6.499088", "o", "A\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 6.75502", "o", "B\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 6.970954", "o", "C\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 7.651234", "o", "#\u001b[?25l\u001b[?25h"],
			["zastepowanieA + 15.155061", "o", "\r"],
			["zastepowanieA + 15.155485", "o", "\u001b[?25l\u001b[1m\u001b[31mW10: Warning: Changing a readonly file\u001b[?1000l\u001b[?2004l"],
			["zastepowanieA + 15.655477", "o", "\u001b[?1000h\u001b[?2004h"],
			["zastepowanieA + 15.657077", "o", "\u001b[m\u001b[13;5H\u001b[1m\u001b[36mABC-data\u001b[m:\u001b[22;14H\u001b[1m\u001b[7m+][RO]\u001b[46C1  \u001b]2;passwd + (/etc)\u0007"],
			["zastepowanieA + 15.65738", "o", "\u001b[13;5H\u001b[?25h"],
			
			["zastepowanieB + 0.963381", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			["zastepowanieB + 0.963885", "o", "\u001b[?25h"],
			["zastepowanieB + 1.011034", "o", "\u001b[?25ls#www#ABC#\u001b[?25h"],
			["zastepowanieB + 1.403251", "o", "g\u001b[?25l\u001b[?25h"],
			["zastepowanieB + 2.131248", "o", "\r"],
			["zastepowanieB + 2.132781", "o", "\u001b[?25l\u001b[13;22H\u001b[1m\u001b[36mABC-data\u001b[m:\u001b[5C\u001b[1m\u001b[32mABC\u001b[m:\u001b[13;5H\u001b[?25h"],
			
			["zastepowanieC + 0.479456", "o", "\u001b[?25l\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h\u001b[?25h"],
			["zastepowanieC + 0.835359", "o", "\u001b[?25ls#ist#ABC#g\u001b[?25h"],
			["zastepowanieC + 1.019257", "o", "\r"],
			["zastepowanieC + 1.019686", "o", "\u001b[?25l\u001b[315m\u001b[41mE486: Pattern not found: ist\u001b[13;5H\u001b[?25h"],
			["zastepowanieC + 3.515454", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			["zastepowanieC + 3.515925", "o", "\u001b[?25h"],
			["zastepowanieC + 4.083152", "o", "\u001b[?25ls#ist#ABC#g\u001b[?25h"],
			["zastepowanieC + 4.467276", "o", "\b"],
			["zastepowanieC + 5.127898", "o", "\b"],
			["zastepowanieC + 5.167837", "o", "\b"],
			["zastepowanieC + 5.207813", "o", "\b"],
			["zastepowanieC + 5.247811", "o", "\b"],
			["zastepowanieC + 5.287811", "o", "\b"],
			["zastepowanieC + 5.327613", "o", "\b"],
			["zastepowanieC + 5.367812", "o", "\b"],
			["zastepowanieC + 5.763202", "o", "\b"],
			["zastepowanieC + 6.299357", "o", "\b"],
			["zastepowanieC + 6.651252", "o", "\b"],
			["zastepowanieC + 7.787531", "o", "%s#ist#ABC#g\u001b[?25l\r:%\u001b[?25h"],
			["zastepowanieC + 8.29942", "o", "\r"],
			["zastepowanieC + 8.299867", "o", "\u001b[?25l5 substitutions on 3 lines"],
			["zastepowanieC + 8.303365", "o", "\u001b[1;21r\u001b[1;1H\u001b[12M\u001b[1;23r\u001b[3;6H\u001b[1m\u001b[36mABC\u001b[m:\u001b[17C\u001b[1m\u001b[36mABC Manager\u001b[m:\u001b[6C\u001b[1m\u001b[32mABC\u001b[m:\u001b[7;39H\u001b[1m\u001b[32mABCent\u001b[m:\r\n\r\n\r\n\u001b[1m\u001b[33m 21 \u001b[m\u001b[1m\u001b[36msshd\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m102\u001b[m:\u001b[1m\u001b[35m65534\u001b[m::\u001b[1m\u001b[32m/var/run/sshd\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 22 \u001b[m\u001b[1m\u001b[36msystemd-timesync\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m103\u001b[m:\u001b[1m\u001b[35m111\u001b[m:\u001b[1m\u001b[36msystemd Time Synchronization,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd\u001b[m:\u001b[1m\u001b[33m/binn\u001b[m\u001b[12;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33m/false\u001b[m\r\n\u001b[1m\u001b[33m 23 \u001b[m\u001b[1m\u001b[36msystemd-network\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m105\u001b[m:\u001b[1m\u001b[35m113\u001b[m:\u001b[1m\u001b[36msystemd Network Management,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd/netif\u001b[m:\u001b[1m\u001b[33m//\u001b[m\u001b[14;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33mbin/false\u001b[m\r\n\u001b[1m\u001b[33m 24 \u001b[m\u001b[1m\u001b[36msystemd-resolve\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m106\u001b[m:\u001b[1m\u001b[35m114\u001b[m:\u001b[1m\u001b[36msystemd Resolver,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd/resolve\u001b[m:\u001b[1m\u001b[33m/bin/falss\u001b[m\u001b[16;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33me\u001b[m\r\n\u001b[1m\u001b[33m 25 \u001b[m\u001b[1m\u001b[36msystemd-bus-proxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m107\u001b[m:\u001b[1m\u001b[35m115\u001b[m:\u001b[1m\u001b[3"],
			["zastepowanieC + 8.30369", "o", "6msystemd Bus Proxy,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\r\n\u001b[1m\u001b[33m 26 \u001b[m\u001b[1m\u001b[36mdcmtk\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m108\u001b[m:\u001b[1m\u001b[35m118\u001b[m::\u001b[1m\u001b[32m/var/lib/dcmtk/db\u001b[m:\u001b[1m\u001b[33m/bin/sh\u001b[m\r\n\u001b[1m\u001b[33m 27 \u001b[m\u001b[1m\u001b[36mtest\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[36m,,,\u001b[m:\u001b[1m\u001b[32m/home/test\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\r\n\u001b[1m\u001b[33m 28 \u001b[m\u001b[1m\u001b[36mvde2-net\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m109\u001b[m:\u001b[1m\u001b[35m119\u001b[m::\u001b[1m\u001b[32m/var/run/vde2\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\r\n\u001b[1m\u001b[33m 29 \u001b[m\u001b[1m\u001b[36m_apt\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m110\u001b[m:\u001b[1m\u001b[35m65534\u001b[m::\u001b[1m\u001b[32m/nonexABCent\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H5 substitutions on 3 lines\u001b[22;63H\u001b[1m\u001b[7m29,\u001b[12C63%\u001b[21;5H\u001b[?25h"],
			
			["zastepowanieD + 0.628193", "o", "\u001b[?25l\u001b[22;64H8,\u001b[20;5H\u001b[?25h"],
			["zastepowanieD + 0.899962", "o", "\u001b[?25l\u001b[m\r\n\r\n\r\n\u001b[1m-- VISUAL --\u001b[m\u001b[23;13H\u001b[K\u001b[20;5H\u001b[?25h"],
			["zastepowanieD + 1.180601", "o", "\u001b[?25l\u001b[19;6H\u001b[1m\u001b[7m\u001b[36mest\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[31mx\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m1001\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m1001\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[36m,,,\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[32m/home/test\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[33m/bin/bash\u001b[m\u001b[7m \u001b[m\u001b[20;5H\u001b[1m\u001b[7m\u001b[36mv\u001b[m\u001b[1m\u001b[36mde2-net\u001b[m:\u001b[22;64H\u001b[1m\u001b[7m7,\u001b[19;5H\u001b[?25h"],
			["zastepowanieD + 1.404459", "o", "\u001b[?25l\u001b[m\u001b[18;6H\u001b[1m\u001b[7m\u001b[36mcmtk\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[31mx\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m108\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m118\u001b[m\u001b[7m::\u001b[m\u001b[1m\u001b[7m\u001b[32m/var/lib/dcmtk/db\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[33m/bin/sh\u001b[m\u001b[7m \u001b[m\u001b[19;5H\u001b[1m\u001b[7m\u001b[36mtest\u001b[m\u001b[7m:\u001b[m\u001b[22;64H\u001b[1m\u001b[7m6,\u001b[18;5H\u001b[?25h"],
			["zastepowanieD + 1.628426", "o", "\u001b[?25l\u001b[m\u001b[17;6H\u001b[1m\u001b[7m\u001b[36mystemd-bus-proxy\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[31mx\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m107\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m115\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[36msystemd Bus Proxy,,,\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[32m/run/systemd\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[33m/bin/false\u001b[m\u001b[7m \u001b[m\u001b[18;5H\u001b[1m\u001b[7m\u001b[36mdcmtk\u001b[m\u001b[7m:\u001b[m\u001b[22;64H\u001b[1m\u001b[7m5,\u001b[17;5H\u001b[?25h"],
			["zastepowanieD + 1.820489", "o", "\u001b[?25l\u001b[m\u001b[16;6H\u001b[7m \u001b[m\u001b[17;5H\u001b[1m\u001b[7m\u001b[36msystemd-bus-proxy\u001b[m\u001b[7m:\u001b[m\u001b[22;64H\u001b[1m\u001b[7m4,77\u001b[16;5H\u001b[?25h"],
			["zastepowanieD + 2.988311", "o", "\u001b[?25l\u001b[m\u001b[15;6H\u001b[1m\u001b[7m\u001b[36mystemd-resolve\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[31mx\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m106\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[35m114\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[36msystemd Resolver,,,\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[32m/run/systemd/resolve\u001b[m\u001b[7m:\u001b[m\u001b[1m\u001b[7m\u001b[33m/bin/falss\u001b[m\u001b[16;1H\u001b[1m\u001b[33m \u001b[m\u001b[3C\u001b[1m\u001b[7m\u001b[33me\u001b[m\u001b[7m \u001b[m\u001b[22;66H\u001b[1m\u001b[7m1  \u001b[15;5H\u001b[?25h"],
			["zastepowanieD + 4.043706", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			["zastepowanieD + 4.044217", "o", "'<,'>\u001b[?25h"],
			["zastepowanieD + 5.883465", "o", "s\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 6.547568", "o", "#\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 7.339503", "o", "f\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 7.627427", "o", "a\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 7.819436", "o", "l\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 8.779673", "o", "#\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 9.507573", "o", "F\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 9.731522", "o", "A\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 10.139345", "o", "L\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 11.947647", "o", "#\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 12.355562", "o", "g\u001b[?25l\u001b[?25h"],
			["zastepowanieD + 12.899428", "o", "\r"],
			["zastepowanieD + 12.899798", "o", "\u001b[?25l3 substitutions on 3 lines"],
			["zastepowanieD + 12.901772", "o", "\u001b[15;6H\u001b[1m\u001b[36mystemd-resolve\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m106\u001b[m:\u001b[1m\u001b[35m114\u001b[m:\u001b[1m\u001b[36msystemd Resolver,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd/resolve\u001b[m:\u001b[1m\u001b[33m/bin/FALss\u001b[m\u001b[16;1H\u001b[1m\u001b[33m \u001b[m\u001b[3C\u001b[1m\u001b[33me\u001b[m\u001b[16;6H\u001b[K\u001b[17;5H\u001b[1m\u001b[36msystemd-bus-proxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m107\u001b[m:\u001b[1m\u001b[35m115\u001b[m:\u001b[1m\u001b[36msystemd Bus Proxy,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd\u001b[m:\u001b[1m\u001b[33m/bin/FALse\u001b[m\u001b[17;77H\u001b[K\u001b[18;5H\u001b[1m\u001b[36mdcmtk\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m108\u001b[m:\u001b[1m\u001b[35m118\u001b[m::\u001b[1m\u001b[32m/var/lib/dcmtk/db\u001b[m:\u001b[1m\u001b[33m/bin/sh\u001b[m\u001b[18;47H\u001b[K\u001b[19;5H\u001b[1m\u001b[36mtest\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[36m,,,\u001b[m:\u001b[1m\u001b[32m/home/test\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\u001b[19;46H\u001b[K\u001b[20;5H\u001b[1m\u001b[36mvde2-net\u001b[m:\u001b[30C\u001b[1m\u001b[33mFALse"],
			["zastepowanieD + 12.902125", "o", "\u001b[m\u001b[22;64H\u001b[1m\u001b[7m8,\u001b[20;5H\u001b[?25h"],
			
			["vimexit + 3.195764", "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h\u001b[?25h"],
			["vimexit + 4.515512", "o", "q\u001b[?25l\u001b[?25h"],
			["vimexit2 - 0.135806", "o", "!\u001b[?25l\u001b[?25h"],
			["vimexit2 + 1.50763", "o", "\r"],
			["vimexit2 + 1.510681", "o", "\u001b[?25l\u001b[?1000l\u001b[?2004l\u001b]2;Thanks for flying Vim\u0007\u001b[23;2t\u001b[23;1t\u001b[22;2t\u001b[22;1t\u001b[23;2t\u001b[23;1t"],
			["vimexit2 + 1.610996", "o", "\u001b[23;1H\u001b[K\u001b[23;1H\u001b[?2004l\u001b[?1l\u001b>\u001b[?25h\u001b[?1049l\u001b[23;0;0t"],
			["vimexit2 + 1.613534", "o", eduMovie.prompt()],
		],
		'text' : [
			'Mamy też możliwość przeskoczenia do wskazanej linii wpisując jej numer i duże G, <m> samo duże G lub 0 duże G spowoduje przeskok do ostatniej linii. <m>'
			'Edytor pozwala także na cofanie wykonywanych modyfikacji przy pomocy u. <mark name="wyszukiwanie" />'
			
			'Wyszukiwanie działa w sposób analogiczny do wyszukiwania w less, <m> czyli po ukośniku możemy wpisać wyszukiwaną frazę, <m> zatwierdzić i wyszukać pierwsze wystąpienie naciskając enter. <m>'
			'Następnie przy pomocy klawisza n możemy wyszukiwać kolejne wystąpienia, <m> a przy pomocy dużego n wyszukiwać wstecz. <mark name="zastepowanieA" />'
			
			'Vim pozwala również na operację typu wyszukaj i zastąp. <m>'
			'Operację taką możemy wykonać na aktualnej linii pisząc <m> <:s>[dwukropek s] jakiś znak który będzie służył nam za separator argumentów tego polecenia, <m> na przykład może to byś krzyżyk, ukośnik, małpa lub inny tego typu znak, <m>'
			'następnie tekst wyszukiwany, ponownie ten sam separator, <m> tekst którym chcemy go zastąpić i znowu separator. <m>'
			'Jak widzimy w przykładzie na ekranie zastąpienie zostało wykonane, <m> ale zastąpieniu uległo tylko pierwsze wystąpienie wyszukiwanego tekstu w danej linii. <m>'
			'Kolejne wywołania powodują kolejne takie zastąpienia. <mark name="zastepowanieB" />'
			
			'Jeżeli chcielibyśmy zastąpić wszystkie wystąpienia <m> w danej linii możemy tutaj podać flagę g. <mark name="zastepowanieC" />'
			
			'Standardowo polecenie s operuje tylko na bieżącej linii <m> możemy przed nim podać zakres linii na których ma zostać wykonana operacja <m>.'
			'Jeżeli zakresem tym będzie % to operacja obejmie wszystkie linie w pliku. <mark name="zastepowanieD" />'
			
			'Możemy też zastępowanie robić na fragmencie zaznaczonym w trybie wizualnym, <m> wtedy po wciśnięciu dwukropka vim nam już podpowiada zakres <m> jakiego najprawdopodobniej chcemy użyć, <m>'
			'czyli zakres oznaczający aktualne zaznaczenie w trybie wizualnym.'
			'Oczywiście jako przedziały możemy też podawać numery linii, <m> czy też ilość linii od bieżącej w przód, bądź w tył i tak dalej. <m>'
			'Szczegóły opisane są w dokumentacji, a ich streszczenie <m> znaleźć można w skrypcie do dzisiejszych zajęć. <m>'
			
			'Wyszukaj i zastąp nie jest jedyną, ani nawet najczęściej używaną <m> komendą rozpoczynającą się od dwukropka, <m> czyli wprowadzaną w wewnętrznej linii poleceń edytora. <mark name="vimexit" />'
			'Najważniejszymi tego typu komendami są <:q>[dwukropek q], <m> który powoduje wyjście z edytora oraz <m> <:w>[dwukropek Wu], który powoduje zapisanie pliku. <m>'
			'Samo <:q>[dwukropek q] nie pozwoli na opuszczenie edytora jeżeli plik został <m> zmodyfikowany i w takiej sytuacji konieczne jest napisanie <:q!>[dwukropek q wykrzyknik]. <mark name="vimexit2" />'
			'Komenda <:w>[dwukropek Wu] opcjonalnie może przyjąć ścieżkę <m> lub nazwę pod którą ma zostać zapisany dany plik. <m>'
			'Często stosowany jest zapis <:wq>[dwukropek Wu Q] czyli zapisz i zakończ. <m>'
		]
	},
	{
		'console': [
			[5.053096, "o", eduMovie.prompt()],
			[5.484534, "o", "vim /tmp/abc /etc/passwd /etc/group"],
			[8.484534, "o", "\rn"],
			[8.708572, "o", "\b\b\b\u001b[1@i\u001b[C\u001b[C\u001b[C"],
			[8.956589, "o", "\b\b\b\u001b[1@m\u001b[C\u001b[C\u001b[C"],
			[9.628533, "o", "\r\u001b[8P" + eduMovie.prompt(clear=False) + "\r\n"],
			[9.636882, "o", "3 files to edit\r\n"],
			[9.649723, "o", "\u001b[?1000h\u001b[?2004h\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\u001b[?2004h\u001b[1;23r\u001b[?12h\u001b[?12l\u001b[22;2t\u001b[22;1t"],
			[9.650151, "o", "\u001b[27m\u001b[23m\u001b[29m\u001b[m\u001b[H\u001b[2J\u001b[?25l\u001b[23;1H\"/tmp/abc\" 4L, 10C"],
			[9.651701, "o", "\u001b[2;1H▽\u001b[6n\u001b[2;1H  \u001b[1;1H\u001b[>c\u001b]10;?\u0007\u001b]11;?\u0007"],
			[9.652115, "o", "\u001b[1;1H\u001b[1m\u001b[33m  1 \u001b[m12\r\n\u001b[1m\u001b[33m  2 \u001b[m17\r\n\u001b[1m\u001b[33m  3 \u001b[m19\r\n\u001b[1m\u001b[33m  4 \u001b[m\r\n\u001b[312m~                                                                               \u001b[6;1H~                                                                               \u001b[7;1H~                                                                               \u001b[8;1H~                                                                               \u001b[9;1H~                                                                               \u001b[10;1H~                                                                               \u001b[11;1H~                                                                               \u001b[12;1H~                                                                               \u001b[13;1H~                                                                               \u001b[14;1H~                                                                               \u001b[15;1H~                                                                   "],
			[9.652465, "o", "            \u001b[16;1H~                                                                               \u001b[17;1H~                                                                               \u001b[18;1H~                                                                               \u001b[19;1H~                                                                               \u001b[20;1H~                                                                               \u001b[21;1H~                                                                               \u001b[m\u001b[22;1H\u001b[1m\u001b[7mabc                                                           1,1            All\u001b]2;abc (.)  (1 of 3)\u0007\u001b[1;5H\u001b[?25h"],
			[11.844606, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h\u001b[?25h"],
			[12.252447, "o", "n\u001b[?25l\u001b[?25h"],
			[12.700475, "o", "\r"],
			[12.70136, "o", "\u001b[?25l\"/etc/passwd\""],
			[12.701738, "o", " [readonly] 36L, 1878C"],
			[12.708642, "o", "\u001b[1;2H\u001b[1m\u001b[33m12 \u001b[m\u001b[1m\u001b[36mproxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m13\u001b[m:\u001b[1m\u001b[35m13\u001b[m:\u001b[1m\u001b[36mproxy\u001b[m:\u001b[1m\u001b[32m/bin\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\u001b[2;2H\u001b[1m\u001b[33m13 \u001b[m\u001b[1m\u001b[36mwww-data\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m33\u001b[m:\u001b[1m\u001b[35m33\u001b[m:\u001b[1m\u001b[36mwww-data\u001b[m:\u001b[1m\u001b[32m/var/www\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\u001b[3;2H\u001b[1m\u001b[33m14 \u001b[m\u001b[1m\u001b[36mbackup\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m34\u001b[m:\u001b[1m\u001b[35m34\u001b[m:\u001b[1m\u001b[36mbackup\u001b[m:\u001b[1m\u001b[32m/var/backups\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\u001b[4;2H\u001b[1m\u001b[33m15 \u001b[m\u001b[1m\u001b[36mlist\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m38\u001b[m:\u001b[1m\u001b[35m38\u001b[m:\u001b[1m\u001b[36mMailing List Manager\u001b[m:\u001b[1m\u001b[32m/var/list\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\r\n\u001b[1m\u001b[33m 16 \u001b[m\u001b[1m\u001b[36mirc\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m39\u001b[m:\u001b[1m\u001b[35m39\u001b[m:\u001b[1m\u001b[36mircd\u001b[m:\u001b[1m\u001b[32m/var/run/ircd\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\u001b[5;53H\u001b[K\u001b[6;1H\u001b[1m\u001b[33m 17 \u001b[m\u001b[1m\u001b[36mgnats\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m41\u001b[m:\u001b[1m\u001b[35m41\u001b[m:\u001b[1m\u001b[36mGnats Bug-Reporting System (admin)\u001b[m:\u001b[1m\u001b[32m/var/lib/gnats\u001b[m:\u001b[1m\u001b[33m/usr/sbin/noo\u001b[m\u001b[7;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33mlogin\u001b[m\u001b[7;10H\u001b[K\u001b[8;1"],
			[12.709029, "o", "H\u001b[1m\u001b[33m 18 \u001b[m\u001b[1m\u001b[36mnobody\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m65534\u001b[m:\u001b[1m\u001b[35m65534\u001b[m:\u001b[1m\u001b[36mnobody\u001b[m:\u001b[1m\u001b[32m/nonexistent\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\u001b[8;63H\u001b[K\u001b[9;1H\u001b[1m\u001b[33m 19 \u001b[m\u001b[1m\u001b[36mrrp\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1000\u001b[m:\u001b[1m\u001b[35m1000\u001b[m:\u001b[1m\u001b[36mRobert Paciorek,,,\u001b[m:\u001b[1m\u001b[32m/rrp\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\u001b[9;54H\u001b[K\u001b[10;1H\u001b[1m\u001b[33m 20 \u001b[m\u001b[1m\u001b[36mmessagebus\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m101\u001b[m:\u001b[1m\u001b[35m104\u001b[m::\u001b[1m\u001b[32m/var/run/dbus\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[10;51H\u001b[K\u001b[11;1H\u001b[1m\u001b[33m 21 \u001b[m\u001b[1m\u001b[36msshd\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m102\u001b[m:\u001b[1m\u001b[35m65534\u001b[m::\u001b[1m\u001b[32m/var/run/sshd\u001b[m:\u001b[1m\u001b[33m/usr/sbin/nologin\u001b[m\u001b[11;54H\u001b[K\u001b[12;1H\u001b[1m\u001b[33m 22 \u001b[m\u001b[1m\u001b[36msystemd-timesync\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m103\u001b[m:\u001b[1m\u001b[35m111\u001b[m:\u001b[1m\u001b[36msystemd Time Synchronization,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd\u001b[m:\u001b[1m\u001b[33m/binn\u001b[m\u001b[13;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33m/false\u001b[m\u001b[13;11H\u001b[K\u001b[14;1H\u001b[1m\u001b[33m 23 \u001b[m\u001b[1m\u001b[36msystemd-network\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m105\u001b[m:\u001b[1m\u001b[35m113\u001b[m:\u001b[1m\u001b[36msystemd Network Management,,,"],
			[12.70969, "o", "\u001b[m:\u001b[1m\u001b[32m/run/systemd/netif\u001b[m:\u001b[1m\u001b[33m//\u001b[m\u001b[15;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33mbin/false\u001b[m\u001b[15;14H\u001b[K\u001b[16;1H\u001b[1m\u001b[33m 24 \u001b[m\u001b[1m\u001b[36msystemd-resolve\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m106\u001b[m:\u001b[1m\u001b[35m114\u001b[m:\u001b[1m\u001b[36msystemd Resolver,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd/resolve\u001b[m:\u001b[1m\u001b[33m/bin/falss\u001b[m\u001b[17;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33me\u001b[m\u001b[17;6H\u001b[K\u001b[18;1H\u001b[1m\u001b[33m 25 \u001b[m\u001b[1m\u001b[36msystemd-bus-proxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m107\u001b[m:\u001b[1m\u001b[35m115\u001b[m:\u001b[1m\u001b[36msystemd Bus Proxy,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[18;77H\u001b[K\u001b[19;1H\u001b[1m\u001b[33m 26 \u001b[m\u001b[1m\u001b[36mdcmtk\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m108\u001b[m:\u001b[1m\u001b[35m118\u001b[m::\u001b[1m\u001b[32m/var/lib/dcmtk/db\u001b[m:\u001b[1m\u001b[33m/bin/sh\u001b[m\u001b[19;47H\u001b[K\u001b[20;1H\u001b[1m\u001b[33m 27 \u001b[m\u001b[1m\u001b[36mtest\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[36m,,,\u001b[m:\u001b[1m\u001b[32m/home/test\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\u001b[20;46H\u001b[K\u001b[21;1H\u001b[1m\u001b[33m 28 \u001b[m\u001b[1m\u001b[36mvde2-net\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m109\u001b[m:\u001b[1m\u001b[35m119\u001b[m::\u001b[1m\u001b[32m/var/run/vde2\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[21;49H\u001b[K\u001b[22;1H\u001b[1m\u001b[7m/etc/passwd [RO]\u001b[46C28,1\u001b[1"],
			[12.709908, "o", "1C57%\u001b]2;passwd (/etc)  (2 of 3)\u0007\u001b[21;5H\u001b[?25h"],
			[13.64472, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			[13.645146, "o", "\u001b[?25h"],
			[14.340643, "o", "n\u001b[?25l\u001b[?25h"],
			[15.076629, "o", "\r"],
			[15.077368, "o", "\u001b[?25l\"/etc/group\""],
			[15.077724, "o", " [readonly] 70L, 968C"],
			[15.083301, "o", "\u001b[1;2H\u001b[1m\u001b[33m 1 \u001b[m\u001b[1m\u001b[36mroot\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m0\u001b[m:\u001b[1;14H\u001b[K\u001b[2;2H\u001b[1m\u001b[33m 2 \u001b[m\u001b[1m\u001b[36mdaemon\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1\u001b[m:\u001b[2;16H\u001b[K\u001b[3;2H\u001b[1m\u001b[33m 3 \u001b[m\u001b[1m\u001b[36mbin\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m2\u001b[m:\u001b[3;13H\u001b[K\u001b[4;2H\u001b[1m\u001b[33m 4 \u001b[m\u001b[1m\u001b[36msys\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m3\u001b[m:\u001b[4;13H\u001b[K\u001b[5;2H\u001b[1m\u001b[33m 5 \u001b[m\u001b[1m\u001b[36madm\u001b[m:\u001b[2C\u001b[1m\u001b[35m4\u001b[m:\u001b[5;13H\u001b[K\u001b[6;2H\u001b[1m\u001b[33m 6 \u001b[m\u001b[1m\u001b[36mtty\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m5\u001b[m:\u001b[1m\u001b[36mrrp\u001b[m\u001b[6;16H\u001b[K\u001b[7;3H\u001b[1m\u001b[33m7 \u001b[m\u001b[1m\u001b[36mdisk\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m6\u001b[m:\u001b[8;2H\u001b[1m\u001b[33m 8 \u001b[m\u001b[1m\u001b[36mlp\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m7\u001b[m:\u001b[8;12H\u001b[K\u001b[9;2H\u001b[1m\u001b[33m 9 \u001b[m\u001b[1m\u001b[36mmail\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m8\u001b[m:\u001b[9;14H\u001b[K\u001b[10;2H\u001b[1m\u001b[33m10 \u001b[m\u001b[1m\u001b[36mnews\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m9\u001b[m:\u001b[10;14H\u001b[K\u001b[11;2H\u001b[1m\u001b[33m11 \u001b[m\u001b[1m\u001b[36muucp\u001b[m:\u001b[4C:\u001b[11;15H\u001b[K\u001b[12;2H\u001b[1m\u001b[33m12 \u001b[m\u001b[1m\u001b[36mman\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m12\u001b[m:\u001b[12;14H\u001b[K\u001b[13;2H\u001b[1m\u001b[33m13 \u001b[m\u001b[1m\u001b[36mproxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m13\u001b[m:\u001b[14;2H\u001b[1m\u001b[33m14 \u001b[m\u001b[1m\u001b[36mkmem\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m15\u001b[m:\u001b["],
			[15.083616, "o", "14;15H\u001b[K\u001b[15;2H\u001b[1m\u001b[33m15 \u001b[m\u001b[1m\u001b[36mdialout\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m20\u001b[m:\u001b[16;2H\u001b[1m\u001b[33m16 \u001b[m\u001b[1m\u001b[36mfax\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m21\u001b[m:\u001b[16;14H\u001b[K\u001b[17;2H\u001b[1m\u001b[33m17 \u001b[m\u001b[1m\u001b[36mvoice\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m22\u001b[m:\u001b[18;2H\u001b[1m\u001b[33m18 \u001b[m\u001b[1m\u001b[36mcdrom\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m24\u001b[m:\u001b[18;16H\u001b[K\u001b[19;2H\u001b[1m\u001b[33m19 \u001b[m\u001b[1m\u001b[36mfloppy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m25\u001b[m:\u001b[19;17H\u001b[K\u001b[20;3H\u001b[1m\u001b[33m0 \u001b[m\u001b[1m\u001b[36mtape\u001b[m:\u001b[2C\u001b[1m\u001b[35m26\u001b[m:\u001b[20;15H\u001b[K\u001b[21;3H\u001b[1m\u001b[33m1 \u001b[m\u001b[1m\u001b[36msudo\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m27\u001b[m:\u001b[21;15H\u001b[K\u001b[22;6H\u001b[1m\u001b[7mgroup [RO]]\b  \u001b[45C1,1  \u001b[10CTop\u001b]2;group (/etc)  (3 of 3)\u0007\u001b[1;5H\u001b[?25h"],
			[19.156724, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			[19.157151, "o", "\u001b[?25h"],
			[19.948637, "o", "s\u001b[?25l\u001b[?25h"],
			[20.204528, "o", "p\u001b[?25l\u001b[?25h"],
			[20.39652, "o", "l\u001b[?25l\u001b[?25h"],
			[20.708556, "o", "i\u001b[?25l\u001b[?25h"],
			[21.02865, "o", "t\u001b[?25l\u001b[?25h"],
			[21.436506, "o", "\r"],
			[21.438346, "o", "\u001b[?25l\u001b[11;1H\u001b[1m\u001b[7m/etc/group [RO]                                               1,1            Top\u001b[m\u001b[12;2H\u001b[1m\u001b[33m 1 \u001b[m\u001b[1m\u001b[36mroot\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m0\u001b[m:\u001b[13;2H\u001b[1m\u001b[33m 2 \u001b[m\u001b[1m\u001b[36mdaemon\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1\u001b[m:\u001b[14;2H\u001b[1m\u001b[33m 3 \u001b[m\u001b[1m\u001b[36mbin\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m2\u001b[m:\u001b[14;13H\u001b[K\u001b[15;2H\u001b[1m\u001b[33m 4 \u001b[m\u001b[1m\u001b[36msys\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m3\u001b[m:\u001b[15;13H\u001b[K\u001b[16;2H\u001b[1m\u001b[33m 5 \u001b[m\u001b[1m\u001b[36madm\u001b[m:\u001b[2C\u001b[1m\u001b[35m4\u001b[m:\u001b[16;13H\u001b[K\u001b[17;2H\u001b[1m\u001b[33m 6 \u001b[m\u001b[1m\u001b[36mtty\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m5\u001b[m:\u001b[1m\u001b[36mrrp\u001b[m\u001b[18;2H\u001b[1m\u001b[33m 7 \u001b[m\u001b[1m\u001b[36mdisk\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m6\u001b[m:\u001b[18;14H\u001b[K\u001b[19;2H\u001b[1m\u001b[33m 8 \u001b[m\u001b[1m\u001b[36mlp\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m7\u001b[m:\u001b[19;12H\u001b[K\u001b[20;2H\u001b[1m\u001b[33m 9 \u001b[m\u001b[1m\u001b[36mmail\u001b[m:\u001b[2C\u001b[1m\u001b[35m8\u001b[m:\u001b[20;14H\u001b[K\u001b[21;2H\u001b[1m\u001b[33m10 \u001b[m\u001b[1m\u001b[36mnews\u001b[m:\u001b[2C\u001b[1m\u001b[35m9\u001b[m:\u001b[21;14H\u001b[K\u001b[22;1H\u001b[7m/etc/group [RO]\u001b[m\u001b[1m\u001b[7m \u001b[m\b\u001b[7m                                               1,1            Top\u001b[1;5H\u001b[?25h"],
			[22.900726, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			[22.901127, "o", "\u001b[?25h"],
			[23.404562, "o", "N\u001b[?25l\u001b[?25h"],
			[23.940657, "o", "\r"],
			[23.941283, "o", "\u001b[?25l\"/etc/passwd\""],
			[23.941411, "o", " [readonly] 36L, 1878C"],
			[23.947553, "o", "\u001b[1;2H\u001b[1m\u001b[33m24 \u001b[m\u001b[1m\u001b[36msystemd-resolve\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m106\u001b[m:\u001b[1m\u001b[35m114\u001b[m:\u001b[1m\u001b[36msystemd Resolver,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd/resolve\u001b[m:\u001b[1m\u001b[33m/bin/falss\u001b[m\u001b[2;1H\u001b[1m\u001b[33m    \u001b[m\u001b[1m\u001b[33me\u001b[m\u001b[2;6H\u001b[K\u001b[3;2H\u001b[1m\u001b[33m25 \u001b[m\u001b[1m\u001b[36msystemd-bus-proxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m107\u001b[m:\u001b[1m\u001b[35m115\u001b[m:\u001b[1m\u001b[36msystemd Bus Proxy,,,\u001b[m:\u001b[1m\u001b[32m/run/systemd\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[4;2H\u001b[1m\u001b[33m26 \u001b[m\u001b[1m\u001b[36mdcmtk\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m108\u001b[m:\u001b[1m\u001b[35m118\u001b[m::\u001b[1m\u001b[32m/var/lib/dcmtk/db\u001b[m:\u001b[1m\u001b[33m/bin/sh\u001b[m\u001b[5;2H\u001b[1m\u001b[33m27 \u001b[m\u001b[1m\u001b[36mtest\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[35m1001\u001b[m:\u001b[1m\u001b[36m,,,\u001b[m:\u001b[1m\u001b[32m/home/test\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\u001b[6;2H\u001b[1m\u001b[33m28 \u001b[m\u001b[1m\u001b[36mvde2-net\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m109\u001b[m:\u001b[1m\u001b[35m119\u001b[m::\u001b[1m\u001b[32m/var/run/vde2\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[7;2H\u001b[1m\u001b[33m29 \u001b[m\u001b[1m\u001b[36m_apt\u001b[m:\u001b[2C\u001b[1m\u001b[35m110\u001b[m:\u001b[1m\u001b[35m65534\u001b[m::\u001b[1m\u001b[32m/nonexistent\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[8;2H\u001b[1m\u001b[33m30 \u001b[m\u001b[1m\u001b[36muuidd\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m100\u001b[m:\u001b[1m\u001b[35m1"],
			[23.947945, "o", "01\u001b[m::\u001b[1m\u001b[32m/run/uuidd\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[9;2H\u001b[1m\u001b[33m31 \u001b[m\u001b[1m\u001b[36mgeoclue\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m111\u001b[m:\u001b[1m\u001b[35m120\u001b[m::\u001b[1m\u001b[32m/var/lib/geoclue\u001b[m:\u001b[1m\u001b[33m/bin/false\u001b[m\u001b[10;2H\u001b[1m\u001b[33m32 \u001b[m\u001b[1m\u001b[36mmf\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m1003\u001b[m:\u001b[1m\u001b[35m1003\u001b[m:\u001b[1m\u001b[36m,,,\u001b[m:\u001b[1m\u001b[32m/home/mf\u001b[m:\u001b[1m\u001b[33m/bin/bash\u001b[m\u001b[11;6H\u001b[1m\u001b[7mpasswd [RO]\u001b[46C28,1\u001b[11C85%\u001b]2;passwd (/etc)  (2 of 3)\u0007\u001b[6;5H\u001b[?25h"],
			[25.876537, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h"],
			[25.876856, "o", "\u001b[?25h"],
			[26.316638, "o", "N\u001b[?25l\u001b[?25h"],
			[26.764492, "o", "\r"],
			[26.765533, "o", "\u001b[?25l\"abc\""],
			[26.765883, "o", " 4L, 10C"],
			[26.771686, "o", "\u001b[1;2H\u001b[1m\u001b[33m 1 \u001b[m12\u001b[1;7H\u001b[K\u001b[2;3H\u001b[1m\u001b[33m2 \u001b[m17\u001b[3;2H\u001b[1m\u001b[33m 3 \u001b[m19\u001b[3;7H\u001b[K\u001b[4;2H\u001b[1m\u001b[33m 4 \u001b[m\u001b[4;5H\u001b[K\u001b[5;1H\u001b[312m~                                                                               \u001b[6;1H~                                                                               \u001b[7;1H~                                                                               \u001b[8;1H~                                                                               \u001b[9;1H~                                                                               \u001b[10;1H~                                                                               \u001b[m\u001b[11;1H\u001b[1m\u001b[7mabcc\b              \u001b[45C1,1  \u001b[10CAll\u001b]2;abc (.)  (1 of 3)\u0007\u001b[1;5H\u001b[?25h"],
			[28.94974, "o", "\u001b]2;group (/etc)  (3 of 3)\u0007"],
			[28.950214, "o", "\u001b[m\u001b[11;1H\u001b[7mabc\u001b[m\u001b[1m\u001b[7m \u001b[m\b\u001b[7m                                                           \u001b[?25l1,1            All\u001b[m\u001b[22;1H\u001b[1m\u001b[7m/etc/group [RO]                                               1,1            Top\u001b[12;5H\u001b[?25h"],
			[29.421347, "o", "\u001b[?25l\u001b[22;63H2,\u001b[13;5H\u001b[?25h"],
			[30.081702, "o", "\u001b[?25l\u001b[22;63H3,\u001b[14;5H\u001b[?25h"],
			[30.12152, "o", "\u001b[?25l\u001b[22;63H4,\u001b[15;5H\u001b[?25h"],
			[30.161546, "o", "\u001b[?25l\u001b[22;63H5,\u001b[16;5H\u001b[?25h"],
			[30.201462, "o", "\u001b[?25l\u001b[22;63H6,\u001b[17;5H\u001b[?25h"],
			[30.241507, "o", "\u001b[?25l\u001b[22;63H7,\u001b[18;5H\u001b[?25h"],
			[30.281492, "o", "\u001b[?25l\u001b[22;63H8,\u001b[19;5H\u001b[?25h"],
			[30.321574, "o", "\u001b[?25l\u001b[22;63H9,\u001b[20;5H\u001b[?25h"],
			[30.361511, "o", "\u001b[?25l\u001b[22;63H10,1\u001b[21;5H\u001b[?25h"],
			[30.401747, "o", "\u001b[?25l\u001b[12;21r\u001b[m\u001b[21;1H\r\n\u001b[1;23r\u001b[21;1H\u001b[1m\u001b[33m 11 \u001b[m\u001b[1m\u001b[36muucp\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m10\u001b[m:\u001b[23;1H\u001b[K\u001b[22;64H\u001b[1m\u001b[7m1,\u001b[12C 1%\u001b[21;5H\u001b[?25h"],
			[30.441582, "o", "\u001b[?25l\u001b[12;21r\u001b[m\u001b[21;1H\r\n\u001b[1;23r\u001b[21;1H\u001b[1m\u001b[33m 12 \u001b[m\u001b[1m\u001b[36mman\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m12\u001b[m:\u001b[22;64H\u001b[1m\u001b[7m2,\u001b[13C3%\u001b[21;5H\u001b[?25h"],
			[30.482031, "o", "\u001b[?25l\u001b[12;21r\u001b[m\u001b[21;1H\r\n\u001b[1;23r\u001b[21;1H\u001b[1m\u001b[33m 13 \u001b[m\u001b[1m\u001b[36mproxy\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m13\u001b[m:\u001b[22;64H\u001b[1m\u001b[7m3,\u001b[13C5%\u001b[21;5H\u001b[?25h"],
			[30.522544, "o", "\u001b[?25l\u001b[12;21r\u001b[m\u001b[21;1H\r\n\u001b[1;23r\u001b[21;1H\u001b[1m\u001b[33m 14 \u001b[m\u001b[1m\u001b[36mkmem\u001b[m:\u001b[1m\u001b[31mx\u001b[m:\u001b[1m\u001b[35m15\u001b[m:\u001b[22;64H\u001b[1m\u001b[7m4,\u001b[13C6%\u001b[21;5H\u001b[?25h"],
			[32.332809, "o", "\u001b[?25l\r\n\r\n\u001b[m:\u001b[?2004h"],
			[32.333206, "o", "\u001b[?25h"],
			[32.716668, "o", "q\u001b[?25l\u001b[?25h"],
			[33.444686, "o", "\r"],
			[33.445099, "o", "\u001b[?25l\u001b[?2004h"],
			[33.446525, "o", "\u001b[11;1H\u001b[312m~                                                                               \u001b[12;1H~                                                                               \u001b[13;1H~                                                                               \u001b[14;1H~                                                                               \u001b[15;1H~                                                                               \u001b[16;1H~                                                                               \u001b[17;1H~                                                                               \u001b[18;1H~                                                                               \u001b[19;1H~                                                                               \u001b[20;1H~                                                                               \u001b[21;1H~                                                                               \u001b[m\u001b[22;1H\u001b[1m\u001b[7mabcc\b             \u001b[47C,1  \u001b[10CAll\u001b]2;abc "],
			[33.446854, "o", "(.)  (1 of 3)\u0007\u001b[1;5H\u001b[?25h"],
			[35.948846, "o", "\u001b[?25l\u001b[m\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h\u001b[?25h"],
			[36.388684, "o", "w\u001b[?25l\u001b[?25h"],
			[37.692848, "o", "\u001b[?25l \u001b[?25h"],
			[38.036815, "o", "a\u001b[?25l\u001b[?25h"],
			[38.38866, "o", "b\u001b[?25l\u001b[?25h"],
			[38.604624, "o", "c\u001b[?25l\u001b[?25h"],
			[38.98884, "o", "2\u001b[?25l\u001b[?25h"],
			[39.332621, "o", "\r"],
			[39.332963, "o", "\u001b[?25l\"abc2\" "],
			[39.343541, "o", "[New] 4L, 10C written"],
			[39.343836, "o", "\u001b[1;5H\u001b[?25h"],
			[41.332829, "o", "\u001b[?25l\u001b[23;1H\u001b[K\u001b[23;1H:\u001b[?2004h\u001b[?25h"],
			[41.900831, "o", "q\u001b[?25l\u001b[?25h"],
			[43.260679, "o", "\r"],
			[43.263846, "o", "\u001b[?25l\u001b[?1000l\u001b[?2004l\u001b]2;Thanks for flying Vim\u0007\u001b[23;2t\u001b[23;1t\u001b[22;2t\u001b[22;1t\u001b[23;2t\u001b[23;1t"],
			[43.364182, "o", "\u001b[23;1H\u001b[K\u001b[23;1H\u001b[?2004l\u001b[?1l\u001b>\u001b[?25h\u001b[?1049l\u001b[23;0;0t"],
			[43.366716, "o", eduMovie.prompt()],
		],
		'text' : [
			"Vim pozwala nam też na otwarcie kilku plików naraz. <m>"
			"Pomiędzy kolejnymi plikami możemy się przełączać przy pomocy <:n>[dwukropek n] <m>, n małe - do przodu, czyli następny plik, N duże - do tyłu, czyli poprzedni plik. <m>"
			"Możemy także podzielić okno vim'a w poziomie poprzez <:split>[dwukropek split] <m> lub w pionie poprzez <:vs>[dwukropek VS] i przełączać się pomiędzy tymi oknami <m> poprzez <Control W>[Control Wu] i strzałka w odpowiednim kierunku. <m>"
			"W różnych takich pod okienkach możemy mieć otwarte różne pliki, <m> dzięki czemu możemy na przykład w łatwy sposób przekopiować dane z jednego pliku do innego. <m>"
			"Poszczególne okienka zamykamy przy pomocy <:q>[dwukropek q], <m> zamykając ostatnie okienko opuścimy vim'a. <m>"
			
			"Natomiast przy pomocy <:e>[dwukropek e] ścieżka do pliku możemy <m> otworzyć wskazany plik z poziomu vim'a. <m>"
		]
	},
]

