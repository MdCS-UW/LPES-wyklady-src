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

code_fork_A = r"""
import os

pid = os.fork()

if pid == 0:
	print("A", os.getpid(), pid)
else:
	print("B", os.getpid(), pid)
"""

code_fork_B = r"""
import os

print("PID:", os.getpid())

pid = os.fork()

if pid == 0:
	print("potomek", os.getpid(), pid)
else:
	print("rodzic", os.getpid(), pid)
"""

code_fork_C = r"""
import os

ppid = os.getpid()

pid = os.fork()

if pid == 0:
	print("potomek", os.getpid(), pid, ppid)
	ppid *= 2
	print(ppid)
else:
	print("rodzic", os.getpid(), pid, ppid)
	ppid = 0
	print(ppid)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.5", "Python:", "procesy potomne", "(fork i exec)" ] },
	
	{ 'comment': 'fork' },
	{
		'consoleTop': [
			[0.0, ""],
			["forkA", eduMovie.clear + eduMovie.code2console(code_fork_A, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["forkArun", eduMovie.runCode(code_fork_A, [], cmd="python3")],
		],
		'text' : [
			'W współczesnych systemach operacyjnych działa na ogół wiele procesów, <m> równolegle bądź naprzemiennie działających programów. <m>'
			
			'Aby mogło się to wydarzyć konieczna jest <m> możliwość tworzenia nowego procesu. <m>'
			'Istnieją dwa podejścia, czyli utworzenie pustego procesu <m> który dopiero zostanie zapełniony jakimś kodem wykonywalnym, <m> albo utworzenie kopii aktualnego procesu. <m>'
			'Co na pierwszy rzut oka może się wydawać trochę dziwne, <m> dominująca jest metoda związana z tworzeniem kopii procesu. <m>'
			'Wynika to z jej większej elastyczności – mając kopie procesu możemy <m> zastąpić go innym albo możemy kontynuować wykonywanie <m> naszego kodu od miejsca rozgałęzienia. <mark name="forkA" />'
			
			'Do rozgałęzienia procesu służy funkcja systemowa fork, <m> w Pythonie znajdująca się w module <os>[O S]. <m>'
			
			'Funkcja ta zwraca wartość liczbową, którą w ogólności może być zero, <m> wartość dodatnia albo wartość ujemna. <m>'
			'W Pythonie zamiast wartości ujemnych, oznaczających błąd <m> zostanie wygenerowany wyjątek, zatem mamy tylko <m> dwa przypadki – zero i coś dodatniego. <m>'
			
			'Pytanie co zwróci funkcja fork w przykładzie pokazanym na ekranie? <break time="700ms"/> <mark name="forkArun" />'
			'Jak widzimy funkcja zwróciła zarówno zero jak i niezerową wartość dodatnią. <m>'
			"Możliwe jest to dzięki temu że nastąpiło rozgałęzienie procesu <m> – od miejsca wykonania funkcji fork zaczęły wykonywać się dwa oddzielne interpretery <m> Pythona które właśnie zakończły wykonywać funkcję fork. <m>"
			
			'W początkowej chwili różnią się one jedynie wartością zwróconą przez fork, <m> wszystkie inne zmienne mają takie same wartości w obu procesach. <m>'
			
			'W jednym z nich, określanym mianem rodzica funkcja fork zwróciła wartość <m> niezerową, będącą identyfikatorem nowo powstałego procesu – potomka. <m>'
			'W potomku natomiast fork zwróciła zero. <m>'
			'Widzimy także że wartość zwracana przez funkcję getpid, <m> podającą identyfikator bieżącego procesu, <m> w potomku jest równa wartości którą zwrócił fork w rodzicu. <m>'
			'Czyli tą niezerową wartością zwracaną przez fork jest identyfikator potomka. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fork_B, "py")],
			["forkC", eduMovie.clear + eduMovie.code2console(code_fork_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_fork_B, [], cmd="python3")],
			["forkC", eduMovie.runCode(code_fork_C, [], cmd="python3")],
		],
		'text' : [
			'Jeżeli dodamy wypisanie identyfikatora procesu przed fork, <m> zauważymy że ma on tą samą wartość co w procesie rodzica. <m>'
			'Dlatego właśnie ten proces nazywamy rodzicem <m> – on nie zmienił swojego identyfikatora, nadal trwa, <m> a utworzył jedynie nowy proces – potomka. <mark name="forkC" />'
			
			'Jeżeli chcemy żeby potomek znał identyfikator rodzica <m> wystarczy że przed wykonaniem fork zapiszemy go do jakiejś zmiennej. <m>'
			'Potomek otrzymuje wierne kopie wszystkich zmiennych rodzica <m> utworzonych przed wywołaniem fork. <m>'
			'Jednak są to kopie – modyfikacje wartości tych zmiennych wykonane <m> po wywołaniu fork nie będą widoczne w drugim procesie <m>'
			'(zarówno modyfikacje w rodzicu nie są widoczne w potomku i na odwrót <m> – modyfikacje w potomku nie są widoczne w rodzicu). <m>'
			'Dotyczy to także obiektów modyfikowalnych jak na przykład listy. <m>'
			
			'Przy czym tak naprawdę kopiowanie odbywa się w momencie modyfikacji, <m> a nie w momencie tworzenia potomka. <m>'
			'Czyli jeżeli mamy proces który zajmuje bardzo dużo pamięci i wykona <m> funkcje fork, to pamięć nie będzie kopiowana w momencie wykonania funkcji fork, <m>'
			'a jedynie jej zmieniane fragmenty <m> będą kopiowane w momencie wykonywania modyfikacji. <m>'
			
			'Kodu używającego fork nie należy wykonywać <m> w trybie interaktywnym Pythona, gdyż komendy wpisywane po fork <m> będą trafiały tylko do jednego procesu. <m> Kod taki należy uruchamiać z pliku. <m>'
		]
	},
]

