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
	{ 'section': 'standardowe \n wejście, wyjście\n oraz strumienie' },
	{
		'image': [
			[0.0, eduMovie.convertFile("strumienie.svg")]
		],
		'text' : [
			'Typowo program posiada trzy strumienie danych <m> – standardowe wejście, standardowe wyjście i standardowe wyjście błędu. <m>'
			'Standardowe wejście, czyli strumień z identyfikatorem zero <m> są to dane wejściowe programu i jeżeli nie zostało ono przekierowane <m> to domyślnie są to dane wczytywane z klawiatury. <m>'
			'Standardowe wyjście ma identyfikator jeden <m> i jest używane do wypisywania danych wyjściowych. <m>'
			'Standardowe wyjście błędu ma identyfikator dwa <m> i jest używane do wypisywania komunikatów o błędach <m> i innych informacji diagnostycznych. <m>'
			'Oba strumienie wyjściowe jeżeli nie zostały przekierowane <m> są domyślnie wypisywane na ekran, czyli na nasz terminal. <m>'
		]
	},
	{
		'console': [
			[0.07756, "o", eduMovie.prompt()],
			[0.973582, "o", "b"],
			[1.133518, "o", "a"],
			[1.325423, "o", "s"],
			[1.517565, "o", "h"],
			[1.701552, "o", " "],
			[2.0855, "o", "-"],
			[2.245439, "o", "-"],
			[2.525401, "o", "h"],
			[2.749333, "o", "e"],
			[2.941435, "o", "l"],
			[3.125424, "o", "p"],
			[3.381427, "o", " "],
			[3.885617, "o", "|"],
			[4.205467, "o", " "],
			[4.461377, "o", "l"],
			[4.645484, "o", "e"],
			[4.901449, "o", "s"],
			[5.061522, "o", "s"],
			[11.933545, "o", "\r\n"],
			[11.939433, "o", "\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\r"],
			[11.939712, "o", "GNU bash, version 5.0.3(1)-release-(x86_64-pc-linux-gnu)\r\nUsage:  bash [GNU long option] [option] ...\r\n        bash [GNU long option] [option] script-file ...\r\nGNU long options:\r\n        --debug\r\n        --debugger\r\n        --dump-po-strings\r\n        --dump-strings\r\n        --help\r\n        --init-file\r\n        --login\r\n        --noediting\r\n        --noprofile\r\n        --norc\r\n        --posix\r\n        --pretty-print\r\n        --rcfile\r\n        --restricted\r\n        --verbose\r\n        --version\r\nShell options:\r\n        -ilrsD or -c command or -O shopt_option         (invocation only)\r\n        -abefhkmnptuvxBCHP or -o option\r\n:\u001b[K"],
			[13.22957, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[13.230032, "o", "\u001b[KB\bB\r\u001b[KType `bash -c \"help set\"' for more information about shell options.\r\n:\u001b[K"],
			[13.889831, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[13.890245, "o", "Type `bash -c help' for more information about shell builtin commands.\r\n:\u001b[K"],
			[13.929741, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[13.930074, "o", "\u001b[KB\bB\r\u001b[KUse the `bashbug' command to report bugs.\r\n:\u001b[K"],
			[13.969981, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[13.970269, "o", "\r\n:\u001b[K"],
			[14.010123, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.010375, "o", "bash home page: <http://www.gnu.org/software/bash>\r\n:\u001b[K"],
			[14.051178, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.05145, "o", "General help using GNU software: <http://www.gnu.org/gethelp/>\r\n:\u001b[K"],
			[14.092095, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.092393, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.132504, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.132758, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.172403, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.172576, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.212631, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.212884, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.252646, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.252905, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.29263, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.292935, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.332634, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.3329, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.372643, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.372913, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.412361, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.41262, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.452507, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.452856, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.492606, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.492874, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.532634, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[14.532947, "o", "\u001b[KB\bB\r\u001b[K\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.572555, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.572788, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.612437, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.6127, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[14.652621, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KB\bB\r\u001b[K"],
			[14.653035, "o", "\u0007\r\u001b[K\u001b[7m(END)\u001b[27m\u001b[K"],
			[15.957604, "o", "\r\u001b[K\u001b[?1l\u001b>\u001b[?1049l\u001b[23;0;0t"],
			[15.959015, "o", eduMovie.prompt()],
		],
		'text' : [
			# EKRAN: bash --help | less po kilku sekundach odpalenie przejście i wyjście
			"Korzystając z pojedynczej pionowej kreski możemy przekierować <m> standardowe wyjście polecenia występującego przed nią <m> na standardowe wejście polecenia występującego po niej. <m>"
			'Tak jak widzimy to w zaprezentowanym przykładzie. <m>'
			"Pozwala nam to między innymi na przekierowanie wyjścia <m> różnych poleceń do komend wyświetlających tekst ekran po ekranie, <m> ale też (jak zobaczymy później) do komend przetwarzających tekst. <m>"
		]
	},
	{
		'console': [
			[1.265926, "o", "ls -l /etc/passwd /etc/BŁĘDNYPLIK 2>&1 | less"],
			[5.532694, "o", "\r\n"],
			[5.538237, "o", "\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\r"],
			[5.539006, "o", "ls: cannot access '/etc/BŁĘDNYPLIK': No such file or directory\r\n"],
			[5.539367, "o", "-rw-r--r-- 1 root root 1.9K  2020-10-24 15:01:47  /etc/passwd\r\n\u001b[7m(END)\u001b[27m\u001b[K"],
			[8.348718, "o", "\r\u001b[K\u001b[?1l\u001b>\u001b[?1049l\u001b[23;0;0t"],
			[8.350174, "o", eduMovie.prompt()],
		],
		'text' : [
			# EKRAN: ls -l /etc/passwd /etc/BŁĘDNYPLIK 2>&1 | less
			'Jeżeli chcielibyśmy przekierować do jakiejś komendy oba <m> strumienie wyjściowe (zwykły i błędu) możemy je połączyć pisząc <m> pozornie dziwne zaklęcie postaci "dwa większe od ampersand jeden", <m> tak jak widzimy to na ekranie. <m>'
			'Oznacza ono polecenie przekierowania strumienia numer dwa <m> do strumienia numer jeden, <m> który następnie przekazywany jest do kolejnego programu. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			[1.0, eduMovie.runCommandString(r"echo AAA > plik", cwd="/tmp")],
			[2.5, eduMovie.runCommandString(r"cat plik", cwd="/tmp")],
			[3.5, eduMovie.runCommandString(r"echo AAA > plik", cwd="/tmp")],
			[4.5, eduMovie.runCommandString(r"cat plik", cwd="/tmp")],
			["dopisywanie + 1.1", eduMovie.runCommandString(r"echo AAA >> plik", cwd="/tmp")],
			["dopisywanie + 2.7", eduMovie.runCommandString(r"cat plik", cwd="/tmp")],
		],
		'text' : [
			'Znaku większości możemy użyć do przekierowania strumieni wyjściowych <m> do pliku pisząc po jego prawej stronie ścieżkę do tego pliku. <mark name="dopisywanie" />'
			'Jeżeli użyjemy go podwójnie <m> (bez spacji pomiędzy dwoma znakami większości) <m> to dane zostaną dopisane na końcu pliku. <m>'
			'Do wyświetlania zawartości plików użyliśmy polecenia cat, <m> które wypisuje treść podanego pliku na standardowe wyjście. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			[1.2, eduMovie.runCommandString(r"ls -l /etc/passwd /etc/BŁĘDNYPLIK 2>> plik", cwd="/tmp")],
			[3.0, eduMovie.runCommandString(r"cat plik", cwd="/tmp")],
		],
		'text' : [
			'Jeżeli poprzedzimy go liczbą <m> (też bez spacji pomiędzy nią a znakiem większości) <m> to zostanie przekierowany strumień o podanym numerze. <m>'
			'W przykładzie pokazanym na ekranie do pliku została dopisana <m> treść strumienia numer dwa, czyli standardowego wyjścia błędu. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			[4.0, eduMovie.runCommandString(r"more < plik", cwd="/tmp")]
		],
		'text' : [
			'Możemy także przekierować dane z pliku na standardowe wejście <m> jakiegoś polecenia, w tym celu korzystamy ze znaku mniejszości <m> po którym podajemy nazwę pliku tak jak widzimy to na ekranie. <m>'
			'Użycie tego w przypadku more lub innych komend, którym można podać <m> plik do odczytu w linii poleceń nie ma większego sensu. <m>'
			'Są jednak programy które w linii poleceń nie przyjmują ścieżki <m> do pliku z danymi i w tych przypadkach to przekierowanie jest użyteczne. <m>'
		]
	},
]
