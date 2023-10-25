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

code_ref_intro_A = r"""
a = [1, 2, 3]
b = a

print(a, b)

b[1]='X'

print(a, b)
"""

code_ref_intro_B = r"""
a = 1
b = [1, 2, 3]

def f(x):
    x=2;
    print(x)

f(a)
print(a)

def g(x):
    x = [9, 8, 7]
    print(x)

g(b)
print(b)
"""

code_ref_intro_C = r"""
a = [1, 2, 3]

def f(x):
  x[1]='X'
  print(x)

f(a)
print(a)
"""

code_ref_A = r"""
a = 1;

def f(x):
    x+=1;
    print(x)

f(a)
print(a)
"""

code_ref_B = r"""
a = [1, 2, 3]

def f(x):
    x[1]='X'
    print(x)

f(a)
print(a)
"""

code_ref_C = r"""
a = [1, 2, 3]
b = a.copy()

print(a, b)

b[1]='X'

print(a, b)
"""

code_ref_id = r"""
a = [1, 2, 3]
b = a.copy()
c = b

print(hex(id(a)), hex(id(b)), hex(id(c)))
"""

code_ref_del = r"""
a = [1, 2, 3]
b = a
del a
print(b)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'referencja' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_ref_intro_A, "py")],
			["introB", eduMovie.clear + eduMovie.code2console(code_ref_intro_B, "py")],
			["introC", eduMovie.clear + eduMovie.code2console(code_ref_intro_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_ref_intro_A, [], cmd="python3")],
			["introB", eduMovie.runCode(code_ref_intro_B, [], cmd="python3")],
			["introC", eduMovie.runCode(code_ref_intro_C, [], cmd="python3")],
		],
		'text' : [
			'Wspomnieliśmy że listy są obiektami modyfikowalnymi, <m> czyli możemy je zmieniać bez tworzenia nowego obiektu <m> i przypisywania go na przykład pod tą samą nazwę. <m>'
			'Fakt ten, w połączeniu z tym jak działa w Pythonie operacja <m> przypisania wartości do zmiennej, ma jeszcze inne istotne następstwo. <m>'
			'Modyfikacja w liście jest widoczna poprzez wszystkie <m> zmienne do których została przypisana ta lista. <m>'
			
			'W przykładzie pokazanym na ekranie widzimy utworzenie dwóch list <m> – a i b, przy czym lista b tworzona jest na zasadzie <m> standardowego przypisania postaci b równa się a. <m>'
			'Następnie modyfikujemy listę b, <m> a wprowadzona zmiana jest widoczna w obu listach. <mark name="introB" />'
			
			'Jak wiemy funkcja przypisując nową wartość do zmiennej, do której <m> zostały podstawione argumenty jej wywołania, nie może zmodyfikować zewnętrznej <m> wartości, czyli tej wartości która do niej została przekazana. <m>'
			'Dzieje się tak również wtedy gdy zmienną tą jest lista. <mark name="introC" />'
			
			'Jednak jeżeli funkcja modyfikuje otrzymaną listę <m> (zamiast przypisywać do zmiennej nową, tak jak w poprzednim przykładzie) <m> to zmiana ta będzie widoczna na zewnątrz. <m>'
			
			'Jest to efektem tego że Python w momencie wykonywania <m> operacji przypisania typu "a równa się b" nie tworzy kopii obiektu b, <m>'
			'a jedynie tworzy nową referencję (wskazanie) <m> na ten obiekt i staje się on dostępny pod dwiema nazwami. <m>'
			'W przypadku obiektów niemodyfikowalnych (na przykład liczb i napisów) <m> nie wywołuje to żadnych skutków ubocznych, <m>'
			'dowolna modyfikacja obiektu powoduje powstanie nowego, <m> który musi być (ponownie) przypisany do jakiejś nazwy.'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_ref_A, "py")],
			["przyp_lista", eduMovie.clear + eduMovie.code2console(code_ref_B, "py")],
			["copy_lista", eduMovie.clear + eduMovie.code2console(code_ref_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_ref_A, [], cmd="python3")],
			["przyp_lista", eduMovie.runCode(code_ref_B, [], cmd="python3")],
			["copy_lista", eduMovie.runCode(code_ref_C, [], cmd="python3")],
		],
		'text' : [
			'Przeanalizujmy przykład z przekazywaniem argumentów do funkcji. <m>'
			'W momencie wywoływania funkcji następuje przypisanie <m> postaci "x równa się a", w efekcie czego x oraz a wskazują na ten sam obiekt <m> związany z wartością <1>[jeden]. <m>'
			'Następnie funkcja tworzy nowy obiekt związany <m> ze zwiększeniem wartości x o jeden <m> i przypisuje referencję do niego do zmiennej x. <m>'
			'Ale funkcja nie ma dostępu do zewnętrznej zmiennej a, <m> aby zmienić jej referencję <m> (nawet gdy użyjemy tej samej nazwy żyją one w innych przestrzeniach), <m> więc ona nadal wskazuje na wartość <1>[jeden]. <m> <break time="200ms"/>'
			
			'Sytuacja zmienia się w przypadku obiektów <m> które możemy zmienić bez tworzenia nowego obiektu. <mark name="przyp_lista" />'
			
			'W przykładzie z modyfikacją listy, w momencie wywołania funkcji <m> utworzona została lokalna zmienna x wskazująca <m> na ten sam obiekt co zewnętrzna zmienna a. <m>'
			'Natomiast nasz kod nie zmienia referencji zmiennej x, <m> ale zmienia wspólny obiekt na który wskazują obie zmienne. <m>'
			'Dlatego zmiana jest widoczna na zewnątrz funkcji. <mark name="copy_lista" />'
			
			'Jeżeli potrzebujemy uzyskać prawdziwą kopię listy <m> powinniśmy skorzystać z metody copy, która tworzy nowy identyczny, <m> ale niezależny obiekt – tak jak w przykładzie widocznym na ekranie. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_ref_id, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_ref_id, [], cmd="python3")],
		],
		'text' : [
			'Identyfikator obiektu na który wskazuje zmienna <m> możemy sprawdzić przy pomocy funkcji <id>[aj di]. <m>'
			'Jeżeli dla dwóch zmiennych jest to ta sama wartość <m> oznacza iż wskazują one na ten sam obiekt. <m>'
			'W najpopularniejszej wersji interpretera Pythona stworzonej <m> z użyciem języka C – <CPython>[C Python] w roli tego identyfikatora <m> używany jest adres w pamięci pod którym znajduje się obiekt. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_ref_del, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_ref_del, [], cmd="python3")],
		],
		'text' : [
			'Instrukcja del kasuje jedynie zmienną (nazwę wskazującą na obiekt), <m> zatem użycie jej w stosunku co do jednej z kilku zmiennych <m> wskazujących na dany obiekt nie ma na niego wpływu - <m>'
			'usuwana jest tylko jedna z kilku referencji. <m>'
			'Dopiero po usunięciu wszystkich referencji <m> Python będzie mógł usunąć obiekt z pamięci. <m>'
		]
	},
]
