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

code_print = r"""
print("ABC", 123, sep="-")
"""

code_funkcja_A = r"""
def nazwa():
    print("ABC")
    print("123")
"""

code_funkcja_A_run = code_funkcja_A + r"""
nazwa()
"""

code_funkcja_B = r"""
def potęga(a, b):
    print("funkcja potęga, argumenty:", a, b)
    print("podnoszę do potęgi ... wynik to:", a**b)
"""

code_funkcja_B_run = code_funkcja_B + r"""
potęga(2,3)
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#02.2", "Python:", "funkcje", "" ] },
	
	{ 'comment': 'Python - funkcje' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_print, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_print, [], cmd="python3")],
		],
		'text' : [
			"Tworząc programy często zachodzi potrzeba wielokrotnego <m> wykorzystania takiego samego lub podobnego <m> fragmentu kodu w różnych miejscach. <m>"
			'W tym celu korzystamy z funkcji – zarówno tych "wbudowanych" <m> w jakiś język lub bibliotekę, jak też tych definiowanych przez nas. <m>'
			"Wywołując jakąś funkcję, na przykład pisząc print od x, <m> odwołujemy się do takiego kawałka kodu i przekazujemy <m> do niego jakieś informacje (nazywane argumentami) <m> umożliwiające wpływanie na jego działanie. <m>"
		]
	},
	{ #  definicja funkcji bezargumentowej - pierwsza linia
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console("def nazwa():", "py")],
		],
		'consoleDown': [
			[0.0, ""],
		],
		'text' : [
			"Python pozwala nam na definiowanie naszych własnych funkcji. <m>"
			"Definicje funkcji zaczynamy od słowa kluczowego def <m> po którym podajemy nazwę funkcji, nawiasy okrągłe i dwukropek. <m>"
		]
	},
	{ # definicja funkcji bezargumentowej - wcięte ciało funkcji - dwa razy print ...
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_A, "py")],
			["wywolanie", eduMovie.clear + eduMovie.code2console(code_funkcja_A_run, "py")]
		],
		'consoleDown': [
			[0.0, ""],
			["wywolanie", eduMovie.runCode(code_funkcja_A_run, [], cmd="python3")]
		],
		'text' : [
			"Dwukropek w Pythonie jest znakiem rozpoczynającym blok kodu, <m> czyli grupę instrukcji (w tym wypadku składających się na naszą funkcję). <m>"
			"Do wcinania kodu możemy używać zarówno spacji jak i tabulatorów, <m> ważne jest natomiast aby nie mieszać tych dwóch sposobów <m>"
			"(dla Pythona wcięcie przy pomocy x tabulatorów będzie czym innym <m> niż dowolne wcięcie przy pomocy spacji). <m>"
			"Blok kodu kończy się z momentem powrotu do poziomu wcięcia <m> sprzed jego rozpoczęcia, czyli poziomu wcięcia linii <m> w której zaczęła się instrukcja zakończona dwukropkiem. <m>"
			"W przypadku definiowania funkcji jest to powrót <m> do poziomu wcięcia linii ze słowem kluczowym def. <m>"
			
			"Wewnątrz bloku kodu mogą występować kolejne takie bloki <m> (np. dla innych instrukcji ich używających). Ich wydzielanie <m> polega na zwiększeniu poziomu wcięcia na czas ich trwania. <m>"
			'Nie mamy klamerek wyznaczających bloki kodu, <m> co niektórzy uważają za dużą zaletę Pythona, <m> inni uważają za jego główną wadę. <mark name="wywolanie" />'
			"Funkcję wywołujemy poprzez jej nazwę, <m> po której podajemy nawiasy okrągłe. <m>"
		]
	},
	{ #  definicja funkcji z kilkoma argumentami (potęga) - pierwsza linia i kolejne: print("podnoszę do potęgi ... wynik to:", a+b)
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_B, "py")],
			["wywolanie2", eduMovie.clear + eduMovie.code2console(code_funkcja_B_run, "py")]
		],
		'consoleDown': [
			[0.0, ""],
			["wywolanie2", eduMovie.runCode(code_funkcja_B_run, [], cmd="python3")],
		],
		'text' : [
			"Jak wiemy funkcje mogą przyjmować też argumenty. <m>"
			"Definiując taką funkcję wewnątrz nawiasów okrągłych <m> podajemy rozdzielane przecinkami nazwy zmiennych <m> pod które mają być one podstawione, <m> gdy funkcja zostanie wywołana. <m>"
			'W ten sposób możemy parametryzować działanie <m> tego nazwanego kawałka kodu, którym jest funkcja. <mark name="wywolanie2" />'
			"Wywołując taką funkcję w nawiasach związanych z jej wywołaniem <m> musimy wpisać odpowiednią liczbę argumentów. <m>"
		]
	},
]


code_funkcja_C = r"""
def potęga(a, b):
    print("funkcja potęga, argumenty:", a, b)
    return a**b
    print("obliczyłem")
"""

code_funkcja_C_run = code_funkcja_C + r"""
x = potęga(2,3)
print(x*2)
"""

code_funkcja_C_run2 = code_funkcja_C + r"""
x = potęga(b=2, a=3)
print(x*2)
"""

code_funkcja_C_run3 = code_funkcja_C + r"""
b=3
x = potęga(b=b, a=2)
print(x*2)
"""

code_funkcja_D = r"""
def abc(a, b=2, c=0):
    return a**b+c

print( abc(4) )
print( abc(4,3) )
print( abc(4,3,2) )
"""

code_funkcja_E = r"""
def abc(a, b=2, c=0):
    return a**b+c

print( abc(4,c=3) )
"""

clipData += [
	{ #  return z funkcji
		'consoleTop': [
			[0.0, ""],
			["_return", eduMovie.clear + eduMovie.code2console(code_funkcja_C, "py")],
			["wywolanie3", eduMovie.clear + eduMovie.code2console(code_funkcja_C_run, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["wywolanie3", eduMovie.runCode(code_funkcja_C_run, [], cmd="python3")],
		],
		'text' : [
			"Jak dotąd nasza funkcja wypisywała <m> wynik swojego działania bezpośrednio na ekran, <m> z użyciem funkcji print. <m>"
			"Natomiast często chcemy żeby funkcja <m> mogła zwrócić jakąś wartość do kodu który ją wywołał. <m>"
			"Czyli na przykład jeżeli mamy funkcję, <m> która wykonuje jakąś operację arytmetyczną <m> na swoich argumentach, to na ogół chcemy <m> uzyskać ten wynik i zapisać go w jakiejś zmiennej, <m>"
				'aby móc wykonywać na nim dalsze operacje, <m> a niekoniecznie wypisać go od razu na ekran. <mark name="_return" />'
			'W tym celu w miejscu, w którym <m> chcemy aby funkcja zakończyła swoje działanie <m> umieszczamy słowo kluczowe return, <m> któremu podajemy wartość jaka ma być zwrócona z funkcji. <mark name="wywolanie3" />'
			'Jak widzimy wynik operacji wykonanej przez funkcję <m> został zwrócony do miejsca jej wywołania i zapisany w zmiennej, <m> na której możemy wykonać dalsze operacje. <m>'
			'Widzimy także że kod funkcji po słowie kluczowym return nie został wykonany, <m> wykonywanie funkcji zostało przerwane w miejscu wywołania tej instrukcji. <m>'
			'Funkcja w Pythonie może zwracać dowolne wartości <m> (na przykład napisy), a nawet wiele różnych wartości. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_C_run2, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_funkcja_C_run2, [], cmd="python3")],
		],
		'text' : [
			"Python pozwala na jawne odwoływanie się <m> do wszystkich nazwanych argumentów funkcji <m> z użyciem ich nazw, pozwala to na podawanie <m> takich argumentów w dowolnej kolejności. <m>"
		]
	},
	{ #  b=3 potęga(b=b...)
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_C_run3, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_funkcja_C_run3, [], cmd="python3")],
		],
		'text' : [
			"Nawet pozornie bezsensowny zapis typu b=b <m> ma w takiej sytuacji sens, gdyż <m> b po lewej stronie znaku równości jest nazwą argumentu <m> (czyli nazwą zmiennej w kodzie funkcji), <m>"
			"a b po prawej stronie jest nazwą zmiennej <m> w miejscu wywołania funkcji – to są inne zmienne. <m>"
		]
	},
	{ #  wartość domyślna
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_funkcja_D, [], cmd="python3")],
		],
		'text' : [
			"Python pozwala na ustawianie wartości domyślnych <m> dla argumentów funkcji, czyniąc je argumentami opcjonalnymi. <m>"
			"W tym celu w definicji funkcji po nazwie argumentu <m> piszemy znak równości i podajemy wartość, <m> która ma być użyta jako domyślna. <m>"
			"Wszystkie argumenty z wartościami domyślnymi, <m> muszą być na prawo od argumentów <m> nie posiadających takich wartości. <m>"
			"Wywołując taką funkcję musimy podać co najmniej tyle argumentów <m> ile wynosi liczba argumentów bez wartości domyślnych, <m> a każdy kolejny podany argument będzie zastępował <m> kolejny od lewej argument z wartością domyślną. <m>"
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_funkcja_E, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_funkcja_E, [], cmd="python3")],
		],
		'text' : [
			"Jeżeli chcemy zmienić wartość tylko wybranych argumentów <m> z wartościami domyślnymi (a te nie są akurat pierwszymi od lewej) <m>"
			"to możemy skorzystać ze znanego już mechanizmu odwoływania się <m> w wywołaniu funkcji do argumentów z użyciem ich nazw. <m>"
			"Jest to bardzo wygodne jeżeli funkcja przyjmuje <m> wiele opcjonalnych argumentów. <m>"
			"Warto zauważyć, iż z opcjonalnych argumentów mających <m> przypisane wartości domyślne korzystaliśmy już <m> w funkcji print do określania separatorów. <m>"
		]
	},
]


code_global_A = r"""
def f1():
   print(a)

def f2():
   a=3
   f1()
"""
""" # w python -i
f1()
f2()

a=1

f2()
f1()
"""

code_global_B = r"""
def f2():
   def f1():
      print(a)
   a=3
   f1()

def f3():
   def f1():
      print(a)
   f1()
"""
""" # w python -i
f2()
f3()

a=1
f2()
f3()
"""

code_global_C = r"""
a = 0
def f1():
   a = 13
   print(a)

f1()
print(a)
"""

code_global_D = r"""
a = 0
def f1():
   global a
   print(a)
   a = 13
   print(a)

f1()
print(a)
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_global_A, "py")],
		],
		'consoleDown': [
			[0.76779, "o", eduMovie.prompt()],
			[0.987317, "o", "python3 -i przykład.py"],
			[1.308461, "o", "\r\n"],
			[1.339151, "o", ">>> "],
			[2.798705, "o", "f1()"],
			[3.684587, "o", "\r\n"],
			[3.685409, "o", "Traceback (most recent call last):\r\n  File \"<stdin>\", line 1, in <module>\r\n"],
			[3.685876, "o", "  File \"przykład.py\", line 2, in f1\r\n"],
			[3.686243, "o", "    print(a)\r\nNameError: name 'a' is not defined\r\n>>> "],
			[6.122277, "o", "f2()"],
			[7.522277, "o", "\r\n"],
			[7.523043, "o", "Traceback (most recent call last):\r\n  File \"<stdin>\", line 1, in <module>\r\n"],
			[7.523877, "o", "  File \"przykład.py\", line 6, in f2\r\n    f1()\r\n  File \"przykład.py\", line 2, in f1\r\n    print(a)\r\nNameError: name 'a' is not defined\r\n>>> "],
			
			["seta + 0.233419", "o", "a=1"],
			["seta + 0.788579", "o", "\r\n"],
			["seta + 0.789396", "o", ">>> "],
			["seta + 3.457304", "o", "f2()"],
			["seta + 4.364584", "o", "\r\n"],
			["seta + 4.36536", "o", "1\r\n"],
			["seta + 4.365763", "o", ">>> "],
			["seta + 6.936607", "o", "f1()"],
			["seta + 7.564464", "o", "\r\n"],
			["seta + 17.565017", "o", "1\r\n>>> "],
		],
		'text' : [
			"Jak wiemy Python przy odwołaniu do nie istniejącej zmiennej generuje błąd. <m>"
			"Natomiast definiując funkcję możemy użyć w niej zmiennej <m> która jest w tym momencie nie zdefiniowana. <m>"
			'Dopiero uruchomienie takiej funkcji <m> może spowodować wypisanie komunikatu o błędzie <m> związanym z niezdefiniowaną zmienną. <mark name="seta" />'
			"Jeżeli zmienna ta zostanie zdefiniowana jako globalna, <m> nawet już po zdefiniowaniu funkcji, to zostanie ona użyta. <m>"
			"W prezentowanym przykładzie widzimy że <m> f1 nie korzysta ze zmiennej a, zdefiniowanej wewnątrz f2 <m> w którym jest wywoływany, <m> ale potrafi skorzystać ze zmiennej globalnej. <m>"
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_global_B, "py")],
		],
		'consoleDown': [
			[0.0, "o", eduMovie.prompt()],
			[0.171683, "o", "python3 -i przykład.py"],
			[1.367028, "o", "\r\n"],
			[1.397505, "o", ">>> "],
			[3.627132, "o", "f2()"],
			[4.09506, "o", "\r\n"],
			[4.095854, "o", "3\r\n"],
			[4.096209, "o", ">>> "],
			[6.232098, "o", "f3()"],
			[8.438972, "o", "\r\n"],
			[8.439799, "o", "Traceback (most recent call last):\r\n  File \"<stdin>\", line 1, in <module>\r\n"],
			[8.440139, "o", "  File \"przykład.py\", line 10, in f3\r\n"],
			[8.440327, "o", "    f1()\r\n  File \"przykład.py\", line 9, in f1\r\n"],
			[8.440591, "o", "    print(a)\r\nNameError: name 'a' is not defined\r\n"],
			[8.440761, "o", ">>> "],
			
			["stepa + 0.07", "o", "a=1"],
			["stepa + 0.103008", "o", "\r\n"],
			["stepa + 0.103825", "o", ">>> "],
			["stepa + 1.972327", "o", "f2()"],
			["stepa + 2.159091", "o", "\r\n"],
			["stepa + 2.159895", "o", "3\r\n"],
			["stepa + 2.1603", "o", ">>> "],
			["stepa + 4.587602", "o", "f3()"],
			["stepa + 4.886914", "o", "\r\n"],
			["stepa + 4.887656", "o", "1\r\n"],
			["stepa + 4.887948", "o", ">>> "],
		],
		'text' : [
			"Jeżeli definiowalibyśmy funkcje wewnątrz funkcji <m> (bo da się tak robić w Pythonie) sprawa trochę się komplikuje. <m>"
			'Stosowny przykład widoczny jest teraz na ekranie. <mark name="stepa" /> Jak widzimy wygrywa tutaj zmienna <m> definiowana na tym poziomie co funkcja. <m>'
			"Natomiast nie będziemy omawiać tego przypadku <m> w szczegółach, gdyż jest on dość rzadko spotykany. <m>"
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_global_C, "py")],
			["useglobal", eduMovie.clear + eduMovie.code2console(code_global_D, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_global_C, [], cmd="python3")],
			["useglobal", eduMovie.runCode(code_global_D, [], cmd="python3")],
		],
		'text' : [
			"Taki dostęp do zmiennych globalnych nie pozwala na ich modyfikację. <m>"
			'Jeżeli zachodzi taka potrzeba należy użyć słowa kluczowego global, <mark name="useglobal" /> w sposób widoczny na ekranie. <m>'
			"Na ogół unikamy jednak korzystania ze zmiennych globalnych <m> w funkcjach i staramy się przekazywać wszystkie wymagane <m> parametry poprzez argumenty funkcji. <m>"
		]
	},
]
