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

code_slown_A = r"""
slownik = { 1: 'a', 'x': True }
"""

code_slown_B = r"""
slownik = { 1: 'a', 'x': True }

print(slownik[1], slownik['x'])

print(slownik[0])
"""

code_slown_C = r"""
slownik = { 1: 'a', 'x': True }

slownik[0]= [1,2]

print(slownik[0])
"""

code_slown_D = r"""
def napisliczba1(napis):
  if napis == "jeden":
    return 1
  elif napis == "dwa":
    return 2
  elif napis == "trzy":
    return 3

napisliczba2 = { "jeden":1, "dwa":2, "trzy":3 }

print( napisliczba1("jeden"), napisliczba2["jeden"] )
"""

code_sort_slown_A = r"""
a = { 3: 'a', 1: 'd', 5:'c' }
x = a.items()

print(x)
"""

code_sort_slown_B = r"""
a = { 3: 'a', 1: 'd', 5:'c' }
x = a.items()

y = list(x)
y.sort()
print( y )

y = sorted(x)
print( y )
"""

code_sort_slown_C = r"""
a = { 3: 'a', 1: 'd', 5:'c' }

def k(x):
    return x[1]

y = sorted( a.items(), key=k )
print( y )
"""

code_sort_slown_D = r"""
def a():
	def b(x):
		print("B:", x)
	return b

c=a()
c(5)

a()(3)
"""

code_slown_globals = r"""
a = 123
b = "xyzzy"
print(globals())
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'słowniki' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_slown_A, "py")],
			["slowB", eduMovie.clear + eduMovie.code2console(code_slown_B, "py")],
			["slowC", eduMovie.clear + eduMovie.code2console(code_slown_C, "py")],
			["slowD", eduMovie.clear + eduMovie.code2console(code_slown_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_slown_A, [], cmd="python3")],
			["slowB", eduMovie.runCode(code_slown_B, [], cmd="python3")],
			["slowC", eduMovie.runCode(code_slown_C, [], cmd="python3")],
			["slowD", eduMovie.runCode(code_slown_D, [], cmd="python3")],
		],
		'text' : [
			'Słownik jest to kontener, trochę podobny do list, <m> przechowujący pary złożone z klucza i przypisanej do niego wartości. <m>'
			'Odwołanie do elementów w tym kontenerze odbywa się poprzez klucz, <m> który jest unikalny (nie może być dwóch par <m> z tym samym kluczem i inną wartością). <m>'
			
			'Definiujemy go poprzez klamerki w których możemy podać <m> kolejne pary postaci klucz dwukropek wartość <m> rozdzielane przecinkami. <m>'
 			'Zarówno klucze jak i wartości w słowniku mogą być różnych typów. <m>'
			'Przy czym klucz nie może być obiektem modyfikowalnym, <m> czyli np. nie może być to lista, ale może być to krotka <m> złożona z elementów niemodyfikowalnych. <mark name="slowB" />'
			
			'Do elementu w słowniku odwołujemy się <m> z użyciem nawiasów kwadratowych i klucza. <m>'
			'Jeżeli odwołamy się do nie istniejącego klucza <m> aby pobrać jego wartość dostaniemy błąd. <mark name="slowC" />'
			'Natomiast możemy do nieistniejącego klucza <m> przypisać wartość, zostanie on wtedy, wraz z tą wartością, dodany do słownika. <m>'
			
			'Słowniki przydatne są jako tablice indeksowane czymś <m> co nie jest liczbą naturalną (na przykład napisem) <m>'
			'lub jeżeli liczby używane do indeksowania nie stanowią <m> ciągłego zakresu liczb naturalnych tylko są rozproszone. <m>'
			'Często wykorzystywane są też jako kontener zapewniający <m> unikalność dodawanych elementów (wtedy dodajemy je jako klucze). <mark name="slowD" />'
			
			'Słowniki wykorzystywane są też do mapowania jednego zbioru wartości <m> na drugi – na przykład liczb zapisanych słownie na wartości numeryczne. <m>'
			'Mapowania takiego możemy też dokonać tworząc rozbudowany if - elif, <m> jednak zapis go z użyciem słownika jest dużo bardziej zwięzły i czytelny. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, ""],
			["sortA", eduMovie.clear + eduMovie.code2console(code_sort_slown_A, "py")],
			["sortB", eduMovie.clear + eduMovie.code2console(code_sort_slown_B, "py")],
			["sortC", eduMovie.clear + eduMovie.code2console(code_sort_slown_C, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["sortA", eduMovie.runCode(code_sort_slown_A, [], cmd="python3")],
			["sortB", eduMovie.runCode(code_sort_slown_B, [], cmd="python3")],
			["sortC", eduMovie.runCode(code_sort_slown_C, [], cmd="python3")],
		],
		'text' : [
			'Słownik w Pythonie jest kolekcją nieposortowaną <m> – nie zachowuje kolejności. <m>'
			'W zależności od wersji Pythona może się zdarzyć tak że <m> elementy słownika będą dostępne w takiej kolejności, <m> w jakiej były do niego wstawione. <m>'
			'Może się zdarzyć też że elementy wstawione do słownika <m> będą posortowane w kolejności na przykład alfabetycznej <m> lub jakiejś innej, której w ogóle nie rozumiemy ale Python ją rozumie. <mark name="sortA" />'
			
			'Słownik nie ma, w związku z tym, metody sortującej. <m>'
			'Możemy go jednak posortować zamieniając wcześniej na listę par, <m> dokładniej obiekt listo-podobny, <m> który możemy uzyskać korzystając z metody items. <mark name="sortB" />'
			
			'Sam obiekt zwrócony przez metodę items nie jest listą <m> i nie ma metody sort, możemy go jednak albo skonwertować na listę <m> i użyć na niej metody sort, albo skorzystać z funkcji sorted. <m>'
			'W obu wypadkach uzyskamy listę posortowaną według <m> pierwszego elementu z każdej pary, czyli klucza. <m>'
			
			'Pytanie, jak posortować wg drugiego elementu pary? <m>'
			'Zarówno metoda sort jak i funkcja sorted pozwalają na zmianę <m> sposobu sortowania z użyciem opcjonalnego argumentu key. <m>'
			'Argumentem tym musi być funkcja przyjmująca element kolekcji <m> (czyli w tym wypadku naszej listy – parę dwóch wartości) <m> i zwracająca element według którego sortujemy. <mark name="sortC" />'
			
			'Warto zauważyć że do funkcji właśnie przekazaliśmy inną funkcję. <m>'
			'W rzeczywostiści funkcja jest obiektem jak każdy inny, <m> również znajduje się gdzieś w pamięci <m> i jej nazwa jest referencją do tego miejsca. <m>'
			'Nawiasy używane do jej uruchomienia i ewentualnego <m> przekazania argumentów stanowią operator wywołania – <m>'
			'warto zauważyć że ich użycie w stosunku co do obiektu <m> nie dającego się wykonać zwróci jedynie wyjątek TypeError <m> o tym mówiący a nie jest błędem składniowym. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_sort_slown_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_sort_slown_D, [], cmd="python3")],
		],
		'text' : [
			'Funkcję możemy przypisać do zmiennej, przekazać do funkcji, <m> czy nawet zwrócić z funkcji z użyciem return. <m>'
			
			'I tutaj dostrzegamy kolejną zaletę słowników <m> zastępujących w pewnych sytuacjach if-elsy. <m>'
			'Słownik taki może mapować wartości na jedną z kilku funkcji, <m> którą następnie możemy wykonać. <m>'
			'Na przykład słownik może jako klucz używać przyjaznej <m> użytkownikowi nazwy używanej w interfejsie naszej aplikacji, <m> a jako wartości przechowywać funkcję, <m> która związana jest z danym poleceniem. <m>'
			'Słownik możemy modyfikować w trakcie działania programu <m> i na przykład nasz program może mieć dynamicznie ładowane wtyczki <m> które do takiego słownika coś dodają, rejestrując nową funkcjonalność. <m>'

		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_slown_globals, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_slown_globals, [], cmd="python3")],
		],
		'text' : [
			'W Pythonie zasadniczo wszystko jest elementem jakiegoś słownika. <m>'
			'Wszystkie zmienne globalne znajdują się w odpowiednim słowniku, <m> który można obejrzeć wywołując funkcję global. <m>'
			'Można tym słownikiem nawet manipulować ręcznie, <m> ale tego akurat nie będziemy robili. <m>'
		]
	},
]


