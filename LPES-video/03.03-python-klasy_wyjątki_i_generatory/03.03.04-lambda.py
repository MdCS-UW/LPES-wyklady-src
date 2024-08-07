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

funkcja_A = r"""
tablica = [None, None, None, None]

for x in [0,1,2,3]:
	def tmp(a):
		return x+a
	tablica[x]=tmp

print( tablica[1](3) )
x=0
print( tablica[1](3) )
"""

funkcja_B = r"""
tablica = [None, None, None, None]

for x in [0,1,2,3]:
	def tmp(a, x=x):
		return x+a
	tablica[x]=tmp

print( tablica[1](3) )
x=0
print( tablica[1](3) )
"""

lamba = r"""
tablicaA = [None, None, None, None]
tablicaB = [None, None, None, None]

for x in [0, 1, 2, 3]:
	tablicaA[x] = lambda a,x=x: x+a
	tablicaB[x] = lambda a: x+a

print (tablicaA[1](3), tablicaB[1](3))
x = 0
print (tablicaA[1](3), tablicaB[1](3))
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'funkcje lokalne i lambda' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(funkcja_A, "py")],
			["argument", eduMovie.clear + eduMovie.code2console(funkcja_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(funkcja_A, [], cmd="python3")],
			["argument", eduMovie.runCode(funkcja_B, [], cmd="python3")],
		],
		'text' : [
			'Python pozwala na definiowanie funkcji wewnątrz funkcji <m> oraz łatwe przechowywanie funkcji w zmiennych, <m> także kolekcjach takich jak listy i słowniki. <m>'
			'Warto zwrócić uwagę na sposób obsługi zmiennych globalnych, <m> czy też zewnętrznych w takich przypadkach. <m>'
			'W przykładzie widocznym na ekranie widzimy, <m> że funkcje tak zdefiniowane nie korzystają z wartości <m> zmiennej x z miejsca definicji, tylko z miejsca wywołania. <mark name="argument" />'
			
			'Jeżeli potrzebujemy takiego zachowania to możemy użyć <m> x jako wartości domyślnej któregoś z argumentów tej funkcji. <m> Tak jak jest to pokazane w tej chwili. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(lamba, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(lamba, [], cmd="python3")],
		],
		'text' : [
			'Innym sposobem lokalnego definiowania funkcji, <m> często dostępnym także w językach nie pozwalających <m> na tak swobodne definiowanie zwykłych funkcji, <m> jest tak zwana lamba. <m>'
			'W tym przypadku definicja jest jeszcze bardziej lokalna, <m> funkcja nawet nie posiada swojej nazwy. <m>'
			'A taka lambda może być bezpośrednio przypisana <m> do jakiejś zmiennej lub przekazana w argumencie. <m>'
			'Widzimy też że sposób traktowania zmiennych zewnętrznych jest analogiczny. <m>'
		]
	}
]
