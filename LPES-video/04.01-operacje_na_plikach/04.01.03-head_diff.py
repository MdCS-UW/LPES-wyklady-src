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

prompt_txt = eduMovie.prompt(clear=False)
prompt_len_str = str( len( eduMovie.prompt(color=False) ) + 1 )

clipData += [
	{ 'comment': 'head tail diff patch' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"head -n3 /etc/passwd")],
			[1.0, eduMovie.runCommandString(r"tail -n3 /etc/passwd")],
		],
		'text' : [
			'Kolejnymi poleceniami związanymi <m> z przetwarzaniem plików tekstowych są head i tail. <m>'
			'Polecenia te domyślnie wypisują <m> odpowiednio 10 pierwszych i ostatnich linii z pliku. <m>'
			'Liczbę wypisywanych linii możemy określić przy pomocy opcji <-n>[minus n] <m>'
		]
	},
	{
		'console': [
			[0.495142, "o", "\u001b[H\u001b[2J\u001b]2;screen\u0007" + prompt_txt],
			[0.495142, "o", "\r\u001b[11B\u001b[7m   0 bash                                                                       \r\u001b[12B   1 bash                                                                       \r\u001b[11A"],
			[0.547436, "o", "\u001b[1m\u001b[31m\u001b[0m\u001b[1m\u001b[36m\u001b[0m" + prompt_txt],
			[0.547436, "o", "\u001b[12A"],
			[1.734813, "o", "echo ABC > /tmp/abc"],
			[2.85095, "o", "\r\u001b[1m\u001b[31mr\b\n\u001b[0m \b"],
			[2.852199, "o", "\u001b[1m\u001b[31m\u001b[0m\u001b[1m\u001b[36m\u001b[0m" + prompt_txt],
			[2.95307, "o", "\u001b[11B"],
			[3.794933, "o", "t"],
			[4.114645, "o", "a"],
			[4.266699, "o", "i"],
			[4.490726, "o", "l"],
			[4.650687, "o", " "],
			[4.842712, "o", "-"],
			[5.090474, "o", "f"],
			[6.106858, "o", " "],
			[7.122872, "o", "/"],
			[7.306787, "o", "t"],
			[7.658798, "o", "m"],
			[7.800701, "o", "p/"],
			[8.354824, "o", "a"],
			[8.794825, "o", "b"],
			[9.001243, "o", "c "],
			[9.40294, "o", "\r\u001b[1m\u001b[31mr\b\n\u001b[0m \b"],
			[9.405786, "o", "ABC\r\n \b"],
			[10.706723, "o", "\u001b[2;" + prompt_len_str + "H"],
			[12.252719, "o", "echo XYZ >> /tmp/abc"],
			[13.02703, "o", "\r\u001b[1m\u001b[31mr\b\n\u001b[0m \b"],
			[13.027487, "o", "\u001b[12BXYZ\r\n \u001b[3;1H"],
			[13.027896, "o", "\u001b[1m\u001b[31m\u001b[0m\u001b[1m\u001b[36m\u001b[0m" + prompt_txt],
			[14.386945, "o", "echo XYZ >> /tmp/abc"],
			[15.434969, "o", "\bc\b"],
			[16.095947, "o", "\bb\b"],
			[16.136801, "o", "\ba\b"],
			[16.17699, "o", "\b/\b"],
			[16.217979, "o", "\bp\b"],
			[16.258927, "o", "\bm\b"],
			[16.299879, "o", "\bt\b"],
			[16.340942, "o", "\b/\b"],
			[16.381804, "o", "\b \b"],
			[16.422858, "o", "\b>\b"],
			[16.463636, "o", "\b>\b"],
			[16.503897, "o", "\b \b"],
			[17.555205, "o", " \u001b[K >> /tmp/abc\u001b[12D"],
			[17.93908, "o", "\u001b[K1 >> /tmp/abc\u001b[12D"],
			[18.122808, "o", "\u001b[K2 >> /tmp/abc\u001b[12D"],
			[18.347092, "o", "\u001b[K3 >> /tmp/abc\u001b[12D"],
			[18.69898, "o", "\r\u001b[1m\u001b[31mr\b\n\u001b[0m \b"],
			[18.699512, "o", "\u001b[12BXYZ 123\r\n \u001b[4;1H"],
		],
		'text' : [
			'W tail mamy bardzo przydatną opcje <-f>[minus f] <m> która powoduje to że tail czeka na dane, <m> które się mogą pojawić w przyszłości w pliku. <m>'
			'Jak widzimy tail czeka na kolejne dane, <m> które mogą zostać dopisane do wskazanego pliku <m> i wypisuje je w momencie kiedy one się w nim pojawiają. <m>'
			'Jest to użyteczna opcja do obserwowania na przykład logów systemowych. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCommandString(r"diff -u /etc/passwd- /etc/passwd")],
			["minusu", eduMovie.runCommandString(r"diff /etc/passwd- /etc/passwd")],
			
			["minusr", eduMovie.runCommandString(r"cp -r /etc/vim /tmp/")],
			["minusr + 0.5", eduMovie.runCommandString(r"echo ABC > /tmp/vim/abc; echo XYZ >> /tmp/vim/vimrc")],
			["minusr + 1.0", eduMovie.runCommandString(r"diff -r -u /etc/vim/ /tmp/vim/")],
			
			["patch", eduMovie.runCommandString(r"diff -u /tmp/vim/vimrc /etc/vim/vimrc > /tmp/patch")],
			["patch + 1.0", eduMovie.runCommandString(r"cd /tmp")],
			["patch + 2.0", eduMovie.runCommandString(r"patch -p2 < /tmp/patch", cwd="/tmp")],
			["patch + 3.0", eduMovie.runCommandString(r"tail -n3 /tmp/vim/vimrc", cwd="/tmp")],
		],
		'text' : [
			'Kolejna grupa komend wiąże się z porównywaniem plików. <m> Są to diff i patch. <m>'
			'Polecenie diff porównuje dwa pliki, typowo dwie wersje jakiegoś pliku <m> i wypisuje na swoje standardowe wyjście informację o różnicach. <mark name="minusu" />'
			
			'Diff przyjmuje kilka opcji związanych z formatowaniem swojego outputu. <m>'
			'Na przykład opcja <-u>[minus u] powoduje formatowanie powszechnie stosowane <m> przez programistów i spotykane w serwisach obsługujących repozytoria kodu. <m>'
			'Minus oznacza linie usuniętą, plus oznacza linię dodaną. <m>'
			'Mamy też podawane adresy linii, które zostały wyświetlone, <m> czyli np. numer pierwszej wyświetlanej w danym bloku linii oraz ilość tych linii, <m> zarówno dla pliku oryginalnego jak i zmodyfikowanego. <mark name="minusr" />'
			
			'Diff może działać rekurencyjnie i porównywać całe katalogi. <m> Służy to tego opcja <-r>[minus r]. <mark name="patch" />'
			
			'Jeżeli wyjście polecenia diff zapiszemy do pliku <m> możemy je użyć w poleceniu patch do uzyskania zmodyfikowanej <m> wersji pliku z oryginalnej lub oryginalnej ze zmodyfikowanej. <m>'
			'Wygenerowane przez diff pliki z różnicami, <m> nazywane plikami łat mogą być przesyłane pomiędzy <m> systemami, czy też osobami celem naniesienia tych samych zmian <m>'
				'w innym miejscu bez konieczności transmisji całej zawartości, <m> gdyż wysyłamy tylko różnicę a nie cały aktualny stan jakiegoś pliku czy katalogu. <m>'
		]
	},
]
