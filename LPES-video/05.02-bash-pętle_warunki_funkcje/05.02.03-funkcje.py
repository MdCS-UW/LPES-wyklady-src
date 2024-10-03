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

code_fun_A = r"""
ff() { echo "AAA"; }
"""

code_fun_A_run = code_fun_A + r"""
ff
"""

code_fun_B = r"""
ff() { echo "$1 -- $2"; }
"""

code_fun_B_run = code_fun_B + r"""
ff "a b c" def gh
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'funkcje' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
			["funA", eduMovie.clear + eduMovie.code2console(code_fun_A, "sh")],
			["funArun", eduMovie.clear + eduMovie.code2console(code_fun_A_run, "sh")],
			["funB", eduMovie.clear + eduMovie.code2console(code_fun_B, "sh")],
			["funBrun", eduMovie.clear + eduMovie.code2console(code_fun_B_run, "sh")],
		],
		'consoleDown': [
			[0.0, ""],
			["funA", eduMovie.runCode(code_fun_A, [], cmd="bash")],
			["funArun", eduMovie.runCode(code_fun_A_run, [], cmd="bash")],
			["funB", eduMovie.runCode(code_fun_B, [], cmd="bash")],
			["funBrun", eduMovie.runCode(code_fun_B_run, [], cmd="bash")],
		],
		'text' : [
			'Bash pozwala także na definiowanie funkcji. <mark name="funA" />'
			
			'Definicja funkcji w bashu rozpoczyna się od podania <m> nazwy funkcji, następnie zawsze następują puste nawiasy okrągłe. <m>'
			'Nawet jeżeli funkcja będzie przyjmowała argumenty, te nawiasy są puste. <m>'
			'Nigdy nie wpisujemy tutaj listy argumentów. <m>'
			
			'Następnie w ramach nawiasów klamrowych wpisujemy treść funkcji, <m> czyli instrukcje które mają być wykonane przy jej wywołaniu. <m>'
			'Kolejne instrukcje oddzielamy średnikami lub znakami nowej linii. <m>'
			'Szczególną uwagę należy zwrócić na spację (lub nową linię) <m> po otwierającym nawiasie klamrowym <m> i średnik przed zamykającym nawiasem klamrowym. <mark name="funArun" />'
			
			'Wywołanie funkcji odbywa się bez nawiasów, <m> tak samo jak każdego innego programu, czy polecenia wbudowanego. <m>'
			'Po prostu podajemy nazwę funkcji, która ma zostać uruchomiona. <mark name="funB" />'
			
			'Funkcja może przyjmować argumenty pozycyjne <m> i do argumentów pozycyjnych odwołujemy się dolar numer argumentu, <m>'
				'czyli dolar jeden - pierwszy argument, dolar dwa - drugi argument itd. <m>'
			'Odwołania te odbywają się tak samo jak do argumentów skryptu. <mark name="funBrun" />'
			
			'Wywołanie funkcji z argumentami wygląda jak wywołanie dowolnej innej <m> komendy z argumentami, po prostu po nazwie funkcji podajemy rozdzielane spacjami <m> od niej i od siebie argumenty. <m>'
			'Nie używamy tutaj nawiasów. <m>'
		]
	},
]

code_fun_C = r"""
ff() {
	echo "podano $# argumentów"
	
	for a in "$@"; do
		echo "$a";
	done;
}

ff "a b c" def gh
"""

code_fun_D = r"""
suma() {
	if [ $# -ne 2 ]; then
		echo "USAGE: $0 x y"
		echo "x, y - numeric values"
		return 1;
	fi
	echo $(( $1 + $2 ))
}
"""

code_fun_shift = r"""
runcmd() {
	cmd=$1
	shift
	for f in "$@"; do
		echo "wykonuję $cmd na pliku $f"
	done
}

runcmd abc /[s-u]*
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fun_C, "sh")],
			["funD", eduMovie.clear + eduMovie.code2console(code_fun_D, "sh")],
			["funShift", eduMovie.clear + eduMovie.code2console(code_fun_shift, "sh")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_fun_C, [], cmd="bash")],
			["funD", eduMovie.runCode(code_fun_D, [], cmd="bash")],
			["funShift", eduMovie.runCode(code_fun_shift, [], cmd="bash")],
		],
		'text' : [
			'W przypadku funkcji także dolar hash i dolar małpa <m> działają tak samo jak w przypadku skryptów <m> i udostępniają odpowiednio liczbę oraz listę wszystkich argumentów. <m>'
			'Dolar małpa może być użyta aby przejść pętlą for po wszystkich argumentach, <m>'
				'przy czym dla poprawnej obsługi argumentów zawierających <m> na przykład spacje powinna być ujęta w cudzysłowa podwójne. <mark name="funD" />'
			
			'Dolar hash jest często używany w skryptach i w funkcjach <m> do sprawdzenia czy została podana wymagana ilość argumentów, <m>'
				'a jeżeli nie to wypisania krótkiej <m> instrukcji obsługi i zakończenia działania. <m>'
			'Widzimy to w przykładzie pokazanym na ekranie. <m>'
			'Warto to robić nawet w skryptach tworzonych wyłącznie na własne potrzeby, <m> bo ułatwia ich późniejsze używanie. <m>'
			
			'Użyta instrukcja return kończy działanie funkcji <m> zwracając podaną do niej wartość jako kod powrotu. <m>'
			'Na poziomie skryptu takie działanie ma instrukcja exit. <mark name="funShift" />'
			
			'Należy jeszcze wspomnieć o poleceniu shift, <m> które zdejmuje (usuwa) podaną do niego liczbę argumentów (domyślnie jeden). <m>'
			'Przydatne jest to zwłaszcza w przypadku funkcji przyjmujących <m> nieokreśloną ilość argumentów, gdzie kilka początkowych ma jakieś znaczenie. <m>'
			'Na przykład pierwszy argument określa operację, <m> a kolejne określają pliki na których ma być wykonana. <m>'
			'Taką sytuację demonstruje widoczny na ekranie przykład. <m>'
			'Oczywiście przed startem pętli warto by sprawdzić czy operacja <m> podana w pierwszym argumencie jest obsługiwaną operacją, <m> a jak nie to wypisać odpowiedni komunikat. <m>'
			
			'Po użyciu shift zmienia się oczywiście nie tylko wartość dolar małpa, <m> ale też wszystkich zmiennych związanych z argumentami. <m>'
			'Dolar jeden zwraca to co wcześniej zwracał dolar dwa, <m> dolar hash zwraca wartość mniejszą o jeden, itd. <m>'
		]
	},
]

code_grup_A = r"""
a=0;
{ echo abc; a=1; }
echo $a
(echo abc; a=2)
echo $a
"""

code_grup_B = r"""
a=0;
{ echo AbC; echo abc; echo XyZ; a=1; } | grep b
echo $a
"""

clipData += [
	{ 'section': 'grupowanie poleceń' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_grup_A, "sh")],
			["grupB", eduMovie.clear + eduMovie.code2console(code_grup_B, "sh")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_grup_A, [], cmd="bash")],
			["grupB", eduMovie.runCode(code_grup_B, [], cmd="bash")],
		],
		'text' : [
			'Należy także wspomnieć o możliwości <m> grupowania poleceń bez definiowania funkcji. <m>'
			'Możemy użyć do tego nawiasów klamrowych (dokładnie tak samo jak przy <m> definiowaniu funkcji i z tymi samymi wymogami <m> dotyczącymi spacji i średników) lub nawiasów okrągłych. <m>'
			
			'Instrukcje podane w nawiasach klamrowych będą wykonane <m> w bieżącej powłoce basha, czyli mogą modyfikować zmienne. <m>'
			'Polecenia podane w nawiasach okrągłych będą wykonane w podpowłoce, <m> czyli ustawione lub zmodyfikowane w nich zmienne <m> nie będą widoczne po zakończeniu bloku. <mark name="grupB" />'
			
			'Grupowanie poleceń jest przydatne na przykład w celu <m> grupowania ich przy używaniu operatorów łączenia poleceń w oparciu o kod powrotu <m> z użyciem podwójnego ampersanda lub podwójnej pionowej kreski, <m>'
				'a także w celu przekazania standardowego wyjścia <m> wielu poleceń w ramach jednego strumienia. <m>'
			'Warto zauważyć że jeżeli użyjemy przekierowania strumienia <m> to nawiasy klamrowe zachowały się jak nawiasy okrągłe. <m>'
			'Jest to przypadek analogiczny do omawianego przy pętli while. <m>'
		]
	},
]
