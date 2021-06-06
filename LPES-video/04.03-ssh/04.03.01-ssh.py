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
	{ 'title': [ "#04.3", "Praca na", "systemach", "zdalnych" ] },
	
	{ 'comment': 'ssh' },
	{
		'console': [
			[0.072915, "o", eduMovie.prompt(user="rrp")],
			[0.849968, "o", "s"],
			[0.976984, "o", "s"],
			[1.168902, "o", "h"],
			[1.384899, "o", " "],
			[1.576891, "o", "b"],
			[1.864854, "o", "m"],
			[2.080914, "o", "s"],
			[2.368941, "o", "-"],
			[2.74491, "o", "b"],
			[3.601069, "o", "2"],
			[3.88899, "o", "9"],
			[4.296914, "o", "\r\n"],
			[5.337939, "o", "Linux bms-b29 4.19.97+ #1294 Thu Jan 30 13:10:54 GMT 2020 armv6l"],
			[5.339007, "o", "\r\n"],
			[5.340075, "o", "\r\nThe programs included with the Debian GNU/Linux system are free software;\r\nthe exact distribution terms for each program are described in the"],
			[5.347979, "o", "\r\nindividual files in /usr/share/doc/*/copyright.\r\n\r\nDebian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent\r\npermitted by applicable law.\r\n"],
			[6.629517, "o", "\u001b[01;32mrrp@bms-b29\u001b[00m:\u001b[01;34m~\u001b[00m$ "],
			[13.196772, "o", "logout\r\n"],
			[13.238512, "o", "Connection to fe80::ba4b:ebff:fee5:7ac1%enp1s0 closed.\r\r\n"],
			[13.240965, "o", eduMovie.prompt(user="rrp")],
		],
		'text' : [
			'Praca w trybie tekstowym pozwala także na proste i efektywne uzyskanie <m> połączenia z innym systemem i interaktywną pracę na zdalnych serwerach. <m>'
			'Służy do tego komenda <ssh>[eses H]  która pozwala na uzyskanie <m> powłoki zdalnego systemu poprzez połączenie szyfrowane. <m>'
			
			'Standardowo polecenie <ssh>[eses H] loguje na użytkownika o takiej samej <m> nazwie jak użytkownik z którego zostało ono wykonane. <m>'
			'Jeżeli mamy potrzebę określenia innego użytkownika gdyż <m> na danym serwerze używamy innej nazwy użytkownika niż na komputerze <m>'
			'z którego wykonujemy połączenie, to możemy ją podać <m> poprzedzoną małpą przed nazwą komputera na który się logujemy. <m>'
			'Oczywiście w ten sposób możemy też się zalogować na tego samego użytkownika. <m>'
		]
		
	},
	{
		'console': [
			[0.0, "x", "ssh -D 8080 uzytkownik@serwer\r\n"],
		],
		'text' : [
			'Z ważniejszych opcje <ssh>[eses H] warto wspomnieć o <-D>[minus d duże] <m> po której podajemy pewien numer, typowo większy od <1024>[tysiąc dwadzieścia cztery]. <m>'
			'Opcja ta aktywuje tunel dynamiczny, zgodny z proxy typu <SOCKS4>[soks cztery] / <SOCKS5>[soks pięć], <m> a podany numer określa numer portu na którym klient <ssh>[eses H] <m> będzie nasłuchiwał połączeń w roli serwera proxy. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('FF-ustawiania_proxy.svg')],
		],
		'text' : [
			'Następnie możemy skonfigurować inny program (na przykład przeglądarkę WWW) <m> żeby korzystał z takiego tunelu (z proxy na podanym numerze portu) <m> dzięki czemu ruch będzie wychodził po stronie zdalnej. <m>'
			'Powoduje to że dla serwerów WWW będzie wyglądało to tak jakby nasza <m> przeglądarka działała na serwerze do którego się połączyliśmy przy pomocy <ssh>[eses H]. <m>'
			'W szczególności będzie ona też miała dostęp do zasobów, sieci, serwerów, <m> które są dostępne jedynie z tego serwera. <m>'
		]
	},
	{
		'console': [
			[0.0, "x", eduMovie.prompt(user="rrp") + "ssh -L 4444:abc:88 serwer\r\n"],
		],
		'text' : [
			'Inną opcją do zestawiania tuneli jest <-L>[minus l duże], <m> która typowo przyjmuje trzy argumenty rozdzielane dwukropkiem. <m>'
			
			'Pierwszym z nich jest numer portu na którym nasz klient <ssh>[eses H] ma słuchać <m> (czyli odpowiednik numeru, który podawaliśmy w opcji duże D), <m>'
			'kolejnym jest nazwa komputera do którego ma zostać nawiązane <m> połączenie z serwera <ssh>[eses H] i ostatnim numer portu na tym komputerze <m> do którego ma zostać nawiązane to połączenie. <m>',
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('../../LPES-booklets/images-src/linux/tunele_ssh.svg', margins=20)],
		],
		'text' : [
			
			'Tego typu tunel pozwala nam na wyciągnięcie wskazanego portu <m> jakiegoś odległego komputera na nasz lokalny komputer. <m>'
			'W widocznym przykładzie zostanie zestawiony tunel który cały ruch <m> kierowany na lokalny port <4444>[cztery tysiące czterysta czterdziesty czwarty] będzie przy pomocy komputera serwer <m> przekazywał do portu <88>[osiemdziesiątego ósmego] komputera <abc>[A B C]. <m>',
			
			'Tunel ten pozwala na uzyskanie dostępu do konkretnego portu, <m> komputera, który nie jest dla nas bezpośrednio dostępny. <m>'
			'Oczywiście host do którego się łączymy po <ssh>[eses H] <m> musi wiedzieć co to jest <abc>[A B C] i móc się z nim połączyć. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
		],
		'text' : [
			'Kolejną opcją w <ssh>[eses H] o której warto powiedzieć jest <-X>[minus x duże], <m> która pozwala na tunelowanie aplikacji środowiska graficznego. <m>'
			'Z użyciem tej opcji po zalogowaniu na serwer <ssh>[eses H] możemy uruchomić <m> aplikację środowiska graficznego (korzystającą z X serwera), <m>'
			'której okienko zostanie wyświetlone na naszym lokalnym komputerze, <m> przez nasz lokalny X serwer. <m>'
			
			'Jeżeli chcemy połączyć się  z serwerem <ssh>[eses H] działającym na <m> niestandardowym numerze portu używamy do jego określenia opcji <-p>[minus p małe]. <m>'
			
			'Do zagadnień sieciowych, numerów portów, ich znaczenia, <m> a także tunelowania wrócimy na dalszych zajęciach poświęconych sieciom komputerowym. <m>'
		]
	},
]
