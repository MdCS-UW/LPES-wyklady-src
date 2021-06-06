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

code_logical_A = r"print( 1<3, 1>3, 0==1, 0!=1, 0 >= 0 )"
code_logical_B = r"print( 1>3 and True, 1>3 or True, not True )"
code_logical_C = r"print(1<3 and 1<5, 1<3 & 1<5, (1<3) & (1<5))"

code_logical_D = r"print(bool(0), bool(1), bool(4))"
code_logical_E = r"print(1 in [1,2,3])"

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'wyrażenia logiczne' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_logical_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_logical_A, [], cmd="python3")],
		],
		'text' : [
			"Pojawiło nam się pojęcie prawdziwości pewnego warunku. <m>"
			"Python może być wykorzystany, nie tylko jako kalkulator <m> operujący na wartościach liczbowych, <m> ale także do obliczania wartości wyrażeń logicznych <m> w oparciu o wbudowany typ boolean. <m>"
			"Wartościami tego typu jest True i False, <m> oznaczające odpowiednio prawdę i fałsz. <m> Należy zauważyć iż pisane są one z wielkiej litery. <m>"
			"Do wartości tego typu ewoluowane są wszelkie warunki <m> oparte na nierównościach i równościach. <m>"
			"Takie warunki porównujące zapisujemy standardowo, <m> jak w zdecydowanej większości języków programowania. <m>"
			"Równość to dwa znaki równości, nie równość to wykrzyknik i znak równości. <m>"
			"Nierówności ostre to znaki mniejsze / większe (czyli nawiasy trójkątne). <m>"
			"Nierówności nieostre to znaki mniejsze / większe z dodanym po nich znakiem równości. <m>"
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_logical_B, "py")],
			["bitowe", eduMovie.clear + eduMovie.code2console(code_logical_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_logical_B, [], cmd="python3")],
			["bitowe", eduMovie.clear],
			["bitowe + 1.3", eduMovie.runCode(code_logical_C, [], cmd="python3")],
		],
		'text' : [
			"Na zmiennych, czy też po prostu wartościach, <m> tego typu możemy wykonywać operacje logiczne <m> takie jak koniunkcja, czy alternatywa. <m>"
			"W Pythonie operatory dla tych działań mają postać słowną <m> – jeżeli oczekujemy spełnienia obu warunków łączymy je operatorem and, <m> jeżeli wystarczy nam spełnienie tylko jednego – operatorem or, <m> negację zapisujemy przy pomocy operatora not. <m>"
			"W Pythonie nie ma operatorów logicznych <m> zapisywanych np. jako podwójny ampersand. <m>"
			'Istnieją operatory bitowe zapisywane z użyciem <mark name="bitowe" /> pojedynczego ampersanda, pojedynczej kreski pionowej, i tak dalej, <m> natomiast nie są to operatory logiczne. <m>'
			"Co prawda zadziałają one sensownie dla typu logicznego, <m> ale na przykład mają inny priorytet, <m> co widać w przykładzie pokazanym na ekranie. <m>"
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_logical_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_logical_D, [], cmd="python3")],
		],
		'text' : [
			"Jeżeli operacje logiczne wykonujemy na innych typach zmiennych <m> zostaną one skonwertowane na typ logiczny. <m>"
			"Konwersję taką możemy też wykonać jawnie <m> poprzez napisanie bool od wartości <m> którą chcemy skonwertować. <m>"
			"Jak widzimy na ekranie liczba zero odpowiada fałszowi, <m> a liczba o wartości różnej od zera prawdzie. <m>"
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_logical_E, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_logical_E, [], cmd="python3")],
		],
		'text' : [
			"Oprócz operacji porównań wartość logiczną <m> zwracają różne funkcję, a także operator in <m>"
			"który może być użyty do sprawdzenia czy wskazany <m> po jego lewej stronie element znajduje się <m> w kolekcji wskazanej po prawej stronie. <m>"
		]
	},
]

code_logical_F = r"""
print(0 == False, 13.0 == 13)
"""

code_logical_G = r"""
print( (900.22 + 13.44) == 913.66 )
"""

code_logical_H = code_logical_G + r"""
print( 900.22 + 13.44 )
"""

code_logical_I = code_logical_H + r"""
eps=0.00001
print( (913.66 - eps) < (900.22 + 13.44) < (913.66 + eps) )
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_logical_F, "py")],
			["porfloat", eduMovie.clear + eduMovie.code2console(code_logical_G, "py")],
			["numerr", eduMovie.clear + eduMovie.code2console(code_logical_H, "py")],
			["epsilon", eduMovie.clear + eduMovie.code2console(code_logical_I, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.runCode(code_logical_F, [], cmd="python3")],
			["porfloat", eduMovie.clear + eduMovie.runCode(code_logical_G, [], cmd="python3")],
			["numerr", eduMovie.clear + eduMovie.runCode(code_logical_H, [], cmd="python3")],
			["epsilon", eduMovie.clear + eduMovie.runCode(code_logical_I, [], cmd="python3")],
		],
		'text' : [
			'Operacje porównania możemy wykonywać także na danych <m> różnych typów i na ogół będzie to działało rozsądnie. <mark name="porfloat"/>'
			'Szczególną uwagę należy zachować jednak porównując <m> liczby zmiennoprzecinkowe, gdyż jak widzimy na ekranie, <m> może to zadziałać nieprawidłowo. <mark name="numerr"/>'
			'Wiąże się to z błędami numerycznymi <m> i wynikiem operacji dodawania jaki uzyskał Python. <mark name="epsilon"/>'
			'Dlatego porównywanie na równość liczb zmiennoprzecinkowych <m> (zarówno w Pythonie, jak też w innych językach programowania) <m> niekoniecznie jest dobrym pomysłem. <m>'
			'W przypadku gdy chcemy porównać wynik obliczeń zmiennoprzecinkowych <m> z jakąś wartością należy porównania dokonać przez dwie nierówności <m> z wartością mniejszą i większą o jakiś epsilon <m> (określający precyzję naszych obliczeń). <m>'
			'Wyjątkiem może być sytuacja gdzie sprawdzamy czy dana zmienna <m> ma na przykład wartość domyślną przypisaną wcześniej jawnie <m> (np. czy nadal jest zerem tak jak ją zainicjowaliśmy). <m>'
		]
	},
]
