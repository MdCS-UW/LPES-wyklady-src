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

code_while_A = r"""
x=0
while x<5.5:
  print(x)
  x=x+1.3
"""

code_while_B = r"""
a, b = 0, 1
while a <= 20:
    print(a, end=" ")
    a, b = b, a + b
print()
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'pętla while' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_while_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_while_A, [], cmd="python3")],
		],
		'text' : [
			"Drugim rodzajem pętli występującej w Pythonie jest pętla while. <m>"
			"Pętla ta rozpoczyna się od słowa kluczowego while <m> po którym następuje warunek logiczny <m> i dwukropek rozpoczynający wcięty blok kodu. <m>"
			"Wykonuje ona swój blok instrukcji dopóki podany na wstępie warunek jest prawdziwy. <m>"
			"Pętla ta pozwala między innymi na stworzenie pętli nieskończonej <m> (co może być wynikiem błędu, ale często jest użyteczne i stosowane celowo) <m>"
			"oraz na iterowanie po liczbach nie całkowitych co pokazane jest na ekranie. <m>"
			"Pętla ta pozwala też na bardziej złożone operacje zmiany wartości <m> zmiennej iteracyjnej niż proste jej zwiększanie, <m> czy też zmniejszanie o stałą wartość tak jak było to w instrukcji range. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_while_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[1.3, eduMovie.runCode(code_while_B, [], cmd="python3")],
		],
		'text' : [
			"Na ekranie widzimy przykład takiego użycia pętli while <m> do obliczania mniejszych niż 20 wartości pewnego znanego ciągu. <m>"
			"Warto w tym miejscu zwrócić uwagę na operację wielokrotnego przypisania <m> w której po lewej stronie znaku równości mamy n zmiennych, <m>"
			"a po prawej stronie n wyrażeń których obliczone wartości <m> zostaną przypisane do tych zmiennych. <m>"
			"Jako że obliczanie wartości wszystkich wyrażeń po prawej stronie <m> odbywa się przed dokonaniem jakiegokolwiek przypisania, <m>"
			"operacja taka pozwala na przykład na zamianę wartości dwóch <m> zmiennych między sobą bez użycia zmiennej pomocniczej. <m>"
		]
	},
]

