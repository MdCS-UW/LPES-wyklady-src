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

code_stdin = r"""
import sys
for line in sys.stdin:
  print("XX:", line, end="")
"""

code_select_A = r"""
import sys, os, select

rdfd, wrfd, _ = select.select([sys.stdin], [], [], 3.0)
"""

code_select_B = code_select_A + r"""
if sys.stdin in rdfd:
	buf = os.read(sys.stdin.fileno(), 1024)
	print("odczytałem", buf.decode())
else:
	print("timeout ?")
"""

print("prepare and exec code_select_A, code_select_B ... plese wait ...", file=sys.stderr)

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'oczekiwanie na dane: \n funkcja select' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_stdin, "py")],
			["selA", eduMovie.clear + eduMovie.code2console(code_select_A, "py")],
			["selB", eduMovie.clear + eduMovie.code2console(code_select_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_stdin, [], cmd="python3", run=False)],
			[1.0, eduMovie.runCommandString(r"/bin/echo -e 'A\nB C\nD 1 2 3' | python3 przykład.py", cwd="/tmp")],
			["selA", eduMovie.runCode(code_select_A, [], cmd="python3")],
			["selB", eduMovie.runCode(code_select_B, [], cmd="python3")],
			["selB + 1.0", eduMovie.runCommandString(r"/bin/echo -e 'A\nB C\nD 1 2 3' | python3 przykład.py", cwd="/tmp")],
		],
		'text' : [
			'W analogiczny sposób jak z pliku <m> możemy wczytywać także dane ze standardowego wejścia. <m>'
			'Nie musimy go nawet otwierać, <m> wystarczy skorzystać z obiektu <stdin>[S T D in] z modułu sys. <m>'
			
			'Z czytaniem danych z takich rzeczy jak na przykład <m> standardowe wejście, czy też danych odbieranych przez sieć komputerową <m> wiąże się zagadnienie czekania na te dane. <mark name="selA" />'
			
			'Czekanie możemy zrealizować z użyciem funkcji systemowej select, <m> dostęp do której zapewnia nam moduł o tej samej nazwie. <m>'
			
			'Przyjmuję ona cztery argumenty <m> – <3>[trzy] z nich są listami, a ostatni, opcjonalny jest liczbą. <m>'
			'Pierwsza lista jest listą otwartych plików <m> dla których czekamy na możliwość odczytu, <m>'
			'druga jest listą otwartych plików dla których <m> czekamy na możliwość zapisu. <m>'
			'Wartość liczbowa określa maksymalny czas czekania, <m> a trzecią listą na razie nie będziemy się zajmować. <m>'
			
			'Oczekiwanie na zapis może wynikać na przykład z faktu <m> iż urządzenie używane do zapisu lub wysłania danych <m> działa wolniej niż nasz program generuje dane. <m>'
			'Pamiętamy tutaj że "wszystko jest plikiem", <m> zatem pod pojęciem pliku rozumiemy tutaj także <m> standardowe wejście, wyjście programu, gniazda sieciowe, porty szeregowe, itd. <m>'
			
			'Funkcja select powoduje wstrzymanie działania programu do czasu <m> aż któryś z podanych plików jest gotowy do wykonania żądanej operacji. <m>'
			'Jeżeli podaliśmy czwarty argument to oczekiwanie zostanie <m> zakończone po upływie czasu w nim określonego. <m>'
			
			'Funkcja ta zwraca także 3 listy, <m> zawierają one odpowiednio elementy list przekazanych do tej funkcji <m> dla których został spełniony warunek gotowości, <m>'
			'czyli pierwsza będzie zawierała pliki przekazane <m> w pierwszym argumencie które są gotowe do odczytu, druga pliki <m> przekazane w drugim argumencie, które są gotowe do zapisu itd. <m>'
			'Każda z tych, a także wszystkie łącznie mogą być puste, <m> na przykład jeżeli select zakończyła się w wyniku timeoutu. <mark name="selB" />'
			
			'Po zwróconych listach możemy iterować pętlą for w celu wykonania <m> pożądanych operacji lub po prostu sprawdzać obecność plików przekazanych <m> do select w tych listach, tak jak widoczne to jest na ekranie. <m>'
		]
	},
]

print("  done", file=sys.stderr)

code_select_C = r"""
import sys, os, select

buf = b''
while True:
	rdfd, wrfd, _ = select.select([sys.stdin], [], [], 3.0)
	
	if rdfd and sys.stdin in rdfd:
		buf2 = os.read(sys.stdin.fileno(), 1024)
		if buf2 == b'':
			break
		buf += buf2
	else:
		print("timeout")
		break

print("odczytałem", buf.decode())
"""

print("prepare and exec code_select_C ... plese wait ...", file=sys.stderr)

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_select_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_select_C, [], cmd="python3")],
			[1.0, eduMovie.runCommandString(r"/bin/echo -e 'A\nB C\nD 1 2 3' | python3 przykład.py", cwd="/tmp")],
		],
		'text' : [
			'Jako że wyjście z select oznacza dostępność jakichś, <m> ale nie koniecznie wszystkich danych to warto tego typu odczyt prowadzić w pętli, <m>'
			"która zostanie przerwana jeżeli select nie zwrócił możliwości <m> wykonania operacji na żadnym z wskazanych plików, <m> co w Pythonie jest równoważne z upłynięciem timeout'u. <m>"
			'Pythonowa funkcja select (w odróżnieniu od tej z C) kończy się <m> normalnie tylko gdy są dane do odczytu lub nastąpił timeout. <m>'
			'W pozostałych wypadkach może generować wyjątki. <m>'
			
			'Drugim powodem wykonywania tej operacji w pętli <m> jest stosowanie funkcji read z modułu <os>[O S]. <m>'
			'Wczyta ona maksymalnie podaną ilość bajtów, w związku z tym jeżeli <m> danych do przeczytania było więcej musimy ponowić jej wywołanie. <m>'
			
			'Funkcji tej używamy zamiast metody read, gdyż jest nie blokująca <m> – nie czeka w nieskończoność na koniec pliku (danych), <m>'
			'tylko wychodzi po przeczytaniu tego co było dostępne, pozwalając <m> na realizację oczekiwania z timeoutem przy pomocy funkcji select. <m>'
			'Funkcję tą musimy wywołać na numerycznym deskryptorze pliku <m> a nie samym obiekcie pliku, dlatego podajemy do niej wynik metody <fileno>[fajl no]. <m>'
			
			'Otwarte pliki w systemach uniksowych <m> identyfikowane są poprzez wartość numeryczną, <m> określaną mianem deskryptora pliku. <m>'
			'Z standardowymi strumieniami wejścia wyjścia <m> związane są standardowe numery deskryptorów, które być może pamiętamy <m> z przekierowywania strumieni poleceń shelowych. <m>'
			'Zero to standardowe wejście, <m> jeden - standardowe wyjście, <m> a dwa - wyjście błędu. <m>'
			'Wszystkim obiektom otwieranym funkcją open <m> przypisywane są wyższe numery (typowo na zasadzie pierwszy wolny). <m>'
			
			'Warto zauważyć także że metody decode <m> używamy dopiero po zakończeniu wczytywania. <m>'
			'Takie wczytywanie i dekodowanie w porcjach mogłoby prowadzić <m> do błędów w funkcji decode (skutkujących wygenerowaniem wyjątku), <m>'
			'w sytuacji gdyby read zakończył się (np. z powodu limitu bufora) <m> wewnątrz ciągu bajtów kodującego jeden znak. <m>'
		]
	},
]

print("  done", file=sys.stderr)
